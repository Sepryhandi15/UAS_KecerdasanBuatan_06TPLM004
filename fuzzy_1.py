
def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class nilaitugas():
    minimum = 40
    maximum = 90

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)

class nilaiuts():
    minimum = 50
    maximum = 90

    def naik(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def turun(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)

class nilaiuas():
    minimum = 50
    maximum = 85

    def naik(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def turun(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)


class nilaiakhir():
    minimum = 55
    maximum = 90
    Tgs = 0
    Uts = 0
    Uas = 0

    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def _inferensi(self, pmt=nilaitugas(), psd=nilaiuts(), uas=nilaiuas()):
        result = []
        # [R1] JIKA nilai tugas turun, dan nilai uts turun, dan nilai uas turun, MAKA
        # Nilai akhir NAIK.
        a1 = min(pmt.turun(self.Tgs), psd.turun(self.Uas), uas.turun(self.Uas))
        z1 = self._berkurang(a1)
        result.append((a1, z1))
        # [R2] JIKA nilai tugas turun, dan nilai uts turun, dan nilai uas turun, MAKA
        # Nilai akhir NAIK.
        a2 = min(pmt.turun(self.Tgs), psd.turun(self.Uas), uas.naik(self.Uas))
        z2 = self._berkurang(a2)
        result.append((a2, z2))
        # [R3] JIKA nilai tugas turun, dan nilai uts naik, dan nilai uas turun, MAKA
        # Nilai akhir NAIK.
        a3 = min(pmt.turun(self.Tgs), psd.naik(self.Uas), uas.turun(self.Uas))
        z3 = self._bertambah(a3)
        result.append((a3, z3))
        # [R4] JIKA nilai tugas naik, dan nilai uts turun, dan nilai uas turun, MAKA
        # Nilai akhir NAIK.
        a4 = min(pmt.naik(self.Tgs), psd.turun(self.Uas), uas.turun(self.Uas))
        z4 = self._bertambah(a4)
        result.append((a4, z4))
        # [R5] JIKA nilai tugas naik, dan nilai uts naik, dan nilai uas naik, MAKA
        # Nilai akhir NAIK.
        a5 = min(pmt.naik(self.Tgs), psd.naik(self.Uas), uas.naik(self.Uas))
        z5 = self._berkurang(a5)
        result.append((a5, z5))
        # [R6] JIKA nilai tugas turun, dan nilai uts naik, dan nilai uas naik, MAKA
        # Nilai akhir NAIK.
        a6 = min(pmt.turun(self.Tgs), psd.naik(self.Uas), uas.naik(self.Uas))
        z6 = self._berkurang(a6)
        result.append((a6, z6))
        # [R5] JIKA nilai tugas naik, dan nilai uts turun, dan nilai uas naik, MAKA
        # Nilai akhir NAIK.
        a7 = min(pmt.naik(self.Tgs), psd.turun(self.Uas), uas.naik(self.Uas))
        z7 = self._berkurang(a7)
        result.append((a7, z7))
        # [R5] JIKA nilai tugas naik, dan nilai uts naik, dan nilai uas turun, MAKA
        # Nilai akhir NAIK.
        a8 = min(pmt.naik(self.Tgs), psd.naik(self.Uas), uas.turun(self.Uas))
        z8 = self._berkurang(a8)
        result.append((a8, z8))
        
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a