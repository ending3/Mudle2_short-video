"""
搜索专区
    - 用户输入关键字，根据关键词筛选出所有匹配成功的短视频资讯。
    - 支持的搜索两种搜索格式：
      - `id=1715025`，筛选出id等于1715025的视频（video.csv的第一列）。
      - `key=文本`，模糊搜索，筛选包含关键字的所有新闻（video.csv的第二列）。
"""
import re
import config


def search_by_id(key_id):
    """根据视频ID查找内容（输出）
    :param key_id:视频ID
    :return:
    """
    num = 1
    for  line, values in config.NEWS_DICT.items():
        news_id = line
        news_title = values[0]
        if key_id == news_id:
            data = f"{num} {news_title}"
            print(data)
            return
        num += 1
    print("查无id")


def search_by_key(key_word):
    """根据内容关键字模糊查找新闻（输出）
    :param key_word:关键字内容
    :return:
    """
    # 用于判断是否有搜索到内容
    check = False
    count = 1
    num = 1
    for keys, values in config.NEWS_DICT.items():
        news_id = keys
        news_title = values[0]
        if key_word in news_title:
            data = f"{count} {news_id} {news_title}"
            print(data)
            count += 1
            check = True
        num += 1
    if not check:
        print("未搜索到相关信息")


def execute():
    """ 根据关键字搜索新闻 """
    print("欢迎进入搜索专区".center(50, '-'))

    while True:
        text = input("请按照搜索条件输入相应搜索，支持【id=1711349 或 key=文本】（Q退出）：")
        if text.upper() == "Q":
            return

        match_object = re.match("(id|key)=(\w+)", text.strip())
        if not match_object:
            print("输入格式错误，请重新输入")
            continue

        name, value = match_object.groups()
        show_data = {
            "id": search_by_id,
            "key": search_by_key,
        }

        # 执行调用字典中对应的功能
        show_data[name](value)

        # 最开始的思路（舍弃）
        # # 判断用户搜索条件是否为id查询
        # if choose[:3] == "id=":
        #     key_id = choose[3:]
        #     search_by_id(key_id)
        #     continue
        #
        # # 判断搜索条件是否为key关键字查询
        # if choose[:4] == "key=":
        #     keyword = choose[4:]
        #     search_by_key(keyword)
        #     continue
        #
        # print("搜索错误，请按照搜索条件重新输入！")
