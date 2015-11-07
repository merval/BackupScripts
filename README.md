# BackupScripts
Homedir Bash Backup Scripts | Written and/or Modified by Dan Walker

If you intend on backing up everything in /home/<users>, you can use home-backup to automatically backup everything within those directories to /backup/users/.

The home-backup script is modified from the default-backup which is/was available on Ubuntu’s website for scripted backups. 

If you use MySQL, you can use mysql-backup, which will backup every database you have. Which is very nice, if you have lots of databases. There isn’t a script to restore though, you can use phpmyadmin to import.

The restore-home script is really the bread and butter of this script set. It allows you to restore folders or files from a specific backup. I spent quite sometime working this one out, making sure it worked correctly. For awhile, I hosted websites on a server in my apartment and used these scripts to automate the backup process. It worked very well.

#Using The Backup Scripts
1. Schedule home-backup with cron or some other scheduling service.
2. Let the magic happen.

#Using The Restore Script
1. Run the script and follow the prompts.


#To-Do
1. Institute error handling across the board. Right now, the scripts expect everything to be “perfect”. 
2. Include optional FTP/Cloud push for backups.

Please feel free to use as your wish and modify for your own needs.
