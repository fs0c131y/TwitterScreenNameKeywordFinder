import sys

from twarc import Twarc

from secrets import (
    access_secret,
    access_token,
    consumer_key,
    consumer_secret
)


def get_screen_name(twarc, screen_name, follower_ids, keyword):
    """
    Get the twitter screen names

    :param twarc:
    :param screen_name:
    :param follower_ids:
    :param keyword:
    :return:
    """
    with open(screen_name + '_' + keyword + '.txt', 'a') as f:
        for counter, user in enumerate(twarc.user_lookup(ids=follower_ids), 1):
            name = user["name"]
            if keyword in name:
                f.write('[+] ' + str(counter) + ': screen_name = ' + user['screen_name'] + ', name = ' + name + '\n')


def get_followers_id(twarc, screen_name):
    """
    Returns the follower IDs

    :param twarc:
    :param screen_name:
    :return:
    """
    return [follower_id for follower_id in twarc.follower_ids(screen_name)]


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
