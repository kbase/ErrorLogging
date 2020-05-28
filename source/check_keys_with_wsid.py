
def check_keys_with_wsid(errored, errlog_dictionary):
    wsid = errored['wsid']
    if wsid == -1:
        wsid = 'unknown'
    errlog_dictionary['workspace_id'] = wsid
    if 'job_input' in errored.keys():
        # Get app_id
        app_id = (errored['job_input']['method'].split('.'))[-1]
        errlog_dictionary['app_id'] = app_id
        if 'params' in errored['job_input'].keys():
            errlog_dictionary['obj_references'] = errored['job_input']['params']
        if 'job_output' in errored.keys() and errored['job_output']:
            try:
                errlog_dictionary['error'] = errored['job_output']['error']['message']
            except KeyError:
                errlog_dictionary['error'] = errored['msg']
            errlog_dictionary['traceback'] = errored['job_output']['error']['error']
            errlog_dictionary['name_of_error'] = errored['job_output']['error']['name']
            errlog_dictionary['error_code'] = errored['job_output']['error']['code']
        elif 'error' in errored.keys():
            errlog_dictionary['error'] = errored['error']['message']
            errlog_dictionary['traceback'] = errored['error']['error']
            errlog_dictionary['name_of_error'] = errored['error']['name']
            errlog_dictionary['error_code'] = errored['error']['code']
        elif 'errormsg' in errored.keys():
            errlog_dictionary['error'] = errored['errormsg']
            errlog_dictionary['error_code'] = errored['error_code']
    return errlog_dictionary
