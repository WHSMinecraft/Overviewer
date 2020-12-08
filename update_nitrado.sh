#!/bin/bash

cd "${0%/*}"

echo --------------------------------------------------
echo Updating world from remote...
echo --------------------------------------------------

./get_worlds.sh

echo --------------------------------------------------
echo Running Overviewer...
echo --------------------------------------------------

./render.sh

echo --------------------------------------------------
echo Copying files to web server...
echo --------------------------------------------------

rsync -ah ./Render/ ~/WebServerRoot/
