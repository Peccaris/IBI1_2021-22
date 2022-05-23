def percentage_calculator(DNA_strand):  # define the function
    running = True
    while running:
        chosen_nucleotide = input(
            'Input the nucleotide that you want to know the percentage:')
        chosen_nucleotide = chosen_nucleotide.upper()
        num_A = DNA_strand.count('A')
        num_G = DNA_strand.count('G')
        num_C = DNA_strand.count('C')
        num_T = DNA_strand.count('T')
        totol_length = len(DNA_strand)

        if chosen_nucleotide == 'A':  # seclect the nucleotide that need to be calculated
            x = num_A
        elif chosen_nucleotide == 'G':
            x = num_G
        elif chosen_nucleotide == 'C':
            x = num_C
        elif chosen_nucleotide == 'T':
            x = num_T
        percentage = x / totol_length  # calculate the percentage
        percentage = '{:.2%}'.format(
            percentage)  # in case the change is an infinite decimal
        print('The percentage of', chosen_nucleotide, 'is', percentage)
        chosen_nucleotide = input(
            "Please input 'y' to calculate another nucleotide percentage or 'q' to quit: \n"
        ).upper()
        if chosen_nucleotide == 'Q':  # provide a choice : continue or quite
            break

DNA_strand = input('Input the DNA strand: ').upper()
percentage_calculator(DNA_strand)  # call the function
