import os
def run():
    print("run.py started")
    count=0
    backend_folder = 'backend/'
    run_script_path = os.path.join(backend_folder,'run.py')
    while True:
        exec(open(run_script_path).read())
        count+=1
        if count==50:
            count=0
            with open('final.csv', 'w') as file:
                file.truncate(0)
