# importing requests library

import requests
# fetching access_token from key.py
from key import ACCESS_TOKEN
# importing urllib library to download user data
import urllib
from textblob import TextBlob
from textblob.sentiments import  NaiveBayesAnalyzer
# Base_url is endpoint of instagram api
import numpy as  np
import matplotlib.pyplot as plt
Base_url = 'https://api.instagram.com/v1/'


# method to get our own info.
def self_info():
    # url for getting our info
    url_my = Base_url + 'users/self/?access_token=%s' % (ACCESS_TOKEN)
    print url_my
    # getting info in form of dictionaries. By using request library funtion
    info = requests.get(url_my).json()
    # checking whether the get request was successful or not.
    if info['meta']['code'] == 200:
        # Printing username and userid
        print "Username: %s" % (info['data']['username'])
        print "User Id: %s" % (info['data']['id'])
    # Handling other codes
    else:
        print 'Error 404.\nLink not found.'


# Creating method for getting own post
def self_post():
    # setting up url to get details.
    url_post = Base_url + 'users/self/media/recent/?access_token=%s' % (ACCESS_TOKEN)
    print url_post
    # getting info of post in form of dictionaries. By using request library funtion
    info_post = requests.get(url_post).json()
    # checking whether the get request was successful or not.
    if info_post['meta']['code'] == 200:
        # declaring variable var for runnig while loop.
        var = 0
        # choosing which post to be selected.
        print "Choose from the following post."
        # running a while loop to get all the recent post available.
        while var < len(info_post['data']):
            # printing var(variable) and post id
            print '%d.%s' % (var + 1, info_post['data'][var]['id'])
            var = var + 1
        # Choosing the post.
        var_new = int(raw_input("Enter the option:"))
        # since dictionaries start from 0.
        var_new = var_new - 1
        # checking for condition that chosen variable is option or not.
        if var_new < len(info_post['data']):
            # using urllib to download the desired post.
            new_image_name = info_post['data'][var_new]['id'] + ".jpeg"
            new_image_link = info_post['data'][var_new]['images']['standard_resolution']['url']
            urllib.urlretrieve(new_image_link, new_image_name)
            print '%s\nDownload Successful.' % (new_image_name)

        # if var_new is not valid.
        else:
            print "Enter a valid option."
    # if get request doesn't work.
    else:
        print "Error 404.\nLink not found."


# creating  function to get user info
def user_info(username):
    # setting up url to get details.
    new_url = Base_url + 'users/search?q=%s&access_token=%s' % (username, ACCESS_TOKEN)
    print new_url
    # getting info of user in form of dictionaries. By using request library funtion
    info_user = requests.get(new_url).json()
    # checking whether the get request was successful or not.
    if info_user['meta']['code'] == 200:
        # getting user id
        if len(info_user['data']) > 0:
            user_id = info_user['data'][0]['id']
            print "User id: %s" % (user_id)
            # return user id
            return user_id
        elif len(info_user['data']) == 0:
            print 'User is not available in Sandbox Mode.'
            exit()
    # if get request doesn't works
    elif info_user['meta']['code'] != 200:
        print "Username Doesn't Exists."
        exit()


# Getting user post
def user_post():
    # getting username from user(client)
    user = raw_input('Enter User Name.')
    # if user is empty.
    if len(user) == 0:
        print 'Enter a valid option.'
        exit()
    # calling user_info method
    id1 = user_info(user)
    # setting up url to get details.
    url = Base_url + 'users/%s/media/recent/?access_token=%s' % (id1, ACCESS_TOKEN)
    print url
    # getting info of user post in form of dictionaries. By using request library funtion
    new_user = requests.get(url).json()
    # checking whether the get request was successful or not.
    if new_user['meta']['code'] == 200:
        # declaring variable var for running while loop.
        var_1 = 0
        # choosing which post to be selected.
        print "Choose from the option."
        # running a while loop to get all the recent post available.
        while var_1 < len(new_user['data']):
            # printing var_1(variable) and post id
            print "%d.%s" % (var_1 + 1, new_user['data'][var_1]['id'])
            var_1 = var_1 + 1
        # Choosing the post.
        var_a = int(raw_input("Enter the Option:"))
        # since dictionaries start from 0.
        var_a = var_a - 1
        # checking for condition that chosen variable is option or not.
        if var_a < len(new_user['data']):
            # using urllib to download the desired post.
            image_name = new_user['data'][var_a]['id'] + ".jpeg"
            image_url = new_user['data'][var_a]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print image_name
        else:
            print 'Enter a valid option.'
    # if get request doesn't works
    else:
        print "Error 404\n Link is not valid. "


