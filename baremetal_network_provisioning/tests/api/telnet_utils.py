# Copyright 2016 Hewlett-Packard Development Company, L.P.
# Copyright 2016 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import telnetlib
import time


def connect_to_switch(device_ip, port, device_username,
                      device_password, timeout):
    tn = telnetlib.Telnet(device_ip, port=port, timeout=timeout)
    tn.write("\n")
    index, match, data = tn.expect(['Press <Enter> twice',
                                    'Press any key to continue', '~#',
                                    'Username: '], 20)
    time.sleep(1)
    if (index == 0 or index == -1):
        tn.write("\r")
        tn.write("\n")
        tn.write("\r")
        tn.write("\n")
        index, match, data = tn.expect(["login:", '~#'], 20)
        if (index == 0):
            tn.write(device_username + "\n")
            index, match, data = tn.expect(['~#', "Password: "], 20)
            tn.write(device_password + "\n")
            tn.read_until('~#', 6)
        else:
            tn.write("\n")
    elif (index == 3):
        tn.write(device_username + "\n")
        index, match, data = tn.expect(['~#', "Password: "], 6)
        tn.write(device_password + "\n")
        tn.read_until('~#', 6)
    time.sleep(1)
    tn.write("\n")
    tn.read_until('~#', 6)
    if (tn):
        return tn
    else:
        raise ValueError('Connection failed!')


def run_cmd_op(tn, command):
    tn.read_until('~#', 2)
    tn.write(command + "\n")
    data = tn.read_until('~#', 2)
    return data
