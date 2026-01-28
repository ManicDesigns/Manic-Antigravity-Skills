# Apple App Store Review Guidelines

> **Source**: https://developer.apple.com/app-store/review/guidelines/

## Overview

The App Store uses expert review to ensure apps are safe, functional, and high-quality. Guidelines are organized into 5 sections: Safety, Performance, Business, Design, and Legal.

---

## 1. Safety

Apps must not contain offensive, harmful, or objectionable content.

### 1.1 Objectionable Content
- **1.1.1**: No defamatory, discriminatory, or mean-spirited content targeting groups
- **1.1.2**: No realistic violence, killing, torture, or abuse
- **1.1.3**: No promotion of weapons or dangerous objects
- **1.1.4**: No sexual/pornographic content, hookup apps
- **1.1.5**: No inflammatory religious content
- **1.1.6**: No false information or fake features
- **1.1.7**: No exploitation of current tragedies

### 1.2 User-Generated Content (UGC)
Apps with UGC **must include**:
- Method to filter objectionable content
- Mechanism to report offensive content
- Ability to block abusive users
- Published contact info for flagging concerns

### 1.3 Kids Category
- No behavioral advertising
- No data collection without parental consent
- Age-appropriate content only

---

## 2. Performance

Apps must be complete, stable, and honest in their presentation.

### 2.1 App Completeness
- Final version with all metadata
- Fully functional, tested on-device
- Include demo account if login required
- No placeholder content

### 2.2 Beta Testing
- Use **TestFlight** for betas, not App Store
- TestFlight apps still must follow guidelines

### 2.3 Accurate Metadata
- Description, screenshots, previews must reflect actual app
- No hidden or undocumented features
- No misleading marketing

### 2.4 Hardware Compatibility
- Apps should work on current OS versions
- Universal apps for iPad must have iPad-optimized UI

### 2.5 Software Requirements
- Use public APIs only
- Use appropriate frameworks (HealthKit, HomeKit, etc.)

---

## 3. Business

Clear monetization and no manipulation.

### 3.1 Payments
- **3.1.1 In-App Purchase Required**: For unlocking features, subscriptions, virtual items
- Cannot use own payment mechanisms for digital goods
- Credits/currencies cannot expire
- Must have restore mechanism

### 3.1.1 Exceptions
- Reader apps (Netflix, Spotify) - can link to external signup
- Physical goods and services - can use external payment
- Free apps with no IAP

### 3.1.2 Subscriptions
- Clear pricing before purchase
- Must provide value continuously
- Free trials must clearly state duration and cost after

### 3.2 Other Business Issues
- No manipulation of ratings/reviews
- No fake downloads or engagement

---

## 4. Design

Apps must provide genuine value and follow platform conventions.

### 4.1 Copycats
- Original ideas required
- No impersonation of other apps
- Cannot use another developer's branding without permission

### 4.2 Minimum Functionality
- More than a repackaged website
- Must provide lasting value or utility
- No primarily marketing/advertising apps

### 4.3 Spam
- No junk apps
- Don't flood categories with similar apps
- Avoid excessive ads

### 4.4 Extensions
- Must provide functionality beyond container app
- Safari extensions must have clear functionality

---

## 5. Legal

Apps must comply with all applicable laws.

### 5.1 Privacy
- **Privacy Policy required** (linked in App Store Connect)
- **App Tracking Transparency** for cross-site tracking (ATT)
- Data collection must be disclosed
- Minimize data retention

### 5.2 Intellectual Property
- Only submit apps you have rights to
- Don't infringe trademarks or copyrights

### 5.3 Gaming/Gambling
- Lotteries require government licensing
- Real-money gambling apps restricted to certain regions

### 5.4 VPN Apps
- Must use NEVPNManager API
- Cannot sell/share user data

---

## Common Rejection Reasons

| Reason | Fix |
|--------|-----|
| Crashes/bugs | Test thoroughly before submission |
| Incomplete metadata | Fill all App Store Connect fields |
| Broken links | Verify all URLs work |
| Placeholder content | Remove "lorem ipsum" and test data |
| Missing privacy policy | Add privacy policy URL |
| Login issue | Provide demo credentials in review notes |
| IAP not visible | Make IAP products discoverable to reviewer |

---

## Submission Checklist

- [ ] App tested on device (not just simulator)
- [ ] All features complete and functional
- [ ] Demo account info provided in review notes
- [ ] Privacy policy URL configured
- [ ] App description accurate and complete
- [ ] Screenshots reflect current app state
- [ ] Support URL functional
- [ ] Age rating questionnaire complete
- [ ] Required entitlements properly configured
