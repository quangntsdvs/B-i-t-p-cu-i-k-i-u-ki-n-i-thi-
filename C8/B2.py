class TuDien:
    def __init__(self):
        self.danh_sach_tu = {}

    def bam(self, tu):
        return tu[0].lower()

    def nhap_tu(self):
        tu = input("Nhập từ: ").strip()
        dong_nghia = input("Nhập các từ đồng nghĩa, cách nhau bởi dấu phẩy (nếu có): ").split(',')
        trai_nghia = input("Nhập các từ trái nghĩa, cách nhau bởi dấu phẩy (nếu có): ").split(',')
        self.danh_sach_tu[tu] = {'dong_nghia': dong_nghia, 'trai_nghia': trai_nghia}

    def dong_nghia(self, tu):
        if tu in self.danh_sach_tu:
            return self.danh_sach_tu[tu]['dong_nghia']
        else:
            return []

    def trai_nghia(self, tu):
        if tu in self.danh_sach_tu:
            return self.danh_sach_tu[tu]['trai_nghia']
        else:
            return []


tu_dien = TuDien()

tu_dien.nhap_tu()

tu_can_tra_cuu = input("Nhập từ cần tra cứu: ").strip()
print("Từ đồng nghĩa:", tu_dien.dong_nghia(tu_can_tra_cuu))
print("Từ trái nghĩa:", tu_dien.trai_nghia(tu_can_tra_cuu))
