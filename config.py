texturepath = "./Resources/client.zip"
outputdir = "./Render"


folder = "~/Spigot/"

worlds["Overworld"] = folder + "world"
worlds["Nether"] = folder + "world_nether"
worlds["End"] = folder + "world_the_end"


radius = 100
center = (-600, 70, -200)
border = (center[0]-radius, center[2]-radius, center[0]+radius, center[2]+radius)


renders["overworldday"] = {
            "title": "Welt am Tag",
                "world": "Overworld",
                    "rendermode": smooth_lighting,
                        "crop": border,
                            "center": center,
                                "showspawn": False
                                }

renders["overworldnight"] = {
            "title": "Welt in der Nacht",
                "world": "Overworld",
                    "rendermode": [Base(), EdgeLines(), SmoothLighting(night=True, strength=0.7)],
                        "crop": border,
                            "center": center,
                                "showspawn": False
                                }

renders['overworldcaves'] = {
            'title': "Unter Tage",
                'world': 'Overworld',
                    'rendermode': [Base(), DepthTinting(), Cave(only_lit=True)],
                        "crop": border
                        }

renders['netherhighways'] = {
            "title": 'Highways',
                'world': 'Nether',
                    "rendermode": [Base(), Depth(min=0, max=53), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
                        "northdirection": "lower-right"
                        }


renders['netheritemines'] = {
            "title": 'Netherite Minen',
                'world': 'Nether',
                    "rendermode": [Base(), Depth(min=0, max=14), EdgeLines(), Nether(), SmoothLighting(strength=0.4)],
                        "northdirection": "lower-right"
                        }

renders['end'] = {
            "title": 'Das Ende',
                'world': 'End',
                    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.3)]
                    }


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


