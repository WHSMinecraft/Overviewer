#!/bin/bash

# git clone git://github.com/overviewer/Minecraft-Overviewer.git
git clone https://github.com/IncredibleHolg/Minecraft-Overviewer.git

pushd Minecraft-Overviewer
git checkout quartz_bricks

python3 setup.py build


popd

mkdir Render
mkdir Resources

./get_textures.sh
