#!/bin/bash

# git clone git://github.com/overviewer/Minecraft-Overviewer.git
git clone https://github.com/IncredibleHolg/Minecraft-Overviewer.git


pushd Minecraft-Overviewer
git checkout quartz_bricks
python3 setup.py build
popd


mkdir Render
mkdir Resources

VERSION=1.16.4
wget https://overviewer.org/textures/${VERSION} -O Resources/client.zip
