import pandas as pd

files='files/'
# Read the input CSV file
df = pd.read_csv(files+'output.csv')

# Rename the columns
df.rename(columns={
    'src_ip': 'Source IP',
    'dst_ip': 'Destination IP',
    'src_port': 'Source Port',
    'dst_port': 'Destination Port',
    'protocol': 'Protocol',
    'fwd_pkts_s': 'Fwd_Packets_s',
    'bwd_pkts_s': 'Bwd_Packets_s',
    'tot_fwd_pkts': 'Total_Fwd_Packets',
    'tot_bwd_pkts': 'Total_Backward_Packets',
    'totlen_fwd_pkts': 'Total_Length_of_Fwd_Packets',
    'totlen_bwd_pkts': 'Total_Length_of_Bwd_Packets',
    'fwd_pkt_len_max': 'Fwd_Packet_Length_Max',
    'fwd_pkt_len_min': 'Fwd_Packet_Length_Min',
    'fwd_pkt_len_mean': 'Fwd_Packet_Length_Mean',
    'fwd_pkt_len_std': 'Fwd_Packet_Length_Std',
    'bwd_pkt_len_max': 'Bwd_Packet_Length_Max',
    'bwd_pkt_len_min': 'Bwd_Packet_Length_Min',
    'bwd_pkt_len_mean': 'Bwd_Packet_Length_Mean',
    'bwd_pkt_len_std': 'Bwd_Packet_Length_Std',
    'pkt_len_max': 'Max_Packet_Length',
    'pkt_len_min': 'Min_Packet_Length',
    'pkt_len_mean': 'Packet_Length_Mean',
    'pkt_len_std': 'Packet_Length_Std',
    'pkt_len_var': 'Packet_Length_Variance',
    'fwd_header_len': 'Fwd_Header_Length',
    'bwd_header_len': 'Bwd_Header_Length',
    'flow_iat_mean': 'Flow_IAT_Mean',
    'flow_iat_max': 'Flow_IAT_Max',
    'flow_iat_min': 'Flow_IAT_Min',
    'flow_iat_std': 'Flow_IAT_Std',
    'fwd_iat_tot': 'Fwd_IAT_Total',
    'fwd_iat_max': 'Fwd_IAT_Max',
    'fwd_iat_min': 'Fwd_IAT_Min',
    'fwd_iat_mean': 'Fwd_IAT_Mean',
    'fwd_iat_std': 'Fwd_IAT_Std',
    'bwd_iat_tot': 'Bwd_IAT_Total',
    'bwd_iat_max': 'Bwd_IAT_Max',
    'bwd_iat_min': 'Bwd_IAT_Min',
    'bwd_iat_mean': 'Bwd_IAT_Mean',
    'bwd_iat_std': 'Bwd_IAT_Std',
    'pkt_size_avg': 'Average_Packet_Size',
    'active_max': 'Active_Max',
    'active_min': 'Active_Min',
    'active_mean': 'Active_Mean',
    'active_std': 'Active_Std',
    'idle_max': 'Idle_Max',
    'idle_min': 'Idle_Min',
    'idle_mean': 'Idle_Mean',
    'idle_std': 'Idle_Std',
    'fwd_byts_b_avg': 'Fwd_Avg_Bytes_Bulk',
    'fwd_pkts_b_avg': 'Fwd_Avg_Packets_Bulk',
    'bwd_byts_b_avg': 'Bwd_Avg_Bytes_Bulk',
    'bwd_pkts_b_avg': 'Bwd_Avg_Packets_Bulk',
    'fwd_blk_rate_avg': 'Fwd_Avg_Bulk_Rate',
    'bwd_blk_rate_avg': 'Bwd_Avg_Bulk_Rate',
    'subflow_fwd_pkts': 'Subflow_Fwd_Packets',
    'subflow_bwd_pkts': 'Subflow_Bwd_Packets',
    'subflow_fwd_byts': 'Subflow_Fwd_Bytes',
    'subflow_bwd_byts': 'Subflow_Bwd_Bytes'
}, inplace=True)

# Keep only the columns mentioned above
df = df[[
    'Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Protocol',
    'Fwd_Packets_s', 'Bwd_Packets_s', 'Total_Fwd_Packets', 'Total_Backward_Packets',
    'Total_Length_of_Fwd_Packets', 'Total_Length_of_Bwd_Packets', 'Fwd_Packet_Length_Max',
    'Fwd_Packet_Length_Min', 'Fwd_Packet_Length_Mean', 'Fwd_Packet_Length_Std',
    'Bwd_Packet_Length_Max', 'Bwd_Packet_Length_Min', 'Bwd_Packet_Length_Mean',
    'Bwd_Packet_Length_Std', 'Max_Packet_Length', 'Min_Packet_Length', 'Packet_Length_Mean',
    'Packet_Length_Std', 'Packet_Length_Variance', 'Fwd_Header_Length', 'Bwd_Header_Length',
    'Flow_IAT_Mean', 'Flow_IAT_Max', 'Flow_IAT_Min', 'Flow_IAT_Std', 'Fwd_IAT_Total',
    'Fwd_IAT_Max', 'Fwd_IAT_Min', 'Fwd_IAT_Mean', 'Fwd_IAT_Std', 'Bwd_IAT_Total',
    'Bwd_IAT_Max', 'Bwd_IAT_Min', 'Bwd_IAT_Mean', 'Bwd_IAT_Std', 'Average_Packet_Size',
    'Active_Max', 'Active_Min', 'Active_Mean', 'Active_Std', 'Idle_Max', 'Idle_Min',
    'Idle_Mean', 'Idle_Std', 'Fwd_Avg_Bytes_Bulk', 'Fwd_Avg_Packets_Bulk', 'Bwd_Avg_Bytes_Bulk',
    'Bwd_Avg_Packets_Bulk', 'Fwd_Avg_Bulk_Rate', 'Bwd_Avg_Bulk_Rate', 'Subflow_Fwd_Packets',
    'Subflow_Bwd_Packets', 'Subflow_Fwd_Bytes', 'Subflow_Bwd_Bytes'
]]

# Save the DataFrame back to the CSV file
df.to_csv(files+'final.csv', index=False)