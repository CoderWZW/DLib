#coding:utf-8
#author:Yu Junliang
import random

import numpy as np
from baseclass.shillingAttack.Attack import Attack

class RandomAttack(Attack):
    def __init__(self,conf):
        super(RandomAttack, self).__init__(conf)


    def insertSpam(self,startID=0):
        self.selectTarget()
        print('Modeling random attack...')
        itemList = self.itemProfile.keys()
        if startID == 0:
            self.startUserID = len(self.userProfile)
        else:
            self.startUserID = startID


        for i in range(int(len(self.userProfile)*self.attackSize)):
            #fill 装填项目
            fillerItems = self.getFillerItems()
            for item in fillerItems:
                self.spamProfile[str(self.startUserID)][str(list(itemList)[item])] = random.randint(self.minScore,self.maxScore)
            #target 目标项目
            for j in range(self.targetCount):
                target = random.randint(0, len(self.targetItems)-1)
                self.spamProfile[str(self.startUserID)][self.targetItems[target]] = self.targetScore
                self.spamItem[str(self.startUserID)].append(self.targetItems[target])
            self.startUserID += 1
