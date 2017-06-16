import requests
from key import ACCESS_TOKEN
import urllib

Base_url = 'https://api.instagram.com/v1/'


def user_info(username):
    new_url = Base_url + 'users/search?q=%s&access_token=%s' % (username, ACCESS_TOKEN)
    print new_url
    info_user = requests.get(new_url).json()
    if info_user['meta']['code'] == 200:
        user_id = info_user['data'][0]['id']
        print "User id:%s" % (user_id)
        return user_id
    else:
        print "Username Doesn't Exists."
    return None


def user_details():
    id1 = user_info('rahul_kr777')
    url = Base_url + 'users/%s/media/recent/?access_token=%s' % (id1, ACCESS_TOKEN)
    print url
    new_user = requests.get(url).json()
    if new_user['meta']['code'] == 200:
        if len(new_user['data']):
            image_name = new_user['data'][0]['id'] + ".jpeg"
            image_url = new_user['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            return new_user['data'][0]['id']


    else:
        print "Sorry."

    return None


user_details()
