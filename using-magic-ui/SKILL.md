---
name: using-magic-ui
description: Magic UI landing page components for React. Use for hero sections, animated text, buttons, and marketing page elements.
---

# Using Magic UI

Magic UI provides beautiful, copy-paste components designed specifically for landing pages and marketing sites.

## When to Use This Skill
- User needs landing page or marketing components
- User mentions "magic ui" or "magical animations"
- Building hero sections, feature grids, or CTAs
- User wants animated text effects or particle effects

## Installation

```bash
# Magic UI uses shadcn CLI
npx shadcn@latest add "https://magicui.design/r/animated-beam"
```

Or copy components directly from https://magicui.design/docs

---

## Component Categories

### Text Animations
| Component | Description |
|-----------|-------------|
| Animated Shiny Text | Shimmering text effect |
| Text Animate | Character animation |
| Word Fade In | Words fade in sequence |
| Blur Fade | Blur-to-focus transition |
| Box Reveal | Box mask reveal |
| Flip Text | 3D text flip |
| Gradual Spacing | Letter spacing animation |
| Letter Pullup | Letters pull up into view |
| Scroll Based Velocity | Speed-based text motion |
| Sparkles Text | Sparkle particle text |
| Typing Animation | Typewriter effect |
| Word Pull Up | Words animate upward |
| Word Rotate | Rotating word carousel |

### Buttons
| Component | Description |
|-----------|-------------|
| Shimmer Button | Shimmer sweep effect |
| Animated Subscribe | Email subscription button |
| Pulsating Button | Pulse animation |
| Rainbow Button | Rainbow gradient border |
| Ripple Button | Click ripple effect |
| Shiny Button | Shine sweep on hover |

### Backgrounds
| Component | Description |
|-----------|-------------|
| Animated Beam | Animated connecting beams |
| Animated Grid Pattern | Moving grid background |
| Dot Pattern | Dot matrix background |
| Grid Pattern | Static grid pattern |
| Linear Gradient | Smooth color gradient |
| Particles | Floating particle effect |
| Retro Grid | 80s-style perspective grid |
| Ripple | Water ripple effect |

### Cards & Containers  
| Component | Description |
|-----------|-------------|
| Bento Grid | Bento box layout |
| Globe | 3D interactive globe |
| Magic Card | Spotlight hover card |
| Meteors | Falling meteor animation |
| Neon Gradient Card | Neon border effect |
| Safari | Browser mockup frame |

### Navigation & UI
| Component | Description |
|-----------|-------------|
| Dock | macOS-style dock |
| Marquee | Infinite scroll marquee |
| Animated List | Staggered list animations |
| Confetti | Celebration confetti |
| Cool Mode | Emoji rain on click |
| Orbiting Circles | Rotating orbit elements |
| Pointer | Custom cursor effects |

### Charts & Data
| Component | Description |
|-----------|-------------|
| Animated Circular Bar | Circular progress |
| Number Ticker | Animated counter |
| Gauge Circle | Gauge visualization |

---

## Usage Examples

### Shimmer Button
```tsx
import { ShimmerButton } from "@/components/magicui/shimmer-button";

<ShimmerButton className="shadow-2xl">
  <span className="text-white font-medium">Get Started</span>
</ShimmerButton>
```

### Animated Beam (Architecture Diagrams)
```tsx
import { AnimatedBeamMultipleOutputDemo } from "@/components/magicui/animated-beam";

<AnimatedBeamMultipleOutputDemo />
```

### Bento Grid
```tsx
import { BentoGrid, BentoCard } from "@/components/magicui/bento-grid";

<BentoGrid>
  <BentoCard
    name="Feature 1"
    description="Description here"
    Icon={Icon1}
    background={<div />}
  />
</BentoGrid>
```

### Number Ticker
```tsx
import { NumberTicker } from "@/components/magicui/number-ticker";

<NumberTicker value={1000} />
```

### Marquee (Logo Scroll)
```tsx
import { Marquee } from "@/components/magicui/marquee";

<Marquee pauseOnHover className="[--duration:20s]">
  {logos.map((logo) => (
    <img key={logo.name} src={logo.src} />
  ))}
</Marquee>
```

---

## Resources
- Documentation: https://magicui.design/docs
- Components: https://magicui.design/docs/components
- Templates: https://magicui.design/templates
