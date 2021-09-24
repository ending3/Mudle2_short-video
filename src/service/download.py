"""
下载专区

    - 用户输入视频id，根据id找到对应的mp4视频下载地址，然后下载视频到项目的files目录。
      - 视频的文件名为：`视频id-年-月-日-时-分-秒.mp4`
      - 下载的过程中，输出已下载的百分比，示例代码如下：
"""
import os
import re
import requests

from datetime import datetime

import config


def download_file(video_id, video_url):
    """下载新闻视频并存放到files文件中
    :param video_id:新闻ID
    :param video_url:新闻视频链接
    :return:
    """
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M")
    new_file_path = os.path.join(config.BASIC_PATH, 'files', "{}-{}.mp4".format(video_id, current_datetime))

    res = requests.get(url=video_url, stream=True)

    print("正在下载中...")

    # 视频总大小（字节）
    file_size = int(res.headers['Content-Length'])
    download_size = 0
    with open(new_file_path, mode='wb') as file_object:
        # 分块读取下载的视频文件（最多一次读128字节），并逐一写入到文件中。 len(chunk)表示实际读取到每块的视频文件大小。
        for chunk in res.iter_content(128):
            download_size += len(chunk)
            file_object.write(chunk)
            file_object.flush()
            percent = round((download_size / file_size) * 100, 2)
            print(f"\r{percent}%", end='')
        file_object.close()
    print("\n下载完成")
    res.close()


def get_video_url(video_id):
    """ 获取新闻视频下载链接 """
    for key,value in config.NEWS_DICT.items():
        news_id = key
        news_url = value[1]
        if video_id == news_id:
            return news_url


def execute():
    """ 下载新闻视频 """
    print("欢迎进入下载专区".center(50, '-'))
    while True:
        text = input("请输入要下载的视频ID（Q退出）：").strip()
        if text.upper() == "Q":
            return

        if not re.match("\d{7}", text):
            print("输入ID格式错误，请重新输入！")
            continue

        video_url = get_video_url(text)
        if not video_url:
            print('视频不存在，请重新输入')
            continue

        download_file(text, video_url)
