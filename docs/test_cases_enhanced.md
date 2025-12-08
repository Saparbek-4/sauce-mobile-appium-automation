# Test Cases — Sauce Labs Mobile App (Android)

**Project:** Appium Mobile Automation Framework  
**Author:** Saparbek (SDET — Mobile UI Automation + Python + Appium)  
**App Under Test:** Sauce Labs Demo Mobile App  
**Last Updated:** December 2025

---

## Test Environment

| Parameter | Value |
|-----------|-------|
| **Platform** | Android |
| **OS Versions** | Android 10, 11, 12, 13 |
| **Devices** | Pixel 5 (Emulator), Samsung Galaxy S21 (Real) |
| **App Version** | 1.3.0 |
| **Appium Version** | 2.x |
| **Language** | English (EN) |

---

## Test Data

### User Credentials

| Username | Password | Status | Purpose |
|----------|----------|--------|---------|
| standard_user | secret_sauce | Active | Valid login, full access |
| locked_out_user | secret_sauce | Locked | Negative testing |
| problem_user | secret_sauce | Active | Visual regression testing |
| performance_glitch_user | secret_sauce | Active | Performance testing |

### Test Products

| Product Name | Price | Category |
|--------------|-------|----------|
| Sauce Labs Backpack | $29.99 | Backpack |
| Sauce Labs Bike Light | $9.99 | Light |
| Sauce Labs Bolt T-Shirt | $15.99 | Clothing |
| Sauce Labs Fleece Jacket | $49.99 | Clothing |
| Sauce Labs Onesie | $7.99 | Clothing |

---

## Test Execution Summary

| Module | Total Cases | To Automate | Priority P0 | Status |
|--------|-------------|-------------|-------------|--------|
| Login | 6 | 5 | 3 | ✅ Ready |
| Menu | 4 | 3 | 2 | ✅ Ready |
| Products | 10 | 8 | 4 | ✅ Ready |
| Product Details | 3 | 3 | 2 | ✅ Ready |
| Cart | 4 | 4 | 3 | ✅ Ready |
| Checkout | 5 | 4 | 3 | ✅ Ready |
| WebView | 2 | 1 | 0 | 📝 Optional |
| QR Scanner | 2 | 0 | 0 | 📝 Optional |
| Geolocation | 2 | 0 | 0 | 📝 Optional |
| Drawing | 1 | 0 | 0 | 📝 Optional |
| Edge Cases | 5 | 3 | 1 | ✅ Ready |

---

## 1. LOGIN SCREEN

### TC-LG-001 — Successful Login with Standard User

**Priority:** P0 (Critical)  
**Type:** Smoke, Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~10 seconds

**Preconditions:**
- App is installed and launched
- No user is currently logged in
- Network connection is available
- Login screen is displayed

**Test Data:**
- Username: `standard_user`
- Password: `secret_sauce`

**Steps:**
1. Launch the Sauce Labs app
2. Verify Login screen is displayed
3. Tap on the username input field
4. Select "standard_user" from the dropdown/auto-complete list
5. Tap on the password input field
6. Enter password: "secret_sauce"
7. Tap the "LOGIN" button

**Expected Result:**
- Form submission fails
- Red error message appears near First Name field
- Error text: "First Name is required"
- Error icon (⚠️) may be visible
- User remains on Checkout Information screen
- Last Name and Zip Code fields remain populated
- "CONTINUE" button remains enabled
- No navigation occurs

**Postconditions:**
- User must fill all required fields to proceed

---

### TC-CH-003 — Checkout with Empty Zip Code

**Priority:** P1 (High)  
**Type:** Negative, Validation  
**Automation:** ✅ Yes  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is on Checkout Information screen

**Test Data:**
- First Name: `John`
- Last Name: `Doe`
- Zip Code: (empty)

**Steps:**
1. Enter First Name: "John"
2. Enter Last Name: "Doe"
3. Leave Zip Code field empty
4. Tap "CONTINUE"

**Expected Result:**
- Form submission fails
- Error message: "Postal Code is required"
- Error appears near Zip Code field
- User remains on same screen
- First Name and Last Name fields remain populated
- No navigation to Overview screen

**Postconditions:**
- Validation enforced
- User must provide Zip Code

---

### TC-CH-004 — Cancel Checkout Process

**Priority:** P2 (Medium)  
**Type:** Functional, Navigation  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Checkout Information screen
- Cart contains items

**Steps:**
1. Tap "CANCEL" button
2. Verify navigation

**Expected Result:**
- User navigates back to Cart screen
- Cart items remain intact (not cleared)
- Cart badge shows correct item count
- No data loss
- Form data is not saved
- User can restart checkout if desired

**Postconditions:**
- Checkout is cancelled
- Cart remains active

---

### TC-CH-005 — Verify Order Summary Totals

**Priority:** P1 (High)  
**Type:** Functional, Data Validation  
**Automation:** ✅ Yes  
**Execution Time:** ~15 seconds

**Preconditions:**
- User has added 2 items to cart:
  - Sauce Labs Backpack ($29.99)
  - Sauce Labs Bike Light ($9.99)
- User is on Checkout Overview screen

**Steps:**
1. Navigate to Checkout Overview
2. Verify price calculations
3. Verify all items listed

**Expected Result:**
- Both items displayed in overview:
  - Sauce Labs Backpack - QTY: 1 - $29.99
  - Sauce Labs Bike Light - QTY: 1 - $9.99
