import csv
import requests
import time


def take_friends(domain):
    token = 'enter your token'
    version = 5.103
    fields = 'nickname'
    order = 'hints'
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/friends.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset,
                                    'fields': fields,
                                    'order': order
                                })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts


def file_writer(all_posts):
    with open('Friends.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Name', 'Surname'))
        for post in all_posts:
            a_pen.writerow((post['first_name'], post['last_name']))
