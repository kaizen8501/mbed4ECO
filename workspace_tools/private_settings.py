"""
mbed SDK
Copyright (c) 2011-2013 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from os.path import join

# These default settings have two purposes:
#    1) Give a template for writing local "private_settings.py"
#    2) Give default initialization fields for the "toolchains.py" constructors

##############################################################################
# Build System Settings
##############################################################################

# ARM

armcc = "keil"

ARM_PATH = "C:/Keil_v5/ARM/armcc"
ARM_BIN = join(ARM_PATH, "bin")
ARM_INC = join(ARM_PATH, "include")
ARM_LIB = join(ARM_PATH, "lib")


ARM_CPPLIB = join(ARM_LIB, "cpplib")
MY_ARM_CLIB = join(ARM_PATH, "lib", "microlib")


##############################################################################
# Test System Settings
##############################################################################
SERVER_ADDRESS = "127.0.0.1"
LOCALHOST = "127.0.0.1"

MUTs = {
        "1" : {"mcu": "WIZwiki_W7500",
        "port":"COM54",
        "disk":"I:\\",
        "peripherals": []
        }
}

##############################################################################
# Private Settings
##############################################################################
try:
    # Allow to overwrite the default settings without the need to edit the
    # settings file stored in the repository
    from workspace_tools.private_settings import *
except ImportError:
    print '[WARNING] Using default settings. Define you settings in the file "workspace_tools/private_settings.py" or in "./mbed_settings.py"'
