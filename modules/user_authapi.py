from modules import db_handler,logger
flag = False
# 账户认证
def auth_user(f):
    def auth_inner(*args):
        user_id = input('UserID:')
        user_default = db_handler.db_port(user_id)
        n = 3
        global flag
        if user_default['status'] == 'unlocked':
            if not flag:
                while n > 0:
                    user_name = input('Username:')
                    user_passwd = input('Password:')
                    if user_name == user_default['name'] and user_passwd == user_default['key']:
                        print('Login Success!')
                        flag = True
                        break
                    else:
                        print('Invalid user or password, please re-enter')
                        n += 1
                        continue
                else:print('Your login frequency is already reach the upper limit,your account has been locked!')
            else:pass
            print()
            f(*args,user_default)
        else:
            print('You account is frost!')
            pass
    return auth_inner
# 查看信息
@auth_user
def view_account_info(user_info):
    for i in user_info.keys():
        print(i+':'+str(user_info[i]))
# 提现
@auth_user
def withdrawal_cash(user_info):
    while True:
        _withdrawal_ = float(input('Please enter your withdrawal amount:'))
        withdrawal_sum = _withdrawal_*(1+0.05)
        if withdrawal_sum <= user_info['balance']:
            user_info['balance'] -= withdrawal_sum
            logger.Log.info('ID:%s,Balance:%f,Change:-%f,Withdraw:%f,Service Fee:%f'%(user_info['id'],['balance'],withdrawal_sum,_withdrawal_,(0.05*_withdrawal_)))
            db_handler.db_w_port(user_info)
            print('Withdraw Success!\nYour current account balance :'+str(user_info['balance']))
        else:
            logger.Log.error('Withdraw Failed!')
            print('''
            -------------------Menu-------------------
            1.re-enter
            2.exit
            ''')
            while True:
                _choose_ = input('>>>')
                if _choose_ == '1':
                    break
                elif _choose_ == '2':
                    break
                else:
                    print('Choice is Vailed ,re-enter!')
                    continue
            if _choose_ == '2':
                break
            else:continue
# 还款
@auth_user
def pay_back(user_info):
    if user_info['balance'] <= user_info['amount']:
        print('Your arrears is:%f'%(user_info['amount']-user_info['balance']))
        _repayment_ = float(input('Enter your repayment amount:'))
        user_info['balance'] += _repayment_
        logger.Log.info('ID:%s,Balance:%f,Change:+%f,Arrears:%f,Repayment:%f,Remaining arrears:%f' % (user_info['id'],user_info['balance'],_repayment_,user_info['amount']-user_info['balance'],_repayment_,user_info['amount']-user_info['balance']-_repayment_))
        db_handler.db_w_port(user_info)
        print('Repay Success!\nYour current arrears:%f and balance:%f'%((user_info['amount']-user_info['balance']),user_info['balance']))
    else:
        print('You have no debts!')
# 转账
@auth_user
def transfer_(user_info):
    print('Your current balance:'+str(user_info['balance']))
    other_id = input('Enter other id:')
    other_user = db_handler.db_port(other_id)
    while True:
        transfer_num = float(input('Enter transfer amount;'))
        if transfer_num*(1+0.05) > user_info['balance']:
            print('transfer amount too much,your account balance is not enough.\nPlease re-enter!')
            continue
        else:
            other_user['balance'] += transfer_num
            logger.Log.info('ID:%s,Get a $%f transfer'%(other_user['id'],transfer_num))
            db_handler.db_w_port(other_user)
            user_info['balance'] -= transfer_num*(1+0.05)
            logger.Log.info('ID:%s,Balance:%f,Change:-%f,Transfer:%f,Service Fee:%f'%(user_info['id'],user_info['balance'],transfer_num*1.05,transfer_num,0.05*transfer_num))
            db_handler.db_w_port(user_info)
            print('Transfer has finished!\nYour current balance :%f'%user_info['balance'])
            break
# 购物车扣款借口
@auth_user
def shopping_port(*args):
    user_info = args[1]
    if args[0] > user_info['balance']:
        print('Your account amount is not enough.')
        pass
    else:
        user_info['balance'] -= float(args[0])
        logger.Log.info('ID:%s,Balance:%f,Change:-%s' % (user_info['id'], user_info['balance'],args[0]))
        db_handler.db_w_port(user_info)
        print('Successful payment!\nYour current account balance :'+str(user_info['balance']))

# test
if __name__ == '__main__':
    view_account_info()
    withdrawal_cash()
    pay_back()
    transfer_()
    shopping_port()


