# Copyright 2021 Oliver Smith SPDX-License-Identifier: GPL-3.0-or-later PYTHON_ARGCOMPLETE_OK
import sys
import logging
import os
import traceback
import dbus.mainloop.glib
import dbus
import dbus.exceptions

from . import actions
from . import config
from . import helpers
from .helpers import logging as tools_logging

import tools.config
from tools import helpers
from tools import services
##from tools import helpers
##import tools.config

#import configparser

#import tools.helpers.props



def main():
    def actionNeedRoot(action):
        if os.geteuid() != 0:
            raise RuntimeError(
                "Action \"{}\" needs root access".format(action))

    # Wrap everything to display nice error messages
    args = None
    try:
        # Parse arguments, set up logging
        args = helpers.arguments()

##        if args.action == "log":

####################### AV bloquant si pas args.work
##        if 1 == 1:
##            print("--work_path:(tools/__init__.py):\t" + args.work_path)
#            args.work = config.defaults["work"] ##### AV pour le non init et non lancement
##            args.work = args.work_path
##            print("args.work:(tools/__init__.py):\t" + args.work)


        if 1 == 1:
##        if args.action == "init":
#        if 'args.work_path' in locals():
            if args.work_path:
                 print("--work_path:(tools/__init__.py):\t" + args.work_path)
                 args.work = args.work_path
            else:
                 args.work = config.defaults["work"]
                 print("NOT WORK PATH (tools/__init__.py")
#        if 'args.images_path' in locals():

        print("args.work suite:(tools/__init__.py):\t" + args.work)
        if args.action == "init":
            if not args.images_path: # OK en mode init et ko en mode log
                 print("NOT IMAGE PATH (tools/__init__.py")
            if args.images_path:
                 print("--images_path:(tools/__init__.py):\t" + args.images_path) # crash if not images_path # ok


######### AV :
#defaults["rootfs"] = defaults["work"] + "/rootfs"
#defaults["overlay"] = defaults["work"] + "/overlay"
#defaults["overlay_rw"] = defaults["work"] + "/overlay_rw"
#defaults["overlay_work"] = defaults["work"] + "/overlay_work"
#defaults["data"] = defaults["work"] + "/data"
#defaults["lxc"] = defaults["work"] + "/lxc" ## AV hard defined !!
#defaults["host_perms"] = defaults["work"] + "/host-permissions"



#        try:
#             args.images_path
#        except NameError:
#             print("--images_path 2:(tools/__init__.py):\t" + args.images_path)
#        else:
#             print("NOT IMAGE PATH 2 (tools/__init__.py")


####        cfg = tools.config.load(args)
##        cfg = configparser.ConfigParser()
###        cfg = tools.config.load(args)
        if args.action == "init":
            if args.data_path:
                 print("--data_path:(tools/__init__.py):\t" + args.data_path)
#                 cfg["waydroid"]["data_path"] = args.data_path
            else:
#                 cfg["waydroid"]["data_path"] = config.session_defaults["waydroid_data"]
                 print("NOT DATA PATH (tools/__init__.py")
##
###        config_path = tools.config.defaults["data_path"]
        config_path = tools.config.channels_defaults["config_path"]

###        cfg = tools.config.load(args)
###        print("cfg[waydroid][data_path] (tools/__init__.py):\t" + cfg["waydroid"].get("data_path"))

        print("exit if init - tools/__init_.py")
#        cfg = tools.config.load(args)
#        print("Vendor type:\t" + cfg["waydroid"]["vendor_type"])
        args.cache = {}
##        args.work = config.defaults["work"] # in initializer.py

#        try:
#             args.work_path
#        except NameError:
#            args.work = args.work_path
#        else:
#            args.work = config.defaults["work"]

#        if 'args.work_path' in globals(): #locals():
#            args.work = args.work_path
#        else:
#            args.work = config.defaults["work"]

####        config.session_defaults["waydroid_data"] = cfg["waydroid"]["data_path"]
        print("config.session_defaults[waydroid_data] (tools/__init__.py):\t" + config.session_defaults["waydroid_data"])

        print("--args.work:(tools/__init__.py):\t" + args.work)

        print("config.defaults[work]:(tools/__init__.py):\t" + config.defaults["work"])

