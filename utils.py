def dec2binstr(num):
    binstr = bin(num)[2:]
    length = len(binstr)
    return "0"*(8-length) + binstr

class Base2Bit:
    def __init__(self):
        self.data = {
            "A": "00",
            "T": "01",
            "G": "10",
            "C": "11"
        }

class Base2Byte:
    def __init__(self):
        self.data = {
            "A": int("00000000", 2),
            "T": int("00100000", 2),
            "G": int("01000000", 2),
            "C": int("01100000", 2),
            "U": int("10000000", 2),
            "N": int("10100000", 2),
            " ": int("11000000", 2)
        }

class Bin2Base:
    def __init__(self):
        self.data = {
            "000": "A",
            "001": "T",
            "010": "G",
            "011": "C",
            "100": "U",
            "101": "N",
            "110": " "
        }

class Byte2Seq:
    def __init__(self):
        self.data = {
            '00000000':'AAAA','00000001':'AAAT','00000010':'AAAG','00000011':'AAAC',
            '00000100':'AATA','00000101':'AATT','00000110':'AATG','00000111':'AATC',
            '00001000':'AAGA','00001001':'AAGT','00001010':'AAGG','00001011':'AAGC',
            '00001100':'AACA','00001101':'AACT','00001110':'AACG','00001111':'AACC',
            '00010000':'ATAA','00010001':'ATAT','00010010':'ATAG','00010011':'ATAC',
            '00010100':'ATTA','00010101':'ATTT','00010110':'ATTG','00010111':'ATTC',
            '00011000':'ATGA','00011001':'ATGT','00011010':'ATGG','00011011':'ATGC',
            '00011100':'ATCA','00011101':'ATCT','00011110':'ATCG','00011111':'ATCC',
            '00100000':'AGAA','00100001':'AGAT','00100010':'AGAG','00100011':'AGAC',
            '00100100':'AGTA','00100101':'AGTT','00100110':'AGTG','00100111':'AGTC',
            '00101000':'AGGA','00101001':'AGGT','00101010':'AGGG','00101011':'AGGC',
            '00101100':'AGCA','00101101':'AGCT','00101110':'AGCG','00101111':'AGCC',
            '00110000':'ACAA','00110001':'ACAT','00110010':'ACAG','00110011':'ACAC',
            '00110100':'ACTA','00110101':'ACTT','00110110':'ACTG','00110111':'ACTC',
            '00111000':'ACGA','00111001':'ACGT','00111010':'ACGG','00111011':'ACGC',
            '00111100':'ACCA','00111101':'ACCT','00111110':'ACCG','00111111':'ACCC',
            '01000000':'TAAA','01000001':'TAAT','01000010':'TAAG','01000011':'TAAC',
            '01000100':'TATA','01000101':'TATT','01000110':'TATG','01000111':'TATC',
            '01001000':'TAGA','01001001':'TAGT','01001010':'TAGG','01001011':'TAGC',
            '01001100':'TACA','01001101':'TACT','01001110':'TACG','01001111':'TACC',
            '01010000':'TTAA','01010001':'TTAT','01010010':'TTAG','01010011':'TTAC',
            '01010100':'TTTA','01010101':'TTTT','01010110':'TTTG','01010111':'TTTC',
            '01011000':'TTGA','01011001':'TTGT','01011010':'TTGG','01011011':'TTGC',
            '01011100':'TTCA','01011101':'TTCT','01011110':'TTCG','01011111':'TTCC',
            '01100000':'TGAA','01100001':'TGAT','01100010':'TGAG','01100011':'TGAC',
            '01100100':'TGTA','01100101':'TGTT','01100110':'TGTG','01100111':'TGTC',
            '01101000':'TGGA','01101001':'TGGT','01101010':'TGGG','01101011':'TGGC',
            '01101100':'TGCA','01101101':'TGCT','01101110':'TGCG','01101111':'TGCC',
            '01110000':'TCAA','01110001':'TCAT','01110010':'TCAG','01110011':'TCAC',
            '01110100':'TCTA','01110101':'TCTT','01110110':'TCTG','01110111':'TCTC',
            '01111000':'TCGA','01111001':'TCGT','01111010':'TCGG','01111011':'TCGC',
            '01111100':'TCCA','01111101':'TCCT','01111110':'TCCG','01111111':'TCCC',
            '10000000':'GAAA','10000001':'GAAT','10000010':'GAAG','10000011':'GAAC',
            '10000100':'GATA','10000101':'GATT','10000110':'GATG','10000111':'GATC',
            '10001000':'GAGA','10001001':'GAGT','10001010':'GAGG','10001011':'GAGC',
            '10001100':'GACA','10001101':'GACT','10001110':'GACG','10001111':'GACC',
            '10010000':'GTAA','10010001':'GTAT','10010010':'GTAG','10010011':'GTAC',
            '10010100':'GTTA','10010101':'GTTT','10010110':'GTTG','10010111':'GTTC',
            '10011000':'GTGA','10011001':'GTGT','10011010':'GTGG','10011011':'GTGC',
            '10011100':'GTCA','10011101':'GTCT','10011110':'GTCG','10011111':'GTCC',
            '10100000':'GGAA','10100001':'GGAT','10100010':'GGAG','10100011':'GGAC',
            '10100100':'GGTA','10100101':'GGTT','10100110':'GGTG','10100111':'GGTC',
            '10101000':'GGGA','10101001':'GGGT','10101010':'GGGG','10101011':'GGGC',
            '10101100':'GGCA','10101101':'GGCT','10101110':'GGCG','10101111':'GGCC',
            '10110000':'GCAA','10110001':'GCAT','10110010':'GCAG','10110011':'GCAC',
            '10110100':'GCTA','10110101':'GCTT','10110110':'GCTG','10110111':'GCTC',
            '10111000':'GCGA','10111001':'GCGT','10111010':'GCGG','10111011':'GCGC',
            '10111100':'GCCA','10111101':'GCCT','10111110':'GCCG','10111111':'GCCC',
            '11000000':'CAAA','11000001':'CAAT','11000010':'CAAG','11000011':'CAAC',
            '11000100':'CATA','11000101':'CATT','11000110':'CATG','11000111':'CATC',
            '11001000':'CAGA','11001001':'CAGT','11001010':'CAGG','11001011':'CAGC',
            '11001100':'CACA','11001101':'CACT','11001110':'CACG','11001111':'CACC',
            '11010000':'CTAA','11010001':'CTAT','11010010':'CTAG','11010011':'CTAC',
            '11010100':'CTTA','11010101':'CTTT','11010110':'CTTG','11010111':'CTTC',
            '11011000':'CTGA','11011001':'CTGT','11011010':'CTGG','11011011':'CTGC',
            '11011100':'CTCA','11011101':'CTCT','11011110':'CTCG','11011111':'CTCC',
            '11100000':'CGAA','11100001':'CGAT','11100010':'CGAG','11100011':'CGAC',
            '11100100':'CGTA','11100101':'CGTT','11100110':'CGTG','11100111':'CGTC',
            '11101000':'CGGA','11101001':'CGGT','11101010':'CGGG','11101011':'CGGC',
            '11101100':'CGCA','11101101':'CGCT','11101110':'CGCG','11101111':'CGCC',
            '11110000':'CCAA','11110001':'CCAT','11110010':'CCAG','11110011':'CCAC',
            '11110100':'CCTA','11110101':'CCTT','11110110':'CCTG','11110111':'CCTC',
            '11111000':'CCGA','11111001':'CCGT','11111010':'CCGG','11111011':'CCGC',
            '11111100':'CCCA','11111101':'CCCT','11111110':'CCCG','11111111':'CCCC'
        }