import json


def check_keys_with_wsid(errored, errlog_dictionary):
    """check_keys_with_wsid is a function that diligently checks the structure and key present in the errorlog coming from EE2.
    This function is made to accommodate many different structures of errored app logs coming from EE2 with many different key patterns.
    If an EE2 error log has a workspace id that's the first pass, ideally the log should also have a 'job_input' key, a 'job_output' key or
    an 'error' or 'errormsg' key. There is no standard for error logs coming from EE2 sometimes error messages have the key 'error',
    sometimes they have the key 'errormsg', and sometimes they have the key 'job_output'.
    We must account for all structures and sub structures."""
    # First take the workspace ID
    wsid = errored['wsid']
    # Sometimes wsid's can be -1, EE2 symbol for an unknown
    if wsid == -1:
        wsid = 'unknown'
    # If wsid not unknown add it to our error dictionary
    errlog_dictionary['workspace_id'] = wsid
    # Check if job input key is present in 'errored'. Here 'errored' is the big json error log coming from EE2
    if 'job_input' in errored.keys():
        # Getuseful keys from job input
        if 'params' in errored['job_input'].keys():
            errlog_dictionary['obj_references'] = json.dumps(errored['job_input']['params'], sort_keys=True, indent=4)[0:199]
        # If a EE2 log as a 'job_output' key then that key leads to a nested dictionary that contains the error msg info
        if 'job_output' in errored.keys() and errored['job_output']:
            # the key 'error' in the job_output dictionary can sometimes lead to a dictionary itself
            # In which case error key leads to another nested dictionary -> 'error':{}
            # This sub-sub dictionary contains a key 'message' which holds the error msg value
            try:
                errlog_dictionary['error'] = errored['job_output']['error']['message']
            # If the 'error' key does not lead to another nested dictionary than the 'job_output' only contains a 'msg' key with the error msg
            except KeyError:
                errlog_dictionary['error'] = errored['msg']
            # Pull traceback key, error code key and name_of_error key (not as helpful a key as one might think: name of error key is
            # just 'job error' or 1 sometimes) from EE2.
            errlog_dictionary['traceback'] = errored['job_output']['error']['error']
            errlog_dictionary['name_of_error'] = errored['job_output']['error']['name']
            errlog_dictionary['error_code'] = errored['job_output']['error']['code']
        # If 'job_output' key is not present in EE2 log then there is a key 'error' that leads to a nested dictionary with error information
        elif 'error' in errored.keys():
            if 'message' in errored["error"]:
                errlog_dictionary['error'] = errored['error']['message']
                errlog_dictionary['traceback'] = errored['error']['error']
                errlog_dictionary['name_of_error'] = errored['error']['name']
                errlog_dictionary['error_code'] = errored['error']['code']
            else:
                errlog_dictionary['error'] = "unknown no [error][message]"
                errlog_dictionary['traceback'] = "unknown no [error][error]"
                errlog_dictionary['name_of_error'] = "unknown no [error][name_of_error]"
                errlog_dictionary['error_code'] = "unknown no [error][error_code]"
        # Else if there is no 'error' key leading to a nested dict, or 'job_output' leading to a nested dict, then the error info is simple under 'error_msg'.
        elif 'errormsg' in errored.keys():
            errlog_dictionary['error'] = errored['errormsg']
            errlog_dictionary['error_code'] = errored['error_code']
    return errlog_dictionary
