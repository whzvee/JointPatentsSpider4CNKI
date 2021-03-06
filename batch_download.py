# -*- coding: cp936 -*-
import sys

import make_patent_list

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)

DATE_SPAN = [
    # 按半月：不全
    # ['2016-03-01', '2016-03-15'],
    # ['2016-03-16', '2016-03-31'],
    # ['2016-04-01', '2016-04-15'],
    # ['2016-04-16', '2016-04-30'],
    # ['2016-05-01', '2016-05-15'],
    # ['2016-05-16', '2016-05-31'],
    # ['2016-06-01', '2016-06-15'],
    # ['2016-06-16', '2016-06-30'],
    # ['2016-07-01', '2016-07-15'],
    # ['2016-07-16', '2016-07-31'],
    # ['2016-08-01', '2016-08-15'],
    # ['2016-08-16', '2016-08-23'],
    # ['2016-08-24', '2016-08-31'],
    # ['2014-12-01', '2014-12-15'],
    # ['2014-12-16', '2014-12-31'],
    # ['2014-09-01', '2014-09-15'],

    # 按月
    # ['2007-01-01', '2007-01-31'],
    # ['2007-02-01', '2007-02-28'],
    # ['2007-03-01', '2007-03-31'],
    # ['2007-04-01', '2007-04-30'],
    # ['2007-05-01', '2007-05-31'],
    # ['2007-06-01', '2007-06-30'],
    # ['2007-07-01', '2007-07-31'],
    # ['2007-08-01', '2007-08-31'],
    # ['2007-09-01', '2007-09-30'],
    # ['2007-10-01', '2007-10-31'],
    # ['2007-11-01', '2007-11-30'],
    # ['2007-12-01', '2007-12-31'],
    # ['2008-01-01', '2008-01-31'],
    # ['2008-02-01', '2008-02-29'],
    # ['2008-03-01', '2008-03-31'],
    # ['2008-04-01', '2008-04-30'],
    # ['2008-05-01', '2008-05-31'],
    # ['2008-06-01', '2008-06-30'],
    # ['2008-07-01', '2008-07-31'],
    # ['2008-08-01', '2008-08-31'],
    # ['2008-09-01', '2008-09-30'],
    ['2008-10-01', '2008-10-31'],
    # ['2008-11-01', '2008-11-30'],
    # ['2008-12-01', '2008-12-31'],
    # ['2009-01-01', '2009-01-31'],
    # ['2009-02-01', '2009-02-28'],
    # ['2009-03-01', '2009-03-31'],
    # ['2009-04-01', '2009-04-30'],
    # ['2009-05-01', '2009-05-31'],
    # ['2009-06-01', '2009-06-30'],
    # ['2009-07-01', '2009-07-31'],
    # ['2009-08-01', '2009-08-31'],
    # ['2009-09-01', '2009-09-30'],
    # ['2009-10-01', '2009-10-31'],
    # ['2009-11-01', '2009-11-30'],
    # ['2009-12-01', '2009-12-31'],
    # ['2010-01-01', '2010-01-31'],
    # ['2010-02-01', '2010-02-28'],
    # ['2010-03-01', '2010-03-31'],
    # ['2010-04-01', '2010-04-30'],
    # ['2010-05-01', '2010-05-31'],
    # ['2010-06-01', '2010-06-30'],
    # ['2010-07-01', '2010-07-31'],
    # ['2010-08-01', '2010-08-31'],
    # ['2010-09-01', '2010-09-30'],
    # ['2010-10-01', '2010-10-31'],
    # ['2010-11-01', '2010-11-30'],
    # ['2010-12-01', '2010-12-31'],
    # ['2011-01-01', '2011-01-31'],
    # ['2011-02-01', '2011-02-28'],
    # ['2011-03-01', '2011-03-31'],
    # ['2011-04-01', '2011-04-30'],
    # ['2011-05-01', '2011-05-31'],
    # ['2011-06-01', '2011-06-30'],
    # ['2011-07-01', '2011-07-31'],
    # ['2011-08-01', '2011-08-31'],
    # ['2011-09-01', '2011-09-30'],
    # ['2011-10-01', '2011-10-31'],
    # ['2011-11-01', '2011-11-30'],
    # ['2011-12-01', '2011-12-31'],
    # ['2012-01-01', '2012-01-31'],
    # ['2012-02-01', '2012-02-29'],
    # ['2012-03-01', '2012-03-31'],
    # ['2012-04-01', '2012-04-30'],
    # ['2012-05-01', '2012-05-31'],
    # ['2012-06-01', '2012-06-30'],
    # ['2012-07-01', '2012-07-31'],
    # ['2012-08-01', '2012-08-31'],
    # ['2012-09-01', '2012-09-30'],
    # ['2012-10-01', '2012-10-31'],
    # ['2012-11-01', '2012-11-30'],
    # ['2012-12-01', '2012-12-31'],
    # ['2013-01-01', '2013-01-31'],
    # ['2013-02-01', '2013-02-28'],
    # ['2013-03-01', '2013-03-31'],
    # ['2013-04-01', '2013-04-30'],
    # ['2013-05-01', '2013-05-31'],
    # ['2013-06-01', '2013-06-30'],
    # ['2013-07-01', '2013-07-31'],
    # ['2013-08-01', '2013-08-31'],
    # ['2013-09-01', '2013-09-30'],
    # ['2013-10-01', '2013-10-31'],
    # ['2013-11-01', '2013-11-30'],
    # ['2013-12-01', '2013-12-31'],
    # ['2014-01-01', '2014-01-31'],
    # ['2014-02-01', '2014-02-28'],
    # ['2014-03-01', '2014-03-31'],
    # ['2014-04-01', '2014-04-30'],
    # ['2014-05-01', '2014-05-31'],
    # ['2014-06-01', '2014-06-30'],
    # ['2014-07-01', '2014-07-31'],
    # ['2014-08-01', '2014-08-31'],
    # ['2014-09-01', '2014-09-30'],
    # ['2014-10-01', '2014-10-31'],
    # ['2014-11-01', '2014-11-30'],
    # ['2014-12-01', '2014-12-31'],
    # ['2015-01-01', '2015-01-31'],
    # ['2015-02-01', '2015-02-28'],
    # ['2015-03-01', '2015-03-31'],
    # ['2015-04-01', '2015-04-30'],
    # ['2015-05-01', '2015-05-31'],
    # ['2015-06-01', '2015-06-30'],
    # ['2015-07-01', '2015-07-31'],
    # ['2015-08-01', '2015-08-31'],
    # ['2015-09-01', '2015-09-30'],
    # ['2015-10-01', '2015-10-31'],
    # ['2015-11-01', '2015-11-30'],
    # ['2015-12-01', '2015-12-31'],
    # ['2016-01-01', '2016-01-31'],
    # ['2016-02-01', '2016-02-29'],
    # ['2016-03-01', '2016-03-31'],
    # ['2016-04-01', '2016-04-30'],
    # ['2016-05-01', '2016-05-31'],
    # ['2016-06-01', '2016-06-30'],
    # ['2016-07-01', '2016-07-31'],
    # ['2016-08-01', '2016-08-31'],
    # ['2016-09-01', '2016-09-30'],
    # ['2016-10-01', '2016-10-31'],
    # ['2016-11-01', '2016-11-30'],
    # ['2016-12-01', '2016-12-31'],

    # 按季度
    # ['2007-01-01', '2007-03-31'],
    # ['2007-04-01', '2007-06-30'],
    # ['2007-07-01', '2007-09-30'],
    # ['2007-10-01', '2007-12-31'],
    # ['2008-01-01', '2008-03-31'],
    # ['2008-04-01', '2008-06-30'],
    # ['2008-07-01', '2008-09-30'],
    # ['2008-10-01', '2008-12-31'],
    # ['2009-01-01', '2009-03-31'],
    # ['2009-04-01', '2009-06-30'],
    # ['2009-07-01', '2009-09-30'],
    # ['2009-10-01', '2009-12-31'],
    # ['2010-01-01', '2010-03-31'],
    # ['2010-04-01', '2010-06-30'],
    # ['2010-07-01', '2010-09-30'],
    # ['2010-10-01', '2010-12-31'],
    # ['2011-01-01', '2011-03-31'],
    # ['2011-04-01', '2011-06-30'],
    # ['2011-07-01', '2011-09-30'],
    # ['2011-10-01', '2011-12-31'],
    # ['2012-01-01', '2012-03-31'],
    # ['2012-04-01', '2012-06-30'],
    # ['2012-07-01', '2012-09-30'],
    # ['2012-10-01', '2012-12-31'],
    # ['2013-01-01', '2013-03-31'],
    # ['2013-04-01', '2013-06-30'],
    # ['2013-07-01', '2013-09-30'],
    # ['2013-10-01', '2013-12-31'],
    # ['2014-01-01', '2014-03-31'],
    # ['2014-04-01', '2014-06-30'],
    # ['2014-07-01', '2014-09-30'],
    # ['2014-10-01', '2014-12-31'],
    # ['2015-01-01', '2015-03-31'],
    # ['2015-04-01', '2015-06-30'],
    # ['2015-07-01', '2015-09-30'],
    # ['2015-10-01', '2015-12-31'],
    # ['2016-01-01', '2016-03-31'],
    # ['2016-04-01', '2016-06-30'],
    # ['2016-07-01', '2016-09-30'],
    # ['2016-10-01', '2016-12-31'],

    # 按半年
    # ['2011-01-01','2011-06-30'],
    # ['2011-07-01','2011-12-31'],
    # ['2012-01-01', '2012-06-30'],
    # ['2012-07-01', '2012-12-31'],
    # ['2013-01-01', '2013-06-30'],
    # ['2013-07-01', '2013-12-31'],
    # ['2014-01-01', '2014-06-30'],
    # ['2014-07-01', '2014-12-31'],
    # ['2015-01-01', '2015-06-30'],
    # ['2015-07-01', '2015-12-31'],
    # ['2016-01-01', '2016-06-30'],
    # ['2016-07-01', '2016-12-31'],

    # 按年份
    # ['2007-01-01', '2007-12-31'],
    # ['2008-01-01', '2008-12-31'],
    # ['2009-01-01', '2009-12-31'],
    # ['2010-01-01', '2010-12-31'],
    # ['2011-01-01', '2011-12-31'],
    # ['2012-01-01', '2012-12-31'],
    # ['2013-01-01', '2013-12-31'],
    # ['2014-01-01', '2014-12-31'],
    # ['2015-01-01', '2015-12-31'],
    # ['2016-01-01', '2016-12-31'],
]

