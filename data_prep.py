import re
import pandas as pd

def data_prep(data_json):

    ### From JSON to DataFrame
    data_sizmek = pd.DataFrame()
    data_sizmek = pd.concat( [data_sizmek, pd.DataFrame(data_json["reportData"])] )
    
    ### Changing columns' names
    change_column_name = lambda c: re.sub("\(|\)","", re.sub(" |-","_",c.lower() ) )
    data_sizmek.columns = list(map(change_column_name, data_sizmek.columns))
    data_sizmek.rename(columns = {'day': 'date'}, inplace = True)

    sorted_columns = [
        'date',
        'campaign_id',
        'campaign_name',
        'placement_id',
        'placement_name',
        'placement_type',
        'placement_dimension',
        'ad_id',
        'ad_name',
        'section_id',
        'section_name',
        'site_id',
        'site_name',
        'target_audience_id',
        'target_audience_name',
        'impressions_net',
        'clicks_net',
        'total_conversions',
        'post_click_conversions',
        'post_impression_conversions',
        'global_onehub_configuration_complete_mx_post_click_conversions',
        'global_onehub_configuration_complete_mx_post_impression_conversions',
        'global_onehub_configuration_complete_mx_total_conversions',
        'global_onehub_configuration_start_mx_post_click_conversions',
        'global_onehub_configuration_start_mx_post_impression_conversions',
        'global_onehub_configuration_start_mx_total_conversions',
        'global_onehub_configuration_step_mx_post_click_conversions',
        'global_onehub_configuration_step_mx_post_impression_conversions',
        'global_onehub_configuration_step_mx_total_conversions',
        'global_onehub_lead_form_submission_mx_post_click_conversions',
        'global_onehub_lead_form_submission_mx_post_impression_conversions',
        'global_onehub_lead_form_submission_mx_total_conversions',
        'global_onehub_showroom_start_model_homepage_mx_post_click_conversions',
        'global_onehub_showroom_start_model_homepage_mx_post_impression_conversions',
        'global_onehub_showroom_start_model_homepage_mx_total_conversions',
        'global_onehub_site_visit_all_pages_mx_post_impression_conversions',
        'global_onehub_site_visit_all_pages_mx_total_conversions',
        'global_onehub_site_visit_session_mx_post_click_conversions',
        'global_onehub_site_visit_session_mx_post_impression_conversions',
        'global_onehub_site_visit_session_mx_total_conversions',
        'global_onehub_site_visit_all_pages_mx_post_click_conversions']
    
    ### Sorting columns and changin types
    data_sizmek = data_sizmek[sorted_columns]
    
    for column in data_sizmek.columns[15:]:
        data_sizmek[column] = data_sizmek[column].astype(int)
    
    data_sizmek = data_sizmek.convert_dtypes()

    return data_sizmek