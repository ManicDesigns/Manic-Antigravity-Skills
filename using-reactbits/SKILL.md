---
name: using-reactbits
description: Adds React Bits animated components to the project. Use when the user asks for "React Bits", animated text, backgrounds, or interactive UI components.
---

# Using React Bits

React Bits is a collection of **120+ high-quality, animated React components**. This skill provides ready-to-use component source files.

## When to Use This Skill
- User asks for animated text effects (SplitText, BlurText, GlitchText, etc.)
- User mentions "React Bits" or "reactbits"
- User wants animated backgrounds (Aurora, Galaxy, Particles, Silk, etc.)
- User needs interactive cards, cursors, menus, or UI effects

## Installation

### Using CLI (Recommended)
```bash
npx shadcn@latest add https://reactbits.dev/r/<ComponentName>-TS-TW
```

### Manual Installation
1. Install common dependencies:
```bash
npm install gsap @gsap/react framer-motion
```
2. Copy component from `resources/<ComponentName>.json`
3. Extract the `content` field and save as `.tsx`

---

## Text Animations (23)

| Component | Description |
|-----------|-------------|
| ASCIIText | ASCII art text rendering |
| BlurText | Blur-to-focus text reveal |
| CircularText | Text arranged in a circle |
| CountUp | Animated number counter |
| CurvedLoop | Text following curved path |
| DecryptedText | Matrix-style decryption animation |
| FallingText | Physics-based falling letters |
| FuzzyText | Fuzzy/static text effect |
| GlitchText | Glitch/distortion effect |
| GradientText | Animated gradient text |
| RotatingText | Rotating word carousel |
| ScrambledText | Scrambled letter animation |
| ScrollFloat | Floating text on scroll |
| ScrollReveal | Reveal text on scroll |
| ScrollVelocity | Velocity-based scroll effect |
| ShinyText | Shimmering highlight effect |
| Shuffle | Shuffling letters animation |
| SplitText | Staggered letter/word entrance |
| TextCursor | Animated text cursor |
| TextPressure | Pressure-responsive text |
| TextType | Typewriter effect |
| TrueFocus | Focus-based text highlight |
| VariableProximity | Proximity-based variable font |

---

## Animations & Effects (27)

| Component | Description |
|-----------|-------------|
| AnimatedContent | Animated content transitions |
| Antigravity | Anti-gravity floating effect |
| BlobCursor | Blob-following cursor |
| ClickSpark | Spark effect on click |
| Crosshair | Crosshair cursor |
| Cubes | 3D cubes animation |
| ElectricBorder | Electric border effect |
| FadeContent | Fade-in content |
| GhostCursor | Ghost trail cursor |
| GlareHover | Glare effect on hover |
| GradualBlur | Gradual blur transition |
| ImageTrail | Image trail on mouse move |
| LaserFlow | Laser beam flow effect |
| LogoLoop | Looping logo animation |
| Magnet | Magnetic hover attraction |
| MagnetLines | Magnetic field lines |
| MetaBalls | Metaball physics animation |
| MetallicPaint | Metallic paint effect |
| Noise | Noise overlay effect |
| PixelTrail | Pixelated cursor trail |
| PixelTransition | Pixel-based transitions |
| Ribbons | Flowing ribbon animation |
| ShapeBlur | Shape with blur effect |
| SplashCursor | Splash effect cursor |
| StarBorder | Animated star border |
| StickerPeel | Sticker peel animation |
| TargetCursor | Target/scope cursor |

---

## UI Components (35)

| Component | Description |
|-----------|-------------|
| AnimatedList | Animated list items |
| BounceCards | Bouncing card stack |
| BubbleMenu | Bubble navigation menu |
| CardNav | Card-based navigation |
| CardSwap | Swappable card deck |
| Carousel | Image/content carousel |
| ChromaGrid | Chromatic grid layout |
| CircularGallery | Circular image gallery |
| Counter | Animated counter display |
| DecayCard | Decay/dissolve card effect |
| Dock | macOS-style dock menu |
| DomeGallery | Dome-shaped gallery |
| ElasticSlider | Elastic range slider |
| FlowingMenu | Flowing navigation menu |
| FluidGlass | Fluid glass morphism |
| FlyingPosters | Flying poster cards |
| Folder | 3D folder component |
| GlassIcons | Glassmorphic icons |
| GlassSurface | Glass surface effect |
| GooeyNav | Gooey navigation |
| InfiniteMenu | Infinite scrolling menu |
| Lanyard | Lanyard badge animation |
| MagicBento | Bento grid with effects |
| Masonry | Masonry grid layout |
| ModelViewer | 3D model viewer |
| PillNav | Pill-shaped navigation |
| PixelCard | Pixelated card hover |
| ProfileCard | Animated profile card |
| ReflectiveCard | Reflective surface card |
| ScrollStack | Scroll-driven card stack |
| SpotlightCard | Spotlight hover effect |
| Stack | Stacked cards |
| StaggeredMenu | Staggered menu animation |
| Stepper | Multi-step indicator |
| TiltedCard | 3D tilt effect on hover |

---

## Backgrounds (35)

| Component | Description |
|-----------|-------------|
| Aurora | Northern lights effect |
| Balatro | Card game aesthetic |
| Ballpit | 3D ball pit physics |
| Beams | Light beam rays |
| ColorBends | Color bending effect |
| DarkVeil | Dark veil overlay |
| Dither | Dithered gradient |
| DotGrid | Animated dot grid |
| FaultyTerminal | Glitchy terminal effect |
| FloatingLines | Floating line patterns |
| Galaxy | Galaxy/space background |
| GradientBlinds | Gradient blinds effect |
| GridDistortion | Distorted grid |
| GridMotion | Interactive grid animation |
| GridScan | Scanning grid effect |
| Hyperspeed | Star field warp effect |
| Iridescence | Iridescent shimmer |
| LetterGlitch | Glitching letter background |
| LightPillar | Light pillar effect |
| LightRays | Radiating light rays |
| Lightning | Lightning effect |
| LiquidChrome | Liquid chrome effect |
| LiquidEther | Ethereal liquid effect |
| Orb | Glowing orb background |
| Particles | Floating particle system |
| PixelBlast | Pixel explosion effect |
| PixelSnow | Pixelated snow fall |
| Plasma | Plasma wave effect |
| Prism | Prismatic light effect |
| PrismaticBurst | Prismatic burst animation |
| RippleGrid | Ripple effect grid |
| Silk | Silk fabric animation |
| Squares | Animated grid squares |
| Threads | Thread-like animations |
| Waves | Animated wave patterns |

---

## Usage Example

```tsx
import SplitText from '@/components/SplitText';

<SplitText
  text="Hello, World!"
  className="text-4xl font-bold"
  delay={50}
  duration={1.0}
/>
```

## Resources

Component source files are in [resources/](resources/). Each `.json` file contains:
- `content`: The component TypeScript/React code
- `dependencies`: Required npm packages
- `registryDependencies`: Other ReactBits components needed

## Creative Tools

ReactBits also offers free creative tools at [reactbits.dev/tools](https://reactbits.dev/tools):
- **Background Studio** - Create custom backgrounds
- **Shape Magic** - Generate SVG shapes
- **Texture Lab** - Create texture patterns
