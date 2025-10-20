class nhanvien: 
    def __init__(self,nhanvien, hoten, luong):
     self.nhanvien = nhanvien
     self.hoten = hoten
     self.luong = luong
     
     def getthunhap(self):
        return self.luong
     
     def get_thue_thu_nhap(self):
        thu_nhap = (self.get_thu_nhap())
        if thu_nhap <= 50000:
            return 0
        elif thu_nhap <= 5000000:
            return (thu_nhap - 50000) * 0.10
        else:
            thue_bac_1 = (5000000 - 50000) * 0.10
            thue_bac_2 = (thu_nhap - 5000000) * 0.12
            return thue_bac_1 + thue_bac_2
     
     def __str__(self):
        return f" {self.nhanvien:<10}{self.hoten:<20}{self.tiepthi:<10.2()}{self.truongphong:<10.2f}"
     
     class tiepthi(nhanvien):
        def __init__(self, nhanvien, hoten, luong, doanhsoNV, hoahong):
           super().__init__(nhanvien, hoten, luong)
           self.doanhsoNV = doanhsoNV
           self.hoahong = hoahong

        def getthunhap(self):
           return self.luonh + self.doanhsoNV * self.hoahong
            
     class truongphong(nhanvien):   
         def __init__(self, nhanvien, hoten, luong, phucap):
            super().__init__(self, nhanvien, hoten, luong)
            self.phucap = phucap

         def getthunhap(self):
            return self.luong + self.phucap
        
    