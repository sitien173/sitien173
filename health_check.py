#!/usr/bin/env python3
import time
from datetime import datetime
import sys

try:
    from anthropic import Anthropic

    start_time = time.time()
    timestamp = datetime.now().isoformat()

    client = Anthropic()
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=10,
        messages=[
            {"role": "user", "content": "ping"}
        ]
    )

    elapsed = time.time() - start_time

    if response and response.content:
        print(f"[{timestamp}] Health check: OK (response time: {elapsed:.2f}s)")
        sys.exit(0)
    else:
        print(f"[{timestamp}] Health check: FAILED (no response)")
        sys.exit(1)

except Exception as e:
    timestamp = datetime.now().isoformat()
    print(f"[{timestamp}] Health check: FAILED ({str(e)})")
    sys.exit(1)
