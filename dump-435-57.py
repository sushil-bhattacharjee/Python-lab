from rich import print as rprint
d = {
    "data":
        [
            {
                "count": 4,
                "detailsURL": "",
                "status": "error",
                "statusList":
                    [
                        {
                            "count": 4,
                            "detailsURL": "/dataservice/device/hardwarehealth/detail?state=normal",
                            "message": "normal",
                            "status": "up"
                        }
                    ]
            }
        ]
}

rprint(d["data"][0]["statusList"][0]["status"])