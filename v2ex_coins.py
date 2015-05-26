#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, re
import http.cookiejar, urllib.request
import json

from datetime import datetime

COOKIE_FILE = 'v2ex_cookie.json'
DOMAIN = r'v2ex.com'
URL = r'https://' + DOMAIN
CREDIT_ACTION = URL + r'/mission/daily'
CREDIT_BALANCE = URL + r'/balance' 
CREDIT_TOKEN = u'(/mission/daily/redeem\?once=\d+|每日登录奖励已领取)'.encode('utf8')
CREDIT_RSPD = u'(已连续登录 \d+ 天)'.encode('utf8')
CREDIT_BALANCE_CHK = u'<td class="d".*?>(?!<.*>)(.+?)<'.encode('utf8')

# Get the current script file's absolute path where the COOKIE_FILE is located in. 
def get_file_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def check_balance(balance_url, balance_chk, balance_date=''):
    data = opener.open(balance_url).read()
    data_lines = data.splitlines()
    i = 0; coins = ''; coins_info = []
    for line in data_lines:
      balance = re.search(balance_chk, line)
      if balance:
        i += 1
        if i == 5:
           coins += '\n'
           coins_info.append(coins)
           coins = ''
           i = 0
        elif i == 4:
           coins += 'Total: ' + (balance.group(1)).decode('utf8')
        else:
           coins += (balance.group(1)).decode('utf8') + '\t'

    balance = [ coin for coin in coins_info if coin.startswith(balance_date)]
    return balance

if __name__ == '__main__':
    if not ('--coins' in sys.argv or '--chk' in sys.argv) or len(sys.argv)>2:
       print('Usage:\n\t{a} --chk\t\tshow your balance and the last 20 records\n\t{a} --coins\ttake daily sign award'\
               .format(a=sys.argv[0]))
       sys.exit(-1)

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add following contents of HTTP header fields, pretend a browser to access the site.
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; rv:38.0) Gecko/20100101 Firefox/38.0')
        , ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        , ('Accept-Language', 'en-US,en;q=0.5')
        , ('Referer', CREDIT_ACTION)
    ]

# Grab the object respond for the site via object requset, the site's cookies as well.
    rqst = urllib.request.Request(URL)
    rspd = opener.open(rqst)

# Read a JSON file for cookies' name and value.
    cookie_filename = '{}/{}'.format(get_file_path(), COOKIE_FILE)
    with open(cookie_filename, encoding='utf8') as cookie_file:
        cookie = json.loads(cookie_file.read())
        
# Add new cookie name and value in CookieJar cj.
    for name, value in cookie.items():
        rspd.headers.add_header('Set-Cookie', '{}={}'.format(name, value))
    cj.extract_cookies(rspd, rqst)

# Sign in v2ex, using added CookieJar cj.
    opener.open(URL)

# for only check the balance
    if '--chk' in sys.argv:
       balance = check_balance(CREDIT_BALANCE, CREDIT_BALANCE_CHK)
       print (str().join(balance))
       sys.exit(-1)

# Check tokens; if got the tokens, take daily coins and check the balance. 
    data = opener.open(CREDIT_ACTION).read()
    tokens = re.search(CREDIT_TOKEN, data)
    if tokens:
       token_txt = (tokens.group()).decode('utf8')
       if 'once=' in token_txt:
          data = opener.open(URL + token_txt).read()   # take the coins with the token once=xxxx
          tokens = re.search(CREDIT_RSPD, data)
          print(datetime.now().strftime("%Y-%m-%d %I:%M:%S%p"), (tokens.group()).decode('utf8'))
          balance = check_balance(CREDIT_BALANCE, CREDIT_BALANCE_CHK, 
                           datetime.now().strftime("%Y-%m-%d"))
          print(str().join(balance))
       else:
          print(datetime.now().strftime("%Y-%m-%d %I:%M:%S%p"), token_txt)
    else: 
      print('Oops, there\'s something wrong whit taking V2EX Coins.')

