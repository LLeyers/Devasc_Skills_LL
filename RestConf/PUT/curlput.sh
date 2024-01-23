curl -i -k -X "PUT" "https://192.168.56.107:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" \
-H 'Content-Type: application/yang-data+json' \
-H 'Accept: application/yang-data+json' \
-u 'cisco:cisco123!' \
-d $'{
  "severity": "warnings"
}'
