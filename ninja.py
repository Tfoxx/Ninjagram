import sys
import instaloader
import getpass
class Ninja():
    def __init__(self,username,password,target):
        self.username = username
        self.password = password
        self.target = target
        self.engine = instaloader.Instaloader()
    def Following_Fallower(self):
        self.engine.login(self.username,self.password)
        profile = instaloader.Profile.from_username(self.engine.context,self.username)
        follow_list = []
        count = 0
        for followee in profile.get_followers():
            follow_list.append(followee.username)
            count = count + 1
        fallowing_list = []
        for x in profile.get_followees():
            fallowing_list.append(x.username)
            count = count + 1
        difference = set(fallowing_list).symmetric_difference(set(follow_list))
        list_difference = list(difference)
        print("these are who don't follow you or who  you don't follow ")
        for x in list_difference:
            print(x)
    def profile_picture(self):
        profile = instaloader.Profile.from_username(self.engine.context,self.target)
        print(profile.profile_pic_url)

try:
    username =input("enter your username: ")
    password =getpass.getpass(prompt="enter your password: ")
except instaloader.exceptions.ConnectionException :
    print("Connection Error . Please check your internet connection")
    sys.exit(1)
except instaloader.exceptions.BadCredentialsException:
    print("Login Error")
    sys.exit(1)
except instaloader.BadResponseException:
    print("Bad Response")    
    sys.exit(1)

target = input("target username name : ")
Ninja_start = Ninja(username,password,target)
Ninja_start.Following_Fallower()
Ninja_start.profile_picture()