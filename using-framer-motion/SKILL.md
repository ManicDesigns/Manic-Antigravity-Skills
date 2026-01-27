---
name: using-framer-motion
description: Framer Motion (now Motion) animation library for React. Use for animations, gestures, scroll effects, and layout transitions.
---

# Using Framer Motion / Motion

Motion (formerly Framer Motion) is a production-ready animation library for React, JavaScript, and Vue.

## When to Use This Skill
- User needs smooth React animations
- User mentions "framer motion", "motion", or "animate"
- User wants scroll animations, gestures, or layout transitions
- Building interactive UI with hover/tap effects

## Installation

```bash
npm install motion
# or for React specifically
npm install framer-motion
```

---

## Core Animation APIs

### Basic Animation
```tsx
import { motion } from "framer-motion"

<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5 }}
>
  Animated content
</motion.div>
```

### Hover & Tap
```tsx
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: "spring", stiffness: 400 }}
>
  Click me
</motion.button>
```

### Exit Animations (AnimatePresence)
```tsx
import { AnimatePresence, motion } from "framer-motion"

<AnimatePresence>
  {isVisible && (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      Removable content
    </motion.div>
  )}
</AnimatePresence>
```

---

## Scroll Animations

### Scroll-Triggered
```tsx
import { motion, useScroll, useTransform } from "framer-motion"

function ParallaxSection() {
  const { scrollYProgress } = useScroll()
  const y = useTransform(scrollYProgress, [0, 1], [0, -200])
  
  return (
    <motion.div style={{ y }}>
      Parallax content
    </motion.div>
  )
}
```

### Scroll Into View
```tsx
<motion.div
  initial={{ opacity: 0, y: 50 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, amount: 0.3 }}
>
  Reveals when scrolled into view
</motion.div>
```

---

## Layout Animations

### Shared Layout
```tsx
<motion.div layout>
  {/* Animates position/size changes automatically */}
  <motion.div layout className={isExpanded ? "large" : "small"} />
</motion.div>
```

### Layout ID (Shared Element Transitions)
```tsx
// List view
<motion.img layoutId={`image-${id}`} src={image} />

// Detail view
<motion.img layoutId={`image-${id}`} src={image} className="large" />
```

---

## Gestures

### Drag
```tsx
<motion.div
  drag
  dragConstraints={{ left: 0, right: 300, top: 0, bottom: 200 }}
  dragElastic={0.2}
>
  Drag me
</motion.div>
```

### Pan & Pinch
```tsx
<motion.div
  onPan={(e, info) => console.log(info.offset)}
  onPinch={(e, info) => console.log(info.scale)}
/>
```

---

## Variants (Orchestrated Animations)

```tsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 }
  }
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
}

<motion.ul variants={container} initial="hidden" animate="show">
  {items.map(i => (
    <motion.li key={i} variants={item}>{i}</motion.li>
  ))}
</motion.ul>
```

---

## Spring Physics

```tsx
<motion.div
  animate={{ x: 100 }}
  transition={{
    type: "spring",
    stiffness: 100,   // Higher = faster
    damping: 10,      // Higher = less bounce
    mass: 1           // Higher = heavier
  }}
/>
```

---

## Timeline Sequences

```tsx
import { useAnimate, stagger } from "framer-motion"

function Sequence() {
  const [scope, animate] = useAnimate()
  
  useEffect(() => {
    animate([
      [".box", { x: 100 }],
      [".box", { rotate: 90 }],
      [".circle", { scale: 1.5 }, { at: "<" }], // simultaneous
    ])
  }, [])
  
  return <div ref={scope}>...</div>
}
```

---

## Resources
- Documentation: https://motion.dev/docs
- Examples: https://motion.dev/examples
- Tutorials: https://motion.dev/tutorials
