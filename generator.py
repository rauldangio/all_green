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


def make_commit():
    date = get_date()
    print(date)
    os.system(f"echo {date} > file.txt")
    os.system("git add file.txt")
    os.system(f"git commit -m 'commit' --date={date} -q")
    

def push_commit(start,end):
    while start < end:
        make_commit()
        start+=1
        os.system("git push origin master -q")


def main():
    push_commit(start,end)



if __name__ == '__main__':
    main()