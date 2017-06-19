import requests
from key import ACCESS_TOKEN
import urllib

Base_url = 'https://api.instagram.com/v1/'

def self_info():
    url_my = Base_url +'users/self/?access_token=%s' % (ACCESS_TOKEN)
    print url_my
    info = requests.get(url_my).json()
    if info['meta']['code'] == 200:
        print "Username: %s" % (info['data']['username'])
        print "User Id: %s" % (info['data']['id'])

    else:
        print 'Error 404.Link not found.'

def self_post():
    url_post = Base_url + 'users/self/media/recent/?access_token=%s' % (ACCESS_TOKEN)
    print url_post
    info_post = requests.get(url_post).json()
    if info_post['meta']['code'] == 200:
        var = 0
        print "Choose from the following post."
        while var < len(info_post['data']):
            print '%d.%s'%(var + 1, info_post['data'][var]['id'])
            var = var + 1
        var_new = int(raw_input("Enter the option."))
        var_new =var_new-1
        if var_new < len(info_post['data']):
            new_image_name = info_post['data'][var_new]['id'] + ".jpeg"
            new_image_link = info_post['data'][var_new]['images']['standard_resolution']['url']
            urllib.urlretrieve(new_image_link, new_image_name)
            print 'Download Successful.'

        else:
            print "Enter a valid option."




def user_info(username):
    new_url = Base_url + 'users/search?q=%s&access_token=%s' % (username, ACCESS_TOKEN)
    print new_url
    info_user = requests.get(new_url).json()
    if info_user['meta']['code'] == 200:
        user_id = info_user['data'][0]['id']
        print "User id: %s" % (user_id)
        return user_id

    else:
        print "Username Doesn't Exists."



def user_post():
    id1 = user_info('rahul_kr777')
    url = Base_url + 'users/%s/media/recent/?access_token=%s' % (id1, ACCESS_TOKEN)
    print url
    new_user = requests.get(url).json()
    if new_user['meta']['code'] == 200:
        varae =0
        print "Choose from the option."
        while varae < len(new_user['data']):
            print "%d.%s" %(varae+1, new_user['data'][varae]['images']['standard_resolution']['url'])
            varae = varae + 1
        var_a = int(raw_input("Option."))
        image_name = new_user['data'][var_a-1]['id'] + ".jpeg"
        image_url = new_user['data'][var_a-1]['images']['standard_resolution']['url']
        urllib.urlretrieve(image_url, image_name)
        print image_name


    else:
        print "Sorry."

def media_id():
    url_new = Base_url + 'users/self/media/recent/?access_token=%s' % (ACCESS_TOKEN)
    print url_new
    media = requests.get(url_new).json()
    if media['meta']['code']==200:
        print "Choose Media: "
        new_var1 = 0
        while new_var1<len(media['data']):
            print "%d. %s" % (new_var1+1, media['data'][new_var1]['id'])
            new_var1 = new_var1 + 1
        choose_var = int(raw_input("Choose From Above."))
        return media['data'][choose_var-1]['id']

    else:
        print "Error 404.\nLink Doesn't Exist."

    return None

def like_post():
    media_id1 = media_id()
    urlnew = Base_url + 'media/%s/likes/?access_token=%s' % (media_id1, ACCESS_TOKEN)
    print urlnew
    like_info = requests.get(urlnew).json()
    if like_info['meta']['code'] == 200:
        for x in range(0, len(like_info['data'])):
            print like_info['data'][x]['username']

    else:
        print "Check The Link."
def like_a_post():
    media_id2 = media_id()
    url_like = Base_url + 'media/%s/likes' % (media_id2)
    payload = {'access_token': ACCESS_TOKEN}
    post_a_like = requests.post(url_like, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Successful.'
    else:
        print 'Unsucessful.'


def get_comments():
    media_id_3 = media_id()
    my_url = Base_url + 'media/%s/comments?access_token=%s' % (media_id_3, ACCESS_TOKEN)
    comment = requests.get(my_url).json()
    if comment['meta']['code'] == 200:
        for x in range(0, len(comment['data'])):
            print 'Username:%s' % (comment['data'][x]['from']['username'])
            print 'Comment:%s' % (comment['data'][x]['text'])
    else:
        print 'No Comments.'



def post_comment():
    media_new =media_id()
    url_1 = Base_url + 'media/%s/comments' %(media_new)
    text = raw_input("Enter the comment.")
    payload_post = {'access_token' : ACCESS_TOKEN,'text' : text }
    comment_post = requests.post(url_1, payload_post)
    if comment_post['meta']['code'] == 200:
        print 'Successful.'
    else:
        print 'Please try again.'

def del_comment():
    new_media_id = media_id()
    url_next = Base_url + 'media/%s/comments/?access_token=%s' % (new_media_id, ACCESS_TOKEN)
    cmnt =requests.get(url_next).json()
    if cmnt['meta']['code'] == 200:
        print 'Choose Comment'
        for x in range(0,len(cmnt['data'])):
            v =int(x)
            print '%s. %s' % (v+1, cmnt['data'][x]['text'])
        var =int(raw_input('Enter The Option.'))
        data = cmnt['data'][var-1]['id']
        url_now =Base_url + 'media/%s/comments/%s?access_token=%s' %(new_media_id, data, ACCESS_TOKEN)
        comment_del = requests.delete(url_now)
        if comment_del['data']['meta'] == 200:
            print 'Successful.'
        else:
            print 'Try Again.'

        if len(cmnt['data']) == 0:
            print 'No Comments.'
    else:
        print 'Error.'
        return None










def choose_post():
    choose = True
    print 'Welcome to InstaBot.'

    while choose:
         option = int(raw_input("Choose from \n1.Self Info. \n2.Self Post. \n3.UserID. \n4.UserPost. \n5.List of People like the Post.\n6.Like a Post.\n7.Get Comments.\n8.Post a comment\n9.Delete a comment \n10.Exit.\n"))
         if option == 1:
             self_info()
         elif option == 2:
             self_post()
         elif option == 3:
             usr_id= user_info('rahul_kr777')
         elif option==4:
             user_post()
         elif option == 5:
             like_post()
         elif option==6 :
             like_a_post()
         elif option == 7:
             get_comments()
         elif option == 8:
             post_comment()
         elif option == 9:
             del_comment()
         elif option == 10:
             print 'Thank You. Have a great day.'
             choose=False



choose_post()