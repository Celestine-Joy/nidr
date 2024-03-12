import os
def run():
    print("run.py started")

    backend_folder = 'backend/'
    run_script_path = os.path.join(backend_folder,'run.py')
    for i in range(10):
        exec(open(run_script_path).read())
