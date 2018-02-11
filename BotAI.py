#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FacebookWebBot import *
import os, json, random, jsonpickle
from Spam import spam

posts_=[]


selfProfile = "https://mbasic.facebook.com/profile.php?fref=pb"
grups = ["https://mbasic.facebook.com/groups/830198010427436",
         "https://m.facebook.com/groups/1660869834170435",
         "https://m.facebook.com/groups/100892180263901",
         "https://m.facebook.com/groups/1649744398596548",
         "https://m.facebook.com/groups/421300388054652",
         "https://m.facebook.com/groups/675838025866331",
         "https://m.facebook.com/groups/1433809846928404",
         "https://m.facebook.com/groups/1625415104400173",
         "https://m.facebook.com/groups/424478411092230",
         "https://m.facebook.com/groups/1056447484369528",
         "https://m.facebook.com/groups/1433809846928404",
         "https://m.facebook.com/groups/421300388054652",
         "https://m.facebook.com/groups/1649744398596548",
         "https://m.facebook.com/groups/751450114953723",
         "https://m.facebook.com/groups/943175872420249"
]

postsList = list()
peopleList = list()
saluteText = "Buenos días usuarios, gracias por activar su unidad moderadora 3000\n" \
             "\nPara información sobre su uso presione la tecla F1, para ayuda presione F2 \n" \
             "Para otras instrucciones remitase al manual de usuario adjunto en el CD instalador"

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
    bot.login("felix.hernandez.uthh@gmail.com", "desa01fhh")
    #bot.save_screenshot("debug.jpg")
    while True:
        try:
            saluteAll()
            spam_group()
            time.sleep(5*60)
        except Exception:
            print ("ERROR!!!")
