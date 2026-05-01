def banda_radar(freq):
    if freq>=0 and freq<=2:
        banfrq =  'L'
    if freq>2 and freq<=4:
        banfrq =  'S'
    if freq>4 and freq<=8:
        banfrq =  'C'
    if freq>8 and freq<=12:
        banfrq =  'X'
    if freq>12 and freq<=18:
        banfrq =  'Ku'
    if freq>18 and freq<=27:
        banfrq =  'K'
    if freq>27 and freq<=40:
        banfrq =  'Ka'
    if freq>40 and freq<=75:
        banfrq =  'V'
    if freq>75 and freq<=110:
        banfrq =  "W"
    return "banda " + banfrq



def fosc(cadena):
    variable=0
    if cadena=='LP':
        variable=0
    elif cadena=='XT':
        variable=1
    elif cadena=='HS':
        variable=2
    else:
        variable=3
    return variable



def mnemonico(opcode):
    binario=bin(opcode).replace("0b","")
    if len(binario)<7:
        ceros=(7-(len(binario)))*'0'
        opcode='0b'+ceros+binario
    else:
        opcode = '0b' + binario
    if opcode=="0b0001110" or opcode=="0b0001111":
        return 'ADDWF'
    if opcode=="0b0001010" or opcode=="0b0001011":
        return 'ANDWF'
    if opcode=="0b0000011":
        return 'CLRF'
    if opcode=="0b0000010":
        return 'CLRW'
    if opcode=="0b0010010" or opcode=="0b0010011":
        return 'COMF'
    if opcode=="0b0000110" or opcode=="0b0000111":
        return 'DECF'
    if opcode=="0b0010110" or opcode=="0b0010111":
        return 'DECFSZ'
    if opcode=="0b0010100" or opcode=="0b0010101":
        return 'INCF'
    if opcode=="0b0011110" or opcode=="0b0011111":
        return 'INCFSZ'
    if opcode=="0b0001000" or opcode=="0b0001001":
        return 'IORWF'
    if opcode=="0b0010000" or opcode=="0b0010001":
        return 'MOVF'
    if opcode=="0b0000000":
        return 'NOP'
    if opcode=="0b0000001":
        return 'MOVWF'
    if opcode=="0b0011010" or opcode=="0b0011011":
        return 'RLF'
    if opcode=="0b0011000" or opcode=="0b0011001":
        return 'RRF'
    if opcode=="0b0000100" or opcode=="0b0000101":
        return 'SUBWF'
    if opcode=="0b0011100" or opcode=="0b0011101":
        return 'SWAPF'
    if opcode=="0b0001100" or opcode=="0b0001101":
        return'XORWF'



def uart_cfg(freq):
    if freq >= 1200 and freq < 2400:
        return 0,207
    if freq >= 2400 and freq < 9600:
        return 0,103
    if freq >= 9600 and freq < 10417:
        return 0,25
    if freq >= 10417 and freq < 19200:
        return 0,23
    if freq >= 19200 and freq < 57600:
        return 0,12
    if freq >= 9600 and freq < 10417:
        return 1,103
    if freq >= 10417 and freq < 19200:
        return 1,95
    if freq >= 19200 and freq < 57600:
        return 1,51
    if freq >= 57600 and freq < 115200:
        return 1,16
    if freq >= 115200:
        return 1,8



def dr_cfg(valor):
    if valor>0 and valor<=8:
        return 0
    if valor>8 and valor<=16:
        return 1
    if valor>16 and valor<=32:
        return 2
    if valor>32 and valor<=64:
        return 3
    if valor>64 and valor<=128:
        return 4
    if valor>128 and valor<=250:
        return 5
    if valor>250 and valor<=475:
        return 6
    if valor>475 and valor<=860:
        return 7



def pga_cfg(v):
    if v>6.144 and v<=4.096:
        return 0
    if v>4.096 and v<=2.048:
        return 1
    if v>2.048 and v<=1.024:
        return 2
    if v>1.024 and v<=0.512:
        return 3
    if v>0.512 and v<=0.256:
        return 4
    if v>0.256:
        return 5



def mux_cfg (e):
    if e==0:
        return 0b100
    if e==1:
        return 0b101
    if e==2:
        return 0b110
    if e==3:
        return 0b111