##        print("tools.config.load(args):(tools/__init__.py):\t" + tools.config.load(args))
###        print("args.images_path:(tools/__init__.py):\t" + args.images_path)
###        print("cfg[waydroid][images_path]:(tools/__init__.py):\t" + cfg["waydroid"]["images_path"])
###        print("tools.config.defaults[images_path]:\t" + tools.config.defaults[images_path])

#        args.work = config.config_keys["work"] # -> error
#        args.work = tools.config.config_keys["arch2"]
##        args.work = args.images_path
##        print(args.images_path)
#        args.work = config.defaults["work"]
#        args.work = cfg["waydroid"].get("work")
# or config.config_keys["work"]
# or tools.config.config_keys["work"]
#tools.config.defaults ???
#        args.work = cfg["waydroid"]["work"] # to test -> error
#        args.work = args.work_path # to test -> error
        args.config = args.work + "/waydroid.cfg"
        print("args.config:(tools/__init__.py):\t" + args.config)

        if args.work_path:
        # or tools.config.defaults
            config.defaults["rootfs"] = args.work + "/rootfs"
            config.defaults["overlay"] = args.work + "/overlay"
            config.defaults["overlay_rw"] = args.work + "/overlay_rw"
            config.defaults["overlay_work"] = args.work + "/overlay_work"
            config.defaults["data"] = args.work + "/data"
            config.defaults["lxc"] = args.work + "/lxc"
            config.defaults["host_perms"] = args.work + "/host-permissions"
            tools.config.defaults["rootfs"] = args.work + "/rootfs"


            print("config.defaults[rootfs]:(tools/__init__.py):\t" + config.defaults["rootfs"])
            print("config.defaults[overlay]:(tools/__init__.py):\t" + config.defaults["overlay"])
            print("config.defaults[overlay_rw]:(tools/__init__.py):\t" + config.defaults["overlay_rw"])
            print("config.defaults[overlay_work]:(tools/__init__.py):\t" + config.defaults["overlay_work"])
            print("config.defaults[data]:(tools/__init__.py):\t" + config.defaults["data"])
            print("config.defaults[lxc]:(tools/__init__.py):\t" + config.defaults["lxc"])
            print("config.defaults[host_perms]:(tools/__init__.py):\t" + config.defaults["host_perms"])

            print("tools.config.defaults[rootfs]:(tools/__init__.py):\t" + tools.config.defaults["rootfs"])


        args.log = args.work + "/waydroid.log"
        args.sudo_timer = True
        args.timeout = 1800


        cfg = tools.config.load(args)
#### PLANTE
##        print("cfg[waydroid][data_path] (tools/__init__.py):\t" + cfg["waydroid"].get("data_path"))
##        print("cfg[waydroid][data_path] (tools/__init__.py):\t" + cfg["waydroid"].get("arch"))
##        print("tools.config.config_keys (tools/__init__.py):\t" + tools.config.config_keys["arch"])

        print("TEST(tools/__init__.py):\t" + cfg["waydroid"]["suspend_action"])
        print("tools.config.session_defaults[waydroid_data] BEFORE :(tools/__init__.py):\t" + tools.config.session_defaults["waydroid_data"])
        if "data_path" in cfg["waydroid"]:
            print("TEST2 : data_path in cfg Waydroid (tools/__init__.py):\t" + cfg["waydroid"]["data_path"])
            print("data_path is detected in cfg Waydroid (tools/__init__.py):\t")
#            print("tools.config.session_defaults[waydroid_data] BEFORE :(tools/__init__.py):\t" + tools.config.session_defaults["waydroid_data"])
#        if not args.action == "init":
            config.session_defaults["waydroid_data"] = cfg["waydroid"]["data_path"]
            args.data_path = cfg["waydroid"]["data_path"]
        print("tools.config.session_defaults[waydroid_data] AFTER :(tools/__init__.py):\t" + tools.config.session_defaults["waydroid_data"])

