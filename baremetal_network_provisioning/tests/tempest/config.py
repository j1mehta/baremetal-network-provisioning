# Copyright (c) 2016 Hewlett-Packard Enterprise Development Company, L.P.
# All Rights Reserved.
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


from oslo_config import cfg

# BMNP related config information

hpe_bnp_opts = [

    cfg.StrOpt('sw_ip_address_inv',
               default='',
               help='Invalid switch IP address'),
    cfg.StrOpt('sw_ip_address',
               default='',
               help='Switch IP address'),
    cfg.StrOpt('sw_usr',
               default='',
               help='Switch user name to log in'),
    cfg.StrOpt('sw_passwd',
               default='',
               help='Switch password to log in'),
    cfg.StrOpt('vendor',
               default='',
               help='Specify vendor'),
    cfg.DictOpt('access_parameter',
                default='',
                help='access_parameter for snmp v1 and v2'),
    cfg.DictOpt('access_parameter_inv',
                default='',
                help='access_parameter with invalid community'),
    cfg.DictOpt('access_parameter_priv',
                default='',
                help='access_parameter_priv'),
    cfg.DictOpt('access_parameter_v3',
                default='',
                help='access_parameter for snmp v3'),
    cfg.StrOpt('access_protocol_v1',
               default='',
               help='access protocol snmpv1'),
    cfg.StrOpt('access_protocol_v2c',
               default='',
               help='access protocol snmpv2'),
    cfg.StrOpt('access_protocol_v3',
               default='',
               help='access protocol snmpv3'),

]


def register_options():
    cfg.CONF.register_opts(hpe_bnp_opts, "hpe_bnp")
