# Author : virualv
# Time : 9/29/2018 11:21 PM
import json
import os

def user_add(id):
    user_default = {'id':id}
    user_default['name'] = input('Set username:')
    user_default['gander'] = input('Set gander:')
    user_default['key'] = input('Set password:')
    flag = input('Whether to customize the balance?[y/n]')
    if flag == 'y':
        user_default['balance'] = input('Balance:')
    user_default.setdefault('balance',15000)
    os.chdir('..'+os.sep+'database')
    f = open(user_default['id']+'.sql','w')
    json.dump(user_default,f)

def user_del(id):
    os.chdir('..' + os.sep + 'database')
    os.remove(id+'.sql')

if __name__ == '__main__':
    id = input("id:")
    user_add(id)
    

