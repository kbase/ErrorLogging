def categories_to_errors_dict():
    """Categories to error dictionary function maps common error substrings to categories.
        The categories are keys in the dictionary and the values are arrays of strings
        or arrays of list.
        Some error categories, such as User Errors, has many subcategories. Thus,
         each subcategory has its own list, but each list is placed in the larger
         User Error array that maps to the key User Error.
         This function returns a dictionary used to organize error logs"""
    # App Errors
    app_errors = ["call_features_rRNA_SEED",
                  "Model likely contains numerical instability",
                  "Object doesnt have required fields",
                  "has invalid provenance reference",
                  "Mandatory arguments missing",
                  "Authentication required for AbstractHandle",
                  "Can't locate object method quality via package",
                  "Can't use an undefined value as an ARRAY reference",
                  "KBaseReport parameter validation status"]
    # User Errors
    general_user_errors = ["Illegal character in object name",
                           "Not one protein family member",
                           "is used for forward and reverse",
                           "duplicate genome display names",
                           "Proteome comparison does not involve genome",
                           "incompatible read library types",
                           "MISSING DOMAIN ANNOTATION FOR",
                           "ALL genomes have no matching Domain Annotation",
                           "There is no taxonomy classification assignment against",
                           "There are no protein translations in genome",
                           "not found in pangenome",
                           "You must include the following additional Genomes in the Pangenome Calculation",
                           "Undefined compound used as reactant",
                           "Duplicate gene ID",
                           "The input directory does not have any files with one of the following extensions",
                           "is not a valid KBase taxon ID.",
                           "Duplicate objects detected in input",
                           "unable to fetch assembly:",
                           "may not read workspace",
                           "No bins produced - skipping the creation",
                           "Must configure at least one of 5 or 3 adapter",
                           "There is no taxonomy classification assignment against",
                           "cannot be accessed",
                           "Object #",
                           "does not exist in the supplied genome"]
    assembly_user_errors = ["There are no contigs to save",
                            "assembly method was not specified",
                            "takes 2 positional arguments but 3 were given"]
    annotation_user_errors = ["Too many contigs",
                              "You must run the RAST SEED Annotation App",
                              "You must supply at least one",
                              "Fasta file is empty.",
                              "Illegal number of separators",
                              "Unable to parse version portion of object reference"]
    blast_user_errors = ["not a valid EXCEL nor TSV file",
                         "Duplicate model names are not permitted",
                         "Must select at least two models to compare",
                         "input_one_sequence",
                         "input_one_ref",
                         "output_one_name",
                         "Query is Empty",
                         "No sequence found in fasta_str"]
    modeling_user_errors = ['not a valid EXCEL nor TSV file',
                            'Duplicate model names are not permitted',
                            'Must select at least two models to compare']
    import_user_errors = ["Both SRA and FASTQ/FASTA file given. Please provide one file type",
                          "FASTQ/FASTA input file type selected. But missing FASTQ/FASTA file",
                          "reads files do not have an equal number of records",
                          "File is not a zip file",
                          "error running command: pigz",
                          "is not a FASTQ file",
                          "Cannot connect to URL",
                          "Invalid FTP Link",
                          "Plasmid assembly requires that one",
                          "Premature EOF",
                          "Reading FASTQ record failed",
                          "Invalid FASTQ",
                          "missing FASTQ/FASTA file",
                          "line count is not divisible by",
                          "But missing SRA file",
                          "Features must be completely contained",
                          "was not found in feature ID list",
                          "unable to parse",
                          "Every feature sequence id must match a fasta sequence id",
                          "Did not recognise the LOCUS line layout",
                          "Could not determine alphabet for",
                          "This FASTA file has non nucleic acid characters",
                          "Not a valid FASTA file",
                          "This FASTA file has non nucleic acid characters",
                          "This FASTA file may have amino acids",
                          "appears more than once in the file",
                          "Duplicate gene ID"]
    other_apps_user_errors = ["missing or empty krona input file",
                              "FeatureSet has multiple reference Genomes",
                              "You must enter either an input genome or input reads"]
    # No such file/dir & other miscellaneous errors
    file_directory_missing = ["No such file or directory"]
    server = ["500 Server closed connection"]
    no_space = ["exit code is 123", "No space left on device"]
    exit = ["exit code is 137"]
    badstatus = ["BadStatusLine"]
    badserver = ["Bad Gateway", "NJSW failed"]
    compression = ["compression tyep 9"]
    job_service = ['Kafka', 'Job service side status']
    lost_connection = ["ProtocolError(Connection aborated)", "Connection has been shutdown"]
    nosuchcontainer = ["No such container"]
    readtimeout = ["ReadTimeError", "504 Gateway Time-out"]
    nooutput = ["Output file is not found"]
    canceled = ["Job was cancelled"]
    noassemblyref = ["does not have reference to the assembly object"]
    user_errors = [general_user_errors, blast_user_errors,
                   annotation_user_errors, modeling_user_errors,
                   assembly_user_errors, other_apps_user_errors, import_user_errors]
    # Construct error dictionary
    error_dictionary = {'User_Error': user_errors,
                        'App Error': app_errors,
                        'NoFileDir': file_directory_missing,
                        '500': server,
                        "NoSpace": no_space,
                        "Exit 137": exit,
                        "BadStatusLine": badstatus,
                        'BadServer': badserver,
                        "Compression": compression,
                        "JobService": job_service,
                        "LostConnection": lost_connection,
                        'NoSuchContainer': nosuchcontainer,
                        "NoOutput": nooutput,
                        "Canceled": canceled,
                        "NoAssemblyRef": noassemblyref,
                        "ReadTimeout": readtimeout}
    return error_dictionary