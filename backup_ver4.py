import os
import time

sourse = ['"C:\\BackupTest"']

target_dir = 'D:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter your comment -->')
 
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Directory created successfully', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(sourse))

if os.system(zip_command) == 0:
    print('The backup was successfully created in', target)
else:
    print('Backup Failed')