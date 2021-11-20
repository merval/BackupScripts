"""
This is a complete rewrite / port of the original Bash Script backups
"""
from utils import get_hostname, get_day_number, get_day_name, get_month_number, make_tarfile, check_backup_dir, \
    list_user_homes


class Backup:
    def __init__(self, home_dir, backup_dir):
        self.dest = backup_dir
        self.home_dir = home_dir
        self.hostname = get_hostname()
        self.day_num = get_day_number()
        self.day_name = get_day_name()
        self.week_file = None
        self.month_file = None
        self.archive_file = None
        self.__weekly_backup_name_gen()
        self.__monthly_backup_name_gen()

    def __weekly_backup_name_gen(self):
        if self.day_num < 7:
            self.week_file = "-week1.tgz"
        elif 7 < self.day_num < 14:
            self.week_file = "-week2.tgz"
        elif 14 < self.day_num < 21:
            self.week_file = "-week3.tgz"
        elif 21 < self.day_num < 32:
            self.week_file = "-week4.tgz"

    def __monthly_backup_name_gen(self):
        month_num = get_month_number() % 2
        if month_num == 0:
            self.month_file = "-month2.tgz"
        else:
            self.month_file = "-month1.tgz"

    def __gen_archive_name(self, name):
        if self.day_num == 1:
            self.archive_file = f"{self.dest}/{name}{self.month_file}"
        elif self.day_name != "Saturday":
            self.archive_file = f"{self.dest}/{name}{self.day_name}.tgz"
        else:
            self.archive_file = f"{self.dest}/{name}{self.week_file}"

    def single_directory(self, directory):
        check_backup_dir(self.dest)
        self.__gen_archive_name(self.hostname)
        make_tarfile(self.archive_file, directory)

    def users_dir_backup(self):
        self.dest = f"{self.dest}/users"
        check_backup_dir(self.dest)
        for user in list_user_homes(self.home_dir):
            self.__gen_archive_name(user)
            make_tarfile(self.archive_file, f'/Users/{user}')


class Restore:
    # TODO: The original shell script has far too many prompts work out how to vastly improve the logic and speed
    def __init__(self):
        raise NotImplementedError('Feature coming soon.')
