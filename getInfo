#!/usr/bin/env python3.7

from psaw import PushshiftAPI
from datetime import datetime
import argparse
import time



psapi = PushshiftAPI()


def validDate(dateInput):
    try:
        return datetime.strptime(dateInput, '%Y%m%d')
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(dateInput)
        raise argparse.ArgumentTypeError(msg)

def toUnixTime(dateObject):
    unixTime = time.mktime(dateObject.timetuple())
    return unixTime

def fetchInput():
    argList = []


    parser = argparse.ArgumentParser(
            description='Script that fetches submissions from Pushshift api'
            )
    parser.add_argument(
            '--subreddit',
            '-s',
            #action = 'store_const',
            type = str,
            help='What is the Subreddit to fetch submissions from',
            required = True
            )
    parser.add_argument(
            '--initial',
            '-i',
            #action = 'store_const',
            type = validDate,
            help = 'Start Date - YYYYMMDD',
            default = '20070101',
            required = True
            )
    parser.add_argument(
            '--final',
            '-f',
            #action = 'store_const',
            type = validDate,
            help = 'End Date - YYYYMMDD',
            required = True,
            default = '20180801'
            )
    parser.add_argument(
            '-c',
            '--content',
            type = str,
            help = 'Content to retrieve from reddit',
            choices = ['submissions','comments','author'],
            default = 'submissions',
            required = True)

    args = parser.parse_args()

    #Update argList with data from argparse
    argList.append(args.subreddit)
    argList.append(args.content)
    argList.append(toUnixTime(args.initial))
    argList.append(toUnixTime(args.final))

    print(args.initial)
    print(argList)
    return args


#submissions = psapi.search_submissions(limit=10)
#results = list(submissions)
fetchInput()
#print(results)

#askSubreddit()
#print(dir(topPosts))
