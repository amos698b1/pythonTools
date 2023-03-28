select 'act_ru_task' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_act_ru_task where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_act_ru_task where dt = '2023-03-26') f 

union
select 'act_ru_variable' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_act_ru_variable where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_act_ru_variable where dt = '2023-03-26') f 


union
select 'own_hi_delegate_config' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_hi_delegate_config where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_hi_delegate_config where dt = '2023-03-26') f 

union
select 'own_hi_process' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_ods.activiti_pro_own_hi_process where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_hi_process where dt = '2023-03-26') f 

union
select 'own_hi_process_final' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_ods.activiti_pro_own_hi_process_final where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_hi_process_final where dt = '2023-03-26') f 

union
select 'own_hi_task' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_hi_task where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_hi_task where dt = '2023-03-26') f 

union
select 'own_hi_task_final' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_hi_task_final where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_hi_task_final where dt = '2023-03-26') f 

union
select 'own_interface_log' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_interface_log where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_interface_log where dt = '2023-03-26') f 

union
select 'own_layoff_user' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_layoff_user where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_layoff_user where dt = '2023-03-26') f 

union
select 'own_model_status' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_model_status where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_model_status where dt = '2023-03-26') f 

union
select 'own_pro_model' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_pro_model where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_pro_model where dt = '2023-03-26') f 

union
select 'own_re_procdef' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_ods.activiti_pro_own_re_procdef where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_re_procdef where dt = '2023-03-26') f 

union
select 'own_ru_delegate_config' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_ru_delegate_config where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_ru_delegate_config where dt = '2023-03-26') f 

union
select 'own_ru_process' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_ods.activiti_pro_own_ru_process where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_ru_process where dt = '2023-03-26') f 

union
select 'own_ru_task' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_ods.activiti_pro_own_ru_task where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_ru_task where dt = '2023-03-26') f 

union
select 'own_task_property' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_task_property where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_task_property where dt = '2023-03-26') f 

union
select 'own_tenant' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_tenant where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_tenant where dt = '2023-03-26') f 

union
select 'own_user' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_own_user where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_own_user where dt = '2023-03-26') f 

union
select 'qrtz_cron_triggers' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_qrtz_cron_triggers where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_qrtz_cron_triggers where dt = '2023-03-26') f 

union
select 'qrtz_job_details' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_qrtz_job_details where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_qrtz_job_details where dt = '2023-03-26') f 

union
select 'qrtz_locks' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_qrtz_locks where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_qrtz_locks where dt = '2023-03-26') f 

union
select 'qrtz_scheduler_state' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_qrtz_scheduler_state where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_qrtz_scheduler_state where dt = '2023-03-26') f 

union
select 'qrtz_triggers' as tableName, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_qrtz_triggers where dt = '2023-03-26' 
union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_qrtz_triggers where dt = '2023-03-26') f 

union
