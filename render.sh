#!/bin/bash

cd "${0%/*}"

echo --------------------------------------------------
echo Rendering tiles...
echo --------------------------------------------------

./Minecraft-Overviewer/overviewer.py --config=config.py

echo --------------------------------------------------
echo Rendering markers...
echo --------------------------------------------------

./Minecraft-Overviewer/overviewer.py --config=config.py --genpoi --skip-players

echo --------------------------------------------------
echo Copying files to web server...
echo --------------------------------------------------

rsync -ah --delete ./Render/ ~/WebServerRoot/map

echo --------------------------------------------------
echo Done!
echo --------------------------------------------------