- Item total: $39.98
- Tax calculated correctly (e.g., 8% = $3.20)
- Total = Item Total + Tax ($43.18)
- All prices formatted as $XX.XX
- Payment Information section visible
- Shipping Information section visible
- No calculation errors

**Postconditions:**
- Accurate pricing displayed
- User can proceed to complete order

---

## 7. WEBVIEW SCREEN

### TC-WV-001 — Open WebView Page

**Priority:** P2 (Medium)  
**Type:** Functional  
**Automation:** ⚠️ Optional  
**Execution Time:** ~12 seconds

**Preconditions:**
- User is logged in
- Network connection available

**Steps:**
1. Open menu
2. Tap "WebView"
3. Wait for page to load

**Expected Result:**
- WebView screen opens
- External website loads (e.g., saucelabs.com)
- Page content visible within app
- Loading indicator shown while loading
- Page loads within 5 seconds
- No app crashes
- Scroll functionality works
- Links within webview are clickable

**Postconditions:**
- User can navigate within webview

---

### TC-WV-002 — Navigate Back from WebView

**Priority:** P2 (Medium)  
**Type:** Navigation  
**Automation:** ⚠️ Optional  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on WebView screen
- Page has loaded

**Steps:**
1. Tap back button or use Android back gesture
2. Verify navigation

**Expected Result:**
- User returns to Products screen
- WebView closes completely
- App state preserved
- No memory leaks
- Smooth transition

**Postconditions:**
- WebView session ended

---

## 8. QR CODE SCANNER

### TC-QR-001 — Open QR Code Scanner

**Priority:** P3 (Low)  
**Type:** Functional  
**Automation:** ❌ No (requires camera)  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is logged in
- Device has camera
- Camera permission not yet granted (first time)

**Steps:**
1. Open menu
2. Tap "QR Code Scanner"
3. Handle permission dialog

**Expected Result:**
- Camera permission dialog appears
- Dialog text: "Allow app to access camera?"
- Options: "Allow" / "Deny"
- If allowed:
  - Camera view opens
  - Scanner overlay visible
  - Instructions displayed
- If denied:
  - Error message or return to previous screen

**Postconditions:**
- Permission status saved

---

### TC-QR-002 — QR Code Scanner Permission Already Granted

**Priority:** P3 (Low)  
**Type:** Functional  
**Automation:** ❌ No  
**Execution Time:** ~5 seconds

**Preconditions:**
- Camera permission already granted

**Steps:**
1. Open menu
2. Tap "QR Code Scanner"

**Expected Result:**
- Camera opens immediately
- No permission dialog
- Scanner ready to use
- Smooth transition

---

## 9. GEOLOCATION

### TC-GEO-001 — Open Geolocation Page

**Priority:** P3 (Low)  
**Type:** Functional  
**Automation:** ❌ No (requires GPS)  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is logged in
- Location permission not granted

**Steps:**
1. Open menu
2. Tap "Geo Location"
3. Handle permission

**Expected Result:**
- Location permission dialog appears
- Dialog text: "Allow app to access location?"
- Options: "Allow" / "Deny"
- If allowed:
  - Geolocation screen displays
  - Coordinates shown (latitude/longitude)
  - Map may be displayed (if applicable)
- If denied:
  - Error message shown

**Postconditions:**
- Permission saved

---

### TC-GEO-002 — Geolocation with Permission Granted

**Priority:** P3 (Low)  
**Type:** Functional  
**Automation:** ❌ No  
**Execution Time:** ~8 seconds

**Preconditions:**
- Location permission already granted

**Steps:**
1. Open menu
2. Tap "Geo Location"

**Expected Result:**
- Geolocation screen opens
- Current coordinates displayed
- Location accuracy shown
- No permission prompt
- Data loads within 3 seconds

---

## 10. DRAWING SCREEN

### TC-DR-001 — Draw on Canvas

**Priority:** P3 (Low)  
**Type:** Functional, UI  
**Automation:** ⚠️ Partial (can automate gestures, visual validation manual)  
**Execution Time:** ~15 seconds

**Preconditions:**
- User is logged in

**Steps:**
1. Open menu
2. Tap "Drawing"
3. Wait for canvas to load
4. Perform swipe/drag gestures on canvas
5. Draw multiple lines/shapes

**Expected Result:**
- Drawing screen opens
- Blank canvas visible
- Canvas is responsive to touch
- Lines appear as user draws
- Lines are smooth (not pixelated)
- Multiple lines can be drawn
- Colors/thickness options may be available
- Clear/Reset button may be present
- No lag during drawing
- Drawing persists until cleared

**Postconditions:**
- Drawing can be cleared
- User can navigate away

---

## 11. EDGE CASES & NON-FUNCTIONAL TESTS

### TC-EG-001 — App Relaunch Preserves Login Session

**Priority:** P1 (High)  
**Type:** Session Management  
**Automation:** ✅ Yes  
**Execution Time:** ~20 seconds

**Preconditions:**
- User is logged in as `standard_user`
- User is on Products screen

**Steps:**
1. Verify user is logged in
2. Close app completely (force stop or kill app)
3. Wait 5 seconds
4. Relaunch app
5. Verify app state

**Expected Result:**
- App reopens to Products screen (or last screen)
- User remains logged in (no login screen)
- Session persists
- Cart items preserved (if any)
- No data loss
- App loads within 3 seconds
- No authentication required

