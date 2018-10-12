# Author : virualv
# Time : 9/29/2018 11:21 PM
import json
import os

def user_add(id):
    user_default = {'id':id}
    user_default['name'] = input('Set username:')
    user_default['gander'] = input('Set gander:')
    user_default['key'] = input('Set password:')
    user_default['status'] = 'unlocked'
    flag = input('Whether to customize the balance?[y/n]')
    if flag == 'y':
        user_default['balance'] = float(input('Balance:'))
    user_default.setdefault('balance',15000)
    user_default['amount'] = user_default['balance']
    os.chdir('..'+os.sep+'database')
    f = open(user_default['id']+'.dbl','w')
    json.dump(user_default,f)

def user_del(id):
    os.chdir('..' + os.sep + 'database')
    os.remove(id+'.dbl')

if __name__ == '__main__':
    id = input("id:")
    user_add(id)

def admin():
    menu ='''
    ------------------Function Menu------------------
    1.Adduser
    2.Deluser
    3.exit
    '''
    print(menu)
    choose = {
        '1':user_add,
        '2':user_del,
        '3':exit
    }
    num = input('>>>').strip()
    userid = None
    if num in ('1','2'):
        userid = input('ID:').strip()
    else:pass
    if num in choose:
        choose[num](userid)

