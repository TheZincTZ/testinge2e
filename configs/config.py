# -*- coding: utf-8 -*-
# @Author: chenxinma
# @Date:   2018-10-01 16:42:42
# @Last Modified by:   Yuanyuan Shi, Meng Qi
# @Last Modified at:   2022-08-28 18:18:03


IDX = ['item_sku_id','sku_id','create_tm','complete_dt']

CAT_FEA = [
    'item_third_cate_cd','int_org_num'
    ]

VLT_FEA = [
    'uprc', 'contract_stk_prc',
    'wt', 'width', 'height', 'calc_volume', 'len',
    'vlt_count', 'vlt_sum', 'vlt_min', 'vlt_max', 'vlt_mean', 'vlt_std',
    'qtty_sum', 'qtty_min', 'qtty_max', 'qtty_mean', 'qtty_std',
    'amount_sum', 'amount_min', 'amount_max', 'amount_mean', 'amount_std',
    'vlt_count_6mo', 'vlt_sum_6mo', 'vlt_min_6mo', 'vlt_max_6mo',
    'vlt_mean_6mo', 'vlt_std_6mo',
    'vendor_vlt_count', 'vendor_vlt_sum', 'vendor_vlt_min', 'vendor_vlt_max',
    'vendor_vlt_mean', 'vendor_vlt_std',
    'vendor_vlt_count_6mo', 'vendor_vlt_sum_6mo', 'vendor_vlt_min_6mo',
    'vendor_vlt_max_6mo', 'vendor_vlt_mean_6mo', 'vendor_vlt_std_6mo',
    'vendor_qtty_sum', 'vendor_qtty_min', 'vendor_qtty_max',
    'vendor_qtty_mean', 'vendor_qtty_std', 'vendor_amount_sum',
    'vendor_amount_min', 'vendor_amount_max', 'vendor_amount_mean'
    ]

SF_FEA = [
    'q_7', 'q_14', 'q_28', 'q_56', 'q_140',
    'mean_3', 'mean_7', 'mean_14', 'mean_28', 'mean_56', 'mean_140',
    'diff_140_mean', 'mean_140_decay', 'median_140', 'min_140', 'max_140',
    'std_140',
    'diff_60_mean', 'mean_60_decay', 'median_60', 'min_60', 'max_60',
    'std_60',
    'diff_30_mean', 'mean_30_decay', 'median_30', 'min_30', 'max_30',
    'std_30',
    'diff_14_mean', 'mean_14_decay', 'median_14', 'min_14', 'max_14',
    'std_14',
    'diff_7_mean', 'mean_7_decay', 'median_7', 'min_7', 'max_7', 'std_7',
    'diff_3_mean', 'mean_3_decay', 'median_3', 'min_3', 'max_3', 'std_3',
    'has_sales_days_in_last_140', 'last_has_sales_day_in_last_140',
    'first_has_sales_day_in_last_140', 'has_sales_days_in_last_60',
    'last_has_sales_day_in_last_60', 'first_has_sales_day_in_last_60',
    'has_sales_days_in_last_30', 'last_has_sales_day_in_last_30',
    'first_has_sales_day_in_last_30', 'has_sales_days_in_last_14',
    'last_has_sales_day_in_last_14', 'first_has_sales_day_in_last_14',
    'has_sales_days_in_last_7', 'last_has_sales_day_in_last_7',
    'first_has_sales_day_in_last_7'
    ]
   
MORE_FEA =[
    'review_period',
    'normal',
    'gamma',
    'eq'
    ]

IS_FEA = [
    'initial_stock',
    ]
    
CAT_FEA_HOT = [
    'item_third_cate_cd_1591',
    'item_third_cate_cd_2677',
    'item_third_cate_cd_5022',
    'item_third_cate_cd_5024',
    'int_org_num_3',
    'int_org_num_4',
    'int_org_num_5',
    'int_org_num_6',
    'int_org_num_9',
    'int_org_num_10',
    'int_org_num_316',
    'int_org_num_772'
             ]

# TO_SCALE = [
#     DISGUISED FEATURE DETAILS
#             ]

SEQ2SEQ = ['Enc_X', 'Enc_y', 'Dec_X', 'Dec_y']


# LABEL = ['target_decision']    
LABEL = ['demand_RV_dp']    
LABEL_vlt = ['vlt_actual']    
LABEL_sf = ['label_sf']    

p1 = len(VLT_FEA) 
p2 = p1 + len(SF_FEA)
p3 = p2 + len(CAT_FEA_HOT)
p4 = p3 + len(MORE_FEA)
p5 = p4 + len(IS_FEA)
p6 = p5 + 1
p7 = p6 + 1
p8 = p7 + 1


SCALE_FEA =  VLT_FEA + SF_FEA + CAT_FEA_HOT + MORE_FEA + IS_FEA  + LABEL_vlt + LABEL_sf
CUT_FEA = VLT_FEA + SF_FEA + MORE_FEA
MODEL_FEA = VLT_FEA + SF_FEA + MORE_FEA + IS_FEA + CAT_FEA_HOT


#Disguised rnn parameters
rnn_hidden_len = 120 #Possible values: 5~200
rnn_cxt_len = 5  #Possible values: 1~10
rnn_pred_long = 60 #Possible values: 7~60
rnn_hist_long = 180 #Possible values: 30~180
rnn_total_long = rnn_pred_long + rnn_hist_long
rnn_input_dim = 2 #Possible value: 2
quantiles = [0.1, 0.6, 0.7, 0.8, 0.9, 0.95] # Example: [0.1, 0.3, 0.5, 0.7, 0.9]
num_quantiles = len(quantiles)