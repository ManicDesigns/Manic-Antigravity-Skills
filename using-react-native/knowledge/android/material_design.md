# Material Design 3 (Material You)

> **Source**: https://m3.material.io/

## Overview

Material Design 3 (M3) is Google's latest design system. Features dynamic color, improved accessibility, and modern component patterns.

---

## Core Principles

### 1. Personalization
- Dynamic color from user's wallpaper
- Adaptive icons and themes
- User preference respect

### 2. Accessibility
- Larger touch targets (48dp minimum)
- Improved contrast ratios
- Clear visual hierarchy

### 3. Expressiveness
- Rounded shapes
- Tonal color palettes
- Smooth animations

---

## Color System

### Tonal Palettes
M3 generates tones (0-100) from key colors:

| Tone | Usage |
|------|-------|
| 0 | Pure black |
| 10 | Darkest surfaces |
| 20 | Dark surfaces |
| 30 | Dark elevated surfaces |
| 40 | Primary container (dark) |
| 80 | Primary container (light) |
| 90 | Light surfaces |
| 100 | Pure white |

### Key Colors
```typescript
const colors = {
  // Primary - main brand color
  primary: '#6750A4',
  onPrimary: '#FFFFFF',
  primaryContainer: '#EADDFF',
  onPrimaryContainer: '#21005D',
  
  // Secondary - less prominent
  secondary: '#625B71',
  onSecondary: '#FFFFFF',
  secondaryContainer: '#E8DEF8',
  onSecondaryContainer: '#1D192B',
  
  // Tertiary - accent
  tertiary: '#7D5260',
  
  // Error
  error: '#B3261E',
  onError: '#FFFFFF',
  errorContainer: '#F9DEDC',
  
  // Surface (backgrounds)
  surface: '#FEF7FF',
  surfaceVariant: '#E7E0EC',
  onSurface: '#1D1B20',
  onSurfaceVariant: '#49454F',
  
  // Outline
  outline: '#79747E',
  outlineVariant: '#CAC4D0',
};
```

---

## Typography

### Type Scale
| Style | Size | Weight | Line Height |
|-------|------|--------|-------------|
| displayLarge | 57sp | 400 | 64sp |
| displayMedium | 45sp | 400 | 52sp |
| displaySmall | 36sp | 400 | 44sp |
| headlineLarge | 32sp | 400 | 40sp |
| headlineMedium | 28sp | 400 | 36sp |
| headlineSmall | 24sp | 400 | 32sp |
| titleLarge | 22sp | 400 | 28sp |
| titleMedium | 16sp | 500 | 24sp |
| titleSmall | 14sp | 500 | 20sp |
| bodyLarge | 16sp | 400 | 24sp |
| bodyMedium | 14sp | 400 | 20sp |
| bodySmall | 12sp | 400 | 16sp |
| labelLarge | 14sp | 500 | 20sp |
| labelMedium | 12sp | 500 | 16sp |
| labelSmall | 11sp | 500 | 16sp |

### React Native Implementation
```typescript
const typography = {
  displayLarge: { fontSize: 57, fontWeight: '400', lineHeight: 64 },
  headlineMedium: { fontSize: 28, fontWeight: '400', lineHeight: 36 },
  titleLarge: { fontSize: 22, fontWeight: '400', lineHeight: 28 },
  bodyLarge: { fontSize: 16, fontWeight: '400', lineHeight: 24 },
  labelLarge: { fontSize: 14, fontWeight: '500', lineHeight: 20 },
};
```

---

## Components

### Buttons

| Type | Usage |
|------|-------|
| Filled | Primary actions |
| Outlined | Secondary actions |
| Text | Low-emphasis actions |
| Elevated | Lift from surface |
| Tonal | Medium emphasis |
| FAB | Floating action button |

```tsx
// React Native Paper (M3)
import { Button, FAB } from 'react-native-paper';

<Button mode="contained" onPress={handlePress}>
  Primary Action
</Button>

<Button mode="outlined" onPress={handlePress}>
  Secondary
</Button>

<FAB icon="plus" onPress={handleAdd} />
```

### Cards
```tsx
import { Card } from 'react-native-paper';

<Card mode="elevated">
  <Card.Content>
    <Title>Card Title</Title>
    <Paragraph>Card content here</Paragraph>
  </Card.Content>
  <Card.Actions>
    <Button>Cancel</Button>
    <Button mode="contained">OK</Button>
  </Card.Actions>
</Card>
```

### Navigation
| Pattern | Usage |
|---------|-------|
| Navigation bar | Bottom nav (3-5 destinations) |
| Navigation drawer | Side menu |
| Navigation rail | Side nav for tablets |
| Tabs | Same-level content switching |

---

## Spacing & Layout

### Spacing Scale
```typescript
const spacing = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 48,
};
```

### Grid
- Margins: 16dp (phone), 24dp (tablet)
- Gutters: 16dp
- Columns: 4 (phone), 8 (tablet), 12 (desktop)

---

## Shapes

### Corner Radius
| Size | Radius | Usage |
|------|--------|-------|
| None | 0dp | Sharp edges |
| Extra Small | 4dp | Small elements |
| Small | 8dp | Chips, inputs |
| Medium | 12dp | Cards |
| Large | 16dp | Bottom sheets |
| Extra Large | 28dp | FAB |
| Full | 50% | Pills, circles |

```typescript
const shapes = {
  extraSmall: 4,
  small: 8,
  medium: 12,
  large: 16,
  extraLarge: 28,
};
```

---

## React Native Paper (M3)

### Installation
```bash
npm install react-native-paper
```

### Theme Setup
```typescript
import { MD3LightTheme, MD3DarkTheme, PaperProvider } from 'react-native-paper';

const theme = {
  ...MD3LightTheme,
  colors: {
    ...MD3LightTheme.colors,
    primary: '#6750A4',
    secondary: '#625B71',
  },
};

function App() {
  return (
    <PaperProvider theme={theme}>
      <YourApp />
    </PaperProvider>
  );
}
```

### Dynamic Colors (Android 12+)
```typescript
import { useMaterial3Theme } from '@pchmn/expo-material3-theme';

function App() {
  const { theme } = useMaterial3Theme();
  
  return (
    <PaperProvider theme={theme}>
      <YourApp />
    </PaperProvider>
  );
}
```

---

## Icons

Use Material Symbols (outlined, rounded, sharp):

```bash
npm install react-native-vector-icons
```

```tsx
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';

<MaterialIcons name="favorite" size={24} color="#6750A4" />
```

---

## Motion

### Duration
| Duration | Usage |
|----------|-------|
| 50ms | Micro feedback |
| 100ms | Small elements |
| 200ms | Medium elements |
| 300ms | Large elements |
| 500ms | Complex animations |

### Easing
```typescript
import { Easing } from 'react-native';

// Standard curve (most common)
const standardEasing = Easing.bezier(0.2, 0.0, 0, 1.0);

// Decelerate (entering)
const decelerateEasing = Easing.bezier(0, 0, 0, 1);

// Accelerate (exiting)
const accelerateEasing = Easing.bezier(0.3, 0, 0.8, 0.15);
```

---

## Resources
- Material Design 3: https://m3.material.io
- React Native Paper: https://callstack.github.io/react-native-paper/
- Material Theme Builder: https://m3.material.io/theme-builder
