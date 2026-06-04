# Safe Debugging Report Template

Use this template when clean-environment execution fails. Do not include real rows, text, IDs, usernames, URLs, exact timestamps, paths, screenshots, or protected values.

## Environment

- Clean environment type:
- Script or command:
- Date of run:
- Code version or commit:

## Sanitized Failure Summary

Describe the structural issue without exposing data.

Example:

> The analysis failed because one expected timestamp column contained values in two formats. No real values are included here.

## Safe Reproduction Information

- Expected schema:
- Observed structural difference:
- Mock-data fixture needed:
- Transformation step affected:

## Unsafe Details Removed

- [ ] Real text.
- [ ] Usernames.
- [ ] URLs.
- [ ] IDs.
- [ ] Exact timestamps.
- [ ] File paths.
- [ ] Screenshots.
- [ ] Real output values.

## Next Step for Dirty Environment

State the agent-safe task.

Example:

> Add a mock fixture with two fake timestamp formats and update the parser so it handles both formats. Do not use real data.
