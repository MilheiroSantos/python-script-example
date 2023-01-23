#! /bin/env bash

set -e  # Ensure a failed command stops the script

docker images --format '{{json .}}' | while read line
do
  # Docker outputs a non-standard format, so we'll do a small conversion
  #   from 2023-01-18 14:06:21 +0100 CET to 2023-01-18T14:06:21 .
  # We ignore the timezone for simplicity
  created_epoch=$(echo "$line" \
    | jq --raw-output '.CreatedAt' \
    | awk 'BEGIN { OFS = "T" } { print $1, $2 }' \
    | date -f - +%s)
  now_epoch=$(date +%s)
  delta=$((now_epoch-created_epoch))

  if [ $delta -gt 1209600 ]; then #14 days
    repository=$(echo "$line" | jq --raw-output '.Repository')
    tag=$(echo "$line" | jq --raw-output '.Tag')
    id=$(echo "$line" | jq --raw-output '.ID')

    echo "deleting repository ${repository}:${tag}"
    docker image rm --force "$id" || True # An error in the removal should not stop the loop
  fi
done
