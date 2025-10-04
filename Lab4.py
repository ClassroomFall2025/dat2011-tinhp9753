def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500,8800,12000,24000)
    if so_nuoc <= 10 and so_nuoc >= 0:
        tien_nuoc_thang = so_nuoc*gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tinh_nuoc_thang = 10 * gia_ban_nuoc[0] * (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tinh_nuoc_thang = 10 * gia_ban_nuoc[0] * 10* gia_ban_nuoc[1] + (so_nuoc - 20)* gia_ban_nuoc[2]
    elif so_nuoc <= 40:
         tinh_nuoc_thang = 10 * gia_ban_nuoc[0] + 10* gia_ban_nuoc[1] + 10 *gia_ban_nuoc[2] +(so_nuoc -30)* gia_ban_nuoc[3]
         return tien_nuoc_thang
    
   

def tinh_nguyen_lieu(s1_bdx, s1_btc, s1_db):
    banh_dau_xanh = {"đường":0.04, "đậu":0.07}
    banh_thuc_cam = {"đường":0.06, "đậu": 0}
    banh_deo = {"đường":0.05, "đậu":0.02}
    duong_hop_banh = s1_bdx*banh_dau_xanh["đường"] + s1_btc*banh_thuc_cam["đường"] + s1_db*banh_deo["đường"]
    dau_hop_banh = s1_bdx*banh_dau_xanh["đậu"] + s1_btc*banh_thuc_cam["đậu"] + s1_db*banh_deo["đậu"]
    nguyen_lieu = {}  # Thêm dòng này để khai báo dictionary
    nguyen_lieu["đường"] = duong_hop_banh
    nguyen_lieu["dầu"] = dau_hop_banh
    return nguyen_lieu

