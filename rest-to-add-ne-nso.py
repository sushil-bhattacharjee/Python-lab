#!/usr/bin/env python

import json
import requests

NE = {
    "device": {
        "name": "ios-device",
        "address": "10.1.10.29",
        "port": 22,
        #"auth"=("sushil", "sushil"),
        "state": {
            "admin-state": "unlocked",
        },

        "authgroup": "sushil",
        "device-type": {
        "cli": {
            "ned-id": "tailf-ned-cisco-ios-id:cisco-ios-cli-3.0"
            }
        }
    }
}


def main():
    baseUri = "http://localhost:8080/restconf/data"
    auth = ("admin", "admin")
    headers = {'Content-Type': 'application/yang-data+json'}
    response = requests.put(baseUri + '/devices/device=ios-device', auth=auth, headers=headers, data=json.dumps(NE))
    print(response)

    baseUriOperation = "http://localhost:8080/restconf/operations"
    response = requests.post(baseUriOperation + "/devices/device=ios-device/ssh/fetch-host-keys", auth=auth, headers=headers)
    print(response)

    response = requests.post(baseUriOperation + "/devices/device=ios3/sync-from", auth=auth, headers=headers)
    print(response)

if __name__ == "__main__":
    main()
