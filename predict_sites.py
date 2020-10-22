#gonna assume each substring is 6 NU long
import math
pseudocount = 0.1

# This function encodes a DNA nucleotide as an integer between 0 and 3
# It returns the encoded value, or -1 if the input is not a valid nucleotide.

def encode(nucleotide):
    """
    Args:
        nucleotide: A string of one character
    Returns:
        An integer encoding the nucleotide, or -1 if not a valid nucleotide
    """
    
    while True: #loops until return statement is executed
        if nucleotide == "A":
            return(0)
        elif nucleotide =="C":
            return(1)
        elif nucleotide =="G":
            return(2)
        elif nucleotide =="T":
            return(3)
        else:
            return(-1)
my_PWM = [[0.370356487039949, 0.07638834586345467, 0.07638834586345467, 0.5893480258118245, -1.4149733479708178, -0.37358066281259295], \
              [-1.4149733479708178, 0.43628500074825727, -1.4149733479708178, -1.4149733479708178, -1.4149733479708178, 0.43628500074825727], \
              [-1.4149733479708178, -1.4149733479708178, 0.43628500074825727, -1.4149733479708178, -0.37358066281259295, -0.09275405323689867], \
              [0.19781050874891748, -1.4149733479708178, -1.4149733479708178, -1.4149733479708178, 0.5440680443502756, -1.4149733479708178]]

nucleotide = "fuck"
print("**** Q1 ****")
print(encode(nucleotide))

def build_PFM(sequences):
    """
    Args:
        sequences: A list of sequences of equal lengths
    Returns:
        The position Frequency Matrix build from the sequences, stored
        as a two-dimensional list
    """
    A=[] # makes lists we can modify for each base
    C=[] # this also gets around having to zero a matrix or define length, etc.
    G=[]
    T=[]
    for j in range(len(sequences[0])): #looping through the list of list
        A.append([i[j] for i in sequences].count('A')) #appending the empty list with a count of each letter
        C.append([i[j] for i in sequences].count('C')) 
        G.append([i[j] for i in sequences].count('G'))
        T.append([i[j] for i in sequences].count('T'))
    return(A, C, G, T) #returns the main list

sequences = ["ACGATG","ACAATG","ACGATC","ACGATC","TCGATC", "TCGAGC","TAGATC","TAAATC","AAAATC","ACGATA"]
PFM = build_PFM(sequences)
print("**** Q2 ****")
print(PFM)

def get_PWM_from_PFM(PFM, pseudocount):
    """
    Args:
        PFM: A position frequency matrix, stored as a two-dimensional list
        pseudocount: A non-negative floating point number
    Returns:
        A position weight matrix, stored as a two-dimensional list
    """
    # You may find this useful: To create a list of lists of 4 rows and L columns:
    # PWM = [[0 for i in range(L)] for j in range(4)]
    PWM =[]                   # list to store the values we want
    for i in range(len(PFM)): # looping through the list of list
        temp_list=[]                  # temporary list to append
        for j in range(len(PFM[i])):  # looping through list of values
            v = math.log10( (PFM[i][j] + pseudocount)/((PFM[0][j]+PFM[1][j]+PFM[2][j]+PFM[3][j])+ (4 * pseudocount)))- math.log10(0.25)
            temp_list.append(v) #adds the calculated value to the temporary list
        PWM.append(temp_list) # adds the temporary calculated value to the main PWM list
    return PWM  # returns the main list

PFM = [[6,3,3,10,0,1],[0,7,0,0,0,7],[0,0,7,0,1,2],[4,0,0,0,9,0]]
PWM=get_PWM_from_PFM(PFM,0.1)
print("*** Question 3 ****")
print(PWM)

def score(sequence, PWM):
    """
    Args:
        sequence: A DNA sequence
        PWM: A position weight matrix, of the same length as the sequence
    Returns:
        A floating point number corresponding to the score of the sequence 
        for the given PWM
    """
    s = 0 #initial place in index is zeroth position
    score = 0 #initial score is zero
    for i in sequence:
       if i == "A":
          score = score + PWM[0][s]
          s = s+1
       elif i == "C":
          score=score + PWM[1][s]
          s = s+1
       elif i == "G":
          score = score + PWM[2][s]
          s = s+1
       elif i=="T":
          score = score + PWM[3][s]
          s = s+1
    return score

print("**** Q4 ****")
my_PWM = [[0.370356487039949, 0.07638834586345467, 0.07638834586345467, 0.5893480258118245, -1.4149733479708178, -0.37358066281259295], \
         [-1.4149733479708178, 0.43628500074825727, -1.4149733479708178, -1.4149733479708178, -1.4149733479708178, 0.43628500074825727], \
         [-1.4149733479708178, -1.4149733479708178, 0.43628500074825727, -1.4149733479708178, -0.37358066281259295, -0.09275405323689867], \
         [0.19781050874891748, -1.4149733479708178, -1.4149733479708178, -1.4149733479708178, 0.5440680443502756, -1.4149733479708178]]
s = score("TCGATG", PWM)
print(s)

PWM=[[0.370356487039949, 0.07638834586345467, 0.07638834586345467, 0.5893480258118245, -1.4149733479708178, -0.37358066281259295], [-1.4149733479708178, 0.43628500074825727, -1.4149733479708178, -1.4149733479708178, -1.4149733479708178, 0.43628500074825727], [-1.4149733479708178, -1.4149733479708178, 0.43628500074825727, -1.4149733479708178, -0.37358066281259295, -0.09275405323689867], [0.19781050874891748, -1.4149733479708178, -1.4149733479708178, -1.4149733479708178, 0.5440680443502756, -1.4149733479708178]]
sequence = "GCATCGATGGCAGCGACTACAGCGCTACTACAGCGGAGACGATGCGATCGATACAAT"

def predict_sites(sequence, PWM, threshold = 0):
    """
    Args:
        sequence: A DNA sequence
        PWM: A position weight matrix
        threshold (optional): Minimum score needed to be predicted as a binding site
    Returns:
        A list of positions with match scores greater or equal to threshold
    """
   # seqScore = score((get_PWM_from_PFM(build_PFM(sequence)), pseudocount), sequence)
    seqPWM = get_PWM_from_PFM(build_PFM(sequence), pseudocount)
    sub_score = [] #score of each substring
    score = [] # we're gonna add the starting positions with scores above the threshold
    for i in range(len(sequence[0])):
        nu_score = score(seqPWM[i])
        subunit_start = sequence[i]
        #iterate score calculation over entire length 6 units at a time
        for sequence[i:(i+6)] in range(len(sequence[0])):
            x = (nu_score[0]+nu_score[1]+nu_score[2]+nu_score[3]+nu_score[4]+nu_score[5]+nu_score[6])
            sub_score.append(x)
            i = i + 1
            print(x)
        if sub_score >= PWM[0]:
            score.append(subunit_start)
        elif sub_score >= PWM[1]:
            score.append(subunit_start)
        elif sub_score >= PWM[2]:
            score.append(subunit_start)
        elif sub_score >= PWM[3]:
            score.append(subunit_start)
    return(score)
            
    

print("**** Q5 ****")
print(score)