def xtor(t):
    if t=="BC546" or t=="BC547" or t=="BC548" or t=="BC549" or t=="BC550":
        return 'npn' and 'CBE'
    if t=="AC187":
        return 'npn' and 'CBE'
    if t=="CL100":
        return 'npn' and 'CBE'
    if t=="2N2222A":
        return 'npn' and 'EBC'
    if t=="2N3904":
        return 'npn' and 'EBC'
    if t=="TIP120" or t=="TIP121" or t=="TIP122":
        return 'npn' and 'BCE'
    if t=="BD139":
        return 'npn' and 'ECB'
    if t=="BC557":
        return 'pnp' and 'EBC'
    if t=="BC558":
        return 'pnp' and 'EBC'
    if t=="AC188":
        return 'pnp' and 'EBC'
    if t=="CK100":
        return 'pnp' and 'EBC'
    if t=="BD140":
        return 'pnp' and 'ECB'
    if t=="TIP125" and t=="TIP126" and t=="TIP127":
        return 'pnp' and 'BCE'
    if t=="MPSA92" and t=="MPSA42" and t=="MPSA44":
        return 'pnp' and 'EBC'
    if t=="BF494" and t=="BF495":
        return 'npn' and 'CEB'
    if t=="C2570":
        return 'npn' and 'BEC'
    if t=="C1730":
        return 'npn' and 'ECB'
    if t=="BD677":
        return 'npn' and 'BCE'



def dscp_meaning(dscp):
    binario = bin(dscp).replace("0b","")
    if dscp=="0b101110":
        return 'EF'
    if dscp=="0b000000":
        return 'BE'
    if dscp=="0b001010":
        return 'AF11'
    if dscp=="0b001100":
        return 'AF12'
    if dscp=="0b001110":
        return 'AF13'
    if dscp=="0b010010":
        return 'AF21'
    if dscp=="0b010100":
        return 'AF22'
    if dscp=="0b010110":
        return 'AF23'
    if dscp=="0b011010":
        return 'AF31'
    if dscp=="0b011100":
        return 'AF32'
    if dscp=="0b011110":
        return 'AF33'
    if dscp=="0b100010":
        return 'AF41'
    if dscp=="0b100100":
        return 'AF42'
    if dscp=="0b100110":
        return 'AF43'



def capacitor(code):
    f=1e-12
    tolerancia={"E":0.5,"F":1,"G":2,"H":3,"J":5,"K":10,"L":15,"M":20,"N":30}
    multiplicador = [0,10,100,1000,10000,100000,1,1,0.01,0.1]
    letras = list(tolerancia.keys())
    tercer = 0
    if len(code)==2:
        return int(code)*f, None
    if len(code)==3 and code[-1] not in letras:
        num = int(code[0]+code[1])
        tercer = int(code[2])
        return num*multiplicador[tercer]*f, None
    if len(code)==3 and code[-1] in letras:
        num = int(code[0]+code[1])
        return num*f, tolerancia[code[-1]]
    if len(code)==4 and code[-1] in letras:
        num = int(code[0]+code[1])
        tercer = int(code[2])
        return num*multiplicador[tercer]*f, tolerancia[code[-1]]





# Descomenta la siguiente línea y la última para ejecutar las pruebas
# Descomenta la siguiente línea y la última para ejecutar las pruebas
from unittest import TestCase, main

