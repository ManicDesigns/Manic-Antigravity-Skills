---
name: using-aceternity-ui
description: Aceternity UI animated React components with Tailwind CSS and Framer Motion. Use for hero sections, cards, backgrounds, and premium landing page effects.
---

# Using Aceternity UI

Aceternity UI provides 200+ beautifully animated React components built with Tailwind CSS and Framer Motion.

## When to Use This Skill
- User wants premium animated landing page components
- User mentions "aceternity", "animated cards", or "hero effects"
- User needs 3D effects, parallax, or spotlight animations
- Building marketing pages, portfolios, or SaaS sites

## Installation

```bash
# Install dependencies
npm install framer-motion clsx tailwind-merge

# Components are copy-paste from https://ui.aceternity.com/components
```

---

## Components by Category

### Cards (15+)
| Component | Description |
|-----------|-------------|
| 3D Card Effect | Perspective hover elevation |
| Glare Card | Glare reflection on hover |
| Draggable Card | Physics-based dragging |
| Comet Card | Perplexity-style tilt |
| Card Spotlight | Spotlight reveal gradient |
| Tooltip Card | Mouse-following tooltip |
| Direction Aware Hover | Direction-based reveal |

### Scroll & Parallax (5+)
| Component | Description |
|-----------|-------------|
| Parallax Scroll | Layered parallax images |
| Sticky Scroll Reveal | Content reveals on scroll |
| Macbook Scroll | Image emerges from laptop |
| Container Scroll | Container animation on scroll |
| Hero Parallax | Full hero parallax effect |

### Text Animations (10+)
| Component | Description |
|-----------|-------------|
| Encrypted Text | Gibberish reveal effect |
| Colourful Text | Multi-color text |
| Text Generate Effect | Character-by-character reveal |
| Typewriter Effect | Typing animation |
| Flip Words | Word rotation animation |
| Text Hover Effect | x.ai-style gradient outline |
| Hero Highlight | Highlighted hero text |
| Text Reveal Card | Text reveal on hover |
| Layout Text Flip | Animated text layout |

### Backgrounds (10+)
| Component | Description |
|-----------|-------------|
| Noise Background | Animated gradients + noise |
| Dotted Glow | Glow with opacity animation |
| Background Lines | Wave pattern SVG paths |
| Background Beams | Exploding beam collision |
| Background Ripple | Click ripple grid |
| Vortex | Rotating particle vortex |
| Aurora Background | Northern lights effect |
| Spotlight | Moving spotlight effect |

### Navigation (7+)
| Component | Description |
|-----------|-------------|
| Floating Navbar | Floating nav with blur |
| Navbar Menu | Animated dropdown menu |
| Sidebar | Collapsible side panel |
| Floating Dock | macOS dock animation |
| Tabs | Animated tab switcher |
| Resizable Navbar | Responsive nav |
| Sticky Banner | Fixed announcement bar |

### Buttons & Inputs (6+)
| Component | Description |
|-----------|-------------|
| Tailwind CSS Buttons | Button collection |
| Hover Border Gradient | Gradient border on hover |
| Moving Border | Animated border movement |
| Stateful Button | Multi-state button |
| Signup Form | Complete signup form |
| Placeholders Vanish Input | Animated placeholder |

### Carousels (4+)
| Component | Description |
|-----------|-------------|
| Images Slider | Full-screen image slider |
| Carousel | Microinteraction carousel |
| Apple Cards Carousel | Apple.com-style cards |
| Testimonials | Animated testimonials |

### Layout & Grid (3+)
| Component | Description |
|-----------|-------------|
| Layout Grid | Animated grid layout |
| Bento Grid | Bento box layout |
| Container Cover | Cover transition |

### Data & Visualization (5+)
| Component | Description |
|-----------|-------------|
| GitHub Globe | 3D interactive globe |
| World Map | Animated world map |
| Timeline | Vertical timeline |
| Compare | Before/after slider |
| Codeblock | Syntax-highlighted code |

### Cursor Effects (3+)
| Component | Description |
|-----------|-------------|
| Following Pointer | Mouse-following elements |
| Pointer Highlight | Highlight under cursor |
| Lens | Magnifying lens effect |

### 3D Components (2+)
| Component | Description |
|-----------|-------------|
| 3D Pin | Location pin with depth |
| 3D Marquee | Rotating 3D marquee |

---

## Usage Example

### 3D Card Effect
```tsx
"use client";
import { CardContainer, CardBody, CardItem } from "@/components/ui/3d-card";

<CardContainer className="inter-var">
  <CardBody className="bg-gray-50 dark:bg-black">
    <CardItem translateZ="50" className="text-xl font-bold">
      Hover me
    </CardItem>
    <CardItem translateZ="100" className="w-full mt-4">
      <img src="/image.jpg" className="rounded-xl" />
    </CardItem>
  </CardBody>
</CardContainer>
```

### Text Generate Effect
```tsx
import { TextGenerateEffect } from "@/components/ui/text-generate-effect";

<TextGenerateEffect words="Words will appear one by one" />
```

### Hero Parallax
```tsx
import { HeroParallax } from "@/components/ui/hero-parallax";

const products = [
  { title: "Product 1", thumbnail: "/1.png", link: "#" },
  { title: "Product 2", thumbnail: "/2.png", link: "#" },
];

<HeroParallax products={products} />
```

---

## Resources
- Components: https://ui.aceternity.com/components
- Pro Version: https://pro.aceternity.com
