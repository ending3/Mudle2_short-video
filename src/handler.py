from src.service import view_news, search, download


def run():
    print("欢迎来到短视频资讯下载平台")

    func_dict = {
        "1": view_news.execute,
        "2": search.execute,
        "3": download.execute,
    }

    while True:
        print("1、分页看新闻，2、搜索专区，3、下载专区")
        text = input("请选择分区：").strip()
        if text.upper() == "Q":
            return
        func = func_dict.get(text)
        if not func:
            print("输入错误，请重新选择！")
            continue

        # 进入功能专区
        func()
