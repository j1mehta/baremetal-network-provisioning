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


from baremetal_network_provisioning.tests.api import base
from baremetal_network_provisioning.tests.tempest import config

from oslo_config import cfg


config.register_options()
CONF = cfg.CONF
sw_ip_address = CONF.hpe_bnp.sw_ip_address
sw_ip_address_inv = CONF.hpe_bnp.sw_ip_address_inv
sw_usr = CONF.hpe_bnp.switch_user
sw_passwd = CONF.hpe_bnp.switch_passwd
vendor = CONF.hpe_bnp.vendor
access_parameter = CONF.hpe_bnp.access_parameter
access_parameter_inv = CONF.hpe_bnp.access_parameter_inv
access_parameter_priv = CONF.hpe_bnp.access_parameter_priv
access_protocol_v1 = CONF.hpe_bnp.access_protocol_v1
access_protocol_v2c = CONF.hpe_bnp.access_protocol_v2c
access_protocol_v3 = CONF.hpe_bnp.access_protocol_v3
access_parameter_v3 = CONF.hpe_bnp.access_parameter_v3


class BMNPExtensionTestJSON(base.BaseAdminNetworkTest):
    _interface = 'json'

    def test_create_show_list_update_delete_switch_snmpv1(self):
        switch = self.admin_client.b_create_switch(ip_address=sw_ip_address,
                                                   vendor=vendor,
                                                   access_protocol=(
                                                       access_protocol_v1),
                                                   **access_parameter)
        switch_id = switch['bnp_switch']['id']
        self.admin_client.b_list_switches()
        self.admin_client.b_update_switch(switch_id)
        self.admin_client.b_delete_switch(switch_id)

    def test_create_show_list_update_delete_switch_snmpv2c(self):
        switch = self.admin_client.b_create_switch(ip_address=sw_ip_address,
                                                   vendor=vendor,
                                                   access_protocol=(
                                                       access_protocol_v2c),
                                                   **access_parameter)
        switch_id = switch['bnp_switch']['id']
        self.admin_client.b_list_switches()
        self.admin_client.b_update_switch(switch_id)
        self.admin_client.b_delete_switch(switch_id)

    def test_create_show_list_update_delete_switch_snmpv3(self):
        switch = self.admin_client.b_create_switch(ip_address=sw_ip_address,
                                                   vendor=vendor,
                                                   access_protocol=(
                                                       access_protocol_v3),
                                                   **access_parameter_v3)
        switch_id = switch['bnp_switch']['id']
        self.admin_client.b_list_switches()
        self.admin_client.b_update_switch(switch_id)
        self.admin_client.b_delete_switch(switch_id)

    def test_list_switches_non_admin_client(self):
        self.client.b_list_switches()
