#!/usr/bin/env python3
import time
from datetime import datetime
from anthropic import Anthropic

def health_check():
    timestamp = datetime.now().isoformat()
    start_time = time.time()

    try:
        client = Anthropic()
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "ping"}
            ]
        )
        response_time = time.time() - start_time
        status = "OK"
        print(f"[{timestamp}] Health check: {status} (response time: {response_time:.2f}s)")
        return True
    except Exception as e:
        response_time = time.time() - start_time
        status = "FAILED"
        print(f"[{timestamp}] Health check: {status} (error: {str(e)}, response time: {response_time:.2f}s)")
        return False

if __name__ == "__main__":
    health_check()
