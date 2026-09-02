# Formata 3.0

Formata 3.0 is the next-generation legal deadline and limitation management platform for law firms.

## Product direction

Formata is a dedicated legal deadline and limitation management layer that integrates with a firm's existing case-management software, applies jurisdiction-specific legal rules, assigns responsibility, and escalates critical deadlines before they are missed.

## Architecture principles

- Firm is the top-level tenant.
- Matters are separate from deadlines.
- Matters can have many parties, events, and deadlines.
- Jurisdictions and legal rules are data-driven, versioned, and auditable.
- Deadline calculations run server-side.
- Permissions are enforced server-side and scoped by firm.
- Integrations normalize external case-management data into Formata matters and events.
- Billing belongs to the firm, not to an individual user.

## Initial domain model

Firm -> Memberships / Users -> Matters -> Parties -> Events -> Jurisdictions -> Legal Rules / Rule Versions -> Calculated Deadlines -> Assignments -> Reminders / Escalations -> Audit History -> Integrations

## Repository policy

This repository is the active development home for Formata 3.0. Formata 1.0 and Formata 2.0 are reference-only and should not be modified as part of 3.0 development.
