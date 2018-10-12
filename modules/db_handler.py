import os,json
# 读取用户信息
def db_port(user_id):
    os.chdir('..' + os.sep + 'database')
    fsql = open(user_id + '.dbl', 'r')
    user_default = json.load(fsql)
    fsql.close()
    return user_default
# 刷新写入用户信息
def db_w_port(user_default):
    os.chdir('..' + os.sep + 'database')
    fsql = open(user_default['id'] + '.dbl', 'w')
    json.dump(user_default,fsql)
    fsql.flush()
    fsql.close()

# test
if __name__ == '__main__':
    user1 =  db_port('001')
    user1['balance'] = 200
    db_w_port(user1)