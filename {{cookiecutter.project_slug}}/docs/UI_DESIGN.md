# UI Design

This file describes the visual and interaction contract for the Modular Base template UI.

## View or Component: HomePage
- Purpose: public landing page for the modular starter app.
- Location: `frontend/src/pages/HomePage.tsx`
- Layout structure: slim header, centered hero, feature grid.
- Visual style: clean marketing shell with primary CTA emphasis and broad spacing.
- States: authenticated CTA variant and anonymous CTA variant.
- Interactions: theme toggle, login/signup/dashboard navigation.
- Responsive behavior: feature grid collapses to a single column on small screens.
- Accessibility notes: icon-only theme toggle must stay labeled.
- Reuse constraints: keep this page lightweight and welcoming rather than operational.
- Last updated: 2026-05-03

## View or Component: AuthPage
- Purpose: route-level wrapper for login vs signup.
- Location: `frontend/src/pages/AuthPage.tsx`
- Layout structure: full-page form shell delegated to child auth forms.
- Visual style: minimal and focused.
- States: login, signup.
- Interactions: route-based mode switching.
- Responsive behavior: inherited from child forms.
- Accessibility notes: switching actions should remain obvious and textual.
- Reuse constraints: do not overload this page with post-auth content.
- Last updated: 2026-05-03

## View or Component: Dashboard
- Purpose: authenticated starting point.
- Location: `frontend/src/pages/Dashboard.tsx`
- Layout structure: navbar, breadcrumbs, hero, feature card grid.
- Visual style: soft card layout with neutral surfaces and a primary accent.
- States: standard authenticated view.
- Interactions: CTA routing into items and settings.
- Responsive behavior: stacked hero actions and collapsing feature grid.
- Accessibility notes: retain strong heading hierarchy.
- Reuse constraints: preserve as a concise hub page.
- Last updated: 2026-05-03

## View or Component: ItemsPage
- Purpose: removable scaffold for modular sample entities from one route family. This is an example implementation pattern, not a product-specific surface.
- Location: `frontend/src/pages/ItemsPage.tsx`
- Layout structure: shared shell plus content that swaps among list/detail/create/edit.
- Visual style: CRUD card interface with inline forms and detail panels.
- States: list, detail, create, edit, loading, missing item.
- Interactions: view, create, edit, back, archive, activate, delete.
- Responsive behavior: action groups wrap; grids collapse gracefully.
- Accessibility notes: destructive actions must keep explicit confirmations.
- Reuse constraints: remove, rename, or replace this page when the product domain is defined; do not preserve visible `Items` navigation in generated apps unless the user explicitly asks for a generic item manager.
- Last updated: 2026-05-03

## View or Component: SettingsPage
- Purpose: profile and integration configuration.
- Location: `frontend/src/pages/SettingsPage.tsx`
- Layout structure: back header, breadcrumbs, stacked settings cards.
- Visual style: administrative but friendly; relies on section cards and explicit button states.
- States: connected, disconnected, connecting, disconnecting, callback processing.
- Interactions: GitHub connect/disconnect, back navigation.
- Responsive behavior: single-column stacked sections.
- Accessibility notes: long-lived async actions must remain perceivable with button states and toasts.
- Reuse constraints: integration sections should stay card-based and separable.
- Last updated: 2026-05-03

## View or Component: ServerStartPage
- Purpose: operational wake/start screen for on-demand deployments.
- Location: `frontend/src/pages/ServerStartPage.tsx`
- Layout structure: centered utility-state panel.
- Visual style: informative and action-oriented rather than decorative.
- States: sleeping backend, starting backend, start failure.
- Interactions: wake/start action.
- Responsive behavior: single-column centered layout.
- Accessibility notes: status messaging should remain readable under reduced viewport widths.
- Reuse constraints: do not mix with 404 or marketing empty-state patterns.
- Last updated: 2026-05-03

## View or Component: ServerDown
- Purpose: hard failure operational screen.
- Location: `frontend/src/pages/ServerDown.tsx`
- Layout structure: centered alert card with stacked buttons.
- Visual style: caution-first with red signal color and simple action hierarchy.
- States: backend unavailable.
- Interactions: retry and go-home actions.
- Responsive behavior: centered narrow column.
- Accessibility notes: primary action stays first.
- Reuse constraints: maintain clear distinction from generic 404 and empty states.
- Last updated: 2026-05-03

