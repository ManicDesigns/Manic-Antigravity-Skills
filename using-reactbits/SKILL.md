---
name: using-reactbits
description: Adds React Bits animated components to the project. Use when the user asks for "React Bits", animated text, backgrounds, or interactive UI components.
---

# Using React Bits

React Bits is a collection of high-quality, animated React components. This skill provides 33+ components ready to use.

## When to Use This Skill
- User asks for "SplitText", "BlurText", or any animated text effect
- User mentions "React Bits"
- User wants animated backgrounds (Aurora, Particles, Waves)
- User needs interactive cards, cursors, or UI effects

## Installation

### Using CLI (Recommended)
```bash
npx shadcn@latest add https://reactbits.dev/r/<ComponentName>-TS-TW
```

### Manual Installation
1. Install dependencies (varies by component, common ones below):
```bash
npm install gsap @gsap/react   # For text animations
npm install framer-motion       # For UI animations
```
2. Copy the component file from `resources/<ComponentName>.json`
3. Extract the `content` field from the JSON and save as `.tsx`

## Available Components

### Text Animations
| Component | Description |
|-----------|-------------|
| SplitText | Staggered letter/word entrance animation |
| BlurText | Blur-to-focus text reveal |
| GradientText | Animated gradient text |
| ShinyText | Shimmering highlight effect |
| GlitchText | Glitch/distortion effect |
| DecryptedText | Matrix-style decryption animation |
| RotatingText | Rotating word carousel |
| FuzzyText | Fuzzy/static text effect |
| CountUp | Animated number counter |

### Backgrounds
| Component | Description |
|-----------|-------------|
| Aurora | Northern lights background |
| Hyperspeed | Star field warp effect |
| Particles | Floating particle system |
| Waves | Animated wave patterns |
| Squares | Animated grid squares |
| GridMotion | Interactive grid animation |
| Ribbons | Flowing ribbon background |
| Threads | Thread-like animations |

### UI Components
| Component | Description |
|-----------|-------------|
| TiltedCard | 3D tilt effect on hover |
| Dock | macOS-style dock menu |
| SpotlightCard | Spotlight hover effect |
| Magnet | Magnetic hover attraction |
| AnimatedContent | Animated content transitions |
| FadeContent | Fade-in content |
| InfiniteMenu | Infinite scrolling menu |
| Carousel | Image/content carousel |
| StarBorder | Animated star border |
| DecayCard | Decay/dissolve card effect |

### Cursors & Effects
| Component | Description |
|-----------|-------------|
| BlobCursor | Blob-following cursor |
| ClickSpark | Spark effect on click |
| Crosshair | Crosshair cursor |

### Galleries
| Component | Description |
|-----------|-------------|
| Masonry | Masonry grid layout |
| CircularGallery | Circular image gallery |
| Stack | Stacked cards |

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
