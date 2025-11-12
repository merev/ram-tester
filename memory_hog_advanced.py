#!/usr/bin/env python3
import time
import sys
import os
import signal

class MemoryHog:
    def __init__(self):
        self.chunks = []
        self.running = True
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        print(f"\nReceived signal {signum}, cleaning up...")
        self.running = False
        sys.exit(0)
    
    def get_memory_info(self):
        """Try to get memory information if available"""
        try:
            import psutil
            process = psutil.Process()
            memory_info = process.memory_info()
            return memory_info.rss  # Resident Set Size
        except ImportError:
            return len(self.chunks) * 1024 * 1024  # Estimated
    
    def run(self):
        print("=== Memory Hog Advanced ===")
        print("This will gradually consume memory until OOM killer terminates the pod")
        print("Memory limit: 64Mi")
        print("=" * 40)
        
        chunk_size = 2 * 1024 * 1024  # 2 MB chunks
        iteration = 0
        
        try:
            while self.running and iteration < 50:  # Safety limit
                # Allocate memory
                chunk = 'x' * chunk_size
                self.chunks.append(chunk)
                
                allocated_mb = len(self.chunks) * 2  # 2MB per chunk
                estimated_memory = self.get_memory_info()
                
                print(f"Iteration {iteration:2d}: Allocated {allocated_mb:3d} MB "
                      f"(Estimated RSS: {estimated_memory/(1024*1024):.1f} MB)")
                
                iteration += 1
                time.sleep(2)
                
        except MemoryError:
            print("\n💥 MEMORY ERROR: Cannot allocate more memory!")
            print("The container should be restarted soon...")
            time.sleep(10)  # Wait to be killed
        except Exception as e:
            print(f"\n⚠️  Exception: {e}")
        
        print("Simulation ended")

if __name__ == "__main__":
    hog = MemoryHog()
    hog.run()
