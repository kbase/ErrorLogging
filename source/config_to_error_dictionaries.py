import configparser
config = configparser.ConfigParser()

def config_to_dictionary():
    config.read('Errors.ini')
    error_dictionary = {}
    key_list = config.sections()
    for section in key_list:
        errors = list(dict(config.items(section)).values())
        app_dictionary = {section: errors}
        error_dictionary.update(app_dictionary)
    return error_dictionary
