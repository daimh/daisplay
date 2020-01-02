## daisplay

#### Overview
A Raspbian Lite-based signage. 


It plays multiple h264 videos simutaneously, shows time, weather and bus information, changes background at user-specified interval. It also supports user's own addon. U of Michigan's Magic Bus, AAATA bus, and weather were implemented in addon as an example. 

Tested on Raspberry Pi 3 Model B at 1080p resolution, and Pi 4 with one 4k resolution display.

#### Demo 
- [1](https://youtu.be/7xs4GRC0qHc) 
- [2](https://youtu.be/MaKyHXSJHWM)

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
* to show realtime weather, get a free appkey from <https://openweathermap.org/api> and put it in /etc/daisplay.conf
* copy multiple background png images to /home/pi/daisplay/var/lib/daisplay/background/. You can even dynamically generate png images in that directory.
* copy h264 format videos files to var/lib/daisplay/video-X1-Y1-X2-Y2-DESCRIPTION/, only 1080p is supported as omxplayer has such a limitation even on Pi 4
* to adjust the video window location, change X1, Y1, X2, Y2 in those video directory names
* command 'png2h264' can convert multiple png files to a h264 video for smooth slideshow
* convert other video format to h264  
	`$ mencoder example.mpg -ovc x264 -x264encopts preset=medium -o example.h264`
* embed subtitle file into a video  
	`$ mencoder example.mpg -ovc x264 -x264encopts preset=medium -sub Market.srt -subfont-text-scale 3 -o example.h264`
* reduce video resolution, as Pi 3 is not powerful enough to play multiple 1080p videos.  
	`$ mencoder large.h264 -ovc x264 -x264encopts preset=medium -vf scale=960:540 -o small.h264`

#### Package and install your own customzation
	$ /home/pi/daisplay/usr/lib/daisplay/bin/daisplay-dpkg-deb
	# copy the deb file to a new Raspbian Lite, log in to the new Pi
	$ sudo apt install ./daisplay_custom.deb
	$ sudo /usr/lib/daisplay/bin/daisplay-init-step-1
	$ sudo shutdown -r now
	$ sudo /usr/lib/daisplay/bin/daisplay-init-step-2
	$ sudo shutdown -r now


#### Copyright

Developed by [Manhong Dai](mailto:daimh@umich.edu)

Copyright © 2020 University of Michigan. License [GPLv3+](https://gnu.org/licenses/gpl.html): GNU GPL version 3 or later 

This is free software: you are free to change and redistribute it.

There is NO WARRANTY, to the extent permitted by law.

#### Acknowledgment

Ruth Freedman, MPH, former administrator of MNI, UMICH

Fan Meng, Ph.D., Research Associate Professor, Psychiatry, UMICH

Huda Akil, Ph.D., Director of MNI, UMICH

Stanley J. Watson, M.D., Ph.D., Director of MNI, UMICH

Copyright free pictures and videos were downloaded from <https://pixabay.com/photos/plouzane-lighthouse-france-landmark-1758197/> and <https://coverr.co>
