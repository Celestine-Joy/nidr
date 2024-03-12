import pandas as pd
import pickle
import os

files='files/'
backend='backend/'

import time

start_time = time.time()  # save start time

# Directory where the models are stored
models_dir = 'models'

# Dictionary to store the models
models = {}

# Load all models
for filename in os.listdir(backend+models_dir):
    if filename.endswith('.pkl'):
        with open(os.path.join(backend+models_dir, filename), 'rb') as file:
            # The model name will be the filename without the extension
            model_name = filename[:-4]
            models[model_name] = pickle.load(file)

def getfeaturename(df):
    names = df.columns.tolist()
    return names

# Read the CSV file into a DataFrame
df = pd.read_csv(files+'final.csv')
def preprocess(df):
    # Select specific columns from the DataFrame
    df = df.loc[:,['Total_Fwd_Packets',
 'Total_Backward_Packets',
 'Total_Length_of_Fwd_Packets',
 'Total_Length_of_Bwd_Packets',
 'Fwd_Packet_Length_Max',
 'Fwd_Packet_Length_Min',
 'Fwd_Packet_Length_Mean',
 'Fwd_Packet_Length_Std',
 'Bwd_Packet_Length_Max',
 'Bwd_Packet_Length_Min',
 'Bwd_Packet_Length_Mean',
 'Bwd_Packet_Length_Std',
 'Flow_IAT_Mean',
 'Flow_IAT_Std',
 'Flow_IAT_Max',
 'Flow_IAT_Min',
 'Fwd_IAT_Total',
 'Fwd_IAT_Mean',
 'Fwd_IAT_Std',
 'Fwd_IAT_Max',
 'Fwd_IAT_Min',
 'Bwd_IAT_Total',
 'Bwd_IAT_Mean',
 'Bwd_IAT_Std',
 'Bwd_IAT_Max',
 'Bwd_IAT_Min',
 'Fwd_Header_Length',
 'Bwd_Header_Length',
 'Fwd_Packets_s',
 'Bwd_Packets_s',
 'Min_Packet_Length',
 'Max_Packet_Length',
 'Packet_Length_Mean',
 'Packet_Length_Std',
 'Packet_Length_Variance',
 'Average_Packet_Size',
 'Fwd_Avg_Bytes_Bulk',
 'Fwd_Avg_Packets_Bulk',
 'Fwd_Avg_Bulk_Rate',
 'Bwd_Avg_Bytes_Bulk',
 'Bwd_Avg_Packets_Bulk',
 'Bwd_Avg_Bulk_Rate',
 'Subflow_Fwd_Packets',
 'Subflow_Fwd_Bytes',
 'Subflow_Bwd_Packets',
 'Subflow_Bwd_Bytes',
 'Active_Mean',
 'Active_Std',
 'Active_Max',
 'Active_Min',
 'Idle_Mean',
 'Idle_Std',
 'Idle_Max',
 'Idle_Min']]
    return df
count=0            
pos=0
zero=0

found_ips_df = pd.DataFrame(columns=['Source IP', 'Destination IP'])

def runml(df,count,pos,zero):
    found_ips_df = pd.DataFrame(columns=['Source IP', 'Destination IP'])
    for i in range(len(df2)):
        row=df2.iloc[i]
        combined = list(zip(fname, row))
        combined_dict = dict(combined)
        df_combined = pd.DataFrame(combined_dict, index=[0])
        for model_name, model in models.items():
            count=1+count
            predictions = model.predict(df_combined)
            if predictions == 1:
                #print(f"found :{pos}")
                #print(f" found :{pos}, Detection made by model: {model_name}")
                #print(df.loc[i, ['Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Protocol']])
                pos=1+pos
                #print("found")
                found_ips_df = pd.concat([found_ips_df, df.loc[i, ['Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Protocol']].to_frame().T])
                break  # Stop checking other models if a detection is made
            else:
                zero=1+zero
            
    return count,pos,zero,found_ips_df

df2 = preprocess(df)
fname=getfeaturename(df2)
df2.columns = fname
df2 = df2[fname]  # Set the order of feature names for df2
count,pos,zero,found_ips_df=runml(df,count,pos,zero)
found_ips_df.to_csv(files+'found_ips.csv', index=False)
attack_source_df = found_ips_df.drop_duplicates(subset=['Source IP'])
if os.path.isfile(files+'attack_source.csv') and os.path.getsize(files+'attack_source.csv') > 0:
    existing_attack_source_df = pd.read_csv(files+'attack_source.csv')
    attack_source_df = pd.concat([existing_attack_source_df, attack_source_df])
    attack_source_df = attack_source_df.drop_duplicates(subset=['Source IP'])
    attack_source_df[['Source IP']].to_csv(files+'attack_source.csv', mode='w', index=False)
else:
    attack_source_df[['Source IP']].to_csv(files+'attack_source.csv', index=False)

df.head()
print("count",count,"pos:",pos,"zero:",zero)

# your code here

end_time = time.time()  # save end time
elapsed_time = end_time - start_time  # calculate elapsed time

print(f"Elapsed time: {elapsed_time} seconds")