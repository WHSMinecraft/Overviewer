#!/bin/bash

set -e

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
echo Rendering claims...
echo --------------------------------------------------

./render_claims.py

echo --------------------------------------------------
echo Copying files to web server...
echo --------------------------------------------------

rsync -rlh --delete ./Render/ /srv/http/whsminecraft.de/map

echo --------------------------------------------------
echo Done!
echo --------------------------------------------------

