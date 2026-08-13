# Local Two-VM Fallback

The recommended vault environment is an institutional server, HPC system, secure VM, managed research workspace, or other infrastructure approved for protected research data. If that is unavailable, a two-VM setup on one local device can be used as a fallback if it is permitted by the relevant data governance rules.

## Midas VM

The Midas VM is for agent-assisted code and documentation work.

- Docker Sandboxes and the AI coding agent are allowed.
- Internet access allowed if needed.
- Contains code, documentation, agent rules, and safe structural examples.
- Contains no real data, real outputs, credentials, or unsanitized logs.
- Pushes reviewed code to GitHub or another approved Git host.

## Vault VM

The Vault VM is for real-data execution.

- No AI coding agent installed.
- No agentic IDE plugin installed.
- Real data stored outside shared folders.
- Pulls reviewed code from Git.
- Does not push real-data outputs, logs, screenshots, or notebooks.
- Keeps protected outputs inside the Vault VM or approved storage.

## Shared Resource Warnings

Avoid:

- Shared clipboards.
- Shared folders.
- Shared home directories.
- Shared cloud-sync folders.
- Screenshots copied from the Vault VM to the Midas VM.
- Logs copied from the Vault VM to the Midas VM.
- SSH keys or credentials mounted into the Midas VM.

## Minimum Separation Test

Before using the setup, verify:

- [ ] The Midas VM cannot see Vault VM files.
- [ ] The Vault VM has no coding agent installed.
- [ ] Real data are outside synced and shared folders.
- [ ] Git tracks only code, documentation, rules, and safe structural examples.
- [ ] `.gitignore` blocks data, outputs, logs, credentials, caches, and checkpoints.
