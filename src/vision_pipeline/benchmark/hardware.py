import platform
import subprocess
import psutil

def get_cpu_name():
    """
    Return the CPU model name.

    Tries multiple methods because platform.processor()
    frequently returns an empty string on Linux.
    """

    # Linux: lscpu
    try:
        output = subprocess.check_output(
            ["lscpu"],
            text=True,
        )

        for line in output.splitlines():
            if line.startswith("Model name:"):
                return line.split(":", 1)[1].strip()

    except Exception:
        pass

    # Linux fallback: /proc/cpuinfo
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("model name"):
                    return line.split(":", 1)[1].strip()

    except Exception:
        pass

    # Generic fallback
    return platform.processor() or "Unknown CPU"

def get_gpu_name():
    """
    Return the GPU model name.

    Tries to detect NVIDIA GPUs using nvidia-smi.
    If not found, returns "not detected".
    """
    try:
        gpu = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            text=True
            ).strip()
    except Exception:
        gpu = "not detected"

    return gpu

def get_total_ram():
    """
    Return the total RAM size in GB.

    Uses psutil to get the total physical memory.
    """
    return round(psutil.virtual_memory().total / (1024**3), 2)