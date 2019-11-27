## daisplay

#### Overview
A Raspbian Lite-based signage

It plays multiple videos simutaneously, shows time and weather, change background at user-specified interval. It also supports user's own addon. U of Michigan's Magic Bus and AAATA bus is implemented in addon as an example. User can package his own customization as Debian package file

Tested on Raspberry Pi 3 Model B

#### Installation
* prepare

prepare a Raspbian Lite image on a SD card, boot it, login as user 'pi', and adjust timezone.

* step 1

```
	$ cd /home/pi
	$ sudo apt install git
	$ git clone https://github.com/daimh/daisplay.git
	$ sudo ln -s /home/pi/daisplay/etc/daisplay.conf /etc/
	$ sudo /home/pi/daisplay/usr/lib/daisplay/bin/daisplay-init-step-1
	$ sudo shutdown -r now
```

* step 2

```
	$ sudo /home/pi/daisplay/usr/lib/daisplay/bin/daisplay-init-step-2
	$ sudo shutdown -r now
```

#### Customization 
* to show realtime weather, get a free appkey from https://openweathermap.org/api and put it in /etc/daisplay.conf
* copy multiple background images to /home/pi/daisplay/var/lib/daisplay/background/. You can even dynamically generate images in that folder.
* copy videos and their subtitles files (*.srt) to var/lib/daisplay/video-X1-Y1-X2-Y2-DESCRIPTION/
* to adjust the video location, change X1, Y1, X2, Y2 in the folder name of those video folders
* /home/pi/daisplay/usr/bin/png2mp4 can convert multiple png files to a mp4 video 
* reduce a video size, as Pi is not powerful enough to play multiple HD videos.  
	```$ mencoder large.mp4 -ovc lavc -lavcopts vcodec=mpeg4:mbd=2 -vf scale=960:540 -o small.mp4```
* put something like '```0 3 * * * root /sbin/shutdown -r now```' in crontab if some processes have memory leak

#### Package and install your own customzation
	$ /home/pi/daisplay/usr/lib/daisplay/bin/daisplay-dpkg-deb
	# copy the deb file to a new Raspbian Lite, log in to the new Pi
	$ sudo apt install ./daisplay_custom.deb
	$ sudo /usr/lib/daisplay/bin/daisplay-init-step-1
	$ sudo shutdown -r now
	$ sudo /usr/lib/daisplay/bin/daisplay-init-step-2
	$ sudo shutdown -r now

#### Acknowledgement
  Copyright free pictures and videos are downloaded from <https://pixabay.com/photos/plouzane-lighthouse-france-landmark-1758197/> and <https://coverr.co>
