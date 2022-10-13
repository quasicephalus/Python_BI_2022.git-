# Function for getting reads from file line-by-line
# Not stripping lines here to make it easier to write into output
def get_read(file):
    read = {}
    read['head'] = file.readline()
    read['seq'] = file.readline()
    read['comm'] = file.readline()
    read['qual'] = file.readline()
    return read


# Function for checking GC content
def gc_check(read, gc_bounds):
    seq = read['seq'].strip()
    gc_count = seq.count('G') + seq.count('C')
    seq_len = len(seq)
    gc_ratio = gc_count / seq_len * 100
    # Probably not the best way to differ arguments,
    # any advice will be much appreciated
    if type(gc_bounds) is tuple:
        return min(gc_bounds) <= gc_ratio <= max(gc_bounds)
    else:
        return gc_ratio <= float(gc_bounds)


# Function for checking read length
# Pretty the same like above
def len_check(read, length_bounds):
    seq = read['seq'].strip()
    length = len(seq)
    if type(length_bounds) is tuple:
        return min(length_bounds) <= length <= max(length_bounds)
    else:
        return length <= float(length_bounds)


# Function for checking average quality of the read.
def quality_check(read, quality_threshold):
    quality = read['qual'].strip()
    score = 0
    for q in quality:
        score += ord(q) - 33
    average_score = score / len(quality)
    if average_score >= quality_threshold:
        return True
    else:
        return False


# Finally!
def main(input_fastq,
         output_file_prefix,
         gc_bounds=(0, 100),
         length_bounds=(0, 2 ** 32),
         quality_threshold=0,
         save_filtered=False):
    # Setting paths for output files
    passed_file = output_file_prefix + '_passed.fastq'
    failed_file = output_file_prefix + '_failed.fastq'
    # Opening input file and creating standard output files...
    with open(input_fastq, 'r') as file,\
            open(passed_file, 'w') as std_out:
        # and creating file for filtered reads if it is requested
        if save_filtered:
            failed_out = open(failed_file, 'w')
        # Reading file in infinite cycle, read-by-read
        while True:
            read = get_read(file)
            # As there's no more reads - break
            if len(read['seq']) == 0:
                break
            # Filtering particular read
            if gc_check(read, gc_bounds) and \
                    len_check(read, length_bounds) and \
                    quality_check(read, quality_threshold):
                # Writing passed read into standard output
                for value in read.values():
                    std_out.write(value)
            # And, if requested, passing filtered read in optional output
            elif save_filtered:
                for value in read.values():
                    failed_out.write(value)
        # Closing filtered output file if it was created
        if save_filtered:
            failed_out.close()
