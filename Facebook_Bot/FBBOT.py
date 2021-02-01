from facepy import GraphAPI
import requests


token = '''EAAtVXT40eBUBALfxj4OPAPzbBcZBwZCsmWYgnWZC4itYPilHwY4C5JOPRZC
h0aF9Y8MAytRT1mzZBgZAr9BUbFhsOow5hGElVFASsPmkNHZAZAUE1UcVcxLLjaJ3j7hOZA41
Ezqs6EVzop4JXWWQfw1THYhzIwBDGErE2ld1DhdpaTwZDZD'''

fburl = f'https://graph-video.facebook.com/v9.0/115161753503896/videos?access_token={token}'
desc = titl = 'First video'


m = {'description': desc,
      'title': titl,}

files = {'source': ('2.mp4', open('2.mp4', 'rb'), 'video/mp4')}

r = requests.post(fburl, data=m, files=files)
print(id)
