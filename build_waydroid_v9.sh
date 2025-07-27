#!/bin/bash
# script name: build_waydroid_v9.sh
# description: Minimal Build Waydroid for Debian or Ubuntu based distro
# Based on   : https://gist.github.com/cniw/98e204d7dbc73a3fa1bf61629b2a2fc1
NC='\033[0m'
RED='\033[1;91m'
GREEN='\033[1;92m'

if [ ! -f /usr/bin/dpkg ]
then
  echo -e "\n${RED}==> Can't run this script because your distro doesn't have dpkg package manager.${NC}\n"
  exit 1
fi

echo
echo -e "${GREEN}==> Setting up build directory ...${NC}"
mkdir -p ~/waydroid-build/packages
cd ${_%/*}
echo -e "${GREEN}==> Setting up build directory, done${NC}\n"

  echo -e "${GREEN}==========> Start preparing <==========${NC}"
  echo -e "${GREEN}==> Cloning git repository ...${NC}"
  mv waydroid waydroid.old
  git clone https://github.com/DavidFirefox/waydroid.git || exit 1 
  echo -e "${GREEN}==> Cloning git repository, done.${NC}\n"

  cd ~/waydroid-build/packages/waydroid
  echo -e "${GREEN}==========> Start building <==========${NC}"
  echo -e "${GREEN}==> Building package(s) ...${NC}"
  sudo debuild -b -uc -us
  if [ ! $? -eq 0 ]
  then
    echo -e "\n${RED}==> Building package(s), failed.${NC}\n"
    exit 1
  else
    echo -e "${GREEN}==> Building package(s), done.${NC}"
    echo -e "${GREEN}==========> Finish building <==========${NC}\n"
