import platform
import socket
import psutil
import json
import os
import psycopg2

from datetime import datetime

#DATABASE_HOST = db; db is the PostgreSQL Compose service name.
def get_database_connection():
    return psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )


def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    cpu_status = get_status(cpu_usage)
    memory_status = get_status(memory_usage)
    disk_status = get_status(disk_usage)

    overall_status = get_overall_status([
        cpu_status,
        memory_status,
        disk_status
        ])
    
    return {
        "hostname": socket.gethostname(),

        "operating_system": platform.system(),
        "os_version": platform.version(),

        "cpu_usage": cpu_usage,
        "cpu_status": cpu_status,   

        "memory_usage": memory_usage,
        "memory_status": memory_status,

        "disk_usage": disk_usage,
        "disk_status": disk_status,

        "overall_status": overall_status,
    
        "timestamp": datetime.now().isoformat()
    }


def get_status(value):
    if value >= 90:
        return "CRITICAL"
    elif value >= 70:
        return "WARNING"
    else:
        return "OK"


def get_overall_status(statuses):
    if "CRITICAL" in statuses:
        return "CRITICAL"
    elif "WARNING" in statuses:
        return "WARNING"
    else:
        return "HEALTHY"


def display_system_info(info):
    print("\n===== SYSTEM MONITOR =====")
    print(f"Hostname:                 {info['hostname']}")
    print(f"Operating System:         {info['operating_system']}")
    print(f"Operating System Version: {info['os_version']}")

    print(f"CPU Usage:                {info['cpu_usage']}% [{info['cpu_status']}]")
    print(f"Memory Usage:             {info['memory_usage']}% [{info['memory_status']}]")
    print(f"Disk Usage:               {info['disk_usage']}% [{info['disk_status']}]")

    print(f"Overall Status:           {info['overall_status']}")

    print(f"Timestamp:                {info['timestamp']}")
    print("===== CHECK COMPLETED =====")


def display_json(info):
    print("\n=====JSON OUTPUT=====")
    print(json.dumps(info, indent=4))
    print("=====JSON OUTPUT COMPLETED=====")



if __name__ == "__main__":
    system_info = get_system_info()

    display_system_info(system_info)
    display_json(system_info)

