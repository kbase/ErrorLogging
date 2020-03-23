def add_category(app_log):
    category = None
    if category is None:
        app_status = app_log.get('status')
        if app_status.find('500 Server closed connection') > 0:
            category = '500'
        elif app_status.find('exit code is 123') >= 0 or app_status.find(
                'No space left on device') >= 0:
            category = 'NoSpace'
        elif app_status.find('exit code is 137') >= 0:
            category = 'Exit 137'
        elif app_status.find('BadStatusLine') >= 0:
            category = 'BadStatusLine'
        elif app_status.find('Bad Gateway') >= 0:
            category = 'BadServer'
        elif app_status.find('NJSW failed') >= 0:
            category = 'BadServer'
        elif app_status.find('compression type 9') >= 0:
            category = 'Compression'
        elif app_status.find('Job service side status') >= 0:
            category = 'JobService'
        elif app_status.find('Kafka') >= 0:
            category = 'JobService'
        elif app_status.find('Connection has been shutdown') >= 0:
            category = 'LostConnection'
        elif app_status.find('ProtocolError(Connection aborted') >= 0:
            category = 'LostConnection'
        elif app_status.find('No such container') >= 0:
            category = 'NoSuchContainer'
        elif app_status.find('Output file is not found') >= 0:
            category = 'NoOutput'
        elif app_status.find('does not have reference to the assembly object') >= 0:
            category = 'NoAssemblyRef'
        elif app_status.find('ReadTimeError') >= 0:
            category = 'ReadTimeout'
        elif app_status.find('504 Gateway Time-out') >= 0:
            category = 'ReadTimeout'
        elif app_status.find('Job was cancelled') >= 0 or app_status.find(
                'job was canceled') >= 0 or app_status.find('ob was Canceled') >= 0:
            category = 'Canceled'

        # App-specific Errors
        elif app_status.find('call_features_rRNA_SEED') >= 0:
            category = 'App Error'
        elif app_status.find('Model likely contains numerical instability') >= 0:
            category = 'App Error'
        elif app_status.find('Object doesnt have required fields') >= 0:
            category = 'App Error'
        elif app_status.find('has invalid provenance reference') >= 0:
            category = 'App Error'
        elif app_status.find('Mandatory arguments missing') >= 0:
            category = 'App Error'
        elif app_status.find('Authentication required for AbstractHandle') >= 0:
            category = 'App Error'
        elif app_status.find("Can't locate object method quality via package") >= 0:
            category = 'App Error'
        elif app_status.find("Can't use an undefined value as an ARRAY reference") >= 0:
            category = 'App Error'
        elif app_status.find('KBaseReport parameter validation statuss') >= 0:
            category = 'App Error'

        # User Errors
        elif app_status.find('Illegal character in object name') >= 0:
            category = 'User Error'
        elif app_status.find('No such file or directory') >= 0:
            category = 'NoFileDir'
        elif app_status.find('Not one protein family member') >= 0:
            category = 'User Error'
        elif app_status.find('is used for forward and reverse') >= 0:
            category = 'User Error'
        elif app_status.find('duplicate genome display names') >= 0:
            category = 'User Error'
        elif app_status.find('Proteome comparison does not involve genome') >= 0:
            category = 'User Error'
        elif app_status.find('incompatible read library types') >= 0:
            category = 'User Error'
        elif app_status.find('MISSING DOMAIN ANNOTATION FOR') >= 0:
            category = 'User Error'
        elif app_status.find('ALL genomes have no matching Domain Annotation') >= 0:
            category = 'User Error'
        elif app_status.find('There is no taxonomy classification assignment against') >= 0:
            category = 'User Error'
        elif app_status.find('There are no protein translations in genome') >= 0 or app_status.find(
                'The genome does not contain any CDSs') >= 0:
            category = 'User Error'
        elif app_status.find(' not found in pangenome') >= 0:
            category = 'User Error'
        elif app_status.find(
                'You must include the following additional Genomes in the Pangenome Calculation') >= 0:
            category = 'User Error'
        elif app_status.find('Undefined compound used as reactant') >= 0:
            category = 'User Error'
        elif app_status.find('Duplicate gene ID') >= 0:
            category = 'User Error'
        elif app_status.find(
                'The input directory does not have any files with one of the following extensions') > 0:
            category = 'User Error'
        elif app_status.find('is not a valid KBase taxon ID.') >= 0:
            category = 'User Error'
        elif app_status.find('Duplicate objects detected in input') >= 0:
            category = 'User Error'
        elif app_status.find('unable to fetch assembly:') >= 0:
            category = 'User Error'
        elif app_status.find('may not read workspace') >= 0:
            category = 'User Error'
        elif app_status.find('No bins produced - skipping the creation') >= 0:
            category = 'User Error'
        elif app_status.find('Must configure at least one of 5 or 3 adapter') >= 0:
            category = 'User Error'
        elif app_status.find('There is no taxonomy classification assignment against ') >= 0:
            category = 'User Error'
        elif app_status.find('cannot be accessed') >= 0 and app_status.find(
                'Workspace') >= 0 and app_status.find('deleted') >= 0:
            category = 'User Error'
        elif app_status.find('Object #') >= 0 and app_status.find('has invalid reference') >= 0:
            category = 'User Error'
        elif app_status.find('Feature ID') >= 0 and app_status.find(
                'does not exist in the supplied genome') >= 0:
            category = 'User Error'
        # Assembly
        elif app_status.find('There are no contigs to save') >= 0:
            category = 'User Error'
        elif app_status.find('assembly method was not specified') >= 0:
            category = 'User Error'
        elif app_status.find('takes 2 positional arguments but 3 were given') >= 0:
            category = 'User Error'
        # Annotation
        elif app_status.find('Too many contigs') >= 0:
            category = 'User Error'
        elif app_status.find('You must run the RAST SEED Annotation App') >= 0:
            category = 'User Error'
        elif app_status.find('You must supply at least one') > 0 or app_status.find(
                'too many contigs') >= 0:
            category = 'User Error'
        elif app_status.find('Fasta file is empty.') >= 0:
            category = 'User Error'
        elif app_status.find('Illegal number of separators') >= 0:
            category = 'User Error'
        elif app_status.find('Unable to parse version portion of object reference') >= 0:
            category = 'User Error'
        # BLAST
        elif app_status.find('input_one_sequence') >= 0 and app_status.find('input_one_ref') >= 0:
            category = 'User Error'
        elif app_status.find('input_one_sequence') >= 0 and app_status.find('output_one_name') >= 0:
            category = 'User Error'
        elif app_status.find('blast') >= 0 and app_status.find('Query is Empty') >= 0:
            category = 'User Error'
        elif app_status.find('No sequence found in fasta_str') >= 0:
            category = 'User Error'
        # Modeling
        elif app_status.find('not a valid EXCEL nor TSV file') >= 0:
            category = 'User Error'
        elif app_status.find('Duplicate model names are not permitted') >= 0:
            category = 'User Error'
        elif app_status.find('Must select at least two models to compare') >= 0:
            category = 'User Error'
        # Import
        elif app_status.find('Both SRA and FASTQ/FASTA file given. Please provide one file type') >= 0:
            category = 'User Error'
        elif app_status.find('FASTQ/FASTA input file type selected. But missing FASTQ/FASTA file') >= 0:
            category = 'User Error'
        elif app_status.find('reads files do not have an equal number of records') >= 0:
            category = 'User Error'
        elif app_status.find('File is not a zip file') >= 0:
            category = 'User Error'
        elif app_status.find('utf-8') >= 0:
                category = 'User Error'
        elif app_status.find('error running command: pigz') >= 0:
            category = 'User Error'
        elif app_status.find(' is not a FASTQ file') >= 0:
            category = 'User Error'
        elif app_status.find('Cannot connect to URL') >= 0:
            category = 'User Error'
        elif app_status.find('Invalid FTP Link') >= 0:
            category = 'User Error'
        elif app_status.find('Plasmid assembly requires that one') >= 0:
            category = 'User Error'
        elif app_status.find('Premature EOF') >= 0:
            category = 'User Error'
        elif app_status.find('Reading FASTQ record failed') >= 0:
            category = 'User Error'
        elif app_status.find('Invalid FASTQ') >= 0:
            category = 'User Error'
        elif app_status.find('missing FASTQ/FASTA file') >= 0:
            category = 'User Error'
        elif app_status.find('line count is not divisible by') >= 0:
            category = 'User Error'
        elif app_status.find('But missing SRA file') >= 0:
            category = 'User Error'
        elif app_status.find('Features must be completely contained') >= 0:
            category = 'User Error'
        elif app_status.find('Parent ID') >= 0 and app_status.find(
                'was not found in feature ID list') >= 0:
            category = 'User Error'
        elif app_status.find('unable to parse') >= 0:
            category = 'User Error'
        elif app_status.find('Every feature sequence id must match a fasta sequence id') >= 0:
            category = 'User Error'
        elif app_status.find('Did not recognise the LOCUS line layout') >= 0:
            category = 'User Error'
        elif app_status.find('Could not determine alphabet for') >= 0:
            category = 'User Error'
        elif app_status.find('This FASTA file has non nucleic acid characters') >= 0:
            category = 'User Error'
        elif app_status.find('Not a valid FASTA file') >= 0:
            category = 'User Error'
        elif app_status.find('This FASTA file has non nucleic acid characters') >= 0 or app_log.get(
                'status').find(
                'This FASTA file may have amino acids') >= 0:
            category = 'User Error'
        elif app_status.find('FASTA header') >= 0 and app_status.find(
                'appears more than once in the file') >= 0:
            category = 'User Error'
        elif app_status.find('Duplicate gene ID') >= 0:
            category = 'User Error'
        # Other apps
        elif app_status.find('missing or empty krona input file') >= 0:
            category = 'User Error'
        elif app_status.find('FeatureSet has multiple reference Genomes') >= 0:
            category = 'User Error'
        elif app_status.find('You must enter either an input genome or input reads') >= 0:
            category = 'User Error'
        else:
            category = app_log.get('method')

        app_log['status'] = app_status.replace("\n", ' \\n ')  # Force a single line so list can be sorted
        app_log['status'] = app_status.replace("\r", ' \\r ')

    return category
