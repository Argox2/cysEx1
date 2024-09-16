from collections import defaultdict, Counter
from itertools import product


# Paso 1. Identificamos los patrones repetidos.
def findRepeatedSequences(text):
    sequences = defaultdict(list)
    lenText = len(text)
    for lenSeq in range(3, int(lenText/2)):
        for i in range(len(text) - lenSeq):
            seq = text[i:i+lenSeq]
            sequences[seq].append(i)

    filteredSequences = {
        seq: pos for seq, pos in sequences.items() if len(pos) > 1
    }

    print("\nSecuencias:")
    for seq, pos in filteredSequences.items():
        print(f"{seq}: {pos}")

    return filteredSequences


# Paso 2. Registramos las distancias
def calcDistances(repeatedSequences):
    distances = []
    for pos in repeatedSequences.values():
        for i in range(len(pos) - 1):
            distances.append(pos[i + 1] - pos[i])

    print("\nDistances: ")
    print(distances)

    return distances


# Paso 3. Calculamos los factores de cada distancia,
# y luego contamos su frecuencia.
def getFactors(distances):
    allFactors = []
    for distance in distances:
        factors = []
        for i in range(1, distance + 1):
            if distance % i == 0:
                factors.append(i)
        allFactors.extend(factors)

    factorCounts = Counter(allFactors)
    mostCommonFactors = factorCounts.most_common(4)[1:]
    factors = [t[0] for t in mostCommonFactors]

    print("\nMost common factors: ")
    print(factors)

    return factors

# Paso 4. Dividimos el texto en n grupos,
# agregando


def splitText(ciphertext, factors):
    groups = []  # To store groups for each factor

    for factor in factors:
        group = [''] * factor

        for i, char in enumerate(cipherText):
            group[i % factor] += char

        groups.append(group)
    print("\nPossible texts:")
    print(groups)
    return groups  # Return all groups for all factors

# Paso 5. Obtenemos nuestras posibles E


def probableShift(text, cipherText):
    # Conseguimos nuestras posibles E.
    posibles_E = []
    for letter in text:
        letter_counts = Counter(letter)
        mostCommonLetter = max(letter_counts.values())
        posible_E = [
            char for char, count
            in letter_counts.items()
            if count == mostCommonLetter
        ]
        posibles_E.append(posible_E)
    # Combinamos las posibles
    combinations = list(product(*posibles_E))

    print(posibles_E)

    #
    for combo in combinations:

        shift = [(ord(char) - ord('E')) % 26 for char in combo]
        key = ''
        for num in shift:
            key += chr(num + ord('A'))
        print(f'\n Key: {key}')
        print(shift)

        decrypted_text = ''

        for i, char in enumerate(cipherText):
            which_shift = shift[i % len(shift)]

            decrypted_char = chr(
                (ord(char) - which_shift - ord('A')) % 26 + ord('A'))
            decrypted_text += decrypted_char

        print(decrypted_text)


# Texto cifrado.
cipherText = """
CJSRV SUJDJ EQASC GLSEL PXMME LJINF GTYCG CVVVX
LHYZR WHIVW GGLHK UCCMW HPGCZ MQLPD KUCEG OTHKF
LHKWU BRDES TRLRX HJZQB XOPJR WXFGE CTWGV FZTTB
GJRPU ZKJFT WOIIC TFSPK YHLSU JGCZK JRRST HCRLS
LMUKC BLAWJ RQXDT FRTVH GURWX ZGMCA HTUVA JKWVP
LTXRG URDIF QKCRM HJVQT TGUVR HTBFY MLMCI FYQHI
VJCRN FKEEI ASOKF TTBUN CGLHQ KFTLS SLCHM WQEQP
KSXZR PEHQR LNTBF RJABB HFPBT HKFLH XQWIG IRDQC
GRRTT RKTPC TBQPG RYZJA WFKMC IASNV TTECH JCRNF
KKWLB HJZLI ASQIE PGWBR RXHBH IMBPV CKQTQ DGTRT
WCHVY RASOG JDRSG KMIAS QMCGT ZNXMK XFPRL RXGVI
SRMIT V """.replace("\n", "").replace(" ", "")


def supposeKasiski(cipherText):
    repeatedSequences = findRepeatedSequences(cipherText)
    distances = calcDistances(repeatedSequences)
    factors = getFactors(distances)
    possibleTexts = splitText(cipherText, factors)
    for text in possibleTexts:
        probableShift(text, cipherText)


supposeKasiski(cipherText)
