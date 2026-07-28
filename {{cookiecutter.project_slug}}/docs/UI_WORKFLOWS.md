# UI Workflows

This file tracks the implemented user-facing workflows for the Modular Base template.

## Flow: Public Landing To Authentication
- Status: implemented
- Last updated: 2026-05-03
- Entry points: `/`, `/login`, `/signup`
- Steps:
  1. Anonymous users start on `HomePage`.
  2. Header actions route into login or signup.
  3. `AuthPage` switches between `LoginForm` and `SignUpForm` based on the active route.
  4. Successful auth redirects to the originally requested protected route or `/dashboard`.
- Empty/loading/error states:
  - App bootstrap uses a full-screen loading state while restoring auth.
  - Auth forms surface their own validation and API errors.
- Dependencies:
  - `frontend/src/pages/HomePage.tsx`
  - `frontend/src/pages/AuthPage.tsx`
  - `frontend/src/components/LoginForm.tsx`
  - `frontend/src/components/SignUpForm.tsx`
- Notes:
  - The public entry path should stay separate from authenticated product workflows.

## Flow: OTP Verification
- Status: implemented
- Last updated: 2026-05-03
- Entry points: `/verify`, `/verify-login`
- Steps:
  1. User reaches verification after an auth initiation step.
  2. Verification component accepts the token input.
  3. Successful validation unlocks the authenticated shell.
- Empty/loading/error states:
  - Loading and invalid-token feedback remain inline within the verification screens.
- Dependencies:
  - `frontend/src/components/VerifyAccount.tsx`
  - `frontend/src/components/VerifyLogin.tsx`
- Notes:
  - Keep verification as a focused full-page step.

## Flow: Authenticated Dashboard Entry
- Status: implemented
- Last updated: 2026-05-03
- Entry points: `/dashboard`
- Steps:
  1. `PrivateRoute` blocks unauthenticated users.
  2. Authenticated users land on `Dashboard`.
  3. Main CTAs route to `/items` and `/settings`.
- Empty/loading/error states:
  - Global loading screen remains visible while auth state initializes.
- Dependencies:
  - `frontend/src/App.tsx`
  - `frontend/src/pages/Dashboard.tsx`
  - `frontend/src/components/shared/Navbar.tsx`
  - `frontend/src/components/shared/Breadcrumbs.tsx`
- Notes:
  - Dashboard is a lightweight app hub and should remain uncluttered.

## Flow: Item Management
- Status: implemented
- Last updated: 2026-05-03
- Entry points: `/items`, `/items/:id`
- Steps:
  1. List mode fetches and renders all items.
  2. Create CTA enters inline create mode.
  3. Item card view action routes to `/items/:id` and loads detail.
  4. Detail mode offers edit and back.
  5. Edit/create reuse the shared `ItemForm`.
  6. Lifecycle actions on cards support archive, activate, and delete.
- Empty/loading/error states:
  - Skeleton grid for initial loading.
  - `EmptyState` for no items.
  - Missing detail card for unknown item IDs.
  - Inline API error banner with dismissal/auto-clear behavior.
- Dependencies:
  - `frontend/src/pages/ItemsPage.tsx`
  - `frontend/src/components/items/ItemList.tsx`
  - `frontend/src/components/items/ItemCard.tsx`
  - `frontend/src/components/items/ItemForm.tsx`
- Notes:
  - Route family and page modes should stay aligned; avoid splitting CRUD into unrelated surfaces.

## Flow: Settings And GitHub Connection
- Status: implemented
- Last updated: 2026-05-03
- Entry points: `/settings`
- Steps:
  1. User navigates to settings.
  2. Profile summary renders in the first card.
  3. GitHub connect action launches OAuth using a backend-issued state token.
  4. Callback query params are validated and exchanged inside the page.
  5. Disconnect remains available as a separate confirmation-based action.
- Empty/loading/error states:
  - Button-level loading indicators for connect/disconnect.
  - Toast feedback for OAuth failures and success states.
- Dependencies:
  - `frontend/src/pages/SettingsPage.tsx`
  - `frontend/src/services/api.ts`
- Notes:
  - Callback handling should stay idempotent and safe to reload.

## Flow: Theme And Language Switching
- Status: implemented
- Last updated: 2026-05-03
- Entry points: home header and global navigation controls
- Steps:
  1. Theme toggles through `ThemeContext`.
  2. `ThemeInitializer` hydrates the saved preference.
  3. Language menu switches between EN and ES.
  4. Language choice persists locally.
- Empty/loading/error states:
  - No distinct loading state; updates are immediate.
- Dependencies:
  - `frontend/src/context/ThemeContext.tsx`
  - `frontend/src/components/shared/ThemeInitializer.tsx`
  - `frontend/src/components/layout/TopBar.tsx`
  - `frontend/src/components/shared/Navbar.tsx`
- Notes:
  - Treat these controls as app-wide utilities, not page-specific decorations.

## Flow: Command Palette Access
- Status: implemented
- Last updated: 2026-05-03
- Entry points: global app shell
- Steps:
  1. `CommandPalette` mounts once at app level.
  2. User opens it through its configured shortcut or trigger.
  3. Palette enables cross-app command/navigation access.
- Empty/loading/error states:
  - Hidden until invoked.
- Dependencies:
  - `frontend/src/components/shared/CommandPalette.tsx`
  - `frontend/src/App.tsx`
- Notes:
  - Keep palette state global across route changes.

## Flow: Backend Unavailable Recovery
- Status: implemented
- Last updated: 2026-05-03
- Entry points: app bootstrap, `/start-server`, `/server-down`
- Steps:
  1. App checks backend health during startup when on-demand startup is configured.
  2. If unhealthy, routing is forced to `/start-server`.
  3. Explicit service failure can render `ServerDown`.
  4. Recovery actions restart or re-enter the app.
- Empty/loading/error states:
  - Full-screen spinner before health is known.
  - Dedicated operational pages for sleep/down cases.
- Dependencies:
  - `frontend/src/App.tsx`
  - `frontend/src/pages/ServerStartPage.tsx`
  - `frontend/src/pages/ServerDown.tsx`
  - `frontend/src/services/BackendManager.ts`
- Notes:
  - Treat on-demand infrastructure states as product workflow, not incidental errors.

## Flow: Unknown Route Handling
- Status: implemented
- Last updated: 2026-05-03
- Entry points: any unmatched route
- Steps:
  1. Router falls through to `NotFoundPage`.
  2. User gets a single return-home action.
- Empty/loading/error states:
  - None beyond the 404 state.
- Dependencies:
  - `frontend/src/pages/NotFoundPage.tsx`
- Notes:
  - Keep the 404 journey short and decisive.
