#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-16 11:01:15
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
import simplejson as json


def getjson():
    with open('db.json','r') as f:
        try:
            rjson = json.loads(f.read())
        except json.scanner.JSONDecodeError:
            rjson = {}
    return rjson

def showmenu():
    suggest = '''
    please select your operation:
        q - quit
        n - add user
        e - login 
        select :'''
    while True:
        s = input(suggest)
        if s == 'n':
            newuser()
        elif s == 'e':
            olduser()
        elif s == 'q':
            quit()

def olduser():
    while True:
        name = input('user name :')
        pwd = input('pwd :')
        passw = db.get(name,None)
        if passw is None:
            print('user is not exists')
            continue
        if pwd == passw:
            print('you login success')
            break
        else:
            print('login failed')

def newuser():
    while True:
        name = input('user name :')
        if name in db:
            print('the user is already exists')
            continue
        else:
            break
    pwd = input('pwd :')
    db[name] = pwd
    with open('db.json','w') as f:
        f.write(json.dumps(db))
    print('add user success')
    return True

if __name__ == '__main__':
    db = getjson()
    try:
        showmenu()
    except KeyboardInterrupt:
        print('you cancel the script')
