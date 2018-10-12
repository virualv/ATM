from modules import user_authapi,db_handler,account_admin,logger
from conf import setting
# 主函数，用于引入到用户接口
def run():
    menu ='''
    ------------------Function Menu------------------
    1.View User Account Information
    2.Withdrawal
    3.Repayment
    4.Transfer
    5.exit
    '''
    print(menu)
    choose = {
        '1':user_authapi.view_account_info,
        '2':user_authapi.withdrawal_cash,
        '3':user_authapi.pay_back,
        '4':user_authapi.transfer_,
        '5':exit
    }
    num = input('>>>').strip()
    if num in choose:
        choose[num]()