class Test(TestCase):

    def test_banda_radar(self):
        self.assertEqual(banda_radar(1.1), 'L')
        self.assertEqual(banda_radar(12.3), 'Ku')
        self.assertEqual(banda_radar(35), 'Ka')
        self.assertEqual(banda_radar(78), 'W')
        self.assertEqual(banda_radar(45), 'V')

    def test_fosc(self):
        self.assertEqual(fosc('LP'),0)
        self.assertEqual(fosc('XT'),1)
        self.assertEqual(fosc('HS'),2)
        self.assertEqual(fosc('RC'),3)

    def test_mnemonico(self):
        self.assertEqual(mnemonico(18),'COMF')
        self.assertEqual(mnemonico(0),'NOP')
        self.assertEqual(mnemonico(29),'SWAPF')
        self.assertEqual(mnemonico(2),'CLRW')
        self.assertEqual(mnemonico(15),'ADDWF')
        self.assertEqual(mnemonico(23),'DECFSZ')
        self.assertEqual(mnemonico(27),'RLF')
        self.assertEqual(mnemonico(11),'ANDWF')
        self.assertEqual(mnemonico(13),'XORWF')
        self.assertEqual(mnemonico(9),'IORWF')

    def test_uart_cfg(self):
        allcfg = set((
            #  rate, bgr, spbrgx
            (  1200, 0, 207),
            (  2400, 0, 103),
            (  9600, 0, 25),
            ( 10417, 0, 23),
            ( 19200, 0, 12),
            (  9600, 1, 103),
            ( 10417, 1, 95),
            ( 19200, 1, 51),
            ( 57600, 1, 16),
            (115200, 1, 8),
        ))
        allspd = set(x[0] for x in allcfg)
        for s in allspd:
            self.assertTrue((s,) + uart_cfg(s) in allcfg)

    def test_dr_cfg(self):
        rates = (8, 15, 32, 60, 128, 200, 475, 600 )
        for i, r in enumerate(rates):
            self.assertEqual(dr_cfg(r), i)

    def test_pga_cfg(self):
        allv = (6.144, 4., 2.048, 1., 0.512, 0.1)
        for i,v in enumerate(allv):
            self.assertEqual(pga_cfg(v), i)

    def test_mux_cfg(self):
        for i in range(4):
            self.assertEqual(mux_cfg(i), 4 + i)

    def test_xtor(self):
        modelos = (
            ('BC546', 'npn', 'CBE'),
            ('BC547', 'npn', 'CBE'),
            ('BC548', 'npn', 'CBE'),
            ('BC549', 'npn', 'CBE'),
            ('BC550', 'npn', 'CBE'),
            ('AC187', 'npn', 'CBE'),
            ('CL100', 'npn', 'CBE'),
            ('2N2222A', 'npn', 'EBC'),
            ('2N3904', 'npn', 'EBC'),
            ('TIP120', 'npn', 'BCE'),
            ('TIP121', 'npn', 'BCE'),
            ('TIP122', 'npn', 'BCE'),
            ('BD139', 'npn', 'ECB'),
            ('BC557', 'pnp', 'EBC'),
            ('BC558', 'pnp', 'EBC'),
            ('AC188', 'pnp', 'EBC'),
            ('CK100', 'pnp', 'EBC'),
            ('BD140', 'pnp', 'ECB'),
            ('TIP125', 'pnp', 'BCE'),
            ('TIP126', 'pnp', 'BCE'),
            ('TIP127', 'pnp', 'BCE'),
            ('MPSA92', 'pnp', 'EBC'),
            ('MPSA42', 'pnp', 'EBC'),
            ('MPSA44', 'pnp', 'EBC'),
            ('BF494', 'npn', 'CBE'),
            ('BF495', 'npn', 'CBE'),
            ('C2570', 'npn', 'BEC'),
            ('C1730', 'npn', 'ECB'),
            ('BD677', 'npn', 'BCE'),
        )
        for modelo, tipo, patas in modelos:
            self.assertEqual(xtor(modelo), (tipo, patas))

    def test_dscp_meaning(self):
        dm = ((46, 'EF'), (0, 'BE'), (10, 'AF11'), (12, 'AF12'), (14, 'AF13'), (18, 'AF21'), (20, 'AF22'), (22, 'AF23'), (26, 'AF31'), (28, 'AF32'), (30, 'AF33'), (34, 'AF41'), (36, 'AF42'), (38, 'AF43'))
        for v, m in dm:
            self.assertEqual(dscp_meaning(v), m)

    def test_capacitor(self):
        caps = (('12', 1.2e-11, None), ('121', 1.2e-10, None), ('12E', 1.2e-11, 0.5), ('122F', 1.2e-09, 1), ('129J', 1.2000000000000001e-12, 5), ('208L', 2e-13, 15), ('105N', 1e-06, 30))
        for l, c, t in caps:
            c1, t1 = capacitor(l)
            self.assertAlmostEqual(c1, c)
            self.assertEqual(t1,t)

# Si usas Jupyter descomenta la segunda línea
main() # IDLE, Python, PyCharm
# main(argv=['first-arg-is-ignored'], exit=False) # Jupyter