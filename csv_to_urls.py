#!/usr/bin/env python3

with open('./following_accounts.csv', 'r') as f:
    urls = []
    for l in f:
        nick, instance = l.split('@')
        urls.append('https://{0}/@{1}\n'.format(instance.strip(), nick))

with open('./tooterslist.txt', 'w') as f:
    for l in urls:
        print(l)
        f.write(l)
