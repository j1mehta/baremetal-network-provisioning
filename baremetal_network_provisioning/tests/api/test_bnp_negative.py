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

from neutron.tests.api import base

from oslo_config import cfg

from baremetal_network_provisioning.tests.tempest import config

from tempest.lib import exceptions as lib_exc

config.register_options()
CONF = cfg.CONF
sw_ip_address = CONF.hpe_bnp.sw_ip_address
sw_ip_address_inv = CONF.hpe_bnp.sw_ip_address_inv
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

    """
    Tests the negative scenarios in the BNP API using the REST client for
    BNP
    """

    def test_invalid_community(self):
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=sw_ip_address, vendor=vendor,
                          access_parameters=access_parameter_inv,
                          access_protocol=access_protocol_v1)

    def test_invalid_snmp_v1_protocol(self):
        acc_proto = access_protocol_v1 + 'xyz'
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=sw_ip_address, vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=acc_proto)

    def test_invalid_snmp_v2c_protocol(self):
        acc_proto = access_protocol_v2c + 'xyz'
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=sw_ip_address, vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=acc_proto)

    def test_invalid_snmp_v3_protocol(self):
        acc_proto = access_protocol_v3 + 'xyz'
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=sw_ip_address, vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=acc_proto)

    def test_invalid_IP_switch(self):
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=sw_ip_address_inv,
                          vendor=vendor, access_parameters=access_parameter,
                          access_protocol=access_protocol_v1)

    def test_unreachable_IP_switch(self):
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address='104.0.1.117', vendor=vendor,
                          access_parameters=access_parameter,
                          access_protocol=access_protocol_v1)

    def test_invalid_vendor(self):
        self.assertRaises(lib_exc.BadRequest,
                          self.admin_client.create_bnp_switche,
                          ip_address=sw_ip_address, vendor='invalid_vendor',
                          access_parameters=access_parameter,
                          access_protocol=access_protocol_v1)
