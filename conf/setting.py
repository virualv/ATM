import os,logging
Base_Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def log_path():
    Log_Path = Base_Path+os.sep+'logs'
    return Log_Path
def log_type():
    type = 'access'
    return type
loggerLevel = logging.INFO

def db_path(db_type):
    if db_type == 'file_db':
        DB_Path = Base_Path+os.sep+'database'
        return DB_Path
if __name__=='__main__':
    print(log_path())
    print(db_path('file_db'))