# Creating fucntion to get media id
def media_id():

    check = raw_input("For own post (Y/N):")
    if check.upper() == 'Y':
        url_new = Base_url + 'users/self/media/recent/?access_token=%s' % (ACCESS_TOKEN)
        print url_new
    elif check.upper() == 'N':
        usr_name = raw_input("Enter Username.")
        user_id = user_info(usr_name)
        url_new = Base_url + 'users/%s/media/recent/?access_token=%s' % (user_id, ACCESS_TOKEN)
        print url_new
    # getting info of user media in form of dictionaries. By using request library funtion
    media = requests.get(url_new).json()
    # checking whether the get request was successful or not.
    if media['meta']['code'] == 200:
        # choosing which post to be selected.
        print "Choose Media: "
        # declaring a variable for while loop.
        new_var1 = 0
        # running a while loop to get all the recent post available.
        while new_var1 < len(media['data']):
            print "%d. %s" % (new_var1 + 1, media['data'][new_var1]['id'])
            new_var1 = new_var1 + 1
        # Choosing the post id
        choose_var = int(raw_input("Choose From Above."))
        # since dictionaries start from 0.

        # checking for condition that chosen variable is option or not.
        if len(media['data']) >= choose_var > 0:
            # returning media id
            choose_var = choose_var - 1
            print media['data'][choose_var]['id']
            return media['data'][choose_var]['id']
        # if choosen option in not valid.
        else:
            print 'Enter a valid option.'

    # if get request doesn't works
    elif media['meta']['code'] != 200:
        print "Error 404.\nLink Doesn't Exist."

    return None


# Creating function to get  likes on post
def like_on_post():
    # getting media id from media_id() function
    media_id1 = media_id()
    # setting up url to get details.
    url_likes = Base_url + 'media/%s/likes/?access_token=%s' % (media_id1, ACCESS_TOKEN)
    print url_likes
    # getting likes of user media in form of dictionaries. By using request library function
    like_info = requests.get(url_likes).json()
    # checking whether the get request was successful or not.
    if like_info['meta']['code'] == 200:
        # using for loop for likes on post
        for x in range(0, len(like_info['data'])):
            print like_info['data'][x]['username']

    # if get request doesn't works
    else:
        print "Link doesn't exist."


# Creating function to like post
def like_a_post():
    # getting media id from media_id() function
    media_id2 = media_id()
    # setting up url
    url_like = Base_url + 'media/%s/likes' % (media_id2)
    # Setting up payload. Post request.
    payload = {'access_token': ACCESS_TOKEN}
    # To like a post
    post_a_like = requests.post(url_like, payload).json()
    # checking whether the post request was successful or not.
    if post_a_like['meta']['code'] == 200:
        print 'Successful.'
    # if post request doesn't work
    else:
        print 'Not Successful.'


# Getting comment on a post.
def get_comments():
    # getting media id from media_id() function
    media_id_3 = media_id()
    # setting up url
    my_url = Base_url + 'media/%s/comments?access_token=%s' % (media_id_3, ACCESS_TOKEN)
    print my_url
    # getting comments on user post in form of dictionaries. By using request library function
    comment = requests.get(my_url).json()
    # checking whether the get request was successful or not.
    if comment['meta']['code'] == 200:
        # checking range of comment posted on the media/post
        if 0 < len(comment['data']):
            for x in range(0, len(comment['data'])):
                # printing username and comment posted on post
                print 'Username: %s' % (comment['data'][x]['from']['username'])
                print 'Comment: %s' % (comment['data'][x]['text'])
            print "Successful."
        # if there are no comments
        elif len(comment['data']) == 0:
            print 'No Comments.'
    # if get request fails
    else:
        print "Link doesn't exist."


