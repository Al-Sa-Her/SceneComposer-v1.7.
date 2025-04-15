import random

class EnvironmentGenerator:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        location_categories = {
            "🏠 Interior": ["none"] + [  # "none" como primera opción
                "living room", "bedroom", "kitchen", "bathroom", "home office",
                "library", "study", "attic", "basement", "garage",
                "dungeon", "throne room", "great hall", "alchemy lab"
            ],
            "🏙️ Urbano": ["none"] + [
                "city street", "alleyway", "park", "plaza", "market square",
                "train station", "subway", "rooftop", "bridge", "construction site",
                "abandoned factory", "parking garage", "sewer system"
            ],
            "🌳 Naturaleza": ["none"] + [
                "forest", "mountains", "lake", "river", "meadow",
                "waterfall", "cave", "volcano", "canyon", "cliffside",
                "beach", "island", "jungle", "swamp", "desert"
            ],
            "🧙 Fantasía": ["none"] + [
                "magic castle", "elf village", "dwarf mine", "floating island",
                "crystal cave", "dragon lair", "wizard tower", "enchanted forest",
                "fairy glen", "underwater city", "cloud city", "haunted mansion"
            ],
            "🚀 Sci-Fi": ["none"] + [
                "space station", "starship interior", "alien city", "cyberpunk street",
                "holographic arena", "robot factory", "virtual world", "moon base",
                "futuristic lab", "nanotech facility", "quantum computer core"
            ],
            "🏛️ Histórico": ["none"] + [
                "medieval village", "ancient temple", "roman forum", "egyptian pyramid",
                "renaissance castle", "samurai dojo", "viking longhouse", "wild west town",
                "industrial revolution factory", "1920s speakeasy"
            ],
            "🌀 Especial": ["none"] + [
                "dreamscape", "heavenly realm", "hellscape", "purgatory",
                "time rift", "dimensional portal", "black hole interior",
                "subatomic world", "cosmic void", "simulation glitch"
            ]
        }
        
        # Preparar lista completa de ubicaciones (excluyendo "none")
        all_locations = []
        for category_locs in location_categories.values():
            all_locations.extend([loc for loc in category_locs if loc != "none"])
        
        return {
            "required": {
                # Ubicación
                "📍 Location Type": (list(location_categories.keys()), {"default": "🌳 Naturaleza"}),
                "🏞️ Location": (["none"] + all_locations, {"default": "forest"}),
                
                # Tiempo
                "🕒 Time": (["none"] + ["morning", "afternoon", "evening", "night", "sunrise", "sunset"], {"default": "day"}),
                
                # Clima
                "☀️ Weather": (["none"] + ["clear", "sunny", "cloudy", "rainy", "stormy", "foggy", "snowy"], {"default": "clear"}),
                
                # Detalles
                "📝 Detail": (["simple", "detailed", "very detailed"], {"default": "detailed"}),
                
                # Randomización
                "🎲 Randomize": ("BOOLEAN", {"default": False}),
                "🌱 Seed": ("INT", {"default": 0, "min": 0, "max": 999999999}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "Environment"
    
    def generate(self, **kwargs):
        # Configuración básica
        config = {
            "location_type": kwargs['📍 Location Type'],
            "location": kwargs['🏞️ Location'],
            "time": kwargs['🕒 Time'],
            "weather": kwargs['☀️ Weather'],
            "detail": kwargs['📝 Detail']
        }
        
        # Randomización si está activada
        if kwargs['🎲 Randomize']:
            random.seed(kwargs['🌱 Seed'])
            location_categories = {
                "🏠 Interior": ["none"] + ["living room", "bedroom", "kitchen"],
                "🏙️ Urbano": ["none"] + ["city street", "alleyway", "park"],
                "🌳 Naturaleza": ["none"] + ["forest", "mountains", "lake"],
                "🧙 Fantasía": ["none"] + ["magic castle", "elf village"],
                "🚀 Sci-Fi": ["none"] + ["space station", "alien city"],
                "🏛️ Histórico": ["none"] + ["medieval village", "ancient temple"],
                "🌀 Especial": ["none"] + ["dreamscape", "heavenly realm"]
            }
            
            # Randomizar ubicación (puede ser "none")
            config['location_type'] = random.choice(list(location_categories.keys()))
            config['location'] = random.choice(location_categories[config['location_type']])
            
            # Randomizar tiempo (puede ser "none")
            config['time'] = random.choice(["none", "morning", "afternoon", "evening", "night"])
            
            # Randomizar clima (puede ser "none") con restricciones lógicas
            weather_options = ["none", "clear", "sunny", "cloudy", "rainy", "stormy", "foggy", "snowy"]
            if config['time'] == "night":
                weather_options.remove("sunny")
            if config['location'] in ["beach", "desert"]:
                weather_options = [w for w in weather_options if w not in ["snowy", "rainy"]]
            config['weather'] = random.choice(weather_options)
        
        # Construir partes del prompt
        parts = []
        
        # Ubicación (solo si no es "none")
        if config['location'] != "none":
            if config['detail'] == "simple":
                location_desc = config['location']
            elif config['detail'] == "detailed":
                descriptors = {
                    "🏠 Interior": ["cozy", "spacious", "cluttered"],
                    "🏙️ Urbano": ["bustling", "gritty", "neon-lit"],
                    "🌳 Naturaleza": ["lush", "vast", "tranquil"],
                    "🧙 Fantasía": ["enchanted", "mystical", "arcane"],
                    "🚀 Sci-Fi": ["futuristic", "high-tech", "gleaming"],
                    "🏛️ Histórico": ["ancient", "timeworn", "grandiose"],
                    "🌀 Especial": ["surreal", "mind-bending", "unearthly"]
                }
                descriptor = random.choice(descriptors.get(config['location_type'], [""]))
                location_desc = f"{descriptor} {config['location']}" if descriptor else config['location']
            else:  # very detailed
                very_detailed = {
                    "forest": "dense ancient forest with bioluminescent plants",
                    "magic castle": "towering gothic magic castle with floating spires",
                    "space station": "massive rotating space station with view of Earth",
                    "city street": "neon-lit cyberpunk street with holographic advertisements"
                }
                location_desc = very_detailed.get(config['location'], 
                    f"{random.choice(['majestic', 'vast', 'intricate'])} {config['location']}")
            
            parts.append(location_desc)
        
        # Tiempo (solo si no es "none")
        if config['time'] != "none":
            parts.append(config['time'])
        
        # Clima (solo si no es "none")
        if config['weather'] != "none":
            parts.append(config['weather'])
        
        # Unir todas las partes no vacías
        prompt = ", ".join(parts).lower()
        return (prompt,)

NODE_CLASS_MAPPINGS = {
    "EnvironmentGenerator": EnvironmentGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EnvironmentGenerator": "🌍 Smart Environment"
}