**Postconditions:**
- Session continues
- User can interact normally

---

### TC-EG-002 — Login Without Network Connection

**Priority:** P2 (Medium)  
**Type:** Negative, Network  
**Automation:** ⚠️ Partial (requires network control)  
**Execution Time:** ~10 seconds

**Preconditions:**
- App is launched
- Network connection is disabled (Airplane mode ON or WiFi/Data OFF)

**Test Data:**
- Username: `standard_user`
- Password: `secret_sauce`

**Steps:**
1. Disable network connection
2. Enter valid credentials
3. Tap "LOGIN"

**Expected Result:**
- Login attempt fails
- Error message appears:
  - "Network connection unavailable"
  - "Please check your internet connection"
  - Or similar network error
- User remains on Login screen
- No crash occurs
- Error is user-friendly

**Postconditions:**
- User can retry after restoring connection

---

### TC-EG-003 — Device Rotation Handling

**Priority:** P2 (Medium)  
**Type:** UI, Responsiveness  
**Automation:** ✅ Yes  
**Execution Time:** ~15 seconds

**Preconditions:**
- User is logged in
- User is on Products screen
- Auto-rotate is enabled

**Steps:**
1. Hold device in portrait mode
2. Verify layout
3. Rotate device to landscape mode
4. Verify layout adjusts
5. Rotate back to portrait
6. Verify layout restores

**Expected Result:**
- Portrait mode:
  - Layout is correct
  - All elements visible
  - Content readable
- Landscape mode:
  - Layout adjusts smoothly
  - No elements cut off
  - Content remains readable
  - Product grid may show more columns
  - No layout breaks
- Rotation between modes:
  - Transition is smooth (< 1 second)
  - No flickering
  - Data persists (cart items, scroll position)
  - No crashes
  - App remains responsive
- Both orientations are fully functional

**Postconditions:**
- App works in both orientations
- No data loss during rotation

---

### TC-EG-004 — Heavy Scrolling Performance

**Priority:** P2 (Medium)  
**Type:** Performance, Stress  
**Automation:** ✅ Yes  
**Execution Time:** ~20 seconds

**Preconditions:**
- User is on Products screen
- All products loaded

**Steps:**
1. Perform fast scroll down to bottom
2. Perform fast scroll up to top
3. Repeat 10 times rapidly
4. Monitor app behavior

**Expected Result:**
- Smooth scrolling throughout
- No lag or frame drops
- Images remain loaded
- No visual glitches
- Product cards remain intact
- Scroll performance consistent
- No memory warnings
- App does not crash
- UI remains responsive
- Scrolling FPS ≥ 30fps

**Postconditions:**
- App remains stable
- Memory usage normal

---

### TC-EG-005 — Stress Test: Add and Remove Item Multiple Times

**Priority:** P2 (Medium)  
**Type:** Stress, Performance  
**Automation:** ✅ Yes  
**Execution Time:** ~30 seconds

**Preconditions:**
- User is on Products screen
- Cart is empty

**Test Data:**
- Product: "Sauce Labs Bike Light"

**Steps:**
1. Tap "ADD TO CART" for Bike Light
2. Verify cart badge = 1
3. Tap "REMOVE"
4. Verify cart badge = 0
5. Repeat steps 1-4 for 20 iterations
6. Monitor app stability

**Expected Result:**
- All 20 iterations complete successfully
- Cart badge updates correctly every time:
  - Increments to 1 on ADD
  - Decrements to 0 on REMOVE
- Button state toggles correctly:
  - "ADD TO CART" ↔ "REMOVE"
  - Blue ↔ Red color
- No lag or delays
- Response time consistent (< 500ms per action)
- No memory leaks
- No UI freezing
- No crashes
- App remains responsive throughout

**Postconditions:**
- App is stable
- Cart state is consistent (empty after final REMOVE)

---

## 12. AUTOMATION PRIORITY MATRIX

### Must Automate (P0 - Critical) — 15 Test Cases

| Test ID | Test Name | Reason |
|---------|-----------|--------|
| TC-LG-001 | Successful Login | Core functionality, smoke test |
| TC-LG-002 | Locked Out User | Security validation |
| TC-MN-002 | Logout | Session management critical |
| TC-PL-001 | Load Products | Core screen, smoke test |
| TC-PL-002 | Add to Cart | Primary user action |
| TC-PL-003 | Add Multiple Items | Common user flow |
| TC-CT-001 | View Cart | Cart verification essential |
| TC-CT-002 | Remove from Cart | Core cart functionality |
| TC-CH-001 | Complete Checkout | End-to-end critical path |

### Should Automate (P1 - High) — 18 Test Cases

| Test ID | Test Name | Reason |
|---------|-----------|--------|
| TC-LG-003 | Invalid Password | Security testing |
| TC-MN-001 | Open/Close Menu | Navigation testing |
| TC-MN-003 | Reset App State | State management |
| TC-PL-004 | Remove Product | Cart management |
| TC-PL-005 | Sort A-Z | Feature validation |
| TC-PL-006 | Sort Price Low-High | Feature validation |
| TC-PD-001 | Open Product Details | Navigation flow |
| TC-PD-002 | Add from Details | Alternative add flow |
| TC-PD-003 | Back Navigation | Navigation testing |
| TC-CT-003 | Continue Shopping | Navigation flow |
| TC-CH-002 | Empty First Name | Form validation |
| TC-CH-003 | Empty Zip Code | Form validation |
| TC-CH-005 | Verify Totals | Data accuracy |
| TC-EG-001 | Session Persistence | State management |

