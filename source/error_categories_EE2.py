
def add_category(app_log):
    category = None
    if category is None:
        error = app_log.get('error')
        if error.find('500 Server closed connection') > 0:
            category = '500'
        elif error.find('exit code is 123') >= 0 or error.find(
                'No space left on device') >= 0:
            category = 'NoSpace'
        elif error.find('exit code is 137') >= 0:
            category = 'Exit 137'
        elif error.find('BaderrorLine') >= 0:
            category = 'BaderrorLine'
        elif error.find('Bad Gateway') >= 0:
            category = 'BadServer'
        elif error.find('NJSW failed') >= 0:
            category = 'BadServer'
        elif error.find('compression type 9') >= 0:
            category = 'Compression'
        elif error.find('Job service side error') >= 0:
            category = 'JobService'
        elif error.find('Kafka') >= 0:
            category = 'JobService'
        elif error.find('Connection has been shutdown') >= 0:
            category = 'LostConnection'
        elif error.find('ProtocolError(Connection aborted') >= 0:
            category = 'LostConnection'
        elif error.find('No such container') >= 0:
            category = 'NoSuchContainer'
        elif error.find('Output file is not found') >= 0:
            category = 'NoOutput'
        elif error.find('does not have reference to the assembly object') >= 0:
            category = 'NoAssemblyRef'
        elif error.find('ReadTimeoutError') >= 0:
            category = 'ReadTimeout'
        elif error.find('504 Gateway Time-out') >= 0:
            category = 'ReadTimeout'
        elif error.find('Job was cancelled') >= 0 or error.find(
                'job was canceled') >= 0 or error.find('ob was Canceled') >= 0:
            category = 'Canceled'

        # App-specific errors
        elif error.find('call_features_rRNA_SEED') >= 0:
            category = 'App Error'
        elif error.find('Model likely contains numerical instability') >= 0:
            category = 'App Error'
        elif error.find('Object doesnt have required fields') >= 0:
            category = 'App Error'
        elif error.find('has invalid provenance reference') >= 0:
            category = 'App Error'
        elif error.find('Mandatory arguments missing') >= 0:
            category = 'App Error'
        elif error.find('Authentication required for AbstractHandle') >= 0:
            category = 'App Error'
        elif error.find("Can't locate object method quality via package") >= 0:
            category = 'App Error'
        elif error.find("Can't use an undefined value as an ARRAY reference") >= 0:
            category = 'App Error'
        elif error.find('KBaseReport parameter validation errors') >= 0:
            category = 'App Error'

        # User Errors
        elif error.find('Illegal character in object name') >= 0:
            category = 'User Error'
        elif error.find('No such file or directory') >= 0:
            category = 'NoFileDir'
        elif error.find('Not one protein family member') >= 0:
            category = 'User Error'
        elif error.find('is used for forward and reverse') >= 0:
            category = 'User Error'
        elif error.find('duplicate genome display names') >= 0:
            category = 'User Error'
        elif error.find('Proteome comparison does not involve genome') >= 0:
            category = 'User Error'
        elif error.find('incompatible read library types') >= 0:
            category = 'User Error'
        elif error.find('MISSING DOMAIN ANNOTATION FOR') >= 0:
            category = 'User Error'
        elif error.find('ALL genomes have no matching Domain Annotation') >= 0:
            category = 'User Error'
        elif error.find('There is no taxonomy classification assignment against') >= 0:
            category = 'User Error'
        elif error.find('There are no protein translations in genome') >= 0 or error.find(
                'The genome does not contain any CDSs') >= 0:
            category = 'User Error'
        elif error.find(' not found in pangenome') >= 0:
            category = 'User Error'
        elif error.find(
                'You must include the following additional Genomes in the Pangenome Calculation') >= 0:
            category = 'User Error'
        elif error.find('Undefined compound used as reactant') >= 0:
            category = 'User Error'
        elif error.find('Duplicate gene ID') >= 0:
            category = 'User Error'
        elif error.find(
                'The input directory does not have any files with one of the following extensions') > 0:
            category = 'User Error'
        elif error.find('is not a valid KBase taxon ID.') >= 0:
            category = 'User Error'
        elif error.find('Duplicate objects detected in input') >= 0:
            category = 'User Error'
        elif error.find('unable to fetch assembly:') >= 0:
            category = 'User Error'
        elif error.find('may not read workspace') >= 0:
            category = 'User Error'
        elif error.find('No bins produced - skipping the creation') >= 0:
            category = 'User Error'
        elif error.find('Must configure at least one of 5 or 3 adapter') >= 0:
            category = 'User Error'
        elif error.find('There is no taxonomy classification assignment against ') >= 0:
            category = 'User Error'
        elif error.find('cannot be accessed') >= 0 and error.find(
                'Workspace') >= 0 and error.find('deleted') >= 0:
            category = 'User Error'
        elif error.find('Object #') >= 0 and error.find('has invalid reference') >= 0:
            category = 'User Error'
        elif error.find('Feature ID') >= 0 and error.find(
                'does not exist in the supplied genome') >= 0:
            category = 'User Error'
        # Assembly
        elif error.find('There are no contigs to save') >= 0:
            category = 'User Error'
        elif error.find('assembly method was not specified') >= 0:
            category = 'User Error'
        elif error.find('takes 2 positional arguments but 3 were given') >= 0:
            category = 'User Error'
        # Annotation
        elif error.find('Too many contigs') >= 0:
            category = 'User Error'
        elif error.find('You must run the RAST SEED Annotation App') >= 0:
            category = 'User Error'
        elif error.find('You must supply at least one') > 0 or error.find(
                'too many contigs') >= 0:
            category = 'User Error'
        elif error.find('Fasta file is empty.') >= 0:
            category = 'User Error'
        elif error.find('Illegal number of separators') >= 0:
            category = 'User Error'
        elif error.find('Unable to parse version portion of object reference') >= 0:
            category = 'User Error'
        # BLAST
        elif error.find('input_one_sequence') >= 0 and error.find('input_one_ref') >= 0:
            category = 'User Error'
        elif error.find('input_one_sequence') >= 0 and error.find('output_one_name') >= 0:
            category = 'User Error'
        elif error.find('blast') >= 0 and error.find('Query is Empty') >= 0:
            category = 'User Error'
        elif error.find('No sequence found in fasta_str') >= 0:
            category = 'User Error'
        # Modeling
        elif error.find('not a valid EXCEL nor TSV file') >= 0:
            category = 'User Error'
        elif error.find('Duplicate model names are not permitted') >= 0:
            category = 'User Error'
        elif error.find('Must select at least two models to compare') >= 0:
            category = 'User Error'
        # Import
        elif error.find('Both SRA and FASTQ/FASTA file given. Please provide one file type') >= 0:
            category = 'User Error'
        elif error.find('FASTQ/FASTA input file type selected. But missing FASTQ/FASTA file') >= 0:
            category = 'User Error'
        elif error.find('reads files do not have an equal number of records') >= 0:
            category = 'User Error'
        elif error.find('File is not a zip file') >= 0:
            category = 'User Error'
        elif error.find('utf-8') >= 0: \
                category = 'User Error'
        elif error.find('Error running command: pigz') >= 0:
            category = 'User Error'
        elif error.find(' is not a FASTQ file') >= 0:
            category = 'User Error'
        elif error.find('Cannot connect to URL') >= 0:
            category = 'User Error'
        elif error.find('Invalid FTP Link') >= 0:
            category = 'User Error'
        elif error.find('Plasmid assembly requires that one') >= 0:
            category = 'User Error'
        elif error.find('Premature EOF') >= 0:
            category = 'User Error'
        elif error.find('Reading FASTQ record failed') >= 0:
            category = 'User Error'
        elif error.find('Invalid FASTQ') >= 0:
            category = 'User Error'
        elif error.find('missing FASTQ/FASTA file') >= 0:
            category = 'User Error'
        elif error.find('line count is not divisible by') >= 0:
            category = 'User Error'
        elif error.find('But missing SRA file') >= 0:
            category = 'User Error'
        elif error.find('Features must be completely contained') >= 0:
            category = 'User Error'
        elif error.find('Parent ID') >= 0 and error.find(
                'was not found in feature ID list') >= 0:
            category = 'User Error'
        elif error.find('unable to parse') >= 0:
            category = 'User Error'
        elif error.find('Every feature sequence id must match a fasta sequence id') >= 0:
            category = 'User Error'
        elif error.find('Did not recognise the LOCUS line layout') >= 0:
            category = 'User Error'
        elif error.find('Could not determine alphabet for') >= 0:
            category = 'User Error'
        elif error.find('This FASTA file has non nucleic acid characters') >= 0:
            category = 'User Error'
        elif error.find('Not a valid FASTA file') >= 0:
            category = 'User Error'
        elif error.find('This FASTA file has non nucleic acid characters') >= 0 or app_log.get(
                'error').find(
                'This FASTA file may have amino acids') >= 0:
            category = 'User Error'
        elif error.find('FASTA header') >= 0 and error.find(
                'appears more than once in the file') >= 0:
            category = 'User Error'
        elif error.find('Duplicate gene ID') >= 0:
            category = 'User Error'
        # Other apps
        elif error.find('missing or empty krona input file') >= 0:
            category = 'User Error'
        elif error.find('FeatureSet has multiple reference Genomes') >= 0:
            category = 'User Error'
        elif error.find('You must enter either an input genome or input reads') >= 0:
            category = 'User Error'
        else:
            category = app_log.get('method')

        app_log['error'] = error.replace("\n", ' \\n ')  # Force a single line so list can be sorted
        app_log['error'] = error.replace("\r", ' \\r ')

    return category
