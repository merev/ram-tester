#!/usr/bin/env python3
import time
import sys
import os

def consume_memory():
    """Gradually consume memory until we hit the limit"""
    chunks = []
    chunk_size = 1024 * 1024  # 1 MB chunks
    target_memory = 70 * 1024 * 1024  # Try to reach ~70MB (slightly over 64Mi limit)
    
    print("Starting memory consumption simulation...")
    print(f"Target memory: {target_memory / (1024*1024):.1f} MB")
    print(f"Memory limit: 64 MiB")
    print("-" * 50)
    
    try:
        allocated = 0
        while allocated < target_memory:
            # Allocate memory in chunks
            chunk = ' ' * chunk_size  # 1 MB string
            chunks.append(chunk)
            allocated += chunk_size
            
            current_mb = allocated / (1024 * 1024)
            print(f"Allocated: {current_mb:.1f} MB")
            
            # Sleep to make it easier to observe
            time.sleep(0.5)
            
    except MemoryError:
        print("\n!!! MemoryError: Cannot allocate more memory !!!")
        return False
    except Exception as e:
        print(f"\n!!! Exception: {e} !!!")
        return False
    
    print("\n✓ Successfully allocated target memory")
    print("Holding memory for observation...")
    
    # Keep the memory allocated
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    
    return True

if __name__ == "__main__":
    print("Memory Hog Simulator")
    print(f"Python version: {sys.version}")
    consume_memory()
