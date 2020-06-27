# Herd-Effect
## 内容说明
        投资学课程论文《中国A股市场羊群效应研究综述》中使用CCK模型对A股市场各行业的羊群效应进行了检验。使用tushare开源数据接口，收集了2020年1月-5月
    的沪深市场上各行业共2800多只股票的有效数据。行业划分主要参考新浪财经关于行业板块的分类，根据实际有效数据，共涉及了35个行业：金融行业、酿酒行业、
    生物制药、家电行业、食品行业、电力行业、房地产、电子器件、水泥行业、机械行业、农林牧渔、建筑建材、仪器仪表、酒店旅游、电子信息、化工行业、交通运输、
    汽车制造、石油行业、煤炭行业、有色金属、医疗器械、钢铁行业、船舶制造、商业百货、服装鞋类、发电设备、飞机制造、家具行业、化纤行业、传媒娱乐、玻璃行业、
    物资外贸、电器行业、其它行业。本仓库存放的是进行检验的所有计算部分代码。
## 代码功能说明
    1、prepare.py: 数据处理代码，输出ri_data.npy（所有行业的所有股票在一段时间内的收益率信息）、
                   rm_data.npy（该行业的市场收益率信息）两个文件。
    2、sheep.py: 基于CSAD指标的羊群效应检验CCK模型，输出为各行业的非线性模型中的a、b1、b2的参数估计。
