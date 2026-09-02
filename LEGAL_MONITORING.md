# Formata 3.0 legal update monitoring

Formata monitors only active `LegalSource` records that point to verified official HTTPS court, legislature, tribunal, or regulator pages.

## Coverage

The jurisdiction catalogue includes every Canadian province and territory, all 50 U.S. states, and the District of Columbia. Each official source is attached to exactly one jurisdiction. Court and legislative source URLs must be verified before they are activated; Formata does not guess or generate authority URLs.

## Scheduled check

Run:

```bash
python manage.py monitor_legal_sources
```

This command is safe to schedule periodically. It uses ETag and Last-Modified conditional requests when the source supports them, stores immutable normalized snapshots, hashes content, and creates a legal-review candidate only when content changes after the baseline.

## Controlled rule workflow

1. The monitor creates a `LegalUpdateCandidate`.
2. Deterministic language detection flags possible limitation or deadline impact.
3. A reviewer creates a structured `RuleChangeProposal` linked to the official source and an existing `LegalRule`.
4. The official-source candidate must be marked legally verified.
5. A user with Django's `rules.change_ruleversion` permission approves and activates the proposal.
6. Formata creates a new immutable verified `RuleVersion`.
7. Open calculated deadlines tied to that rule and effective date are recalculated atomically.
8. Every changed deadline receives a `DeadlineAudit` entry and a `DeadlineImpactReview` record.
9. Calculation failures are flagged for manual review and do not silently change a deadline.

Source monitoring, heuristics, and AI output cannot activate a production rule by themselves.
