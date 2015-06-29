'''
Created on 20150420

@author: liyankun
'''

from novaclient import user_info 
client = user_info.client

ipsan = {'auth_method':'ttt',
          'ip': '192.168.2.206',
           'password': 'dcfgn',
           'port': '4',
           'target': 'youyun',
           'username':'lioveni',
           'size': '4',
           'status': 'free'}

if __name__ == "__main__":
    print client.ipsan.create(ipsan)


