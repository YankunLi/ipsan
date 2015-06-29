# Copyright 2013 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from novaclient import base
from novaclient.openstack.common.gettextutils import _
from novaclient import utils


class Ipsan(base.Resource):
    def delete(self):
        self.manager.delete(network=self)
    
class IpsanManager(base.ManagerWithFind):
    resource_class = Ipsan

    def list(self):
        return self._list('/os-ipsans', 'ipsans')

    def get(self, ipsan):
        return self._get('/os-ipsans/%s' % ipsan.get('id'),
                         'ipsan')

    def delete(self, ipsan):
        self._delete('/os-ipsans/%s' % ipsan.get('id'))

    def create(self, ipsan):
        body = ipsan
        return self._create('/os-ipsans', body, 'ipsan')
    
    def update(self, ipsan):
        body = ipsan
        return self._update('/os-ipsans/%s' %ipsan.get('id'), body, response_key='ipsan' )
        pass



