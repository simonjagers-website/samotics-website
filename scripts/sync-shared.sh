#!/bin/bash
cd "$(dirname "$0")/.." && python scripts/sync-shared.py "$@"
