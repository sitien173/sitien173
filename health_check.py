#!/usr/bin/env python3
import anthropic
import time
from datetime import datetime

def health_check():
    try:
        start_time = time.time()
        timestamp = datetime.now().isoformat()

        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "ping"}
            ]
        )

        response_time = time.time() - start_time

        # Check if we got a valid response
        if message.content and len(message.content) > 0:
            print(f"[{timestamp}] Health check: OK (response time: {response_time:.2f}s)")
            return True
        else:
            print(f"[{timestamp}] Health check: FAILED")
            return False

    except Exception as e:
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] Health check: FAILED ({str(e)})")
        return False

if __name__ == "__main__":
    health_check()
