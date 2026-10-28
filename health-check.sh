#!/bin/bash

# Health check script for remote server monitoring
# This script pings a remote server to verify the system is online

REMOTE_SERVER="${REMOTE_SERVER_URL:-http://localhost:8000}"
TIMEOUT="${TIMEOUT:-5}"
LOG_FILE="${LOG_FILE:-/tmp/health-check.log}"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Checking remote server health: $REMOTE_SERVER" >> "$LOG_FILE"

# Try to curl the remote server
if curl -s --max-time "$TIMEOUT" "$REMOTE_SERVER" > /dev/null 2>&1; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✓ Remote server is ONLINE" >> "$LOG_FILE"
    exit 0
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✗ Remote server is OFFLINE or unreachable" >> "$LOG_FILE"
    exit 1
fi