### Optional Automation (P2-P3 - Medium/Low) — 12 Test Cases

| Test ID | Test Name | Reason |
|---------|-----------|--------|
| TC-LG-004 | Empty Credentials | Basic validation |
| TC-LG-005 | Problem User | Visual regression |
| TC-PL-007-010 | Additional Sorting/Validation | Nice to have |
| TC-MN-004 | About Page | Non-critical feature |
| TC-CH-004 | Cancel Checkout | Edge case |
| TC-EG-002-005 | Edge Cases | Stability testing |

### Manual Only — 8 Test Cases

| Test ID | Test Name | Reason |
|---------|-----------|--------|
| TC-WV-001-002 | WebView | Visual validation needed |
| TC-QR-001-002 | QR Scanner | Requires physical QR code |
| TC-GEO-001-002 | Geolocation | Requires GPS simulation |
| TC-DR-001 | Drawing | Visual validation |

---

## 13. TEST EXECUTION GUIDELINES

### Smoke Test Suite (Runtime: ~3 minutes)
Run before every build/deployment:
- TC-LG-001 (Login)
- TC-PL-001 (Load Products)
- TC-PL-002 (Add to Cart)
- TC-CT-001 (View Cart)
- TC-CH-001 (Checkout E2E)
- TC-MN-002 (Logout)

### Regression Test Suite (Runtime: ~25 minutes)
Run daily or before releases:
- All P0 tests (15 cases)
- All P1 tests (18 cases)
- Selected P2 tests (5 cases)

### Full Test Suite (Runtime: ~45 minutes)
Run weekly or before major releases:
- All automated tests (40+ cases)

---

## 14. DEFECT SEVERITY DEFINITIONS

| Severity | Definition | Example |
|----------|------------|---------|
| **Critical** | App crash, data loss, security breach | Login fails for all users |
| **High** | Major feature broken, blocks workflow | Cannot add items to cart |
| **Medium** | Feature partially broken, workaround exists | Sort not working |
| **Low** | Minor UI issue, cosmetic | Text alignment off |

---

## 15. NOTES FOR AUTOMATION

### Locator Strategy Recommendations
- **Prefer:** Accessibility ID > Resource ID > XPath
- **Avoid:** Complex XPath chains
- **Use:** Explicit waits (not implicit)

### Test Data Management
- Store credentials in `test_data/users.json`
- Use data-driven approach for products
- Parameterize test inputs

### Reporting Requirements
- Screenshot on failure
- Video recording for E2E tests
- Allure report generation
- Log all API/network calls (if applicable)

### CI/CD Integration
- Run smoke tests on every commit
- Run regression nightly
- Parallel execution on multiple devices
- Fail build on P0 test failures

---

## DOCUMENT VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Dec 2025 | Saparbek | Initial comprehensive test case documentation |

---

**END OF DOCUMENT**

Total Test Cases: **50**  
Automation Candidates: **42** (84%)  
Manual Only: **8** (16%)  
Estimated Automation Effort: **80-100 hours** Login is successful without errors
- User is redirected to Products screen
- Products screen displays title "PRODUCTS"
- At least 6 product items are visible
- Menu icon (hamburger ☰) is visible in top-left corner
- Cart icon is visible in top-right corner
- Cart badge displays "0" or is not visible
- No error messages are displayed

**Postconditions:**
- User remains logged in
- Session persists after app restart

---

### TC-LG-002 — Login with Locked Out User

**Priority:** P1 (High)  
**Type:** Negative, Security  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- App is launched on Login screen

**Test Data:**
- Username: `locked_out_user`
- Password: `secret_sauce`

**Steps:**
1. Tap on username field
2. Select "locked_out_user" from the list
3. Tap on password field
4. Enter password: "secret_sauce"
5. Tap "LOGIN" button

**Expected Result:**
- Login attempt fails
- Red error banner appears below the login button
- Error message displays: "Sorry, this user has been locked out."
- Error icon (⚠️) is visible
- User remains on Login screen
- Username and password fields remain populated
- LOGIN button remains enabled

**Postconditions:**
- User is not authenticated
- No session is created

---

### TC-LG-003 — Login with Invalid Password

**Priority:** P1 (High)  
**Type:** Negative, Security  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- App is launched on Login screen

**Test Data:**
- Username: `standard_user`
- Password: `invalid_password_123`

**Steps:**
1. Tap on username field
2. Select "standard_user"
3. Tap on password field
4. Enter invalid password: "invalid_password_123"
5. Tap "LOGIN" button

**Expected Result:**
- Login attempt fails
- Red error banner appears
- Error message displays: "Username and password do not match any user in this service"
- User remains on Login screen
- Password field is cleared (security best practice)
- Username field remains populated

**Postconditions:**
- No authentication occurs
- Login screen remains active

---

### TC-LG-004 — Login with Empty Credentials

**Priority:** P2 (Medium)  
**Type:** Negative, Validation  
**Automation:** ✅ Yes  
**Execution Time:** ~5 seconds

**Preconditions:**
- App is launched on Login screen

**Steps:**
1. Leave username field empty
2. Leave password field empty
3. Tap "LOGIN" button

