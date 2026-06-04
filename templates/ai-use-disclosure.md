# AI-Use Disclosure Template

Use this template in a manuscript, appendix, or repository documentation. Adapt it to the specific project and journal requirements.

## Short Version

We used AI coding agents for code drafting, refactoring, documentation, and mock-data debugging in an agent-safe development environment. The agents did not have access to protected research data, real-data outputs, credentials, or unsanitized logs. Real-data analyses were executed in a separate protected environment without AI coding-agent access. We validated the code through mock-data tests, clean-environment execution checks, and human review of core transformations and final outputs.

## Detailed Version

AI coding agents were used for the following tasks:

- [ ] Code drafting.
- [ ] Refactoring.
- [ ] Documentation.
- [ ] Mock-data debugging.
- [ ] Test drafting.
- [ ] Visualization drafting.
- [ ] Manuscript language support.

AI coding agents were not allowed to access:

- [ ] Real data.
- [ ] Protected outputs.
- [ ] Credentials or secrets.
- [ ] Unsanitized logs or error reports.
- [ ] Notebooks or screenshots containing real observations.

Real-data execution took place in:

- [ ] Institutional server/HPC/secure VM.
- [ ] Clean local VM.
- [ ] Other approved protected environment: `[describe]`

Validation included:

- [ ] Mock-data tests.
- [ ] Clean-environment execution checks.
- [ ] Human review of core transformations.
- [ ] Human review of final tables and figures.
- [ ] Independent reproduction by a collaborator.

Residual risks:

`[Briefly state remaining limitations, such as the possibility of undetected code errors or incomplete mock-data coverage.]`
