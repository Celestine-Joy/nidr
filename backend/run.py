import time

start_time = time.time()  # save start time



import subprocess

backend_folder = 'backend/'
files = 'files/'

# List of files to run in order
scripts = ["scan.py", "cal.py", "conv.py", "pmlanalyzer.py"]

# Run each file in order
for script in scripts:
    subprocess.run(["python", backend_folder+script])
    end_time = time.time()  # save end time
    elapsed_time = end_time - start_time  # calculate elapsed time
    print(f"{script} method Elapsed time: {elapsed_time} seconds")




# your code here

end_time = time.time()  # save end time
elapsed_time = end_time - start_time  # calculate elapsed time

print(f"Rund method Elapsed time: {elapsed_time} seconds")