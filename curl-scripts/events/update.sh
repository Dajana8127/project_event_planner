#!/bin/bash

curl "http://localhost:8000/events/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "event": {
      "name": "'"${NAME}"'",
      "place": "'"${PLACE}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
