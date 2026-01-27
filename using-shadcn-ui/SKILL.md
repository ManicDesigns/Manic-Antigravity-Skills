---
name: using-shadcn-ui
description: shadcn/ui accessible React components built on Radix UI. Use for forms, dialogs, tables, navigation, and production UI.
---

# Using shadcn/ui

shadcn/ui is a collection of beautifully-designed, accessible components built on Radix UI primitives with Tailwind CSS styling.

## When to Use This Skill
- User needs accessible, production-ready form components
- User asks for "shadcn", "radix", or "accessible UI"
- User needs data tables, dialogs, or complex form inputs
- Building admin dashboards or SaaS applications

## Installation

### Quick Setup
```bash
npx shadcn@latest init
```

### Add Components
```bash
npx shadcn@latest add button
npx shadcn@latest add dialog
npx shadcn@latest add form
```

---

## Components (60+)

### Form Controls
| Component | Description |
|-----------|-------------|
| Button | Primary action buttons with variants |
| Button Group | Grouped button actions |
| Checkbox | Checkbox input with label |
| Input | Text input field |
| Input Group | Input with addons |
| Input OTP | One-time password input |
| Label | Form field labels |
| Native Select | Native HTML select |
| Radio Group | Radio button group |
| Select | Custom select dropdown |
| Slider | Range slider input |
| Switch | Toggle switch |
| Textarea | Multi-line text input |

### Feedback & Display
| Component | Description |
|-----------|-------------|
| Alert | Status alert messages |
| Alert Dialog | Confirmation dialogs |
| Badge | Status badges |
| Progress | Progress indicator |
| Skeleton | Loading placeholder |
| Sonner | Toast notifications |
| Spinner | Loading spinner |
| Toast | Notification toasts |
| Tooltip | Hover tooltips |

### Navigation
| Component | Description |
|-----------|-------------|
| Breadcrumb | Page breadcrumbs |
| Command | Command palette (⌘K) |
| Context Menu | Right-click menu |
| Dropdown Menu | Action dropdown |
| Menubar | Application menubar |
| Navigation Menu | Site navigation |
| Pagination | Page navigation |
| Sidebar | Application sidebar |
| Tabs | Tab navigation |

### Layout & Content
| Component | Description |
|-----------|-------------|
| Accordion | Expandable sections |
| Aspect Ratio | Fixed aspect ratio container |
| Avatar | User avatars |
| Calendar | Date picker calendar |
| Card | Content cards |
| Carousel | Content carousel |
| Chart | Data visualization |
| Collapsible | Collapsible section |
| Data Table | Full-featured data table |
| Date Picker | Date selection |
| Dialog | Modal dialogs |
| Drawer | Side drawer panel |
| Empty | Empty state display |
| Hover Card | Hover popup cards |
| Popover | Popup content |
| Resizable | Resizable panels |
| Scroll Area | Custom scrollbars |
| Separator | Visual separator |
| Sheet | Slide-out panel |
| Table | Data tables |
| Toggle | Toggle button |
| Toggle Group | Toggle button group |
| Typography | Text styles |

---

## Usage Examples

### Form with Validation
```tsx
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export function LoginForm() {
  return (
    <form className="space-y-4">
      <div>
        <Label htmlFor="email">Email</Label>
        <Input id="email" type="email" placeholder="you@example.com" />
      </div>
      <div>
        <Label htmlFor="password">Password</Label>
        <Input id="password" type="password" />
      </div>
      <Button type="submit" className="w-full">Sign In</Button>
    </form>
  )
}
```

### Dialog Modal
```tsx
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"

<Dialog>
  <DialogTrigger asChild>
    <Button>Open Dialog</Button>
  </DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Confirm Action</DialogTitle>
    </DialogHeader>
    <p>Are you sure you want to proceed?</p>
  </DialogContent>
</Dialog>
```

### Data Table
```tsx
import { DataTable } from "@/components/ui/data-table"

const columns = [
  { accessorKey: "name", header: "Name" },
  { accessorKey: "email", header: "Email" },
  { accessorKey: "status", header: "Status" },
]

<DataTable columns={columns} data={users} />
```

---

## Theming

### CSS Variables (globals.css)
```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --muted: 210 40% 96.1%;
    --accent: 210 40% 96.1%;
    --destructive: 0 84.2% 60.2%;
    --border: 214.3 31.8% 91.4%;
    --radius: 0.5rem;
  }
  
  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
  }
}
```

---

## Resources
- Documentation: https://ui.shadcn.com/docs
- Components: https://ui.shadcn.com/docs/components
- Themes: https://ui.shadcn.com/themes
- Registry: https://ui.shadcn.com/docs/directory
