#!/bin/bash
# System health check - verify connectivity and system status

set -e

# Configuration (update these with your actual remote server details)
REMOTE_SERVER="${REMOTE_SERVER_URL:-https://www.google.com}"
TIMEOUT=10
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "[${TIMESTAMP}] Starting system health check..."

# Check internet connectivity
if curl -s -m $TIMEOUT --connect-timeout 5 "$REMOTE_SERVER" > /dev/null 2>&1; then
    echo "[${TIMESTAMP}] ✓ System is online - Remote server is reachable"
    echo "[${TIMESTAMP}] ✓ Health check passed"
    exit 0
else
    echo "[${TIMESTAMP}] ✗ System health check failed - Unable to reach remote server"
    exit 1
fi
