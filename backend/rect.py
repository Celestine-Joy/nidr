import os
import pandas as pd
import subprocess
files='files/'
backend='backend/'
models='/backend/models/'

def rectify(attack_source_path = files+'attack_source.csv'):
    try:
        if os.path.exists(attack_source_path):
            attack_source_df = pd.read_csv(attack_source_path)
            attack_ips = attack_source_df['Source IP'].unique()

            for ip in attack_ips:
                subprocess.run(['iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
        else:
            print("File does not exist.")
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: Empty data in the CSV file.")
    except subprocess.CalledProcessError:
        print("Error: Failed to run the iptables command.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def restore(attack_source_path = files+'attack_source.csv'):
    try:
        if os.path.exists(attack_source_path):
            attack_source_df = pd.read_csv(attack_source_path)
            attack_ips = attack_source_df['Source IP'].unique()

            for ip in attack_ips:
                subprocess.run(['iptables', '-I', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
        else:
            print("File does not exist.")
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: Empty data in the CSV file.")
    except subprocess.CalledProcessError:
        print("Error: Failed to run the iptables command.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        try:
                if os.path.exists(attack_source_path):
                    open(attack_source_path, 'w').close()
                    print("CSV file emptied successfully.")
                else:
                    print("File does not exist.")
        except Exception as e:
                print(f"An error occurred: {str(e)}")
