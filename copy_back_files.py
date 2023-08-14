import os

SQL_BACKUP_PATCH = '\\\kas-crc-sql01\\f$\\SQLBackups\\KAS-CRC-SQL01\\'
current_folder = 'prod.toir\\FULL\\'

dir_list = os.listdir(SQL_BACKUP_PATCH + current_folder)

for f in dir_list:
    print(f)