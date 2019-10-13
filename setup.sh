#!/bin/bash
cp ~/.config/mpv ~/.config/mpv-backup -r
rm -rf ~/.config/mpv
rm -rf ~/.config/mpv-master
wget -O ~/.config/mpv.zip https://github.com/fnx4/mpv/archive/master.zip
unzip ~/.config/mpv.zip -d ~/.config 
mv ~/.config/mpv-master ~/.config/mpv
rm ~/.config/mpv.zip
rm ~/.config/mpv/README.md
rm ~/.config/mpv/setup.sh
echo 
echo Done.