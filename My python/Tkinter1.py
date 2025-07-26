# send multiple msg
'''import pyautogui
import time
time.sleep(4)
for _ in range(50):
    pyautogui.typewrite("its a hack")
    pyautogui.press("enter")'''
#send msg automatically
'''import pywhatkit as kit
import pyautogui

kit.sendwhatmsg("+919600044129","nkjednjk",17,24)
pyautogui.press("enter")'''


'''def fact(x):
 if x == 1:
    return 1
 else:
    return x * fact(x-1)
print(fact(4))'''

'''def sum(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+sum(arr[1:]) 
print(sum([1, 2, 3, 5]))'''
'''
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=3 
width=n+(n-1)+((n-1)*2)
x=n
o=0
p=""
for i in range(n):
    if x==n:
        print((lst[n]).center(width," "))
        x-=1
        o+=1
    else:'''

'''n = int(input())
arr = list(map(int, input().split())) 
if len(arr)==nbreak
print(arr)'''

def timeConversion(s):
    # Write your code here
    change_AM=["01","02","04","04","05","06","07","08","09","10","11","12"]
    change_PM=["13","14","15","16","17","18","19","20","21","22","23","00"]
    if "PM" in s:
        a=int(s[0:2])
        change_AM.index(a)
        return ()
    elif "AM" in s:
        return ("hello")    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()