**Expected Result:**
- Login attempt fails
- Red error banner appears
- Error message displays: "Username is required"
- Both fields remain empty
- LOGIN button remains enabled
- No navigation occurs

**Postconditions:**
- User remains on Login screen

---

### TC-LG-005 — Login with Problem User (Visual Regression)

**Priority:** P2 (Medium)  
**Type:** Visual Regression  
**Automation:** ✅ Yes (with screenshot comparison)  
**Execution Time:** ~12 seconds

**Preconditions:**
- App is launched

**Test Data:**
- Username: `problem_user`
- Password: `secret_sauce`

**Steps:**
1. Log in as `problem_user`
2. Navigate to Products screen
3. Capture screenshots of product images
4. Compare with baseline (standard_user images)

**Expected Result:**
- Login is successful
- Products screen loads
- Some product images display incorrectly (broken/wrong images)
- Image issues are documented for visual regression testing
- App functionality remains intact despite visual bugs

**Postconditions:**
- Visual defects are logged
- Screenshots saved for comparison

---

### TC-LG-006 — Empty Username with Valid Password

**Priority:** P2 (Medium)  
**Type:** Negative, Validation  
**Automation:** ✅ Yes  
**Execution Time:** ~6 seconds

**Preconditions:**
- App is on Login screen

**Test Data:**
- Username: (empty)
- Password: `secret_sauce`

**Steps:**
1. Leave username field empty
2. Enter valid password: "secret_sauce"
3. Tap "LOGIN" button

**Expected Result:**
- Login fails
- Error message: "Username is required"
- Password field remains populated
- No authentication occurs

---

## 2. MENU (SIDE DRAWER)

**Menu Items:**
- All Items
- WebView
- QR Code Scanner
- Geo Location
- Drawing
- About
- Logout
- Reset App State

---

### TC-MN-001 — Open and Close Menu

**Priority:** P1 (High)  
**Type:** Functional, UI  
**Automation:** ✅ Yes  
**Execution Time:** ~5 seconds

**Preconditions:**
- User is logged in
- User is on Products screen

**Steps:**
1. Tap hamburger menu icon (☰) in top-left corner
2. Verify menu drawer opens from left side
3. Verify all menu items are visible
4. Tap "X" close button

**Expected Result:**
- Menu drawer slides in from left with animation
- Menu overlay covers part of the screen
- All 8 menu items are displayed vertically:
  - All Items
  - WebView
  - QR Code Scanner
  - Geo Location
  - Drawing
  - About
  - Logout
  - Reset App State
- Close button (X) is visible in top-right of menu
- Tapping X closes the menu smoothly
- Menu slides out to the left
- User returns to Products screen

**Postconditions:**
- Menu is closed
- Products screen remains in same state

---

### TC-MN-002 — Logout Functionality

**Priority:** P0 (Critical)  
**Type:** Functional, Security  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is logged in as `standard_user`
- User is on any screen within the app

**Steps:**
1. Open hamburger menu
2. Scroll to "Logout" option (if needed)
3. Tap "Logout"
4. Verify navigation to Login screen

**Expected Result:**
- User is logged out successfully
- App navigates to Login screen
- Session is terminated
- All user data is cleared from memory
- Cart items are cleared (if any)
- Login fields are empty
- No error messages appear

**Postconditions:**
- User must re-authenticate to access app
- Previous session data is not accessible

---

### TC-MN-003 — Reset App State

**Priority:** P1 (High)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~15 seconds

**Preconditions:**
- User is logged in
- At least 2 items are added to cart

**Steps:**
1. Add "Sauce Labs Backpack" to cart
2. Add "Sauce Labs Bike Light" to cart
3. Verify cart badge shows "2"
4. Open menu
5. Tap "Reset App State"
6. Close menu
7. Check cart badge

**Expected Result:**
- Cart badge resets from "2" to "0"
- Cart badge disappears or shows "0"
- All items are removed from cart
- "ADD TO CART" buttons are restored for all products
- No "REMOVE" buttons are visible
- User remains logged in
- User remains on current screen
- No error messages appear

**Postconditions:**
- App state is reset
- Cart is empty
- User session persists

---

### TC-MN-004 — Navigate to About Page

**Priority:** P2 (Medium)  
**Type:** Functional  
**Automation:** ⚠️ Optional  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is logged in
- Network connection available

**Steps:**
1. Open menu
2. Tap "About"
3. Wait for page to load

**Expected Result:**
- WebView opens within the app
- External URL loads (e.g., saucelabs.com)
- Page content is visible
- Back button is available
- Page loads within 5 seconds
- No app crashes occur

**Postconditions:**
- User can navigate back to app

---

## 3. PRODUCTS LIST SCREEN

### TC-PL-001 — Load Products Screen Successfully

**Priority:** P0 (Critical)  
**Type:** Smoke, Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is logged in as `standard_user`
- Network connection available

**Steps:**
1. Complete login
2. Wait for Products screen to load
3. Verify all UI elements

**Expected Result:**
- Products screen loads within 3 seconds
- Screen title displays "PRODUCTS"
- Exactly 6 product cards are visible:
  1. Sauce Labs Backpack
  2. Sauce Labs Bike Light
  3. Sauce Labs Bolt T-Shirt
  4. Sauce Labs Fleece Jacket
  5. Sauce Labs Onesie
  6. Test.allTheThings() T-Shirt (Red)
