import requests
from bs4 import BeautifulSoup
import os
import glob

class Crawler:
    def __init__(self, channels_list, N):
        self.ch_list = channels_list
        self.N = N
    def get_videos_url(self, channel):
        ch_url = 'https://www.youtube.com/user/' + channel + '/videos'
        data = requests.get(ch_url)
        html = BeautifulSoup(data.text, 'html.parser')
        v_list = list(map(lambda x : x['href'], html.select('div[class="yt-lockup-thumbnail"] a')))
        if len(v_list) == 0:
            ch_url = 'https://www.youtube.com/channel/' + channel + '/videos'
            data = requests.get(ch_url)
            html = BeautifulSoup(data.text, 'html.parser')
            v_list = list(map(lambda x : x['href'], html.select('div[class="yt-lockup-thumbnail"] a')))
        return v_list
    def get_channel_name(self, channel):
        ch_url = 'https://www.youtube.com/user/' + channel + '/videos'
        data = requests.get(ch_url)
        html = BeautifulSoup(data.text, 'html.parser')
        v_list = list(map(lambda x : x['href'], html.select('div[class="yt-lockup-thumbnail"] a')))
        if len(v_list) == 0:
            ch_url = 'https://www.youtube.com/channel/' + channel + '/videos'
            data = requests.get(ch_url)
            html = BeautifulSoup(data.text, 'html.parser')
        
        
        title = html.select('title')[0].getText()
        return title[2:title.find('-')-1]
    def get_videos(self):
        for ch in self.ch_list:
            ch_name = self.get_channel_name(ch)
            if not os.path.exists('out/' + ch_name):
                os.makedirs('out/' + ch_name)
            files = [f for f in glob.glob('out/' + ch_name+"/*")]
            already_dowloaded = map(lambda x:x[-x[::-1].find('-'):-x[::-1].find('.')-1] ,files)
            for video in  self.get_videos_url(ch)[:self.N]:
                if(video[video.find('=')+1:] not in already_dowloaded):
                    os.system('youtube-dl -o "out/' +ch_name+ '/%(upload_date)s. - %(title)s -' + video[video.find('=')+1:] +  '.%(ext)s" https://www.youtube.com' + video)
                else:
                    print("video " +video[video.find('=')+1:]+" already downloaded")

