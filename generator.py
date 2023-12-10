import os
import random

start = 0
end = 45000

def get_date():
    day = random.randint(1,31)
    mouth = random.randint(1,12)
    year = random.randint(2022,2023)
    date = f'{year}/{mouth}/{day}'

    return date


def make_commit(date):
    while start <= 45000:
        print(date)
        os.system(f"echo {date} > file.txt")
        os.system("git add file.txt")
        os.system(f"git commit -m 'commit' --date={date} -q")
    

def main():
    date = get_date()
    make_commit(date)
    os.system('git push origin master')


if __name__ == '__main__':
    main()