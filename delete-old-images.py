#! /bin/env python3

import subprocess
import json
from datetime import datetime, timedelta

docker_list = subprocess.run(
    ["docker images --format '{{json .}}'"],
    shell=True, capture_output=True)

if docker_list.returncode != 0:
    print("error listing docker images", docker_list.stderr)

# Each line is a JSON object, last line is empty
lines = docker_list.stdout.decode().split("\n")[:-1]

for line in lines:
    parsed = json.loads(line)
    # Docker outputs a non-standard format, so we'll do a small conversion
    #   from 2023-01-18 14:06:21 +0100 CET to 2023-01-18T14:06:21 .
    # We ignore the timezone for simplicity
    created_at = "T".join(parsed["CreatedAt"].split(" ")[0:2])

    delta = datetime.now() - datetime.fromisoformat(created_at)
    if delta > timedelta(days=14):
        print(f"deleting docker image {parsed['Repository']}:{parsed['Tag']}")
        docker_remove = subprocess.run(
            [f"docker image rm --force {parsed['ID']}"],
            shell=True, capture_output=True)
        if docker_remove.returncode != 0:
            print("error removing docker image:", docker_remove.stderr)
