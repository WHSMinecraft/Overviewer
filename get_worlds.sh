#!/bin/bash

PASS=$(cat nitrado-pass.txt)


wget -q --show-progress --user=ni4469609_1 --password=${PASS} -r -N -l inf "ftp://ms1632.gamedata.io/minecraftbukkit/world*"