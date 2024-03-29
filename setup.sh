#!/bin/bash

set -e

git clone ssh://git@github.com/overviewer/Minecraft-Overviewer.git


pushd Minecraft-Overviewer
python3 setup.py build
popd


mkdir Render
mkdir Resources
mkdir World

VERSION=1.17.1
wget https://overviewer.org/textures/${VERSION} -O Resources/client.zip
