#!/bin/bash
#installAdminApp.sh
# for android 6.0 to install ctsAdmin.app to devices on same PC
adb_options=" "
if [ $# -eq 2 ]; then
  echo " More than one devices,will install device what you want"
  adb_options=""$1" "$2""
elif [ $# -eq 0 ]; then
  echo " only one devices,so install default device"
else
  echo "Usage: installAdminAPP.sh  [-s serial]"
  echo "  eg."
  echo "  installAdminAPP.sh //only one devices"
  echo "  installAdminAPP.sh -s TMMPG4250D700056 //install on device that the serial is TMMPG4250D700056"
  exit
fi

adb $adb_options install -r ./android-cts/repository/testcases/CtsDeviceAdmin.apk
