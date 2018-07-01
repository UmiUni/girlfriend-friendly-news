#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
"""
Flask Server
@author: pkugoodspeed
@date: 06/30/2018
@copyright: jogchat.com
"""

import json
import argcomplete, argparse
from newsutils.config import SRCS
from newsutils.query import queryFromSrc
from newsutils.extractor import extractFromSrc, extractFromUrl


parser = argparse.ArgumentParser()
parser.add_argument("--src", type=str, default="")
parser.add_argument("--url", type=str, default="")
argcomplete.autocomplete(parser)


o = parser.parse_args()


if __name__ == "__main__":
    if o.src:
        for src in o.src.split(","):
            extractFromSrc(src)
    elif o.url:
        for url in o.url.split(","):
            extractFromUrl(url)
    else:
        for src in SRCS:
            queryFromSrc(SRCS[src])
