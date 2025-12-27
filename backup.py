import subprocess

MYSQLDUMP_PATH = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"
MYSQL_PATH = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"

def backup():
    subprocess.run([
        MYSQLDUMP_PATH,
        "-u", "root",
        "-p",
        "universite"
    ], stdout=open("universite_dump.sql", "w"))

def restore():
    subprocess.run([
        MYSQL_PATH,
        "-u", "root",
        "-p",
        "universite_test"
    ], stdin=open("universite_dump.sql", "r"))

if __name__ == "__main__":
    backup()
