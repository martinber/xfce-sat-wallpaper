xfce-sat-wallpaper
==================

Wallpaper showing current satellite locations for xfce
------------------------------------------------------

Script that creates a world image showing current satellite positions each 30 seconds  
It's a little CPU heavy because of imagemagick's composite command

It's easily adaptable for other desktop environment, you only need to change the set wallpaper command. 
Needs python, pyephem and imagemagick (composite)

Displays ISS, Tiangong 1 and Hubble Space Telescope positions on an equirectangular world map. You can add more satellites ([you need the TLE orbital data](http://en.wikipedia.org/wiki/Two-line_element_set)), you also can change the images (you may change some variables in the script though)

Sorry for my bad english

### Installation

* Install python, most distros already come with python
* Install imagemagick, most distros already come with imagemagick
* Install pyephem
```
sudo apt-get install python-pip
sudo pip install pyephem

```
* Extract anywhere
* Change wallpaper set command, see next section
* Set to execute this script at boot in xfce settings

### Commands for wallpaper changing

This script needs to execute a command to change wallpaper, this command varies between distros or between hardware. for example my notebook uses XFCE and the right command is:
```
xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitoreDP1/workspace0/last-image --set [image location]
```
So in my code I wrote:
```
xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitoreDP1/workspace0/last-image --set " + workingDirectory + "/" + outImage
```

Most XFCE computers use this command instead:
```
xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor0/image-path --set [image location]
```



