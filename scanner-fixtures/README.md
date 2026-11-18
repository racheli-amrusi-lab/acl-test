# Scanner test fixtures

These files contain intentionally insecure, non-production examples for scanner validation. All credential-like values are fake placeholders and must never be treated as real credentials. Do not deploy or install these fixtures.

Categories:
- `secrets/` — fake credential-like strings
- `sast/` — unsafe code patterns
- `sca/` — intentionally outdated dependency declarations
- `aca/` — access-control misconfiguration examples (assuming ACA means access-control analysis)

If your scanner uses a different meaning for “ACA,” replace that fixture category accordingly.
