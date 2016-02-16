from neutron.tests.api import base
from tempest_lib import exceptions as lib_exc
import telnet_utils

ip_address = "105.0.1.107"
ip_address_invalid = "105.0.1.266"
ip_address_unreachable = ""
sw_usr = 'sdn'
sw_passwd = 'skyline'
telnet_port = 23
vendor = "hp"
access_parameter = {"write_community": "public"}
access_parameter_priv = {"write_community": "private"}
access_protocol_v1 = "snmpv1"
access_protocol_v2c = "snmpv2c"
access_protocol_v3 = "snmpv3"
access_parameter_v3 = {"write_community": "public", "security_name":"bmnpusr33", "auth_protocol": "md5", "auth_key":"abcdabcdd", "priv_protocol": "des56", "priv_key":"abcdabcdd"}

class BMNPExtensionTestJSON(base.BaseAdminNetworkTest):
    _interface = 'json'

    def test_create_show_list_update_delete_switch_snmpv1(self):
        self.admin_client.create_bnp_switch(ip_address=ip_address,vendor=vendor,access_parameters=access_parameter, access_protocol=access_protocol_v1) 
        switch_list = self.admin_client.list_bnp_switches()
        switch_id = switch_list["bnp_switches"][0]['id']
        print switch_list
        switch = self.admin_client.show_bnp_switche(switch_id)
        print switch
        switch = self.admin_client.update_bnp_switche(switch_id, enable='false')
        print switch
        self.admin_client.delete_bnp_switche(switch_id)
        
    def test_create_show_list_update_delete_switch_snmpv2c(self):
        self.admin_client.create_bnp_switch(ip_address=ip_address,vendor=vendor,access_parameters=access_parameter,access_protocol=access_protocol_v2c) 
        switch_list = self.admin_client.list_bnp_switches()
        switch_id = switch_list["bnp_switches"][0]['id']
        print switch_list
        switch = self.admin_client.show_bnp_switche(switch_id)
        print switch
        switch = self.admin_client.update_bnp_switche(switch_id, enable='false')
        print switch
        self.admin_client.delete_bnp_switche(switch_id)

    def test_create_show_list_update_delete_switch_snmpv3(self):
        self.admin_client.create_bnp_switch(ip_address=ip_address,vendor=vendor,access_parameters=access_parameter_v3,access_protocol=access_protocol_v3)
        switch_list = self.admin_client.list_bnp_switches()
        switch_id = switch_list["bnp_switches"][0]['id']
        print switch_list
        switch = self.admin_client.show_bnp_switche(switch_id)
        print switch
        switch = self.admin_client.update_bnp_switche(switch_id, enable='false')
        print switch
        self.admin_client.delete_bnp_switche(switch_id)

    def test_snmp_disabled_switch_discovery(self):
        tn = telnet_utils.connect_to_switch(ip_address,telnet_port,sw_usr,sw_passwd,10)
        telnet_utils.run_cmd_op(tn,"sys")
        x=telnet_utils.run_cmd_op(tn,"undo snmp-agent")
        self.assertRaises(lib_exc.BadRequest, self.admin_client.create_bnp_switche,ip_address=ip_address,vendor=vendor,access_parameters=access_parameter, access_protocol=access_protocol_v1)
        x=telnet_utils.run_cmd_op(tn,"snmp-agent")

    def test_invalid_snmp_v1_protocol(self):
        acc_proto = access_protocol_v1 + 'xyz'
        self.assertRaises(lib_exc.BadRequest, self.admin_client.create_bnp_switche,ip_address=ip_address,vendor=vendor,access_parameters=access_parameter, access_protocol=acc_proto)

    def test_invalid_snmp_v2c_protocol(self):
        acc_proto = access_protocol_v2c + 'xyz'
        self.assertRaises(lib_exc.BadRequest, self.admin_client.create_bnp_switche,ip_address=ip_address,vendor=vendor,access_parameters=access_parameter, access_protocol=acc_proto)

    def test_invalid_snmp_v3_protocol(self):
        acc_proto = access_protocol_v3 + 'xyz'
        self.assertRaises(lib_exc.BadRequest, self.admin_client.create_bnp_switche,ip_address=ip_address,vendor=vendor,access_parameters=access_parameter, access_protocol=acc_proto)

    def test_invalid_IP_switch(self):
        self.assertRaises(lib_exc.BadRequest, self.admin_client.create_bnp_switche,ip_address=ip_address_invalid,vendor=vendor,access_parameters=access_parameter,access_protocol=access_protocol_v1)

    def test_unreachable_IP_switch(self):
        self.assertRaises(lib_exc.BadRequest, self.admin_client.create_bnp_switche, ip_address=ip_address_unreachable,vendor=vendor,access_parameters=access_parameter,access_protocol=access_protocol_v1)
   
    def test_create_duplicate_switch(self):
        self.admin_client.create_bnp_switche(ip_address=ip_address,vendor=vendor,access_parameters=access_parameter, access_protocol=access_protocol_v1) 
        switch_list = self.admin_client.list_bnp_switches()
        self.assertRaises(lib_exc.Conflict, self.admin_client.create_bnp_switche,ip_address=ip_address,vendor=vendor,access_parameters=access_parameter,access_protocol=access_protocol_v1)
        switch_id = switch_list["bnp_switches"][0]['id']
        switch = self.admin_client.update_bnp_switche(switch_id, enable='false')
        self.admin_client.delete_bnp_switche(switch_id)
