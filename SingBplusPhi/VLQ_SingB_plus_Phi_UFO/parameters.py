# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.0 for Linux x86 (64-bit) (May 10, 2021)
# Date: Tue 15 Nov 2022 22:00:59



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
kge = Parameter(name = 'kge',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\text{kge}',
                lhablock = 'PhiCouplings',
                lhacode = [ 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

MUB1 = Parameter(name = 'MUB1',
                 nature = 'external',
                 type = 'real',
                 value = 10.,
                 texname = '\\text{MUB1}',
                 lhablock = 'VLQMixing',
                 lhacode = [ 1 ])

MUB2 = Parameter(name = 'MUB2',
                 nature = 'external',
                 type = 'real',
                 value = 25.,
                 texname = '\\text{MUB2}',
                 lhablock = 'VLQMixing',
                 lhacode = [ 2 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

LambdaA = Parameter(name = 'LambdaA',
                    nature = 'external',
                    type = 'real',
                    value = 0.3,
                    texname = '\\text{LambdaA}',
                    lhablock = 'FRBlock',
                    lhacode = [ 1 ])

LambdaB = Parameter(name = 'LambdaB',
                    nature = 'external',
                    type = 'real',
                    value = 0.3,
                    texname = '\\text{LambdaB}',
                    lhablock = 'FRBlock',
                    lhacode = [ 2 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MBP = Parameter(name = 'MBP',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MBP}',
                lhablock = 'MASS',
                lhacode = [ 6000007 ])

Meta = Parameter(name = 'Meta',
                 nature = 'external',
                 type = 'real',
                 value = 400,
                 texname = '\\text{Meta}',
                 lhablock = 'MASS',
                 lhacode = [ 6000025 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WBP = Parameter(name = 'WBP',
                nature = 'external',
                type = 'real',
                value = 10,
                texname = '\\text{WBP}',
                lhablock = 'DECAY',
                lhacode = [ 6000007 ])

Weta = Parameter(name = 'Weta',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{Weta}',
                 lhablock = 'DECAY',
                 lhacode = [ 6000025 ])

cosThPsiL = Parameter(name = 'cosThPsiL',
                      nature = 'internal',
                      type = 'real',
                      value = 'cmath.cos(0.5*cmath.atan((2*(MBP*MUB1 + MB*MUB2))/(MB**2 - MBP**2 + MUB1**2 - MUB2**2)))',
                      texname = '\\text{cosThPsiL}')

cosThPsiR = Parameter(name = 'cosThPsiR',
                      nature = 'internal',
                      type = 'real',
                      value = 'cmath.cos(0.5*cmath.atan((2*(MB*MUB1 + MBP*MUB2))/(MB**2 - MBP**2 - MUB1**2 + MUB2**2)))',
                      texname = '\\text{cosThPsiR}')

sineThPsiL = Parameter(name = 'sineThPsiL',
                       nature = 'internal',
                       type = 'real',
                       value = 'cmath.sin(0.5*cmath.atan((2*(MBP*MUB1 + MB*MUB2))/(MB**2 - MBP**2 + MUB1**2 - MUB2**2)))',
                       texname = '\\text{sineThPsiL}')

sineThPsiR = Parameter(name = 'sineThPsiR',
                       nature = 'internal',
                       type = 'real',
                       value = 'cmath.sin(0.5*cmath.atan((2*(MB*MUB1 + MBP*MUB2))/(MB**2 - MBP**2 - MUB1**2 + MUB2**2)))',
                       texname = '\\text{sineThPsiR}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

CZR = Parameter(name = 'CZR',
                nature = 'internal',
                type = 'real',
                value = '0.',
                texname = '\\text{CZR}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

CbbPhi = Parameter(name = 'CbbPhi',
                   nature = 'internal',
                   type = 'real',
                   value = 'cosThPsiR*LambdaB*sineThPsiL - LambdaA*sineThPsiL*sineThPsiR',
                   texname = '\\text{CbbPhi}')

CPhiL = Parameter(name = 'CPhiL',
                  nature = 'internal',
                  type = 'real',
                  value = '-(cosThPsiL*cosThPsiR*LambdaB) + cosThPsiL*LambdaA*sineThPsiL',
                  texname = '\\text{CPhiL}')

CPhiR = Parameter(name = 'CPhiR',
                  nature = 'internal',
                  type = 'real',
                  value = 'cosThPsiR*LambdaA*sineThPsiL + LambdaB*sineThPsiL*sineThPsiR',
                  texname = '\\text{CPhiR}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

CHL = Parameter(name = 'CHL',
                nature = 'internal',
                type = 'real',
                value = '(cosThPsiR*MB*sineThPsiL - MUB1*sineThPsiL*sineThPsiR)/vev',
                texname = '\\text{CHL}')

CHR = Parameter(name = 'CHR',
                nature = 'internal',
                type = 'real',
                value = '(cosThPsiL*cosThPsiR*MUB1 + cosThPsiL*MB*sineThPsiR)/vev',
                texname = '\\text{CHR}')

CWL = Parameter(name = 'CWL',
                nature = 'internal',
                type = 'real',
                value = '(gw*sineThPsiL)/cmath.sqrt(2)',
                texname = '\\text{CWL}')

CZL = Parameter(name = 'CZL',
                nature = 'internal',
                type = 'real',
                value = '-((cosThPsiL*gw*sineThPsiL)/cw)',
                texname = '\\text{CZL}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

