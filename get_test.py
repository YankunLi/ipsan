'''
Created on 20150420

@author: liyankun
'''

from novaclient import user_info  
client = user_info.client

if __name__ == "__main__":
    print client.ipsan.list()
