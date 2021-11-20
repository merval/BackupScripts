import socket
import datetime
import tarfile
import os.path
import os


def check_backup_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_hostname():
    return socket.gethostname()


def get_day_name():
    now = datetime.datetime.now()
    return now.strftime("%A")


def get_day_number():
    now = datetime.datetime.now()
    return int(now.strftime("%d"))


def get_month_number():
    now = datetime.datetime.now()
    return int(now.strftime("%m"))


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        for root, dirs, files in os.walk(source_dir):
            for f in files:
                try:
                    tar.add(os.path.join(root, f))
                except (PermissionError, IOError):
                    pass
            for d in dirs:
                try:
                    tar.add(os.path.join(root, d), recursive=False)
                except (PermissionError, IOError):
                    pass


def list_user_homes(path):
    users = os.listdir(path)
    if ".localized" in users:
        users.remove('.localized')
    if "Shared" in users:
        users.remove('Shared')
    return users
