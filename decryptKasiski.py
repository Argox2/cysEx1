import sys

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
SRMIT V
""".replace("\n", "").replace(" ", "")


def resolveKasiski(cipherText, key):
    key_shift = [(ord(char) + ord('A')) % 26 for char in key]

    decrypted_text = ''

    for i, char in enumerate(cipherText):
        which_shift = key_shift[i % len(key_shift)]

        decrypted_char = chr(
            (ord(char) - which_shift - ord('A')) % 26 + ord('A'))
        decrypted_text += decrypted_char

    print(decrypted_text)


key = sys.argv[1]
resolveKasiski(cipherText, key)
