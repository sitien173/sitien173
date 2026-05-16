#!/usr/bin/env python3
import time
from datetime import datetime
from anthropic import Anthropic

timestamp = datetime.now().isoformat()

try:
    start_time = time.time()
    client = Anthropic()
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=5,
        messages=[{"role": "user", "content": "ping"}]
    )
    response_time = time.time() - start_time
    print(f"[{timestamp}] Health check: OK (response time: {response_time:.2f}s)")
except Exception as e:
    print(f"[{timestamp}] Health check: FAILED ({str(e)})")
