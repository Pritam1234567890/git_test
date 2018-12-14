
###################
# DATA STRUCTURES #
###################
import calendar
import os
import platform
import time
print("\033[91m")
print("\033[88m///////////////////-\n!SYSTEM STRUCTURES!"+" "+time.ctime()+"\n///////////////////-")
def cal():
    print("----------\n","\calendar\n",'-------------')
    try:
        year = int(input("year: "))
        month = int(input("month: "))
        if month <=12:
            v = calendar.month(year,month)
            print(v)
    except Exception:
        cal()

def sys():
    print("your os is",platform.system())
    print("version:",platform.dist())
    print("pc bite",platform.machine())
    print("user name:",platform.node())
def o():
    print("your directory:",os.getcwd())
    print("your file on this dir\n||||",*os.listdir(),sep='\n')
    print("1)change dir\n2)main_manu")
    def o2():
            try:
                ch = input("dir_name:")
                v= os.chdir(ch)
                print(os.getcwd())
                print("\033[32myour file\n","|||",*os.listdir(),sep='\n')
            except Exception:
                o2()

    num = input("write:")
    if num == '1':
        print(os.getcwd())
        o2()
        o()
    elif num == '2':
        bar()
    elif num !='1' or num !='2':
        o()
def bar():
    print("\33[91m1)system infu\n2)calendar\n3)pwd")
    i = input("\033[1mchoose: ")
    if i=='1':
        sys()
        bar()
    elif i =='2':
        cal()
        bar()
    elif i=='3':
        o()
        bar()
    elif i != '1' or '2':
        print("****")
        bar()
bar()