CODE_DICT = {
    ##### 电力工业（C042) #####
    # 'C042_1': '电力工业概况',
    # 'C042_2': '一般性问题',
    # 'C042_3': '电工基础理论',
    # 'C042_4': '电工材料',
    # 'C042_5': '电机',
    # 'C042_6': '变压器变流器及其它电力变换器',
    # 'C042_7': '电器',
    # 'C042_8': '发电发电厂',
    # 'C042_9': '输配电工程电力网及电力系统',
    # 'C042_A': '高电压技术',
    # 'C042_B': '电源技术',
    # 'C042_C': '电气化电能应用',
    # 'C042_D': '电气测量技术及仪器',

    ##### 新能源（C041) #####
    # 'C041_1': '太阳能',
    # 'C041_2': '风能',
    # 'C041_3': '生物质能',
    # 'C041_4': '地热能',
    # 'C041_5': '海洋能',
    # 'C041_6': '化学能',
    # 'C041_7': '天然气水合物',
    # 'C041_8': '原子能',
    #
    # 'C037_8': '水能利用_水电站工程',

    ##### 医药卫生科技（E) #####
    # 'E': '医药卫生科技',
    # 'E053': '医药卫生方针政策与法律法规研究',
    # 'E054': '医学教育与医学边缘学科',
    # 'E055': '预防医学与卫生学',
    # 'E056': '中医学',
    # 'E057': '中药学',
    # 'E058': '中西医结合',
    # 'E059': '基础医学',
    # 'E060': '临床医学',
    # 'E061': '感染性疾病及传染病',
    # 'E062': '心血管系统疾病',
    # 'E063': '呼吸系统疾病',
    # 'E064': '消化系统疾病',
    # 'E065': '内分泌腺及全身性疾病',
    # 'E066': '外科学',
    # 'E067': '泌尿科学',
    # 'E068': '妇产科学',
    # 'E069': '儿科学',
    # 'E070': '神经病学',
    # 'E071': '精神病学',
    # 'E072': '肿瘤学',
    # 'E073': '眼科与耳鼻咽喉科',
    # 'E074': '口腔科学',
    # 'E075': '皮肤病与性病',
    # 'E076': '特种医学',
    # 'E077': '急救医学',
    # 'E078': '军事医学与卫生',
    # 'E079': '药学',
    # 'E080': '生物医学工程',
}

if __name__ == '__main__':
    break_count = 1
    for each_code in CODE_DICT:
        for each_span in DATE_SPAN:
            my_list = make_patent_list.PatentList(
                outfile='csv/' + str(CODE_DICT[each_code]).decode('gb18030') + '_' + each_span[0].replace('-', '') +
                        '_' + each_span[1].replace('-', '') + '.csv',
                patent_code=each_code, start_time=each_span[0], end_time=each_span[1])
            break_count = my_list.make_list(break_count)
