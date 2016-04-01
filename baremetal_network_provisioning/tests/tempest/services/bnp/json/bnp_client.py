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

from oslo_serialization import jsonutils as json
from tempest.lib.common import rest_client as service_client


class BnpClientJSON(service_client.RestClient):

    @classmethod
    def setup_clients(cls):
        super(BnpClientJSON, cls).setup_clients()
        cls.sw_client = cls.os_adm.network_client
        cls.sw_identity_admin_client = cls.os_adm.tenants_client

    version = '2.0'
    uri_prefix = "v2.0"

    def get_uri(self, plural_name):
        # get service prefix from resource name

        # The following list represents resource names that do not require
        # changing underscore to a hyphen
        hyphen_exceptions = ["service_profiles"]
        # the following map is used to construct proper URI
        # for the given neutron resource
        service_resource_prefix_map = {
            'bnp-switch': '',
        }
        service_prefix = service_resource_prefix_map.get(
            plural_name)
        if plural_name not in hyphen_exceptions:
            plural_name = plural_name.replace("_", "-")
        if service_prefix:
            uri = '%s/%s/%s' % (self.uri_prefix, service_prefix,
                                plural_name)
        else:
            uri = '%s/%s' % (self.uri_prefix, plural_name)
        return uri

    def pluralize(self, resource_name):
        # get plural from map or just add 's'
        # map from resource name to a plural name
        # needed only for those which can't be constructed as name + 's'
        resource_plural_map = {
            'bnp_switch': 'bnp_switches',
        }
        return resource_plural_map.get(resource_name, resource_name + 'es')

    def serialize(self, data):
        return json.dumps(data)

    def _creater(self, resource_name):
        def _create(**kwargs):
            plural = self.pluralize(resource_name)
            uri = self.get_uri(plural)
            post_data = self.serialize({resource_name: kwargs})
            resp, body = self.post(uri, post_data)
            body = self.deserialize_single(body)
            self.expected_success(201, resp.status)
            return service_client.ResponseBody(resp, body)
        return _create

    def b_create_switch(self, ip_address, vendor,
                        access_protocol, **access_parameters):
        uri = '%s/bnp-switches' % (self.uri_prefix)
        body = {"bnp_switch": {"access_parameters": access_parameters,
                               "vendor": vendor, "ip_address": ip_address,
                               "access_protocol": access_protocol}}
        body = json.dumps(body)
        resp, body = self.post(uri, body)
        self.expected_success(201, resp.status)
        body = json.loads(body)
        return body

    def b_list_switches(self):
        uri = '%s/bnp-switches' % (self.uri_prefix)
        resp, body = self.get(uri)
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return body

    def b_update_switch(self, switch_id):
        uri = '%s/bnp-switches/%s' % (self.uri_prefix, switch_id)
        body = {"bnp_switch": {"enable": "False"}}
        body = json.dumps(body)
        resp, body = self.put(uri, body)
        self.expected_success(200, resp.status)
        return True

    def b_delete_switch(self, switch_id):
        uri = '%s/bnp-switches/%s' % (self.uri_prefix, switch_id)
        resp, body = self.delete(uri)
        self.expected_success(204, resp.status)
        return True
