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
        if "OVERVIEWER" == poi['Text1']:
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


# ==================== Overworld =====================
center = (0, 80, 0)
radius = 20000
crop = (center[0]-radius, center[2]-radius, center[0]+radius, center[2]+radius)

renders["overworldday"] = {
	"title": "Tag",
	"world": "Overworld",
	"rendermode": smooth_lighting,
	"crop": crop,
	"center": center,
	"showspawn": False,
        "defaultzoom": 5,
        "maxzoom": -1,
        "markers": markers
}

# ==================== Nether =====================
radius = 3500
center = (0, 80, 0)
crop = (center[0]-radius, center[2]-radius, center[0]+radius, center[2]+radius)

renders['netherhighways'] = {
	"title": 'Highways',
	'world': 'Nether',
	"rendermode": [Base(), Depth(min=0, max=53), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "maxzoom": -1,
        "center": center,
        "crop": crop,
        "markers": markers
}


renders['netherceiling'] = {
	"title": 'Über Bedrock',
	'world': 'Nether',
	"rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "maxzoom": -1,
        "center": center,
        "crop": crop,
        "markers": markers
}
renders['netheritemines'] = {
	"title": 'Netherite Minen',
	'world': 'Nether',
	"rendermode": [Base(), Depth(min=0, max=15), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "maxzoom": -1,
        "center": center,
        "crop": crop,
        "markers": markers
}


# ==================== End =====================
radius = 30000
center = (0, 80, 0)
crop = (center[0]-radius, center[2]-radius, center[0]+radius, center[2]+radius)

renders['end'] = {
	"title": 'Das Ende',
	'world': 'End',
	"rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.3)],
        "defaultzoom": 6,
        "maxzoom": -1,
        "center": center,
        "crop": crop,
        "markers": markers
}
