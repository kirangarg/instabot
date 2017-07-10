#all global variables are here
import requests
import urllib
#instagram api access token
APP_ACCESS_TOKEN = '2008525763.b4eff92.5d4acde85c564413bce58eb73cc55d84'
#instagram api base url
BASE_URL = 'https://api.instagram.com/v1/'

from self_info import *
from get_user_info import *
from get_own_post import *
from get_user_post import *
from like_user_post import *
from comment_user_post import *
from delete_bad_comment import *



def start_bot():
    while True:
        print "Welcome to instaBot!"
        print "Menu options:"
        print "1.Get your own details"
        print "2.Get details of a user by username"
        print "3.Get your own recent post"
        print "4.Get the recent post of a user by username"
        print "5.Like the recent post of a user"
        print "6.Make a comment on the recent post of a user"
        print "7.delete bad comment on recent post"
        print "8.Exit"

        choice = int(raw_input("Enter you choice: "))
        if choice == 1:
            self_info()
        elif choice == 2:
            user_name = raw_input("Enter the username of the user: ")
            get_user_info(user_name)
        elif choice == 3:
            get_own_post()
        elif choice == 4:
            user_name = raw_input("Enter the username of the user: ")
            get_user_post(user_name)
        elif choice == 5:
           user_name = raw_input("Enter the username of the user: ")
           like_user_post(user_name)
        elif choice == 6:
           user_name = raw_input("Enter the username of the user: ")
           comment_user_post(user_name)
        elif choice == 7:
            user_name = raw_input("Enter the username of the user: ")
            delete_bad_comment(user_name)
        elif choice == 8:
            exit()
        else:
            print "wrong choice"

start_bot()