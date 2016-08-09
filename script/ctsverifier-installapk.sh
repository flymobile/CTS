#!/bin/bash
#ctsverifier-installapk.sh
# install more app with ctsverifier-installapk.sh on same PC
adb_options=" "
if [ $# -eq 2 ]; then
  echo " More than one devices,will install device what you want"
  adb_options=""$1" "$2""
elif [ $# -eq 0 ]; then
  echo " only one devices,so install default device"
else
  echo "Usage: ctsverifier-installapk.sh  [-s serial]"
  echo "  eg."
  echo "  ctsverifier-installapk.sh //only one devices"
  echo "  ctsverifier-installapk.sh -s TMMPG4250D700056 //install on device that the serial is TMMPG4250D700056"
  exit
fi

adb $adb_options install -r ./android-cts-verifier/CtsPermissionApp.apk
adb $adb_options install -r ./android-cts-verifier/CtsVerifier.apk
adb $adb_options install -r ./android-cts-verifier/NotificationBot.apk
