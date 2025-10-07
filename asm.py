menu = """1. Nhap danh sach nhan vien
        2. Doc thong tin nhan vien
        3. Tim và hien thi nhan vien theo ma
        4. Xoa nhan vien
        5. Cap nhat thong tin nhan vien
        6. Tim cac nhan vien theo khoang luong
        7. Sap xep nhan vien theo ho va ten
        8. Sap xep nhan vien theo thu nhap
        9. Xuat 5 nhan vien co thu nhap cao nhat"""
while True:
    print(menu)
    lua_chon = input("Nhap lua chon cua ban (0 de thoat): ")
    match lua_chon:
        case "0":
            print("Thoat chuong trinh")
            break
        case "1":
            print("Nhap danh sach nhan vien")
        case "2":
            print("Doc thong tin nhan vien")
        case "3":
            print("Tim va hien thi nhan vien theo ma")
        case "4":
            print("Xoa nhan vien")
        case "5":
            print("Cap nhat thong tin nhan vien")
        case "6":
            print("Tim cac nhan vien theo khoang luong")
        case "7":
            print("Sap xep nhan vien theo ho va ten")
        case "8":
            print("Sap xep nhan vien theo thu nhap")
        case "9":
            print("Xuat 5 nhan vien co thu nhap cao nhat")
        case "00":
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")