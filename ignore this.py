def get_dna_strand():
    
    '''Gives user a random DNA strand from the list below'''
    
    import numpy as np
    
    dna_strands = ['GGAGAACGATTACTTTCA',
                   'TGAGCACGATAATTAAGA',
                   'ACCCGATGACTTGCATCA',
                   'CTATCTCGATAATTAAGA',
                   'CTACGATTAACACTTAGA',
                   'AGATGAGCACGATTACTA',
                   'AAACGATACTAAGAAATA',
                   'AAAGAACGATTTCTTTCA',
                   'TAATACGGACGAGAACTT',
                   'TCATAATACGGAGAACTT']
    
    dna_strand = np.random.choice(dna_strands)
    
    print('Your DNA strand is: ' + dna_strand)


def dna_to_rna(dna_strand): 
    
    '''Loops though the DNA strand chosen above and returns the complementary RNA strand'''
    
    rna_strand = ''
    
    for base in dna_strand: 
        
        if base == 'A': 
            
            rna_strand = rna_strand + 'U'
