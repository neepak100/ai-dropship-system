import time
import psutil

class SystemMetrics:
    def __init__(self):
        self.start_time = time.time()

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return memory.percent

    def get_uptime(self):
        return time.time() - self.start_time

    def display_metrics(self):
        print(f'CPU Usage: {self.get_cpu_usage()}%')
        print(f'Memory Usage: {self.get_memory_usage()}%')
        print(f'Uptime: {self.get_uptime()} seconds')

if __name__ == '__main__':
    metrics = SystemMetrics()
    while True:
        metrics.display_metrics()
        time.sleep(5)  # Adjust the sleep time as needed