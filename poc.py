import sys

from twarc import Twarc

from secrets import access_secret
from secrets import access_token
from secrets import consumer_key
from secrets import consumer_secret


def get_screen_name(twarc, screen_name, follower_ids, keyword):
	counter = 0
	with open(screen_name + '_' + keyword + '.txt', 'a') as f:
		for user in twarc.user_lookup(ids=follower_ids):
			name = user["name"]
			if keyword in name:
				counter = counter + 1
				f.write('[+] ' + str(counter) + ': screen_name = ' + user['screen_name'] + ', name = ' + name + '\n')


def get_followers_id(twarc, screen_name):
	follower_ids = []
	for follower_id in twarc.follower_ids(screen_name):
		follower_ids.append(follower_id)

	return follower_ids


def main():
	if len(sys.argv) > 2:
		screen_name = sys.argv[1]
		keyword = sys.argv[2]

		t = Twarc(consumer_key, consumer_secret, access_token, access_secret)
		follower_ids = get_followers_id(t, screen_name)
		get_screen_name(t, screen_name, follower_ids, keyword)
	else:
		print('Usage: python poc.py fs0c131y chowkidar')


if __name__ == '__main__':
	main()
