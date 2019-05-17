import argparse
import configparser
import tweepy
import time
import logging

logger = logging.getLogger()
temps_debut = time.time()
config = configparser.ConfigParser()
config.read('config.ini')


def twitterconnect():
    ConsumerKey = config['twitter']['ConsumerKey']
    SecretKey = config['twitter']['SecretKey']
    AccessToken = config['twitter']['AccessToken']
    AccessTokenSecret = config['twitter']['AccessTokenSecret']

    auth = tweepy.OAuthHandler(ConsumerKey, SecretKey)
    auth.set_access_token(AccessToken, AccessTokenSecret)
    return tweepy.API(auth)


def main():
    args = parse_args()
    api = twitterconnect()

    for page in tweepy.Cursor(api.user_timeline).pages():
        for tweet in page:
            if args.dry_run:
                print(f"Not deleting : {tweet.text}")
            else:
                print(f"Deleting : {tweet.text}")
                api.destroy_status(tweet.id)


def parse_args():
    parser = argparse.ArgumentParser(description='delete-all-tweets')
    parser.add_argument('--debug', help="Display debugging information", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('-d', '--dry_run', help="Dry run (doesn't delete anything)", dest='dry_run', action='store_true')
    parser.set_defaults(dry_run=False)
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    return args


if __name__ == '__main__':
    main()
