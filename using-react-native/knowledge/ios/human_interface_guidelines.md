# Apple Human Interface Guidelines (iOS)

> **Source**: https://developer.apple.com/design/human-interface-guidelines/

## Core Principles

### Clarity
- Text is legible at every size
- Icons are precise and clear
- Adornments are subtle and appropriate
- Focus on essential content

### Deference
- Fluid motion and crisp interface help people understand and interact
- Content fills the entire screen
- Translucency and blur hint at more

### Depth
- Visual layers and realistic motion convey hierarchy
- Touch and discoverability enhance delight
- Transitions provide sense of depth

---

## iOS Design Patterns

### Navigation
| Pattern | Use When |
|---------|----------|
| **Tab Bar** | Top-level navigation (3-5 items) |
| **Navigation Bar** | Hierarchical content (back button) |
| **Modals** | Self-contained tasks, settings |
| **Search** | Extensive content filtering |

### Tab Bar
- 3-5 tabs maximum
- Use SF Symbols for icons
- Highlight selected tab
- Always visible (except in rare cases)

```tsx
// React Native Tab Navigation
<Tab.Navigator>
  <Tab.Screen name="Home" component={HomeScreen} />
  <Tab.Screen name="Search" component={SearchScreen} />
  <Tab.Screen name="Profile" component={ProfileScreen} />
</Tab.Navigator>
```

### Navigation Bar
- Title in center
- Back button on left
- Action buttons on right (max 2)
- Support large titles for scrollable content

---

## Typography

### System Fonts
Use **SF Pro** (San Francisco) - automatically used in React Native

### Dynamic Type Sizes
| Style | Default Size | Usage |
|-------|--------------|-------|
| largeTitle | 34pt | Screen titles |
| title1 | 28pt | Section headers |
| title2 | 22pt | Sub-headers |
| title3 | 20pt | Cards |
| headline | 17pt (semi-bold) | Emphasized body |
| body | 17pt | Primary content |
| callout | 16pt | Secondary content |
| subhead | 15pt | Subtitles |
| footnote | 13pt | Captions, hints |
| caption1 | 12pt | Timestamps |
| caption2 | 11pt | Fine print |

---

## Colors

### System Colors
Use adaptive system colors that adjust for light/dark mode:

| Color | Light | Dark | Usage |
|-------|-------|------|-------|
| label | Black | White | Primary text |
| secondaryLabel | Gray | Light gray | Secondary text |
| tertiaryLabel | Lighter gray | Darker gray | Tertiary text |
| systemBackground | White | Black | Background |
| secondaryBackground | Light gray | Dark gray | Grouped content |
| systemBlue | #007AFF | #0A84FF | Links, actions |
| systemGreen | #34C759 | #30D158 | Success |
| systemRed | #FF3B30 | #FF453A | Errors, destructive |

---

## Layout

### Safe Areas
- Content must respect safe areas (notch, home indicator)
- Use `SafeAreaView` in React Native

```tsx
import { SafeAreaView } from 'react-native-safe-area-context';

<SafeAreaView style={{ flex: 1 }}>
  <YourContent />
</SafeAreaView>
```

### Spacing System
- Minimum touch target: **44x44 points**
- Standard margins: 16-20 points
- Common padding: 8, 12, 16, 20, 24 points

---

## SF Symbols

Apple's icon system with 6,000+ symbols.

### Usage in React Native
```bash
npm install react-native-sfsymbols
```

```tsx
import { SFSymbol } from 'react-native-sfsymbols';

<SFSymbol name="heart.fill" size={24} color="#FF3B30" />
```

### Common Symbols
| Symbol | Name |
|--------|------|
| ❤️ | heart.fill |
| ⚙️ | gearshape |
| 🏠 | house |
| 🔍 | magnifyingglass |
| ➕ | plus |
| ✓ | checkmark |
| ← | chevron.left |
| → | chevron.right |

---

## Platform Conventions

### Gestures
| Gesture | Action |
|---------|--------|
| Tap | Select, activate |
| Swipe left on row | Delete, actions |
| Pull down | Refresh content |
| Edge swipe | Navigate back |
| Long press | Context menu |

### Haptic Feedback
Use haptics for important interactions:
- Selection changes
- Toggle switches
- Success/error states
- Action confirmations

```tsx
import ReactNativeHapticFeedback from 'react-native-haptic-feedback';

ReactNativeHapticFeedback.trigger('impactLight');
```

---

## Dark Mode

- Support both light and dark appearance
- Use semantic colors (systemBackground, label)
- Test all screens in both modes
- Avoid pure black (#000000) - use #1C1C1E

---

## Resources
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- SF Symbols: https://developer.apple.com/sf-symbols/
- Design Resources: https://developer.apple.com/design/resources/
