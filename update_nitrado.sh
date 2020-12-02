#!/bin/bash

cd "${0%/*}"


./get_worlds.sh
./render.sh
rsync -ah Render/ ~/WebServerRoot
