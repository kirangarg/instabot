#all global variables is here
import requests
#instagram api access token
APP_ACCESS_TOKEN = '2008525763.b4eff92.5d4acde85c564413bce58eb73cc55d84'
#instagram api base url
BASE_URL = 'https://api.instagram.com/v1/'
from like_user_post import *
from self_info import *
from get_user_info import *
from get_own_post import *
from delete_bad_comment import *
from comment_user_post import *

def start_bot():
    while True:
        print "Welcome to instaBot!\n"
        print "Menu options:\n"
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        print "5.Get a list of people who have liked the recent post of a user\n"
        print "6.Like the recent post of a user\n"
        print "7.Get a list of comments on the recent post of a user\n"
        print "8.Make a comment on the recent post of a user\n"
        print "9.Delete negative comments from the recent post of a user\n"
        print "10.Exit"

        choice = int(raw_input("Enter you choice: "))
        if choice == 1:
            self_info()
        elif choice == 2:
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == 3:
            get_own_post()
        elif choice == 4:
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
       #elif choice==5:
          #insta_username = raw_input("Enter the username of the user: ")
          #get_like_list(insta_username)
        elif choice==6:
           insta_username = raw_input("Enter the username of the user: ")
           like_user_post(insta_username)
        #lif choice==7:
         # insta_username = raw_input("Enter the username of the user: ")
          #get_comment_list(insta_username)
        elif choice==8:
           insta_username = raw_input("Enter the username of the user: ")
           comment_user_post(insta_username)
        elif choice==9:
           insta_username = raw_input("Enter the username of the user: ")
           delete_bad_comment(insta_username)
        elif choice == 10:
            exit()
        else:
            print "wrong choice"

start_bot()