'''
Created on 20150420

@author: liyankun
'''

from novaclient.v1_1.contrib import ipsans
from novaclient.v1_1 import client as nova_client
from novaclient.v1_1.contrib import ipsans

user_info = {
             'username': 'admin',
             'passwd': 'admin',
             'tenant': 'admin',
             'authurl' : 'http://192.168.2.206:5000/v2.0'
             }
class ExtensionManagerMeta(object):
    def __init__(self, name, manager_class):
        self.name = name
        self.manager_class = manager_class
        
extensions = [ExtensionManagerMeta('ipsan', ipsans.IpsanManager)]

client = nova_client.Client(user_info.get('username'), user_info.get('passwd'),
                     project_id=user_info.get('tenant'), auth_url=user_info.get('authurl'),
                     extensions=extensions)
client.ipsan.get()
