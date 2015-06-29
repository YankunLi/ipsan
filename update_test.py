'''
Created on 20150420

@author: liyankun
'''
from novaclient import user_info  
client = user_info.client

ipsan = { 'id':5,
          'auth_method':'ttt',
          'ip': '192.168.2.226',
           'password': 'dcfgn',
           'port': '4',
           'target': 'shanghai',
           'username':'jjjjjjj',
           'size': '4',
           'status': 'free'}
client.ipsan.update( ipsan)

if __name__ == "__main__":
    print client.ipsan.update( ipsan)
