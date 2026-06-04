# Local Two-VM Fallback

The recommended clean environment is an institutional server, HPC system, secure VM, or other infrastructure approved for protected research data. If that is unavailable, a two-VM setup on one local device can be used as a fallback if it is permitted by the relevant data governance rules.

## Dirty VM

The dirty VM is for agent-assisted development.

- AI coding agent allowed.
- Internet access allowed if needed.
- Contains code, mock data, Docker, tests, and documentation.
- Contains no real data, real outputs, credentials, or unsanitized logs.
- Pushes reviewed code to GitHub, Codeberg, or GitLab.

## Clean VM

The clean VM is for real-data execution.

- No AI coding agent installed.
- No agentic IDE plugin installed.
- Real data stored outside shared folders.
- Pulls reviewed code from Git.
- Does not push real-data outputs, logs, screenshots, or notebooks.
- Keeps protected outputs inside the clean VM or approved storage.

## Shared Resource Warnings

Avoid:

- Shared clipboards.
- Shared folders.
- Shared home directories.
- Shared cloud-sync folders.
- Screenshots copied from the clean VM to the dirty VM.
- Logs copied from the clean VM to the dirty VM.
- SSH keys or credentials mounted into the dirty VM.

## Minimum Separation Test

Before using the setup, verify:

- [ ] The dirty VM cannot see clean VM files.
- [ ] The clean VM has no coding agent installed.
- [ ] Real data are outside synced and shared folders.
- [ ] Git tracks only code, mock data, tests, and documentation.
- [ ] `.gitignore` blocks data, outputs, logs, credentials, caches, and checkpoints.
