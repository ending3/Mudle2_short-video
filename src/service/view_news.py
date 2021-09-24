"""
分页看新闻（每页显示10条），提示用户输入页码，根据页码显示指定页面的数据。
    - 提示用户输入页码，根据页码显示指定页面的数据。
    - 当用户输入的页码不存在时，默认显示第1页

"""
import config


def show_news(index):
    """根据页码获取对应的10条新闻，并在页面进行展示分页信息（输出）
    :param index:页码
    :return:
    """
    # 对应页码10条新闻的起始序号位置
    count = index * 10
    num = 1
    print(f"第{index + 1}页")
    for line, values in config.NEWS_DICT.items():
        if count < num <= count + 10:
            news_id = line
            news_title = values[0]
            data = f"{num} {news_id} {news_title}"
            print(data)
        num += 1
        if num > count + 10:
            return


def execute():
    """ 分页看新闻 """
    print("分页看新闻（每页显示10条）".center(50, '-'))
    while True:
        text = input("请输入页码【范围1-100】（Q退出）：").strip()
        if text.upper() == "Q":
            return

        if not text.isdecimal():
            print("输入格式错误，请重新输入！")
            continue

        page_index = int(text)
        if not 0 < page_index <= 100:
            page_index = 1

        show_news(page_index - 1)
