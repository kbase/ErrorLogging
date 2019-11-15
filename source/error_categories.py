
def add_category(app_log):
    category = None
    if category is None:

        if app_log.get('status').find('BadStatusLine') > 0:
            category = 'BadStatusLine'
        elif app_log.get('status').find('ReadTimeout') >= 0:
            category = 'BadServer'
        elif app_log.get('status').find('Bad Gateway') > 0:
            category = 'BadServer'
        elif app_log.get('status').find('Server closed connection') > 0:
            category = '500'
        elif app_log.get('status').find('NJSW failed') > 0:
            category = 'BadServer'
        elif app_log.get('status').find('No such container') >= 0:
            category = 'NoSuchContainer'
        elif app_log.get('status').find('No such file or directory') >= 0:
            category = 'NoSuchFileDir'
        elif app_log.get('status').find('compression type 9') >= 0:
            category = 'Compression'
        elif app_log.get('status').find('Output file is not found') >= 0:
            category = 'NoOutput'
        elif app_log.get('status').find('Illegal character in object name') >= 0:
            category = 'BadName'
        elif app_log.get('status').find('does not have reference to the assembly object') >= 0:
            category = 'NoAssemblyRef'
        elif app_log.get('status').find('Job service side error') >= 0:
            category = 'JobService'
        elif app_log.get('status').find('Connection has been shutdown') >= 0:
            category = 'LostConnection'

        # App-specific errors
        elif app_log.get('status').find('call_features_rRNA_SEED') >= 0:
            category = 'RAST_rRNA'
        elif app_log.get('status').find('Model likely contains numerical instability') >= 0:
            category = 'fbaTimeOut'

        # User Errors
        elif app_log.get('status').find(' is not a FASTQ file') > 0:
            category = 'appFASTQ'
        elif app_log.get('status').find('Reading FASTQ record failed') >= 0:
            category = 'appFASTQ'
        elif app_log.get('status').find('Invalid FASTQ') >= 0:
            category = 'appFASTQ'
        elif app_log.get('status').find('This FASTA file has non nucleic acid characters') >= 0:
            category = 'appFASTA'
        elif app_log.get('status').find('This FASTA file has non nucleic acid characters') >= 0 or app_log.get('status').find(
                'This FASTA file may have amino acids') >= 0:
            category = 'appFASTA'
        elif app_log.get('status').find('FASTA header') >= 0 and app_log.get('status').find(
                'appears more than once in the file') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('Must select at least two models to compare') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('There are no contigs to save') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('This genome does not contain features') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('You must supply at least one') > 0 or app_log.get('status').find('too many contigs') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('Not one protein family member') >= 0:
            category = 'User Error'
        elif app_log.get('status').find(' is used for forward') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('Both SRA and FASTQ/FASTA file given. Please provide one file type only') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('not a valid EXCEL nor TSV file') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('reads files do not have an equal number of records') > 0:
            category = 'User Error'
        elif app_log.get('status').find('duplicate genome display names') > 0:
            category = 'User Error'
        elif app_log.get('status').find('You must run the RAST SEED Annotation App') > 0:
            category = 'User Error'
        elif app_log.get('status').find('Proteome comparison does not involve genome') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('incompatible read library types') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('File is not a zip file') > 0:
            category = 'User Error'
        elif app_log.get('status').find('MISSING DOMAIN ANNOTATION FOR') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('genomes have no matching Domain Annotation') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('Too many contigs') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('But missing SRA file') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('Every feature sequence id must match a fasta sequence id') >= 0:
            category = 'User Error'
        elif app_log.get('status').find(' not found in pangenome') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('assembly method was not specified as metagenomic') >= 0:
            category = 'User Error'
        elif app_log.get('status').find('following extensions') > 0:
            category = 'Bad Extension'
        elif app_log.get('status').find('input_one_sequence') >= 0 and app_log.get('status').find('input_one_ref') >= 0:
            category = 'appBLASTError'
        elif app_log.get('status').find('input_one_sequence') >= 0 and app_log.get('status').find('output_one_name') >= 0:
            category = 'appBLASTError'
        elif app_log.get('status').find('blast') >= 0 and app_log.get('status').find('Query is Empty') >= 0:
            category = 'appBLASTError'
        else:
            category = "Undefined"

    return category