# Creating function to comment on a post
def post_comment():
    # getting media id from media_id() function
    media_new = media_id()
    # setting up url
    url_1 = Base_url + 'media/%s/comments' % (media_new)
    print url_1
    # Comment to be posted.
    text = raw_input("Enter the comment.")
    # Setting up payload. Post request.
    payload_post = {'access_token': ACCESS_TOKEN, 'text': text}
    # posting comments on user post in form of dictionaries. By using request library function
    comment_post = requests.post(url_1, payload_post).json()
    # checking whether the post request was successful or not.
    if comment_post['meta']['code'] == 200:
        print "Successfully posted."
    # post request doesn't works
    else:
        print "Not Successful."
        # checking whether the post request was successful or not.


# creating funtion to delete comments
def del_comment():
    # getting media id from media_id() function
    new_media_id = media_id()
    # setting up url
    url_next = Base_url + 'media/%s/comments?access_token=%s' % (new_media_id, ACCESS_TOKEN)
    # getting comments on user post in form of dictionaries. By using request library function
    cmnt = requests.get(url_next).json()
    # checking whether the get request was successful or not.
    if cmnt['meta']['code'] == 200:
        # Selecting comment to be deleted
        if len(cmnt['data']) != 0:

            for x in range(0, len(cmnt['data'])):
                blob =TextBlob(cmnt['data'][x]['text'],analyzer=NaiveBayesAnalyzer())
                blob.sentiment
                if blob.sentiment.p_pos < blob.sentiment.p_neg:
                    print cmnt['data'][x]['id']
                    data = cmnt['data'][x]['id']
                    url_now = Base_url + 'media/%s/comments/%s?access_token=%s' % (new_media_id, data, ACCESS_TOKEN)
            # Asking user to delete which comment
                    comment_del = requests.delete(url_now).json()
                    if comment_del['meta']['code'] == 200:
            # setting up url
                        print 'Successfully Deleted.'
            # deleting the comment from the post.
                    else:
                        print "There was a problem comment couldn't be deleted."
            # checking whether the delete request was successful or not.

        elif len(cmnt['data']) == 0:
            print 'There are no comments.'
    # if getting comment didn't work
    elif cmnt['meta']['code'] != 200:
        print 'There was a problem'


def frnd_hashtag():
    new_user_hash = media_id()

    url_hash = Base_url + 'media/%s?access_token=%s' % (new_user_hash, ACCESS_TOKEN)
    hash_req = requests.get(url_hash).json()
    if hash_req['meta']['code'] == 200:
        new_text =hash_req['data']['caption']['text']
        print hash_req['data']['caption']['text']
        i = 0
        count = 0
        while i < len(new_text):
            if new_text[i] == '#':
                count = count + 1
            i = i + 1

        hash = new_text.split('#', count)
        for x in range(1, len(hash)):
            blob = TextBlob(hash[x], analyzer=NaiveBayesAnalyzer())
            blob.sentiment

            plt.axis([0, len(hash), -1, 1])
            plt.xlabel("Interest")
            plt.xlabel("Post")
            post = 1
            if blob.sentiment.p_neg <= blob.sentiment.p_pos:
                point_y = blob.sentiment.p_pos
                line, =plt.plot(post, point_y, '-')
                post = post + 1
            else:
                point_y =blob.sentiment.p_neg
                line, = plt.plot(post, -point_y, '-')
                post = post + 1

        line.set_antialiased(False)
        plt.setp(line, color='r', linewidth=2.0)
        plt.show()
        print 'SuccessFul.'

    elif hash_req != 200:
        print 'Unsuccessful.'


# creating a method to choose option
def choose_option():
    choose = True
    print 'Welcome to InstaBot.'
    # choosing the option from the list operations
    while choose:
        option = int(raw_input(
            "Choose from \n1.Self Info. \n2.Self Post. \n3.UserPost. \n4.List of People like the Post.\n5.Like a Post.\n6.Get Comments.\n7.Post a comment\n8.Delete a comment \n9.HashTag.\n10.Exit\n"))
        if option == 1:
            self_info()
        elif option == 2:
            self_post()
        elif option == 3:
            user_post()
        elif option == 4:
            like_on_post()
        elif option == 5:
            like_a_post()
        elif option == 6:
            get_comments()
        elif option == 7:
            post_comment()
        elif option == 8:
            del_comment()
        elif option == 9:
            frnd_hashtag()
        elif option == 10:

            print 'Thank You. Have a great day.'
            choose = False
        else:
            print 'Enter a valid option.'


# calling choose option
choose_option()
