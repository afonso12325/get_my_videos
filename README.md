# get_my_videos
Simple web crawler to retrieve the last N videos per channel from a list of YouTube channels.


## Install system depencences by running
```console
cat install/requirements.system | xargs sudo apt install

pip install -r install/requirements.txt
```

## Usage
```console 
usage: get_my_videos.py [-h] channels N

positional arguments:
  channels    path to file including list of channels
  N           number of videos to download from each channel

optional arguments:
  -h, --help  show help message and exit
```