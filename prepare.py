import tushare as ts
import pandas as pd
import numpy as np

#按照新浪财经对沪深股票进行的行业分类，返回所有股票所属行业的信息。
id_industry_data = ts.get_industry_classified()
id_industry_data.to_csv('id_industry_data.csv',index=0)
#id_industry_data = pd.read_csv('id_industry_data.csv',dtype=object,header=0, encoding='UTF-8')

industry_list = ['玻璃行业','船舶制造','传媒娱乐','电力行业','电器行业','电子器件','电子信息','房地产','发电设备','飞机制造',
                 '服装鞋类','钢铁行业','化工行业','化纤行业','家电行业','酒店旅游','家具行业','金融行业','交通运输','机械行业',
                 '建筑建材','酿酒行业','煤炭行业','农林牧渔','汽车制造','其它行业','水泥行业','食品行业','生物制药','商业百货',
                 '石油行业','物资外贸','医疗器械','仪器仪表','有色金属']

#获得指定时间段内各行业所有股票的收益率数据
datenum = 60 #交易日总数，全阶段为82，上升期为60，下降期为39
up_down = 1 #0表示全阶段，1表示上升期，-1表示下降期
ri_data = {}
for i in industry_list:
    print(i)
    industry_data = {}
    for idx, row in id_industry_data.iterrows():
        if row['c_name'] == i:
            if up_down != 0:
                if up_down == -1:
                    his_data1 = ts.get_hist_data(code=row['code'],start='2020-01-01',end='2020-02-01')
                    his_data2 = ts.get_hist_data(code=row['code'],start='2020-03-01',end='2020-04-01')
                elif up_down == 1:
                    his_data1 = ts.get_hist_data(code=row['code'],start='2020-02-01',end='2020-03-01')
                    his_data2 = ts.get_hist_data(code=row['code'],start='2020-04-01',end='2020-06-01')
                if his_data1 is None or his_data2 is None :
                    #print(row['code'])
                    continue
                his_data = pd.concat([his_data1,his_data2])
            else:
                his_data = ts.get_hist_data(code=row['code'],start='2020-02-01',end='2020-06-01')
                if his_data is None:
                    #print(row['code'])
                    continue

            his_data['returns'] = (his_data['close']-his_data['close'].shift(1))/his_data['close'].shift(1)
            stock_data = his_data["returns"].values
            stock_data_list = stock_data.tolist()
            stock_data_list = stock_data_list[1:]  # 舍去空值
            if len(stock_data_list) != datenum-1:
                #print(row['code'])
                #print(len(stock_data_list))
                continue
            industry_data.update({row['code']:stock_data_list})
    ri_data.update({i:industry_data})
np.save('ri_data.npy', ri_data)

#根据指定时间段内沪深300成分股的权重，计算得出市场组合在每个行业的收益率
weight = {}
w = pd.read_table('weight.txt',dtype=object,header=0, encoding='UTF-8', sep=',')
for idx, row in w.iterrows():
    for k,v in ri_data.items():
        if row['code'] in v:
            if k in weight:
                weight[k].append(row['code'])
            else:
                weight.update({k:[row['code']]})
#print(weight)
rm_data = {}
for k,v in weight.items():
    s = [0]*(datenum-1)
    s1 = 0
    for code in v:
        if code in ri_data[k]:
            tmp = w.loc[w['code'] == code,'w']
            sw = float(tmp.values[0])
            for i in range(0,len(s)):
                s[i] += ri_data[k][code][i] * sw
            s1 += sw
    for i in range(0,len(s)):
        s[i] /= s1
    rm_data.update({k:s})
np.save('rm_data.npy', rm_data)




