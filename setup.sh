#!/bin/bash

git clone git://github.com/overviewer/Minecraft-Overviewer.git

pushd Minecraft-Overviewer

python3 setup.py build


popd

mkdir Render
mkdir Resources

./get_textures.sh