- Each product card displays:
  - Product image
  - Product name
  - Product description (1 line)
  - Price (format: $XX.XX)
  - "ADD TO CART" button (blue)
- Sort dropdown button is visible (top-right)
- Filter icon is visible (if available)
- Menu icon (hamburger) is visible (top-left)
- Cart icon is visible (top-right)
- Screen is scrollable

**Postconditions:**
- Products remain loaded
- User can interact with products

---

### TC-PL-002 — Add Single Product to Cart

**Priority:** P0 (Critical)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Products screen
- Cart is empty (badge shows "0" or not visible)

**Test Data:**
- Product: "Sauce Labs Bike Light"

**Steps:**
1. Locate "Sauce Labs Bike Light" product card
2. Verify "ADD TO CART" button is visible and enabled
3. Tap "ADD TO CART" button for Bike Light
4. Wait for UI update

**Expected Result:**
- Button text changes from "ADD TO CART" to "REMOVE"
- Button color changes from blue to red
- Button remains in the same position
- Cart badge in top-right corner:
  - Appears if it was hidden
  - Updates from "0" to "1"
  - Badge is visible and readable
- Product card remains in same position
- Other products remain unchanged
- No error messages appear
- Action completes in < 1 second

**Postconditions:**
- Cart contains 1 item
- Item persists in cart until removed or checkout

---

### TC-PL-003 — Add Multiple Products to Cart

**Priority:** P0 (Critical)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~12 seconds

**Preconditions:**
- User is on Products screen
- Cart is empty

**Test Data:**
- Product 1: "Sauce Labs Backpack"
- Product 2: "Sauce Labs Bike Light"

**Steps:**
1. Tap "ADD TO CART" for "Sauce Labs Backpack"
2. Verify cart badge shows "1"
3. Tap "ADD TO CART" for "Sauce Labs Bike Light"
4. Verify cart badge shows "2"

**Expected Result:**
- First addition:
  - Backpack button changes to "REMOVE" (red)
  - Cart badge shows "1"
- Second addition:
  - Bike Light button changes to "REMOVE" (red)
  - Cart badge increments to "2"
- Both "REMOVE" buttons remain red
- Cart badge is clearly visible
- No items are duplicated in cart
- Other products remain unchanged

**Postconditions:**
- Cart contains 2 unique items
- Badge accurately reflects cart count

---

### TC-PL-004 — Remove Product from Products Screen

**Priority:** P1 (High)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is on Products screen
- "Sauce Labs Bike Light" is already in cart
- Cart badge shows "1"
- Button shows "REMOVE"

**Steps:**
1. Verify "REMOVE" button is visible (red) for Bike Light
2. Tap "REMOVE" button
3. Wait for UI update

**Expected Result:**
- Button text changes from "REMOVE" to "ADD TO CART"
- Button color changes from red to blue
- Cart badge decreases from "1" to "0"
- Cart badge disappears or shows "0"
- Product remains in product list
- Product position unchanged
- No error messages

**Postconditions:**
- Cart is empty
- Product can be added again

---

### TC-PL-005 — Sort Products by Name (A → Z)

**Priority:** P1 (High)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Products screen
- Default sort order is active

**Steps:**
1. Tap sort dropdown button (top-right area)
2. Select "Name (A to Z)"
3. Wait for list to re-render

**Expected Result:**
- Sort dropdown menu opens
- "Name (A to Z)" option is visible
- After selection, dropdown closes
- Products re-order alphabetically:
  1. Sauce Labs Backpack
  2. Sauce Labs Bike Light
  3. Sauce Labs Bolt T-Shirt
  4. Sauce Labs Fleece Jacket
  5. Sauce Labs Onesie
  6. Test.allTheThings() T-Shirt (Red)
- Sort animation is smooth (if any)
- Cart items remain unchanged
- Sort indicator shows "Name (A to Z)"

**Postconditions:**
- Sort preference is maintained during session
- Cart state persists

---

### TC-PL-006 — Sort Products by Price (Low → High)

**Priority:** P1 (High)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Products screen

**Steps:**
1. Tap sort dropdown
2. Select "Price (low to high)"
3. Verify product order

**Expected Result:**
- Products sorted by ascending price:
  1. Sauce Labs Onesie ($7.99)
  2. Sauce Labs Bike Light ($9.99)
  3. Sauce Labs Bolt T-Shirt ($15.99)
  4. Test.allTheThings() T-Shirt ($15.99)
  5. Sauce Labs Backpack ($29.99)
  6. Sauce Labs Fleece Jacket ($49.99)
- Prices are clearly visible
- Sort indicator updates
- Cart state unchanged

**Postconditions:**
- Sort order persists

---

### TC-PL-007 — Sort Products by Price (High → Low)

**Priority:** P2 (Medium)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Products screen

**Steps:**
1. Tap sort dropdown
2. Select "Price (high to low)"

**Expected Result:**
- Products sorted by descending price:
  1. Sauce Labs Fleece Jacket ($49.99)
  2. Sauce Labs Backpack ($29.99)
  3. Sauce Labs Bolt T-Shirt ($15.99)
  4. Test.allTheThings() T-Shirt ($15.99)
  5. Sauce Labs Bike Light ($9.99)
  6. Sauce Labs Onesie ($7.99)
- Sort indicator shows "Price (high to low)"

**Postconditions:**
- Sort remains active

