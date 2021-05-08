#!/usr/bin/env python3

import yaml
import glob
import os
import json
import requests


claimdata = os.path.expanduser("/srv/minecraft/survival/plugins/GriefPreventionData/ClaimData/")

regionfile = os.path.expanduser("./Render/regions.js")



playercache = {}
def getPlayerName(uuid):
    if uuid in playercache:
        return playercache[uuid]

    request = requests.get("https://api.mojang.com/user/profiles/%s/names" % uuid)
    currentname = ""
    if request.status_code != 200:
        currentname = "[Unbekannt]"
    else:
        names = request.json()
        currentname = names[-1].get('name')

    playercache[uuid] = currentname
    return currentname



output = {
        "world": [],
        "world_nether": [],
        "world_the_end": []
}


center = (-335, 80, -195)
radius = 50000
crop = (center[0]-radius, center[2]-radius, center[0]+radius, center[2]+radius)


for f in glob.glob(claimdata + '*.yml'):
    with open(f) as c:
        data = yaml.load(c, Loader=yaml.FullLoader)

        arr1 = data['Lesser Boundary Corner'].split(';')
        dimension = arr1[0]

        lbc = (int(arr1[1]), int(arr1[2]), int(arr1[3]))

        arr2 = data['Greater Boundary Corner'].split(';')
        gbc = (int(arr2[1]), int(arr2[2]), int(arr2[3]))

        # Outside tiles/map
        if gbc[0] < crop[0] or gbc[2] < crop[1] or lbc[0] > crop[2] or lbc[2] > crop[3]:
            continue

        uuid = data['Owner']

        # Not rendering subclaims, not really worth the effort
        subclaim = uuid == '' and data['Parent Claim ID'] != -1
        if subclaim:
            continue

        admin = uuid == ''
        hovertext = ''

        if (admin):
            owner = '[ADMIN]'
            hovertext  = owner
        elif not subclaim:
            owner = getPlayerName(uuid)
            hovertext = '<div><img src="https://crafatar.com/avatars/' + uuid + '?size=16&overlay=true" /> ' + owner + '</div>'

        sea_level = 70 if dimension == "world" else 0
        # y_level = max(lbc[1], gbc[1])
        y_level = max(sea_level, 5 + min(lbc[1], gbc[1]))

        data = dict(
            hovertext=hovertext,
            strokeColor='#00b3ff' if admin else '#ff7800',
            strokeWeight=2,
            fill=True,
            points=[
                {'x': lbc[0], 'y': y_level, 'z': lbc[2]},
                {'x': gbc[0], 'y': y_level, 'z': lbc[2]},
                {'x': gbc[0], 'y': y_level, 'z': gbc[2]},
                {'x': lbc[0], 'y': y_level, 'z': gbc[2]},
                {'x': lbc[0], 'y': y_level, 'z': lbc[2]}
            ]
        )

        output[dimension].append(data)
        print("Added claim for {} at: \tx = {}\tz = {}\t in {}".format(owner, lbc[0], lbc[2], dimension))





with open(regionfile, "w") as r:
    r.write('// Generated by script, do not edit\n')
    r.write('\n')
    r.write('markersDB["claims_overworld"] = {\n')
    r.write('    "name": "claims_overworld",\n')
    r.write('    "created": false,\n')
    r.write('    "raw": ')
    json.dump(output["world"], r, indent=4)
    r.write('\n}\n')
    r.write('\n')
    r.write('markersDB["claims_nether"] = {\n')
    r.write('    "name": "claims_nether",\n')
    r.write('    "created": false,\n')
    r.write('    "raw": ')
    json.dump(output["world_nether"], r, indent=4)
    r.write('\n}\n')
    r.write('\n')
    r.write('markersDB["claims_end"] = {\n')
    r.write('    "name": "claims_end",\n')
    r.write('    "created": false,\n')
    r.write('    "raw": ')
    json.dump(output["world_the_end"], r, indent=4)
    r.write('\n}\n')
    r.write('\n')
    r.write('markers["overworldday"].push({\n')
    r.write('    "groupName": "claims_overworld",\n')
    r.write('    "icon": "/assets/gp_logo.jpg",\n')
    r.write('    "createInfoWindow": false,\n')
    r.write('    "showIconInLegend": true,\n')
    r.write('    "displayName": "Claims"\n')
    r.write('});\n')
    r.write('\n')
    r.write('markers["netherhighways"].push({\n')
    r.write('    "groupName": "claims_nether",\n')
    r.write('    "icon": "/assets/gp_logo.jpg",\n')
    r.write('    "createInfoWindow": false,\n')
    r.write('    "showIconInLegend": true,\n')
    r.write('    "displayName": "Claims"\n')
    r.write('});\n')
    r.write('\n')
    r.write('markers["netherceiling"].push({\n')
    r.write('    "groupName": "claims_nether",\n')
    r.write('    "icon": "/assets/gp_logo.jpg",\n')
    r.write('    "createInfoWindow": false,\n')
    r.write('    "showIconInLegend": true,\n')
    r.write('    "displayName": "Claims"\n')
    r.write('});\n')
    r.write('\n')
    r.write('markers["netheritemines"].push({\n')
    r.write('    "groupName": "claims_nether",\n')
    r.write('    "icon": "/assets/gp_logo.jpg",\n')
    r.write('    "createInfoWindow": false,\n')
    r.write('    "showIconInLegend": true,\n')
    r.write('    "displayName": "Claims"\n')
    r.write('});\n')
    r.write('\n')
    r.write('markers["end"].push({\n')
    r.write('    "groupName": "claims_end",\n')
    r.write('    "icon": "/assets/gp_logo.jpg",\n')
    r.write('    "createInfoWindow": false,\n')
    r.write('    "showIconInLegend": true,\n')
    r.write('    "displayName": "Claims"\n')
    r.write('});\n')
