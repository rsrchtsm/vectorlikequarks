# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.0 for Linux x86 (64-bit) (May 10, 2021)
# Date: Tue 15 Nov 2022 22:00:59


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.eta,P.bp):'((3*CPhiL**2*MB**2 + 3*CPhiR**2*MB**2 + 12*CPhiL*CPhiR*MB*MBP + 3*CPhiL**2*MBP**2 + 3*CPhiR**2*MBP**2 - 3*CPhiL**2*Meta**2 - 3*CPhiR**2*Meta**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*Meta**2 - 2*MBP**2*Meta**2 + Meta**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.H,P.bp):'((3*CHL**2*MB**2 + 3*CHR**2*MB**2 + 12*CHL*CHR*MB*MBP + 3*CHL**2*MBP**2 + 3*CHR**2*MBP**2 - 3*CHL**2*MH**2 - 3*CHR**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MH**2 - 2*MBP**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.Z,P.bp):'(((3*CZL**2*ee**2*MB**2)/(4.*cw**2*sw**2) + (3*CZR**2*ee**2*MB**2)/(4.*cw**2*sw**2) - (9*CZL*CZR*ee**2*MB*MBP)/(cw**2*sw**2) + (3*CZL**2*ee**2*MBP**2)/(4.*cw**2*sw**2) + (3*CZR**2*ee**2*MBP**2)/(4.*cw**2*sw**2) + (3*CZL**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZR**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZL**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) - (3*CZR**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) + (3*CZL**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZR**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZL**2*ee**2*MZ**2)/(2.*cw**2*sw**2) - (3*CZR**2*ee**2*MZ**2)/(2.*cw**2*sw**2))*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MZ**2 - 2*MBP**2*MZ**2 + MZ**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_bp = Decay(name = 'Decay_bp',
                 particle = P.bp,
                 partial_widths = {(P.eta,P.b):'((3*CPhiL**2*MB**2 + 3*CPhiR**2*MB**2 + 12*CPhiL*CPhiR*MB*MBP + 3*CPhiL**2*MBP**2 + 3*CPhiR**2*MBP**2 - 3*CPhiL**2*Meta**2 - 3*CPhiR**2*Meta**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*Meta**2 - 2*MBP**2*Meta**2 + Meta**4))/(96.*cmath.pi*abs(MBP)**3)',
                                   (P.H,P.b):'((3*CHL**2*MB**2 + 3*CHR**2*MB**2 + 12*CHL*CHR*MB*MBP + 3*CHL**2*MBP**2 + 3*CHR**2*MBP**2 - 3*CHL**2*MH**2 - 3*CHR**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MH**2 - 2*MBP**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP)**3)',
                                   (P.W__minus__,P.t):'((3*CWL**2*MBP**2 + 3*CWL**2*MT**2 + (3*CWL**2*MBP**4)/MW**2 - (6*CWL**2*MBP**2*MT**2)/MW**2 + (3*CWL**2*MT**4)/MW**2 - 6*CWL**2*MW**2)*cmath.sqrt(MBP**4 - 2*MBP**2*MT**2 + MT**4 - 2*MBP**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MBP)**3)',
                                   (P.Z,P.b):'(((3*CZL**2*ee**2*MB**2)/(4.*cw**2*sw**2) + (3*CZR**2*ee**2*MB**2)/(4.*cw**2*sw**2) - (9*CZL*CZR*ee**2*MB*MBP)/(cw**2*sw**2) + (3*CZL**2*ee**2*MBP**2)/(4.*cw**2*sw**2) + (3*CZR**2*ee**2*MBP**2)/(4.*cw**2*sw**2) + (3*CZL**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZR**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZL**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) - (3*CZR**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) + (3*CZL**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZR**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZL**2*ee**2*MZ**2)/(2.*cw**2*sw**2) - (3*CZR**2*ee**2*MZ**2)/(2.*cw**2*sw**2))*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MZ**2 - 2*MBP**2*MZ**2 + MZ**4))/(96.*cmath.pi*abs(MBP)**3)'})

