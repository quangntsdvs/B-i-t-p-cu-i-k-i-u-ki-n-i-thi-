class BaiHat:
    def __init__(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.ten_bai_hat = ten_bai_hat
        self.ten_nhac_si = ten_nhac_si
        self.ten_ca_si = ten_ca_si

class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.danh_sach_bai_hat = []

    def them_bai_hat(self, bai_hat):
        self.danh_sach_bai_hat.append(bai_hat)

class TuDien:
    def __init__(self):
        self.danh_sach_album = {}

    def bam(self, ten):
        return ten.lower()

    def nhap_album(self):
        ten_album = input("Nhập tên album: ")
        album = Album(ten_album)

        so_bai_hat = int(input("Nhập số lượng bài hát trong album: "))
        for i in range(so_bai_hat):
            ten_bai_hat = input("Nhập tên bài hát: ")
            ten_nhac_si = input("Nhập tên nhạc sĩ sáng tác: ")
            ten_ca_si = input("Nhập tên ca sĩ: ")
            bai_hat = BaiHat(ten_bai_hat, ten_nhac_si, ten_ca_si)
            album.them_bai_hat(bai_hat)

        self.danh_sach_album[self.bam(ten_album)] = album

    def xem_album(self, ten):
        if ten in self.danh_sach_album:
            album = self.danh_sach_album[ten]
            print("Tên album:", album.ten_album)
            print("Danh sách bài hát:")
            for bai_hat in album.danh_sach_bai_hat:
                print("- Tên bài hát:", bai_hat.ten_bai_hat)
                print("  Tên nhạc sĩ:", bai_hat.ten_nhac_si)
                print("  Tên ca sĩ:", bai_hat.ten_ca_si)
        else:
            print("Không tìm thấy album.")

tu_dien = TuDien()

tu_dien.nhap_album()

ten_album_can_xem = input("Nhập tên album cần xem: ")
tu_dien.xem_album(tu_dien.bam(ten_album_can_xem))