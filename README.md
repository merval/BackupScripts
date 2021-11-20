# BackupScripts
Python Backup Scripts | Written by Dan Walker

If you intend on backing up everything in your users home directories, you can use Backup(home_dir="/path/to/homes", backup_dir="/path_to_backups").users_dir_backup() to automatically backup everything within those directories to your backup directory in a "users" directory.

~~If you use MySQL, you can use mysql-backup, which will backup every database you have. Which is very nice, if you have lots of databases. There isn’t a script to restore though, you can use phpmyadmin to import.~~
There isn't yet a backup for mysql built into the python version.

~~The restore-home script is really the bread and butter of this script set. It allows you to restore folders or files from a specific backup. I spent quite sometime working this one out, making sure it worked correctly. For awhile, I hosted websites on a server in my apartment and used these scripts to automate the backup process. It worked very well.~~
Restore functionality coming soon.

#Using The Backup Scripts
1. Schedule the backup with cron or some other scheduling service.
2. Let the magic happen.


#To-Do
1. Flesh out the restore functionality, this should include simplifying the ability to restore without a slurry of questions.
2. Currently, doing backups is a single threaded operation. If you have a massive directory it could take a very long time to backup. Having a few worker threads that run through looking for files and directories would improve the speed.

Please feel free to use as your wish and modify for your own needs.
