# Author ='zuoxi'
#date =2018/1/3
#登录验证
# for i in range(100):
#     if i< 50 or i > 70:
#         print(i)

_username = "zuoxiaojun"
_passwd  = "1234567"

passed_authentication = False #假 ，初始判断登录不成功 flag

for i in range (3):
    username = input("username :")
    passwd = input("passwad :")
    if username == _username and passwd ==_passwd:
        print("welcome %s login" %_username)
        passed_authentication = True #真，登录成功
        break
    else:
        print("Invalid username or passwad!")
if not passed_authentication: #没登录成功
    print("三次都错了，还试个毛线")