---

### TC-PL-008 — Sort Products by Name (Z → A)

**Priority:** P2 (Medium)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Products screen

**Steps:**
1. Tap sort dropdown
2. Select "Name (Z to A)"

**Expected Result:**
- Products sorted in reverse alphabetical order:
  1. Test.allTheThings() T-Shirt (Red)
  2. Sauce Labs Onesie
  3. Sauce Labs Fleece Jacket
  4. Sauce Labs Bolt T-Shirt
  5. Sauce Labs Bike Light
  6. Sauce Labs Backpack
- Sort indicator updates correctly

---

### TC-PL-009 — Scroll Through Product List

**Priority:** P2 (Medium)  
**Type:** UI, Performance  
**Automation:** ✅ Yes  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is on Products screen
- At least 6 products visible

**Steps:**
1. Scroll down to bottom of product list
2. Scroll back up to top
3. Repeat 3 times

**Expected Result:**
- Smooth scrolling with no lag
- All product cards remain visible during scroll
- Images load correctly
- No flickering or rendering issues
- Scroll performance is consistent
- App does not freeze or crash
- Cart badge remains visible during scroll

**Postconditions:**
- Screen remains responsive

---

### TC-PL-010 — Verify Product Price Format

**Priority:** P2 (Medium)  
**Type:** Functional, Data Validation  
**Automation:** ✅ Yes  
**Execution Time:** ~5 seconds

**Preconditions:**
- User is on Products screen

**Steps:**
1. Iterate through all visible products
2. Verify price format for each product

**Expected Result:**
- All prices follow format: $XX.XX
- Currency symbol ($) is present
- Two decimal places always shown
- Prices are:
  - Sauce Labs Backpack: $29.99
  - Sauce Labs Bike Light: $9.99
  - Sauce Labs Bolt T-Shirt: $15.99
  - Sauce Labs Fleece Jacket: $49.99
  - Sauce Labs Onesie: $7.99
  - Test.allTheThings() T-Shirt: $15.99
- No formatting errors (e.g., $9.9 or 9.99)

---

## 4. PRODUCT DETAILS SCREEN

### TC-PD-001 — Open Product Details Page

**Priority:** P1 (High)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Products screen

**Test Data:**
- Product: "Sauce Labs Backpack"

**Steps:**
1. Locate "Sauce Labs Backpack" product card
2. Tap on product name/title (clickable text)
3. Wait for details page to load

**Expected Result:**
- Product details page opens within 2 seconds
- Back button (←) is visible in top-left
- Product details displayed:
  - Product name: "Sauce Labs Backpack"
  - Large product image (full-width)
  - Full product description (multi-line)
  - Price: $29.99
  - "ADD TO CART" button (blue) OR "REMOVE" button (red) if already in cart
- All elements are properly aligned
- Text is readable
- Image is not distorted
- Page is scrollable (if content exceeds screen height)

**Postconditions:**
- User can navigate back to Products screen
- Product state (in cart or not) remains consistent

---

### TC-PD-002 — Add to Cart from Product Details

**Priority:** P1 (High)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is on Product Details page for "Sauce Labs Bike Light"
- Cart is empty
- "ADD TO CART" button is visible

**Steps:**
1. Verify "ADD TO CART" button is displayed (blue)
2. Tap "ADD TO CART" button
3. Verify UI changes

**Expected Result:**
- Button changes from "ADD TO CART" to "REMOVE"
- Button color changes from blue to red
- Cart badge in top-right updates to "1"
- Cart badge becomes visible if hidden
- No navigation occurs (user remains on details page)
- No error messages
- Action completes within 1 second

**Postconditions:**
- Product is in cart
- User can remove from details page

---

### TC-PD-003 — Navigate Back from Product Details

**Priority:** P1 (High)  
**Type:** Functional, Navigation  
**Automation:** ✅ Yes  
**Execution Time:** ~6 seconds

**Preconditions:**
- User is on Product Details page

**Steps:**
1. Locate back button (← arrow) in top-left corner
2. Tap back button
3. Verify navigation

**Expected Result:**
- User navigates back to Products screen
- Back navigation is smooth (no lag)
- Products list is displayed
- Scroll position is preserved (if possible)
- Cart state is maintained
- Sort order is maintained
- No data is lost
- Back navigation completes in < 1 second

**Postconditions:**
- User is on Products screen
- App state unchanged

---

## 5. CART SCREEN

### TC-CT-001 — Open Cart and View Items

**Priority:** P0 (Critical)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is logged in
- 2 items are in cart:
  - Sauce Labs Backpack ($29.99)
  - Sauce Labs Bike Light ($9.99)
- Cart badge shows "2"

**Steps:**
1. Tap cart icon in top-right corner
2. Wait for cart screen to load
3. Verify cart contents

**Expected Result:**
- Cart screen opens within 2 seconds
- Screen title displays "YOUR CART"
- Cart item list is visible
- Each cart item displays:
  - Quantity label: "QTY" and quantity number
  - Product name
  - Product description (1 line)
  - Price
  - "REMOVE" button (below each item)
- Total 2 items are listed:
  1. Sauce Labs Backpack - QTY: 1 - $29.99
  2. Sauce Labs Bike Light - QTY: 1 - $9.99
- Bottom buttons visible:
  - "CONTINUE SHOPPING" button
  - "CHECKOUT" button (blue/green)
