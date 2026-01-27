# Gluestack UI Overview

## Introduction

### gluestack-ui philosophy

#### Why gluestack-ui exists

- Problem:Traditional UI libraries often force developers into rigid patterns, heavy dependencies, or platform-specific implementations.
- Solution:gluestack-ui promotes a universal, modular, and copy-paste approach that lets developers own their UI components completely.
- Inspiration:We started gluestack-ui v1 with a philosophy similar to React Aria & Radix UI, to keep the customization decoupled from component API and accessibility. By the time we announced v2, shadcn/ui had already taken over the web and today gluestack-ui and shadcn/ui are very similar, although gluestack-ui exists in the mobile and web world both!

#### Goals & Non-Goals

##### Our goals

- Universal Consistency:One codebase, same behavior across React, Next.js, and React Native.
- Developer Ownership:Copy-paste components, modify freely, avoid vendor lock-in.
- Performance & Accessibility:Lightweight, optimized, and accessible components by default.
- Community-Driven:Open architecture encouraging contributions and experimentation.

##### Non-goals

- Create another monolithic UI library with hundreds of pre-styled components
- Provide opinionated design themes that limit creative freedom
- Replace platform-specific optimizations with lowest-common-denominator solutions
- Build a proprietary styling system that requires learning new APIs
- Create dependencies that become bottlenecks for your project's evolution

#### How gluestack-ui works

- Source-to-Destination Architecture:Maintain a single source of truth for components that automatically syncs across projects.
- Copy-Paste Components:Grab only what you need—no heavy dependencies required.
- Theming & Tailwind Integration:Flexible styling system that works for web & mobile.
- TypeScript & RSC Ready:Modern architecture for type safety and server-rendered apps.

#### Design 101

- Atomic, Composable Components:Each component is small, reusable, and composable into more complex UIs.
- Compound Components:Components with sub-components (e.g.,<Button><ButtonText>Click Me</ButtonText></Button>), allowing more flexible layouts.
- Accessibility by Default:ARIA support baked in, keyboard navigable.
- Minimal Runtime Overhead:Lightweight runtime ensures high performance.

#### Code 101

- Copy-Paste Philosophy:No “magical imports.” You copy the component directly into your codebase.
- Fully Customizable:You can override styles, props, and behavior easily.
- Single Source of Truth:All component logic lives in src/ for maintainability and easy updates.
- Integration Ready:Works out-of-the-box with Tailwind, NativeWind, and Next.js RSC.

### Future Considerations

### Community

#### Discord

#### Twitter

#### GitHub

#### Stackoverflow

#### LinkedIn

### All Components

### Contributing

- Component Development: Help build new components or improve existing ones
- Documentation: Improve guides, examples, and API documentation
- Bug Reports: Help us identify and fix issues
- Feature Requests: Suggest new features and improvements