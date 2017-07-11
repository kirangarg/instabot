from self_info import *
from get_user_info import *
from get_own_post import *
from get_user_post import *
from like_user_post import *
from comment_user_post import *
from delete_bad_comment import *
from like_list import *
from comment_list import *
#importing function files



def insta_bot():
    while True:
        #provide choices
        print "Welcome to instaBot!"
        print "Menu options:"
        print "1.Get your own details"
        print "2.Get details of a user by username"
        print "3.Get your own recent post"
        print "4.Get the recent post of a user by username"
        print "5.Like the recent post of a user"
        print "6.Make a comment on the recent post of a user"
        print "7.list of likes on recent post of a user"
        print "8.list of comments on a recnet post of a user"
        print "9.delete bad comment on recent post"
        print "10.Exit"

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
           like_list(user_name)
        elif choice == 8:
            user_name = raw_input("Enter the username of the user: ")
            comment_list(user_name)
        elif choice == 9:
            user_name = raw_input("Enter the username of the user: ")
            delete_bad_comment(user_name)
        elif choice == 10:
            exit()
        else:
            print "wrong choice"

