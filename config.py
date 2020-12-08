texturepath = "./Resources/client.zip"
outputdir = "./Render"


folder = "./ms1632.gamedata.io/minecraftbukkit/"

worlds["Overworld"] = folder + "world"
worlds["Nether"] = folder + "world_nether"
worlds["End"] = folder + "world_the_end"


radius = 50000

renders["overworldday"] = {
	"title": "Welt am Tag",
	"world": "Overworld",
	"rendermode": smooth_lighting,
	"crop": (-radius, -radius, radius, radius),
	"center": (-600, 80, -180),
	"showspawn": False,
        "defaultzoom": 5
}

"""
renders["overworldnight"] = {
	"title": "Welt in der Nacht",
	"world": "Overworld",
	"rendermode": [Base(), EdgeLines(), SmoothLighting(night=True, strength=0.7)],
	"crop": border,
	"center": center,
	"showspawn": False
}
"""

"""
renders['overworldcaves'] = {
	'title': "Unter Tage",
	'world': 'Overworld',
	'rendermode': [Base(), DepthTinting(), Cave(only_lit=True)],
	"crop": border
}
"""

renders['netherhighways'] = {
	"title": 'Highways',
	'world': 'Nether',
	"rendermode": [Base(), Depth(min=0, max=53), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "center": (-250, 50, 0)
}


renders['netheritemines'] = {
	"title": 'Netherite Minen',
	'world': 'Nether',
	"rendermode": [Base(), Depth(min=0, max=15), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
        "defaultzoom": 8,
        "center": (-250, 50, 0)
}

renders['end'] = {
	"title": 'Das Ende',
	'world': 'End',
	"rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.3)],
        "defaultzoom": 8,
        "center": (0, 80, 0)
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
