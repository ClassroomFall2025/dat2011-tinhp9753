
class sinhvien :
    # các thuộc tính 
    ten_sinh_vien = ""
    nam_sinh = ""
    diem = ""
    
    # các phương thức
    def them_sinh_vien(self, ten, namsinh, diem):
        self.ten_sinh_vien = ten
        self.nam_sinh = namsinh
        self.diem = diem
    def hien_thi_thong_tin(self):
        print(f"Tên sinh viên: {self.ten_sinh_vien}")
        print(f"Năm sinh: {self.nam_sinh}")
        print(f"Điểm: {self.diem}")