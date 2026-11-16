def validate_dna(dna):
    return len(dna) > 0 and all(base in "ATGC" for base in dna)

def length(dna):
    return len(dna)

def nucleotide_frequency(dna):
    for base in "ATGC":
        print(f"{base}: {dna.count(base)}")

def calculate_gc(dna):
    GC = dna.count("G") + dna.count("C")
    return (GC/len(dna))*100

def transcribe_dna(dna):
    return dna.replace("T", "U")

def templ_dna(dna):
    return dna.translate(str.maketrans('ATGC','UACG'))





print("*********************************")
print(" Welcome to DNA Analysis Program")
print("*********************************")
print()
# Get a valid DNA sequence
while True:
    dna = input("Give your DNA sequence: ").strip().upper()

    if validate_dna(dna):
        break
    else:
        print("Invalid DNA sequence. Use only A, T, G and C.")
        print()

# Main menu
while True:
    print("\nWhich feature would you like to use?")
    print("1. Sequence Length")
    print("2. Calculate nucleotide frequency")
    print("3. Calculate GC content")
    print("4. Transcribe DNA to RNA (coding strand)")
    print("5. Transcribe DNA to RNA (template strand)")
    print("6. Exit")

    try:
        num = int(input("Write the feature number: "))
    except ValueError:
        print("Please enter an integer from 1 to 6.")
        continue

    if num == 1:
        print('Length of the DNA Sequence is : ', length(dna))

    elif num == 2:
        nucleotide_frequency(dna)

    elif num == 3:
        print(f"GC Content: {calculate_gc(dna):.2f}%")

    elif num == 4:
        print("RNA sequence:", transcribe_dna(dna))

    elif num == 5:
        print("RNA sequence:", templ_dna(dna))

    elif num == 6:
        print("You exited the program.........")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
