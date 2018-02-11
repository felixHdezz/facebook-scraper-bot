#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FacebookWebBot import *
import os, json, random, jsonpickle
from Spam import spam

posts_=[]


selfProfile = "https://mbasic.facebook.com/profile.php?fref=pb"
grups = ["https://mbasic.facebook.com/groups/830198010427436"
]

postsList = list()
peopleList = list()

def getPost():
    global postsList


def saluteAll():
    global grups, bot, saluteText
    for g in grups:
        try:
            bot.postInGroup(g, eula)
            print("DONE")
        except Exception:
            print("Fail")


def getUsers():
    global peopleList, grups, bot
    for g in grups:
        try:
            pg = bot.getGroupMembers(g, 1, random.randint(0, 20))
            peopleList += pg
            print("DONE", len(pg))
        except Exception:
            print("fail")
    print(len(peopleList))


def addAll():
    global bot, grups, peopleList
    for p in peopleList:
        try:
            bot.sendFriendRequest(p.profileLink)
            print("Added: ", p.name)
        except Exception:
            print("Fail to add: ", p.name)


def spam_group():
    global bot, groups,posts_
    for g in grups:
        try:
            posts_ += bot.getPostInGroup(g)[0]
            print("Number of posts: ", len(posts_))
        except Exception:
            print("Fail get posts in :", bot.title)
    for p in posts_:
        try:
            n=bot.commentInPost(p.linkToComment, random.choice(spam))
            bot.save_screenshot(n)
            print("Commenting in", bot.title)
        except Exception:
            print("Fail comment in ", bot.title)


if __name__ == "__main__":
    bot = FacebookBot()
    bot.login("felix.hernandez.uthh@gmail.com", "")
    while True:
        try:
            saluteAll()
            spam_group()
            time.sleep(5*60)
        except Exception:
            print ("ERROR!!!")