## A FAIRE : session["xdg_data_home"] pour     apps_dir = session["xdg_data_home"] + "/applications/" (user_manager.py)


        if os.geteuid() == 0:
            if not os.path.exists(args.work):
                os.mkdir(args.work)
        elif not os.path.exists(args.log):
            args.log = "/tmp/tools.log"

        tools_logging.init(args)

        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        dbus.mainloop.glib.threads_init()
        dbus_name_scope = None

        if not actions.initializer.is_initialized(args) and \
                args.action and args.action not in ("init", "first-launch", "log"):
            if args.wait_for_init:
                try:
                    dbus_name_scope = dbus.service.BusName("id.waydro.Container", dbus.SystemBus(), do_not_queue=True)
                    actions.wait_for_init(args)
                except dbus.exceptions.NameExistsException:
                    print('ERROR: WayDroid service is already awaiting initialization')
                    return 1
            else:
                print('ERROR: WayDroid is not initialized, run "waydroid init"')
                return 0

        # Initialize or require config
        if args.action == "init":
            actionNeedRoot(args.action)
            actions.init(args)
        elif args.action == "upgrade":
            actionNeedRoot(args.action)
            actions.upgrade(args)
        elif args.action == "session":
            if args.subaction == "start":
                actions.session_manager.start(args)
            elif args.subaction == "stop":
                actions.session_manager.stop(args)
            else:
                logging.info(
                    "Run waydroid {} -h for usage information.".format(args.action))
        elif args.action == "container":
            actionNeedRoot(args.action)
            if args.subaction == "start":
                if dbus_name_scope is None:
                    try:
                        dbus_name_scope = dbus.service.BusName("id.waydro.Container", dbus.SystemBus(), do_not_queue=True)
                    except dbus.exceptions.NameExistsException:
                        print('ERROR: WayDroid container service is already running')
                        return 1
                actions.container_manager.start(args)
            elif args.subaction == "stop":
                actions.container_manager.stop(args)
            elif args.subaction == "restart":
                actions.container_manager.restart(args)
            elif args.subaction == "freeze":
                actions.container_manager.freeze(args)
            elif args.subaction == "unfreeze":
                actions.container_manager.unfreeze(args)
            else:
                logging.info(
                    "Run waydroid {} -h for usage information.".format(args.action))
        elif args.action == "app":
            if args.subaction == "install":
                actions.app_manager.install(args)
            elif args.subaction == "remove":
                actions.app_manager.remove(args)
            elif args.subaction == "launch":
                actions.app_manager.launch(args)
            elif args.subaction == "intent":
                actions.app_manager.intent(args)
            elif args.subaction == "list":
                actions.app_manager.list(args)
            else:
                logging.info(
                    "Run waydroid {} -h for usage information.".format(args.action))
        elif args.action == "prop":
            if args.subaction == "get":
                actions.prop.get(args)
            elif args.subaction == "set":
                actions.prop.set(args)
            else:
                logging.info(
                    "Run waydroid {} -h for usage information.".format(args.action))
        elif args.action == "shell":
            actionNeedRoot(args.action)
            helpers.lxc.shell(args)
        elif args.action == "logcat":
            actionNeedRoot(args.action)
            helpers.lxc.logcat(args)
        elif args.action == "show-full-ui":
            actions.app_manager.showFullUI(args)
        elif args.action == "first-launch":
            actions.remote_init_client(args)
            if actions.initializer.is_initialized(args):
                actions.app_manager.showFullUI(args)
        elif args.action == "status":
            actions.status.print_status(args)
        elif args.action == "adb":
            if args.subaction == "connect":
                helpers.net.adb_connect(args)
            elif args.subaction == "disconnect":
                helpers.net.adb_disconnect(args)
            else:
                logging.info("Run waydroid {} -h for usage information.".format(args.action))
        elif args.action == "log":
            if args.clear_log:
                helpers.run.user(args, ["truncate", "-s", "0", args.log])
            try:
                helpers.run.user(
                    args, ["tail", "-n", args.lines, "-F", args.log], output="tui")
            except KeyboardInterrupt:
                pass
        else:
            logging.info("Run waydroid -h for usage information.")

        #logging.info("Done")

    except Exception as e:
        # Dump log to stdout when args (and therefore logging) init failed
        if not args:
            logging.getLogger().setLevel(logging.DEBUG)

        logging.info("ERROR: " + str(e))
        logging.info("See also: <https://github.com/waydroid>")
        logging.debug(traceback.format_exc())

        # Hints about the log file (print to stdout only)
        log_hint = "Run 'waydroid log' for details."
        if not args or not os.path.exists(args.log):
            log_hint += (" Alternatively you can use '--details-to-stdout' to"
                         " get more output, e.g. 'waydroid"
                         " --details-to-stdout init'.")
        print(log_hint)
        return 1


if __name__ == "__main__":
    sys.exit(main())
