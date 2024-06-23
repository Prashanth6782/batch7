import psutil
import socket
import time

# Define the CPU usage threshold
CPU_USAGE_THRESHOLD = 2

def get_ip_address():
    """Get the IP address of the local machine."""
    try:
        # Get the hostname of the machine
        hostname = socket.gethostname()
        # Get the IP address using the hostname
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Unable to get IP address: {e}"

def monitor_cpu_usage():
    print("Monitoring CPU usage...")
    
    # Print the IP address of the local machine
    ip_address = get_ip_address()
    print(f"IP address of the system being monitored: {ip_address}")
    
    try:
        while True:
            # Get the current CPU usage as a percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > CPU_USAGE_THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)  # Wait for a second before checking again
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu_usage()
