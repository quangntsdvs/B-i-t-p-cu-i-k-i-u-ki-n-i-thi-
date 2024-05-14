class TuDien:
    def __init__(self):
        self.danh_sach_tu = {}

    def NhapTu(self):
        tu = input("Nhập từ: ").strip()
        dongnghia = input("Nhập từ đồng nghĩa (nếu có): ").strip()
        trai_nguoc = input("Nhập từ trái nghĩa (nếu có): ").strip()

        key = tu[0].lower()

        if key in self.danh_sach_tu:
            self.danh_sach_tu[key][tu] = {"dongnghia": dongnghia, "trai_nguoc": trai_nguoc}
        else:
            self.danh_sach_tu[key] = {tu: {"dongnghia": dongnghia, "trai_nguoc": trai_nguoc}}

    def TraTu(self, tu):
        key = tu[0].lower()

        if key in self.danh_sach_tu and tu in self.danh_sach_tu[key]:
            return self.danh_sach_tu[key][tu]
        else:
            return {"dongnghia": None, "trai_nguoc": None}

tudien = TuDien()

while True:
    print("\n1. Nhập từ vào từ điển")
    print("2. Tra cứu từ trong từ điển")
    print("3. Thoát")
    choice = input("Chọn chức năng (1/2/3): ")

    if choice == '1':
        tudien.NhapTu()
    elif choice == '2':
        tu_can_tra_cuu = input("Nhập từ cần tra cứu: ").strip()
        ket_qua = tudien.TraTu(tu_can_tra_cuu)
        print("Từ đồng nghĩa:", ket_qua["dongnghia"])
        print("Từ trái nghĩa:", ket_qua["trai_nguoc"])
    elif choice == '3':
        print("Đã thoát chương trình.")
        break
    else:
        print("Chọn không hợp lệ. Vui lòng chọn lại.")