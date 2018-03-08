#!/usr/bin/python3
from prometheus_client import start_http_server, Metric, REGISTRY
from requests.auth import HTTPDigestAuth
from metrics_classes import *
from urls import bundles

import sys
import json
import requests
import time

host = sys.argv[1]

if __name__ == "__main__":
    start_http_server(int(sys.argv[2]))
    host = sys.argv[1]

    for bundle in bundles:
        try:
            REGISTRY.register(bundle[0](*bundle[1]))
        except Exception as excpt:
            print(excpt)

    while True:
        time.sleep(1)
