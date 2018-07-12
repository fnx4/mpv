#!/bin/bash
cp ~/.config/mpv ~/.config/mpv-backup -r
rm -rf ~/.config/mpv
rm -rf ~/.config/mpv-master
wget -O ~/.config/mpv.zip https://github.com/fnx4/mpv/archive/master.zip
unzip ~/.config/mpv.zip -d ~/.config 
mv ~/.config/mpv-master ~/.config/mpv
wget -O ~/.config/mpv/shaders/FSRCNNX_x2_16-0-4-1.glsl https://github.com/igv/FSRCNN-TensorFlow/releases/download/1.1/FSRCNNX_x2_16-0-4-1.glsl
wget -O ~/.config/mpv/shaders/SSimDownscaler.glsl https://gist.githubusercontent.com/igv/36508af3ffc84410fe39761d6969be10/raw/6447c0c024885564165753b67a97fc13f58da2a3/SSimDownscaler.glsl
rm ~/.config/mpv.zip
rm ~/.config/mpv/README.md
rm ~/.config/mpv/setup.sh
echo 
echo Done.