# 被动听牌的MAER分析

outs_list = [4,8,9,12,15]
bet_scale = [0.5, 0.66,1,1.5]

for outs in outs_list:
    for bet in bet_scale:
        w = outs/46
        o = bet/(2*bet+1)
        m_c = 1/w - 1/o
        m_p_river = o*(1+o)*m_c
        if m_p_river<0.5:
            print(f'w:{w:.2f} o:{o:.2f} m/c:{m_c:.2f} m_p_river:{m_p_river:.2f} Excellent')
        elif m_p_river<1:
            print(f'w:{w:.2f} o:{o:.2f} m/c:{m_c:.2f} m_p_river:{m_p_river:.2f} Good')
        else:
            print(f'w:{w:.2f} o:{o:.2f} m/c:{m_c:.2f} m_p_river:{m_p_river:.2f}')