- Back button visible in top-left
- Cart badge still shows "2"

**Postconditions:**
- Cart remains accessible
- Items persist in cart

---

### TC-CT-002 — Remove Item from Cart

**Priority:** P0 (Critical)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~8 seconds

**Preconditions:**
- User is on Cart screen
- Cart contains "Sauce Labs Bike Light"
- Cart badge shows at least "1"

**Steps:**
1. Locate "Sauce Labs Bike Light" in cart list
2. Tap "REMOVE" button for that item
3. Wait for UI update

**Expected Result:**
- Item "Sauce Labs Bike Light" disappears from cart list immediately
- Cart badge decreases by 1
- If cart becomes empty:
  - Cart list is empty
  - Badge shows "0" or disappears
  - "CHECKOUT" button may be disabled
- If items remain:
  - Other items stay in cart
  - Badge shows correct count
- No error messages
- Cart screen remains open
- Removal animation is smooth (if any)

**Postconditions:**
- Item is removed from cart
- Cart count updated
- Item can be added again from Products screen

---

### TC-CT-003 — Continue Shopping from Cart

**Priority:** P1 (High)  
**Type:** Functional, Navigation  
**Automation:** ✅ Yes  
**Execution Time:** ~6 seconds

**Preconditions:**
- User is on Cart screen
- Cart contains at least 1 item

**Steps:**
1. Scroll to bottom of cart (if needed)
2. Locate "CONTINUE SHOPPING" button
3. Tap "CONTINUE SHOPPING"

**Expected Result:**
- User navigates back to Products screen
- Navigation is smooth
- Products list is displayed
- Cart items remain in cart (not cleared)
- Cart badge shows correct count
- Sort order is preserved
- Scroll position may reset to top
- No data loss occurs

**Postconditions:**
- Cart state persists
- User can continue shopping

---

### TC-CT-004 — Verify Cart is Empty

**Priority:** P2 (Medium)  
**Type:** Functional  
**Automation:** ✅ Yes  
**Execution Time:** ~5 seconds

**Preconditions:**
- User is logged in
- Cart is empty (no items added)

**Steps:**
1. Tap cart icon
2. Verify empty cart state

**Expected Result:**
- Cart screen opens
- Screen title: "YOUR CART"
- Cart list is empty (no items displayed)
- Cart badge shows "0" or is not visible
- "CHECKOUT" button may be disabled or hidden
- "CONTINUE SHOPPING" button is visible and enabled
- Empty cart message may be displayed (if applicable)
- No errors occur

**Postconditions:**
- User can add items and return to cart

---

## 6. CHECKOUT FLOW

### TC-CH-001 — Complete Successful Checkout

**Priority:** P0 (Critical)  
**Type:** End-to-End, Smoke  
**Automation:** ✅ Yes  
**Execution Time:** ~25 seconds

**Preconditions:**
- User is logged in
- Cart contains at least 1 item (e.g., "Sauce Labs Backpack")
- User is on Cart screen

**Test Data:**
- First Name: `John`
- Last Name: `Doe`
- Zip/Postal Code: `12345`

**Steps:**
1. Tap "CHECKOUT" button on Cart screen
2. Wait for Checkout Information screen to load
3. Enter First Name: "John"
4. Enter Last Name: "Doe"
5. Enter Zip Code: "12345"
6. Tap "CONTINUE" button
7. Wait for Checkout Overview screen
8. Verify order summary (items, prices, totals)
9. Tap "FINISH" button
10. Wait for Checkout Complete screen

**Expected Result:**

**Step 2 - Checkout Information screen:**
- Screen title: "CHECKOUT: INFORMATION"
- Three input fields visible:
  - First Name (placeholder/label visible)
  - Last Name (placeholder/label visible)
  - Zip/Postal Code (placeholder/label visible)
- "CONTINUE" button visible (blue)
- "CANCEL" button visible
- Back button in top-left

**Step 7 - Checkout Overview screen:**
- Screen title: "CHECKOUT: OVERVIEW"
- Cart items listed with:
  - QTY: 1
  - Product name
  - Description
  - Price
- Payment Information section displays
- Shipping Information section displays
- Price Total section shows:
  - Item total: $29.99
  - Tax: (calculated amount)
  - Total: (item + tax)
- "FINISH" button visible (green/blue)
- "CANCEL" button visible

**Step 10 - Checkout Complete screen:**
- Screen title: "CHECKOUT: COMPLETE!"
- Success message displayed: "THANK YOU FOR YOUR ORDER"
- Success icon/image visible (checkmark or delivery image)
- Subtext message visible: "Your order has been dispatched..."
- "BACK HOME" button visible
- No error messages
- Cart is cleared (badge = 0)

**Postconditions:**
- Order is completed
- Cart is empty
- User can tap "BACK HOME" to return to Products screen

---

### TC-CH-002 — Checkout with Empty First Name

**Priority:** P1 (High)  
**Type:** Negative, Validation  
**Automation:** ✅ Yes  
**Execution Time:** ~10 seconds

**Preconditions:**
- User is on Checkout Information screen
- Cart has at least 1 item

**Test Data:**
- First Name: (empty)
- Last Name: `Doe`
- Zip Code: `12345`

**Steps:**
1. Leave First Name field empty
2. Enter Last Name: "Doe"
3. Enter Zip Code: "12345"
4. Tap "CONTINUE" button

**Expected Result:**
-