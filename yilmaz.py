import instaloader

ig = instaloader.Instaloader()

ig.login('epixı', 'şifre') ## Kullanıcı adını ve şifrenizi buraya yazını
## 
person = 'yilmazuc4r'  # aranacak kişiyi buraya yazabilirsiniz doğrudan kullanıcı adı @ olmadan

profile = instaloader.Profile.from_username(ig.context, person)

my_followers = []

for follower in profile.get_followers():

    username = follower.username

    my_followers.append(username)  # append in the list

my_following = []

for followee in profile.get_followees():

    username = followee.username

    my_following.append(username)  # append in list



for followee in my_following:

    if followee not in my_followers:

        print(followee)