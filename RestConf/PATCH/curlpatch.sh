curl -i -k -X "PATCH" "https://192.168.56.107:443/restconf/data/Cisco-IOS-XE-native:native" \
-H 'Content-Type: application/yang-data+json' \
-H 'Accept: application/yang-data+json' \
-u 'cisco:cisco123!' \
-d $'{
  "native": {
    "logging": {
      "monitor": {
        "severity": "informational"
      }
    }
  }
}'
