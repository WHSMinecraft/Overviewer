global json, getJSONText
import json
from .observer import LoggingObserver


texturepath = "./Resources/client.zip"
outputdir = "./Render/"

customwebassets = "./WebAssets"

observer = LoggingObserver()


folder = "/srv/minecraft/survival/"

worlds["Overworld"] = folder + "world"
worlds["Nether"] = folder + "world_nether"
worlds["End"] = folder + "world_the_end"



def getJSONText(jsonText):
    return json.loads(jsonText)['text']

def markerFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "MARKER" == poi['Text1']:
            return " ".join([poi['Text2'], poi['Text3'], poi['Text4']])
    elif poi['id'] == 'Lectern' or poi['id'] == 'minecraft:lectern':
        if 'Book' in poi and poi['Book']['id'] == 'minecraft:written_book':
            nbt = poi['Book']['tag']
            if nbt['title'] == 'OVERVIEWER':
                poi['icon'] = "book_icon.png"
                title = getJSONText(nbt['pages'][0])  # First page
                pages = map(getJSONText, nbt['pages'][1:])  # Rest of pages
                return (title, " ".join(pages))

markers = [dict(name="Marker", filterFunction=markerFilter, icon="signpost_icon.png", showIconInLegend=True)]

radius = 50000

renders["overworldday"] = {
	"title": "Welt am Tag",
	"world": "Overworld",
	"rendermode": smooth_lighting,
	"crop": (-radius, -radius, radius, radius),
	"center": (-600, 80, -180),
	"showspawn": False,
        "defaultzoom": 5,
        "markers": markers
}


renders["overworldnight"] = {
	"title": "Welt in der Nacht",
	"world": "Overworld",
	"rendermode": [Base(), EdgeLines(), SmoothLighting(night=True, strength=0.7)],
	"crop": (-radius, -radius, radius, radius),
	"center": (-600, 80, -180),
	"showspawn": False,
        "defaultzoom": 5,
        "markers": markers
}

"""
renders['overworldcaves'] = {
	'title': "Unter Tage",
	'world': 'Overworld',
	'rendermode': [Base(), DepthTinting(), Cave(only_lit=True)],
	"crop": border
}
"""

renders['netherceiling'] = {
	"title": 'Über Bedrock',
	'world': 'Nether',
	"rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "center": (-250, 50, 0),
        "markers": markers
}

renders['netherhighways'] = {
	"title": 'Highways',
	'world': 'Nether',
	"rendermode": [Base(), Depth(min=0, max=53), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "center": (-250, 50, 0),
        "markers": markers
}


renders['netheritemines'] = {
	"title": 'Netherite Minen',
	'world': 'Nether',
	"rendermode": [Base(), Depth(min=0, max=15), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "center": (-250, 50, 0),
        "markers": markers
}

renders['end'] = {
	"title": 'Das Ende',
	'world': 'End',
	"rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.3)],
        "defaultzoom": 8,
        "center": (0, 80, 0),
        "markers": markers
}

"""

renders['slimeoverlay'] = {
	'title': "Slimechunks",
	'world': 'Overworld',
	'rendermode': [ClearBase(), SlimeOverlay()],
	"crop": border,
	'overlay': ['overworldday', 'overworldnight', 'overworldcaves']
}



renders['biomeoverlay'] = {
	'title': "Biome",
	'world': 'Overworld',
	'rendermode': [ClearBase(), BiomeOverlay()],
	"crop": border,
	'overlay': ['overworldday', 'overworldnight', 'overworldcaves']
}


"""
