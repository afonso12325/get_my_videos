from crawler import Crawler
import argparse

parser = argparse.ArgumentParser(description='downloads all N recent videos from a list of channels.')
parser.add_argument('channels', type=str,
                    help='path to file including list of channels')
parser.add_argument('N', type=int,
                    help='number of videos to download from each channel')
args = parser.parse_args()
with open(args.channels) as f:
    channels = f.read().splitlines()
c = Crawler(channels, args.N)
c.get_videos()       