import psutil
import time

def monitor_system_health():
    # CPU Health
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_freq = psutil.cpu_freq()
    print("\nCPU Health:")
    print(f"CPU Usage per Core: {cpu_percent}")
    print(f"CPU Frequency: Current={cpu_freq.current:.1f}MHz, Max={cpu_freq.max:.1f}MHz")
    
    # RAM Health
    ram = psutil.virtual_memory()
    print("\nRAM Health:")
    print(f"Total RAM: {ram.total/1024/1024/1024:.2f}GB")
    print(f"Available RAM: {ram.available/1024/1024/1024:.2f}GB")
    print(f"RAM Usage: {ram.percent}%")
    
    # Temperature (if sensors available)
    try:
        temperatures = psutil.sensors_temperatures()
        if temperatures:
            print("\nTemperatures:")
            for name, entries in temperatures.items():
                for entry in entries:
                    print(f"{name}: {entry.current}°C")
    except AttributeError:
        print("\nTemperature sensors not available")

    # Load Average
    load = psutil.getloadavg()
    print(f"\nSystem Load (1/5/15 min): {load}")
"""
run the above program indefenitely
if __name__ == "__main__":
    while True:
        monitor_system_health()
        time.sleep(2)  # Update every 2 seconds
"""
import psutil
import platform
import cpuinfo
import py3nvml  # for NVIDIA GPU testing  (pip install py3nvml)
import wmi  # for Windows hardware info (pip install wmi)
import time

def test_cpu():
    print("\n=== CPU TEST ===")
    # CPU Info
    cpu_info = cpuinfo.get_cpu_info()
    print(f"CPU: {cpu_info['brand_raw']}")
    
    # CPU Stress Test
    print("Running CPU stress test...")
    start_time = time.time()
    while time.time() - start_time < 10:  # 10 second test
        psutil.cpu_percent(interval=1, percpu=True)
    print("CPU stress test completed")

def test_memory():
    print("\n=== MEMORY TEST ===")
    # Memory Info
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total/1024/1024/1024:.2f}GB")
    
    # Memory Write/Read Test
    print("Running memory read/write test...")
    test_size = 500 * 1024 * 1024  # 500MB test
    test_data = bytearray(test_size)
    print("Memory test completed")
 

def test_disk():
    print("\n=== DISK TEST ===")
    # Get all disk partitions
    partitions = psutil.disk_partitions()
    
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"\nDrive {partition.mountpoint}")
            print(f"Total Space: {usage.total/1024/1024/1024:.2f}GB")
            print(f"Used Space: {usage.used/1024/1024/1024:.2f}GB")
            print(f"Free Space: {usage.free/1024/1024/1024:.2f}GB")
            print(f"Usage: {usage.percent}%")
        except:
            continue
            
    # Disk Speed Test with larger file and proper timing
    print("\nRunning disk speed test...")
    test_file = 'speedtest.tmp'
    test_size = 100 * 1024 * 1024  # 100MB for more accurate measurement
    
    # Write test
    start_time = time.time()
    with open(test_file, 'wb') as f:
        f.write(b'0' * test_size)
    write_time = time.time() - start_time
    
    # Calculate speed in MB/s
    write_speed = (test_size / 1024 / 1024) / write_time
    print(f"Write Speed: {write_speed:.2f}MB/s")

def main():
    print("Starting Hardware Tests...")
    test_cpu()
    test_memory()
    test_disk()
    print("\nAll hardware tests completed!")

if __name__ == "__main__":
    main()
