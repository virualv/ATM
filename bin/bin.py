# Author : virualv
# Time : 9/29/2018 11:16 PM
import sys,os
# 将根目录ATM的绝对路径加入环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from modules import main
from modules import account_admin
print('''
-------------Main Port-------------
1.KitBar Bank
2.KitBar Super Market
''')
if __name__ == '__main__':
    def bank():
        print('''
        -------------User Login-------------
        1.Administrator
        2.User
        ''')
        user_class = {
            '1':account_admin.admin,
            '2':main.run
        }
        No = input('>>>').strip()
        if No in user_class:
            user_class[No]()
    def shop():
        pass
    mainport = {
        '1':bank,
        '2':shop
    }
    mport = input('>>>').strip()
    if mport in mainport:
        mainport[mport]()