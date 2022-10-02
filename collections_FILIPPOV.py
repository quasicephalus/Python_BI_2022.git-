# Set dictionaries for DNA and RNA
# It is done first because these dictionaries will be needed in nearly all next steps
DNA_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',
            'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}
RNA_dict = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G',
            'a': 'u', 'u': 'a', 'g': 'c', 'c': 'g'}

# Manual text
help_text = 'What commands do:\n\n' \
            'transcribe\n' \
            'Build mRNA from given DNA sequence, which considered to be sense. ' \
            'Reverse transcription is not supported!\n\n' \
            'reverse\n' \
            'Just it.\n\n' \
            'complement\n' \
            'Build complementary DNA for given DNA sequence\n' \
            'or\n' \
            'Build complementary RNA for given RNA sequence\n' \
            'or\n' \
            'Specify what nucleic acid you want to get if type is unclear (like AGCGA).\n\n' \
            'reverse complement \n' \
            'Reverse sequence, then build complementary nucleic acid as described as described above.\n\n' \
            'Supported sequences are DNA and RNA, and therefore must consist' \
            ' ONLY of characters "A", "T", "U", "G", "C" (case insensitive).' \
            ' "T" and "U" must not appear together.\n\n'


# Define main functions:

# Check if entered sequence either DNA or RNA
def check(seq):
    for char in seq:
        # Probably worse code to check if:
        # 1. all characters in sequence are in [Aa, Tt, Gg, Cc, Uu]
        # 2. there is no Uu and Tt together in sequence
        if char not in DNA_dict and char not in RNA_dict:
            return False
        elif 'U' in seq and 'T' in seq:
            return False
        elif 'U' in seq and 't' in seq:
            return False
        elif 'u' in seq and 'T' in seq:
            return False
        elif 'u' in seq and 't' in seq:
            return False
    # If alles gut:
    return True


# Transcribe sequence
def transcribe(seq):
    return seq.replace('t', 'u')


# Reverse sequence
def reverse(seq):
    return seq[::-1]


# Complement sequence
def complement(seq, typus):
    # Function takes "typus" argument that defines which dictionary it will use.
    # Have no idea how to optimize complement function from Git course.
    # Maybe list comprehension is at least faster...
    if typus == 'DNA':
        compl_seq = [DNA_dict[nucl] for nucl in seq]
    elif typus == 'RNA':
        compl_seq = [RNA_dict[nucl] for nucl in seq]
    return ''.join(compl_seq)


# Complement reversed sequence
def reverse_complement(seq, typus):
    seq = seq[::-1]
    if typus == 'DNA':
        compl_seq = [DNA_dict[nucl] for nucl in seq]
    if typus == 'RNA':
        compl_seq = [RNA_dict[nucl] for nucl in seq]
    return ''.join(compl_seq)


# Set correct commands
comms = ['exit', 'transcribe', 'reverse',
         'complement', 'reverse complement', 'help']

# Little manual
print('Supported commands are:\n\n'
      'transcribe\n'
      'reverse\n'
      'complement\n'
      'reverse complement \n\n'
      'For help type "help"!\n\n')

# Initialize infinite cycle
while True:
    # Command input and check
    comm = input('Enter command: ').lower().strip('"')
    if comm == 'exit':
        break
    elif comm not in comms:
        print('Incorrect command.\n')
        continue
    elif comm == 'help':
        print(help_text)
        continue

    # Sequence input
    seq = input('Enter sequence:')

    # Program won't execute till sequence is correct
    while not check(seq):
        print('Entered sequence is neither DNA nor RNA.\n')
        seq = input('Enter sequence:')
    # Execution
    if comm == 'transcribe':
        # Check that transcribed sequence is DNA
        while 'U' in seq or 'u' in seq:
            print('Reverse transcription is not supported :(\n')
            seq = input('Enter DNA sequence:')
        print(transcribe(seq))
    if comm == 'reverse':
        print(reverse(seq))
    if comm == 'complement':
        # If type of nucleic acid can't be defined from sequence
        if 'U' not in seq and \
                'u' not in seq and \
                'T' not in seq and \
                't' not in seq:
            print('DNA or RNA?')
            typus = input('Write "DNA" or "RNA":').upper()
            while typus != 'DNA' and typus != 'RNA':
                typus = input('Write "DNA" or "RNA":').upper()
        # If type of nucleic acid can be defined from sequence
        elif 'U' in seq or 'u' in seq:
            typus = 'RNA'
        else:
            typus = 'DNA'
        print(complement(seq, typus))
    if comm == 'reverse complement':
        # If type of nucleic acid can't be defined from sequence
        if 'U' not in seq and \
                'u' not in seq and \
                'T' not in seq and \
                't' not in seq:
            print('DNA or RNA?')
            typus = input('Write "DNA" or "RNA":').upper()
            while typus != 'DNA' and typus != 'RNA':
                typus = input('Write "DNA" or "RNA":').upper()
        # If type of nucleic acid can be defined from sequence
        elif 'U' in seq or 'u' in seq:
            typus = 'RNA'
        else:
            typus = 'DNA'
        print(reverse_complement(seq, typus))

print('Mission accomplished.')
