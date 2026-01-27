"""
ReactBits Component Crawler
Fetches component JSON files from the ReactBits registry API
"""
import os
import json
import time
import requests

# Configuration
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources")
DELAY = 0.5  # Seconds between requests
BASE_URL = "https://reactbits.dev/r"

# All components organized by category
COMPONENTS = {
    "TextAnimations": [
        "ASCIIText", "BlurText", "CircularText", "CountUp", "CurvedLoop",
        "DecryptedText", "FallingText", "FuzzyText", "GlitchText", "GradientText",
        "RotatingText", "ScrambledText", "ScrollFloat", "ScrollReveal", "ScrollVelocity",
        "ShinyText", "Shuffle", "SplitText", "TextCursor", "TextPressure",
        "TextType", "TrueFocus", "VariableProximity"
    ],
    "Animations": [
        "AnimatedContent", "Antigravity", "BlobCursor", "ClickSpark", "Crosshair",
        "Cubes", "ElectricBorder", "FadeContent", "GhostCursor", "GlareHover",
        "GradualBlur", "ImageTrail", "LaserFlow", "LogoLoop", "Magnet",
        "MagnetLines", "MetaBalls", "MetallicPaint", "Noise", "PixelTrail",
        "PixelTransition", "Ribbons", "ShapeBlur", "SplashCursor", "StarBorder",
        "StickerPeel", "TargetCursor"
    ],
    "Components": [
        "AnimatedList", "BounceCards", "BubbleMenu", "CardNav", "CardSwap",
        "Carousel", "ChromaGrid", "CircularGallery", "Counter", "DecayCard",
        "Dock", "DomeGallery", "ElasticSlider", "FlowingMenu", "FluidGlass",
        "FlyingPosters", "Folder", "GlassIcons", "GlassSurface", "GooeyNav",
        "InfiniteMenu", "Lanyard", "MagicBento", "Masonry", "ModelViewer",
        "PillNav", "PixelCard", "ProfileCard", "ReflectiveCard", "ScrollStack",
        "SpotlightCard", "Stack", "StaggeredMenu", "Stepper", "TiltedCard"
    ],
    "Backgrounds": [
        "Aurora", "Balatro", "Ballpit", "Beams", "ColorBends", "DarkVeil",
        "Dither", "DotGrid", "FaultyTerminal", "FloatingLines", "Galaxy",
        "GradientBlinds", "GridDistortion", "GridMotion", "GridScan", "Hyperspeed",
        "Iridescence", "LetterGlitch", "LightPillar", "LightRays", "Lightning",
        "LiquidChrome", "LiquidEther", "Orb", "Particles", "PixelBlast",
        "PixelSnow", "Plasma", "Prism", "PrismaticBurst", "RippleGrid",
        "Silk", "Squares", "Threads", "Waves"
    ]
}

def fetch_component(name):
    """Fetch a component JSON from the ReactBits registry."""
    # ReactBits uses format: ComponentName-TS-TW for TypeScript + Tailwind
    url = f"{BASE_URL}/{name}-TS-TW.json"
    print(f"Fetching: {name}")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"  Warning: Status {response.status_code} for {name}")
            return None
    except Exception as e:
        print(f"  Error fetching {name}: {e}")
        return None

def save_component(name, data):
    """Save component JSON to file."""
    filepath = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"  Saved: {name}.json")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    total = sum(len(components) for components in COMPONENTS.values())
    fetched = 0
    failed = []
    
    print(f"Starting ReactBits component sync...")
    print(f"Total components to fetch: {total}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("-" * 50)
    
    for category, components in COMPONENTS.items():
        print(f"\n=== {category} ({len(components)} components) ===")
        for name in components:
            # Check if already exists
            filepath = os.path.join(OUTPUT_DIR, f"{name}.json")
            if os.path.exists(filepath):
                print(f"  Skipping {name} (already exists)")
                fetched += 1
                continue
            
            data = fetch_component(name)
            if data:
                save_component(name, data)
                fetched += 1
            else:
                failed.append(name)
            
            time.sleep(DELAY)
    
    print("\n" + "=" * 50)
    print(f"Sync complete!")
    print(f"Fetched: {fetched}/{total}")
    if failed:
        print(f"Failed ({len(failed)}): {', '.join(failed)}")

if __name__ == "__main__":
    main()