## View or Component: NotFoundPage
- Purpose: fallback for unknown routes.
- Location: `frontend/src/pages/NotFoundPage.tsx`
- Layout structure: centered card and one CTA.
- Visual style: calm empty-state presentation.
- States: 404.
- Interactions: go home.
- Responsive behavior: narrow centered content block.
- Accessibility notes: keep heading and CTA prominent.
- Reuse constraints: avoid adding extra operational messaging.
- Last updated: 2026-05-03

## View or Component: ItemList
- Purpose: list/filter layer for modular sample data.
- Location: `frontend/src/components/items/ItemList.tsx`
- Layout structure: header row, error band, filter row, responsive grid.
- Visual style: compact management UI with a clear create CTA.
- States: loading skeletons, empty state, error state, filtered list.
- Interactions: status filtering and item lifecycle actions.
- Responsive behavior: controls stack before shrinking tap targets.
- Accessibility notes: form labels and dismiss buttons remain explicit.
- Reuse constraints: keep card density moderate for readability.
- Last updated: 2026-05-03

## View or Component: ItemCard
- Purpose: summarize a modular item with lifecycle actions.
- Location: `frontend/src/components/items/ItemCard.tsx`
- Layout structure: title/status row, metadata lines, action row.
- Visual style: compact card with colored badge and small action buttons.
- States: draft, active, archived.
- Interactions: view, archive, activate, delete.
- Responsive behavior: buttons wrap to new lines when needed.
- Accessibility notes: actions stay text-first.
- Reuse constraints: avoid embedding heavy inline editors here.
- Last updated: 2026-05-03

## View or Component: ItemForm
- Purpose: shared create/edit form.
- Location: `frontend/src/components/items/ItemForm.tsx`
- Layout structure: title, error block, field stack, footer actions.
- Visual style: simple form treatment consistent with the shared primitives.
- States: create, edit, loading submit, validation error, API error.
- Interactions: input editing, submit, cancel.
- Responsive behavior: vertical stack throughout.
- Accessibility notes: required markers and error messaging must remain clear.
- Reuse constraints: keep the form narrow enough to fit inline in page workflows.
- Last updated: 2026-05-03

## View or Component: Shared Navigation And Utility Layer
- Purpose: keep global nav, orientation, theme, and command utilities consistent.
- Location:
  - `frontend/src/components/shared/Navbar.tsx`
  - `frontend/src/components/shared/Breadcrumbs.tsx`
  - `frontend/src/components/shared/CommandPalette.tsx`
  - `frontend/src/components/shared/ThemeInitializer.tsx`
  - `frontend/src/components/layout/TopBar.tsx`
- Layout structure: compact top navigation and supporting global utilities.
- Visual style: low-chrome, neutral surfaces, primary accent highlights.
- States: language menu open/closed, user menu open/closed, theme dark/light.
- Interactions: navigation, theme change, language change, command access, user actions.
- Responsive behavior: utility clusters should compress before core actions disappear.
- Accessibility notes: menus must support focus and clear labels.
- Reuse constraints: keep nav height and control vocabulary consistent across pages.
- Last updated: 2026-05-03

## View or Component: Shared Foundation
- Purpose: primitive building blocks for every screen.
- Location:
  - `frontend/src/components/shared/Button.tsx`
  - `frontend/src/components/shared/Card.tsx`
  - `frontend/src/components/shared/Badge.tsx`
  - `frontend/src/components/shared/Input.tsx`
  - `frontend/src/components/shared/Modal.tsx`
  - `frontend/src/components/shared/EmptyState.tsx`
  - `frontend/src/components/shared/Loading.tsx`
  - `frontend/src/components/shared/Skeleton.tsx`
  - `frontend/src/components/shared/Sidebar.tsx`
  - `frontend/src/components/shared/SmartImage.tsx`
- Layout structure: primitives only.
- Visual style: rounded edges, soft borders, dark-mode-compatible tokens.
- States: variant-specific per primitive.
- Interactions: dependent on primitive role.
- Responsive behavior: primitives should scale without per-page overrides where possible.
- Accessibility notes: primitives define the baseline accessible patterns for the template.
- Reuse constraints: add variants carefully instead of duplicating primitives locally.
- Last updated: 2026-05-03