Decay_eta = Decay(name = 'Decay_eta',
                  particle = P.eta,
                  partial_widths = {(P.b,P.b__tilde__):'((-24*CbbPhi**2*MB**2 + 6*CbbPhi**2*Meta**2)*cmath.sqrt(-4*MB**2*Meta**2 + Meta**4))/(16.*cmath.pi*abs(Meta)**3)',
                                    (P.b,P.bp__tilde__):'((-3*CPhiL**2*MB**2 - 3*CPhiR**2*MB**2 - 12*CPhiL*CPhiR*MB*MBP - 3*CPhiL**2*MBP**2 - 3*CPhiR**2*MBP**2 + 3*CPhiL**2*Meta**2 + 3*CPhiR**2*Meta**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*Meta**2 - 2*MBP**2*Meta**2 + Meta**4))/(16.*cmath.pi*abs(Meta)**3)',
                                    (P.bp,P.b__tilde__):'((-3*CPhiL**2*MB**2 - 3*CPhiR**2*MB**2 - 12*CPhiL*CPhiR*MB*MBP - 3*CPhiL**2*MBP**2 - 3*CPhiR**2*MBP**2 + 3*CPhiL**2*Meta**2 + 3*CPhiR**2*Meta**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*Meta**2 - 2*MBP**2*Meta**2 + Meta**4))/(16.*cmath.pi*abs(Meta)**3)',
                                    (P.g,P.g):'(2*G**4*kge**2*Meta**6)/(cmath.pi*vev**2*abs(Meta)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.b,P.bp__tilde__):'((-3*CHL**2*MB**2 - 3*CHR**2*MB**2 - 12*CHL*CHR*MB*MBP - 3*CHL**2*MBP**2 - 3*CHR**2*MBP**2 + 3*CHL**2*MH**2 + 3*CHR**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MH**2 - 2*MBP**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp,P.b__tilde__):'((-3*CHL**2*MB**2 - 3*CHR**2*MB**2 - 12*CHL*CHR*MB*MBP - 3*CHL**2*MBP**2 - 3*CHR**2*MBP**2 + 3*CHL**2*MH**2 + 3*CHR**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MH**2 - 2*MBP**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.bp):'((3*CWL**2*MBP**2 + 3*CWL**2*MT**2 + (3*CWL**2*MBP**4)/MW**2 - (6*CWL**2*MBP**2*MT**2)/MW**2 + (3*CWL**2*MT**4)/MW**2 - 6*CWL**2*MW**2)*cmath.sqrt(MBP**4 - 2*MBP**2*MT**2 + MT**4 - 2*MBP**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.bp__tilde__):'((-3*CWL**2*MBP**2 - 3*CWL**2*MT**2 - (3*CWL**2*MBP**4)/MW**2 + (6*CWL**2*MBP**2*MT**2)/MW**2 - (3*CWL**2*MT**4)/MW**2 + 6*CWL**2*MW**2)*cmath.sqrt(MBP**4 - 2*MBP**2*MT**2 + MT**4 - 2*MBP**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.bp__tilde__):'(((-3*CZL**2*ee**2*MB**2)/(4.*cw**2*sw**2) - (3*CZR**2*ee**2*MB**2)/(4.*cw**2*sw**2) + (9*CZL*CZR*ee**2*MB*MBP)/(cw**2*sw**2) - (3*CZL**2*ee**2*MBP**2)/(4.*cw**2*sw**2) - (3*CZR**2*ee**2*MBP**2)/(4.*cw**2*sw**2) - (3*CZL**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZR**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZL**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) + (3*CZR**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) - (3*CZL**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZR**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZL**2*ee**2*MZ**2)/(2.*cw**2*sw**2) + (3*CZR**2*ee**2*MZ**2)/(2.*cw**2*sw**2))*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MZ**2 - 2*MBP**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.bp,P.b__tilde__):'(((-3*CZL**2*ee**2*MB**2)/(4.*cw**2*sw**2) - (3*CZR**2*ee**2*MB**2)/(4.*cw**2*sw**2) + (9*CZL*CZR*ee**2*MB*MBP)/(cw**2*sw**2) - (3*CZL**2*ee**2*MBP**2)/(4.*cw**2*sw**2) - (3*CZR**2*ee**2*MBP**2)/(4.*cw**2*sw**2) - (3*CZL**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZR**2*ee**2*MB**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZL**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) + (3*CZR**2*ee**2*MB**2*MBP**2)/(2.*cw**2*MZ**2*sw**2) - (3*CZL**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) - (3*CZR**2*ee**2*MBP**4)/(4.*cw**2*MZ**2*sw**2) + (3*CZL**2*ee**2*MZ**2)/(2.*cw**2*sw**2) + (3*CZR**2*ee**2*MZ**2)/(2.*cw**2*sw**2))*cmath.sqrt(MB**4 - 2*MB**2*MBP**2 + MBP**4 - 2*MB**2*MZ**2 - 2*MBP**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

