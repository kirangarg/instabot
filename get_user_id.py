import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
def get_user_id(insta_username):
    #functions logic
    def get_user_id(insta_username):
        request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        user_info = requests.get(request_url).json()
