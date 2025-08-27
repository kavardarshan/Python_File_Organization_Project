import os, platform, subprocess, datetime

# current time
now = datetime.datetime.now()

if platform.system() == "Windows":
    cpu_out = subprocess.check_output(["wmic", "cpu", "get", "loadpercentage"]).decode().split()
    cpu = cpu_out[1] if len(cpu_out) > 1 else "0"

    # get memory info
    mem_out = subprocess.check_output([
        "wmic", "OS", "get", "FreePhysicalMemory,TotalVisibleMemorySize", "/Value"
    ]).decode().split()
    free_mem = int([x.split('=')[1] for x in mem_out if x.startswith("FreePhysicalMemory")][0])
    total_mem = int([x.split('=')[1] for x in mem_out if x.startswith("TotalVisibleMemorySize")][0])
    mem = round((1 - free_mem / total_mem) * 100, 2)

else:
    cpu_line = subprocess.getoutput("top -bn1 | grep 'Cpu(s)'")
    cpu = cpu_line.split('%')[0].split()[-1]

    mem_line = subprocess.getoutput("free -m | grep Mem").split()
    mem = round(int(mem_line[2]) / int(mem_line[1]) * 100, 2)

# save to file
with open("system_log.txt", "a") as f:
    f.write(f"{now} - CPU: {cpu}% | Memory: {mem}%\n")
