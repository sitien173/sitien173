#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime
from anthropic import Anthropic

def health_check():
    """Check if Anthropic API is reachable."""
    timestamp = datetime.now().isoformat()
    start_time = time.time()

    try:
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        # Send minimal message
        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "ping"}
            ]
        )

        response_time = time.time() - start_time

        # Verify we got a response
        if response and response.content:
            print(f"[{timestamp}] Health check: OK (response time: {response_time:.2f}s)")
            return 0
        else:
            print(f"[{timestamp}] Health check: FAILED")
            return 1

    except Exception as e:
        print(f"[{timestamp}] Health check: FAILED")
        sys.stderr.write(f"Error: {e}\n")
        return 1

if __name__ == "__main__":
    sys.exit(health_check())
