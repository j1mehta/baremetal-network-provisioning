# Copyright 2015 Hewlett-Packard Development Company, L.P.
# Copyright 2015 OpenStack Foundation
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

from neutron.tests.api import base

from oslo_config import cfg

from baremetal_network_provisioning.tests.tempest import config

from tempest_lib import exceptions as lib_exc

config.register_options()
CONF = cfg.CONF
ip_address = CONF.hpeBNP.ip_address
sw_usr = CONF.hpeBNP.switch_user
sw_passwd = CONF.hpeBNP.switch_passwd
vendor = CONF.hpeBNP.vendor
access_parameter = CONF.hpeBNP.access_parameter
access_parameter_priv = CONF.hpeBNP.access_parameter_priv
access_protocol_v1 = CONF.hpeBNP.access_protocol_v1
access_protocol_v2c = CONF.hpeBNP.access_protocol_v2c
access_protocol_v3 = CONF.hpeBNP.access_protocol_v3
access_parameter_v3 = CONF.hpeBNP.access_parameter_v3


class BMNPExtensionTestJSON(base.BaseAdminNetworkTest):
    _interface = 'json'

    """
    Tests the negatvie scenarios in the BNP API using the REST client for
    BNP
    """

    def test_invalid_snmp_v1_protocol(self):
        acc_proto = access_protocol_v1 + 'xyz'
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=ip_address, vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=acc_proto)

    def test_invalid_snmp_v2c_protocol(self):
        acc_proto = access_protocol_v2c + 'xyz'
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=ip_address, vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=acc_proto)

    def test_invalid_snmp_v3_protocol(self):
        acc_proto = access_protocol_v3 + 'xyz'
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=ip_address, vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=acc_proto)

    def test_invalid_IP_switch(self):
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address='105.0.1.266',
                          vendor=vendor, access_parameters=access_parameter,
                          access_protocol=access_protocol_v1)

    def test_unreachable_IP_switch(self):
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address='104.0.1.117', vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=access_protocol_v1)
