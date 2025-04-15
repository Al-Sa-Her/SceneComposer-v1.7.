import random

class CharacterDescriptor:
    @classmethod
    def INPUT_TYPES(cls):
        feature_options = ["none"] + [  # "none" como primera opción
            "cybernetic arm", "cybernetic leg", "cybernetic eye", "mechanical prosthetics",
            "demon horns", "pointed ears", "red skin", "claws", "tail",
            "angel wings", "halo", "golden eyes", "radiant skin",
            "pale skin", "fangs", "red eyes", "cloak",
            "wolf ears", "fangs", "claws", "hairy body",
            "fairy wings", "glowing dust", "pointed ears",
            "mechanical joints", "LED eyes", "metal plating",
            "dragon scales", "snake eyes", "feather hair",
            "tentacles", "antennae", "glowing marks",
            "skeletal parts", "ghostly aura", "tattered flesh"
        ]
        
        inputs = {
            "required": {
                # Body
                "🍒 Breast Size": (["none", "flat chest", "small breast", "medium breast", "large breast", "huge breast", "extra large breast"],),
                "🦶 Skin Tone": (["none"] + ["pale", "porcelain", "olive", "dark", "tan", "blueice", "green mint", "red"],),
                "🏋️ Body Type": (["none"] + ["petite", "slim", "skinny", "athletic", "muscular", "curvy", "plump", "chubby"],),
                
                # Face
                "💄 Lip Color": (["none"] + ["red", "white", "green", "pink", "brown", "black", "gray", "light gray", "lime green", "light blue", "purple"],),
                "💋 Lip Style": (["none", "natural lips", "lipstick", "neon lipstick"],),
                "😊 Attitude": (["none"] + ["happy", "smirk", "bored", "upset", "crazy", "flirty", "determined"], {"default": "happy"}),
                
                # Hair
                "🧏🏼‍♀️ Base Color": (["none"] + ["black", "white", "silver", "blonde", "ginger", "gray", "brown", "brunette"],),
                "✂️ Dye Style": (["none", "full dyed hair", "dyed hair tips"],),
                "✂️ Style": (["none"] + ["straight", "wavy", "curly", "afro", "braided", "viking braided", "ponytail", "high ponytail", "bun", "bun messy", "layered", "pixie cut", "twist"],),
                "🎨 Dyed?": (["none", "yes", "no"],),
                "🎨 Dye Color": (["none"] + ["red", "white", "green", "pink", "brown", "black", "gray", "light gray", "lime green", "light blue", "purple"],),
                "📏 Length": (["none"] + ["short", "medium", "long", "very long"],),
                
                # Eyes
                "👁️‍🗨️ Color": (["none"] + ["black", "brown", "blue", "green", "red", "yellow", "orange", "purple", "pink", "grey", "white"],),
                "👁️‍🗨️ Shape": (["none"] + ["almond", "downturned", "upturned", "hooded", "monolid"],),
                "💅 Makeup": (["none", "eyeliner", "eyeshadow"],),
                "🎨 Makeup Color": (["none"] + ["black", "blue", "cyan", "red", "green", "pink", "white", "yellow", "orange"],),
                
                # Special Features
                "🎭 Feature Count": ("INT", {"default": 0, "min": 0, "max": 5, "step": 1}),
                
                # Randomization
                "🎲 Randomize All": ("BOOLEAN", {"default": False}),
                "🌱 Seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
        
        # Add feature inputs (reduced to 5 max for better UI)
        for i in range(1, 6):
            inputs["required"][f"✨ Feature {i}"] = (feature_options, {"default": "none"})
        
        return inputs

    RETURN_TYPES = ("STRING",)
    FUNCTION = "describe_character"
    CATEGORY = "Custom Nodes/Character"

    def describe_character(self, **kwargs):
        parts = []
        
        # Body
        body_parts = []
        if kwargs["🏋️ Body Type"] != "none":
            body_parts.append(f"{kwargs['🏋️ Body Type']} body")
        if kwargs["🦶 Skin Tone"] != "none":
            body_parts.append(f"{kwargs['🦶 Skin Tone']} skin")
        if kwargs["🍒 Breast Size"] != "none":
            body_parts.append(kwargs["🍒 Breast Size"])
        if body_parts:
            parts.append(", ".join(body_parts))
        
        # Face (only if both color and style are not none)
        if kwargs["💋 Lip Style"] != "none" and kwargs["💄 Lip Color"] != "none":
            parts.append(f"{kwargs['💄 Lip Color']} {kwargs['💋 Lip Style']}")
        
        # Hair
        hair_parts = []
        if kwargs["🧏🏼‍♀️ Base Color"] != "none":
            hair_parts.append(f"{kwargs['🧏🏼‍♀️ Base Color']} hair")
            if kwargs["🎨 Dyed?"] == "yes" and kwargs["✂️ Dye Style"] != "none" and kwargs["🎨 Dye Color"] != "none":
                hair_parts.append(f"{kwargs['🎨 Dye Color']} {kwargs['✂️ Dye Style']}")
        if kwargs["✂️ Style"] != "none":
            hair_parts.append(kwargs["✂️ Style"])
        if kwargs["📏 Length"] != "none":
            hair_parts.append(f"{kwargs['📏 Length']} hair")
        if hair_parts:
            parts.append(", ".join(hair_parts))
        
        # Eyes
        eye_parts = []
        if kwargs["👁️‍🗨️ Color"] != "none":
            eye_parts.append(f"{kwargs['👁️‍🗨️ Color']} eyes")
        if kwargs["👁️‍🗨️ Shape"] != "none":
            eye_parts.append(f"{kwargs['👁️‍🗨️ Shape']} shaped")
        if kwargs["💅 Makeup"] != "none" and kwargs["🎨 Makeup Color"] != "none":
            eye_parts.append(f"{kwargs['🎨 Makeup Color']} {kwargs['💅 Makeup']}")
        if eye_parts:
            parts.append(", ".join(eye_parts))
        
        # Attitude (if not none)
        if kwargs["😊 Attitude"] != "none":
            attitude_desc = kwargs["😊 Attitude"]
            # Add attitude details
            if kwargs["😊 Attitude"] == "happy":
                attitude_desc += ", smiling"
            elif kwargs["😊 Attitude"] == "smirk":
                attitude_desc += ", smirking"
            elif kwargs["😊 Attitude"] == "bored":
                attitude_desc += ", looking bored"
            elif kwargs["😊 Attitude"] == "upset":
                attitude_desc += ", frowning"
            elif kwargs["😊 Attitude"] == "crazy":
                attitude_desc += ", wild expression"
            elif kwargs["😊 Attitude"] == "flirty":
                attitude_desc += ", flirty look"
            elif kwargs["😊 Attitude"] == "determined":
                attitude_desc += ", determined gaze"
            parts.append(attitude_desc)
        
        # Special Features (only non-none features)
        features = [kwargs[f"✨ Feature {i}"] for i in range(1, 6) if kwargs[f"✨ Feature {i}"] != "none"]
        if features:
            parts.append(", ".join(features))
        
        # Join all non-empty parts
        full_description = ", ".join(parts).lower()
        return (full_description,)

NODE_CLASS_MAPPINGS = {
    "CharacterDescriptor": CharacterDescriptor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterDescriptor": "👤 Smart Character"
}
