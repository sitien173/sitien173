#!/usr/bin/env python3
import os
import time
from datetime import datetime
from anthropic import Anthropic

def health_check():
    try:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        client = Anthropic(api_key=api_key)
        start_time = time.time()
        timestamp = datetime.now().isoformat()

        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "ping"}
            ]
        )

        end_time = time.time()
        response_time = end_time - start_time

        print(f"[{timestamp}] Health check: OK (response time: {response_time:.3f}s)")
        return True

    except Exception as e:
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] Health check: FAILED")
        return False

if __name__ == "__main__":
    health_check()
