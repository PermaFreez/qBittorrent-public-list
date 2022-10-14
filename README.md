# qBittorrent-public-list
This python script I wrote let's you generate a basic HTML site, that lists the torrents opened in your qBittorrent client, along with thier magnet-links. It uses the WebUI's API trough the https://github.com/rmartin16/qbittorrent-api python library. You can use softwares like `crontab`, to automate the running of this script. This way you can get a webpage, that is always up-to-date.

![Screenshot from 2022-10-14 22-46-55](https://user-images.githubusercontent.com/25381594/195940759-2428a0a5-5bf4-4755-a2bd-eaa32a87c9de.png)

If you're on private trackers, which you don't want to list you can put
```
 25   if torrent.tracker == "http://private1.tracker" or torrent.tracker == "http://private2.tracker":
 26      continue
```
in the code. Keep in mind that this isn't a proper solution and those torrents will still be counted at the "Number of my torrents:" part.
