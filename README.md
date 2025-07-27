# Waydroid

Waydroid uses a container-based approach to boot a full Android system on a
regular GNU/Linux system like Ubuntu.

## Overview

Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a
full Android system in a container and provide Android applications on
any GNU/Linux-based platform.

The Android system inside the container has direct access to any needed hardware.

The Android runtime environment ships with a minimal customized Android system
image based on [LineageOS](https://lineageos.org/). The image is currently based
on Android 11.

## Documentation

Our documentation site can be found at [docs.waydro.id](https://docs.waydro.id)

## Documentation - MODIFICATIONS / UPDATE

Waydroid could work as before if it have no new parameters. So it could work with GUI application as before.  

You can choose the profile data folder "waydroid_data" (default = ~/.local/share/waydroid). You have to use --data_path during the init for example :  sudo waydroid init --data_path /home/user/waydroid_data  

You can choose the work folder "work" (default = /var/lib/waydroid). You have to ALWAYS use --work_path so for example : (var/lib/waydroid2 is the folder)  
- Init : sudo waydroid --work_path /var/lib/waydroid2 init
- Init WITH other profile data folder : sudo waydroid --work_path /var/lib/waydroid2 init --data_path /home/user/waydroid_data
- Log : waydroid --work_path /var/lib/waydroid2 log
- Container start : sudo waydroid --work_path /var/lib/waydroid2 container start
- Session start : waydroid --work_path /var/lib/waydroid2 session start
- Show-full-ui : waydroid --work_path /var/lib/waydroid2 show-full-ui

It remain to look if network works, if not have a look to usr/lib/waydroid/data/scripts/waydroid-net.sh -> Because we just have one now (no one by profile) and it have :   
vnic=$(awk "\$1 == \"$net_link_key\" {print \$3}" /var/lib/waydroid/lxc/waydroid/config)

You have to manually edit /etc/systemd/system/multi-user.target.wants/waydroid-container.service and replace the :   
ExecStart=/usr/bin/waydroid -w container start  
BY  
ExecStart=/usr/bin/waydroid -w --work_path /var/lib/waydroid2 container start  
Before modify it, stop the previous session, the container and the service.  
Modify it  
Reload : sudo systemctl daemon-reload  
Start the service and the container, if it stay waydroid connection error, reboot.  
So this could be scripted, and need each time you change profile. It is boring now, but will be modify and upgraded !!  

It will be update to a profile number with a service by profile. If any one have idea please contact me !  

## Reporting bugs

If you have found an issue with Waydroid, please [file a bug](https://github.com/Waydroid/waydroid/issues/new/choose).

## Testing

I test it on a Droidian arm64 phone, and all works !  
Could other test it ?  
Could anyone test it on Ubuntu Touch ? on desktop ?  
-> Please repport your results here https://github.com/DavidFirefox/waydroid/discussions/2  

I keep lot of log and print for testing and for the next option !  

## Get in Touch

If you want to get in contact with the developers please feel free to join the
*Waydroid* groups in [Matrix](https://matrix.to/#/#waydroid:matrix.org) or [Telegram](https://t.me/WayDroid).  
Or for this fork : https://github.com/DavidFirefox/waydroid/discussions/3

## Build / Install

I build the waydroid_1.5.4.1_all.deb on my Droidian arm64 phone, but it should be use by all arch.  
You just have to dpkg it.  
Try if you could download needed version of libgbinder and libglibutil required for Waydroid > 1.5.  
You cloud take it from my Release and download on a new folder and sudo dpkg -i *.deb  

You could build it with the build_waydroid_v9.sh, adapt to just build waydroid, and take it from my git. Dependence are visible on the script but not install, you could uncomment it.

## What NEXT ?

I think it could be fine, if we use a profile number instead of a work-path.
With a common cfg file, with the work-path of all profiles.  
So GUI software could be adapted to use multi-profiles.  

Maybe try to see if more than one container could be start as the same time ? Multiple Waydroid instance.  
You could see https://github.com/DavidFirefox/waydroid/discussions/3
