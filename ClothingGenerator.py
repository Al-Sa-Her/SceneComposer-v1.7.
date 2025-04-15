import random

class OutfitGenerator:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        colors = ["none"] + [  # "none" como primera opción
            "black", "white", "blue", "red", "green", "gray", "yellow", "striped",
            "ivory", "charcoal", "slate", "cream", "purple", "orange", "pink", "cyan",
            "magenta", "gold", "silver", "bronze", "copper", "rose gold", "emerald",
            "sapphire", "ruby", "amber", "olive", "pastel pink", "mint green", "lavender",
            "sky blue", "peach", "navy", "burgundy", "forest green", "midnight blue",
            "polka dot", "checkered", "floral", "camouflage", "geometric", "gradient",
            "ombré", "iridescent", "neon", "glow-in-the-dark"
        ]
        
        return {
            "required": {
                # Upper Clothing
                "👕 Upper": (["none", "t-shirt", "crop top", "button-up shirt", "sweater", "hoodie", 
                             "blouse", "tank top", "corset", "kimono", "peasant top", 
                             "leather jacket", "denim jacket", "bomber jacket", "trench coat", 
                             "parka", "blazer", "cyberpunk vest", "fur coat", "sundress", 
                             "ball gown", "slip dress", "mini dress", "jumpsuit", 
                             "victorian dress", "sci-fi bodysuit"], {"default": "t-shirt"}),
                "🎨 Upper Color": (colors, {"default": "white"}),
                
                # Lower Clothing
                "👖 Lower": (["none", "jeans", "slim fit pants", "cargo pants", "leather pants", 
                             "sweatpants", "high-waisted pants", "harem pants", "mini skirt", 
                             "pencil skirt", "pleated skirt", "tiered skirt", "metallic skirt", 
                             "asymmetrical skirt", "denim shorts", "athletic shorts", 
                             "high-waisted shorts", "bermuda shorts"], {"default": "jeans"}),
                "🎨 Lower Color": (colors, {"default": "blue"}),
                
                # Accessories
                "💍 Accessory": (["none", "necklace", "bracelet", "watch", "ring", "scarf", "belt", 
                                 "gloves", "handbag", "choker", "statement necklace", 
                                 "hoop earrings", "stud earrings", "nose ring", "smartwatch", 
                                 "AR gloves", "holographic bracelet", "cybernetic arm implants", 
                                 "bandana", "suspenders", "chain belt", "fingerless gloves", 
                                 "hairpins", "floral crowns", "headbands", "cybernetic hair clips", 
                                 "glowing hair tattoos"], {"default": "necklace"}),
                "🎨 Acc. Color": (colors, {"default": "gold"}),
                
                # Footwear
                "👟 Footwear": (["none", "sneakers", "loafers", "sandals", "slip-ons", "canvas shoes", 
                                "ankle boots", "knee-high boots", "combat boots", "cowboy boots", 
                                "platform boots", "stilettos", "block heels", "mules", 
                                "strappy heels", "armored greaves", "cyberpunk LED shoes", 
                                "elf-like pointed boots", "transparent soles"], {"default": "sneakers"}),
                "🎨 Footwear Color": (colors, {"default": "black"}),
                
                # Headwear
                "🧢 Headwear": (["none", "baseball cap", "beanie", "fedora", "beret", "bucket hat", 
                                "top hat", "fascinator", "trilby", "bowler hat", "mage hood", 
                                "crown", "tiara", "samurai helmet", "halo"], {"default": "baseball cap"}),
                "🎨 Headwear Color": (colors, {"default": "black"}),
                
                # Randomization
                "🎲 Randomize All": ("BOOLEAN", {"default": False}),
                "🌱 Seed": ("INT", {"default": 0, "min": 0, "max": 999999999}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "Clothing"

    def generate(self, **kwargs):
        # Randomize if enabled
        if kwargs['🎲 Randomize All']:
            random.seed(kwargs['🌱 Seed'])
            
            # Available options
            categories = {
                'upper': ["none", "t-shirt", "sweater", "hoodie", "leather jacket"],
                'lower': ["none", "jeans", "leather pants", "skirt", "shorts"],
                'accessory': ["none", "necklace", "watch", "glasses", "ring"],
                'footwear': ["none", "sneakers", "boots", "sandals", "heels"],
                'headwear': ["none", "baseball cap", "beanie", "fedora", "hood"]
            }
            
            colors = ["none", "black", "white", "red", "blue", "green", "gold", "silver"]
            
            for category in categories:
                kwargs[f"👕 Upper" if category == 'upper' else 
                      f"👖 Lower" if category == 'lower' else
                      f"💍 Accessory" if category == 'accessory' else
                      f"👟 Footwear" if category == 'footwear' else
                      f"🧢 Headwear"] = random.choice(categories[category])
                
                kwargs[f"🎨 Upper Color" if category == 'upper' else 
                      f"🎨 Lower Color" if category == 'lower' else
                      f"🎨 Acc. Color" if category == 'accessory' else
                      f"🎨 Footwear Color" if category == 'footwear' else
                      f"🎨 Headwear Color"] = random.choice(colors)
        
        # Build outfit description
        outfit_parts = []
        
        # Upper
        if kwargs["👕 Upper"] != "none" and kwargs["🎨 Upper Color"] != "none":
            outfit_parts.append(f"{kwargs['🎨 Upper Color']} {kwargs['👕 Upper']}")
        
        # Lower
        if kwargs["👖 Lower"] != "none" and kwargs["🎨 Lower Color"] != "none":
            outfit_parts.append(f"{kwargs['🎨 Lower Color']} {kwargs['👖 Lower']}")
        
        # Accessory
        if kwargs["💍 Accessory"] != "none" and kwargs["🎨 Acc. Color"] != "none":
            outfit_parts.append(f"{kwargs['🎨 Acc. Color']} {kwargs['💍 Accessory']}")
        
        # Footwear
        if kwargs["👟 Footwear"] != "none" and kwargs["🎨 Footwear Color"] != "none":
            outfit_parts.append(f"{kwargs['🎨 Footwear Color']} {kwargs['👟 Footwear']}")
        
        # Headwear
        if kwargs["🧢 Headwear"] != "none" and kwargs["🎨 Headwear Color"] != "none":
            outfit_parts.append(f"{kwargs['🎨 Headwear Color']} {kwargs['🧢 Headwear']}")
        
        return (", ".join(outfit_parts).lower(),)

NODE_CLASS_MAPPINGS = {
    "OutfitGenerator": OutfitGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OutfitGenerator": "👗 Smart Outfit Generator"
}
