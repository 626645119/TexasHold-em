import math
import numpy as np

# 连续听牌赔率
c1_list = [0.33, 0.50, 0.66, 1.00, 1.50, 2.00]
c2_list = [0.33, 0.50, 0.66, 1.00, 1.50, 2.00]

def fun1():
    for c1 in c1_list:
        for c2 in c2_list:
            cost_scale = c1 + c2 + 2 * c1 * c2
            odds = cost_scale / (1 + 2 * cost_scale)
            print('c1:' + str(c1) + '\tc2:' + str(c2) + '\tcost:' + str(round(cost_scale, 2)) + '\todds:' + str(
                round(odds, 2)))

fun1()

# outs数量、胜率、赔率与隐含赔率
# c1:0.33	c2:0.66	cost:1.43	odds:0.37
# c1:0.5	c2:0.66	cost:1.82	odds:0.39
# c1:0.66	c2:0.66	cost:2.19	odds:0.41
outs_list = [5,8,9,12,15]
odds_list = np.arange(0.33,0.5,0.02)

def fun2():
    for outs in outs_list:
        # 反超概率
        exceed_prob_in_turn = outs / 47
        exceed_prob_in_river = outs / 46
        exceed_prob_all = exceed_prob_in_turn + exceed_prob_in_river*(1-exceed_prob_in_turn)

        print('--------------------outs:'+str(outs)+'------------------------')
        # 隐含赔率所要求的最小收益投入比（投入指翻后投入）
        for odds in odds_list:
            rate = 1/exceed_prob_all - 1/odds
            cost = odds / (1 - 2 * odds)
            print('odds:'+str(round(odds,2))+'\tcost:'+str(round(cost,2))+'\trate:'+str(round(rate,2))+
                  '\tcost*rate:'+str(round(cost*rate,2))+'\tcost*rate/river_pot:'+str(round(cost*rate/(2*cost+1),2)))

fun2()