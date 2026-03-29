# oop: object-oriented promgramming
# tao lop vat nuoi(giong, mau sac, tuoi, can nang)

# VatNuoi: kieu du lieu tham chieu (doi tuong)
class Vatnuoi:
    # khai bao thuoc tinh
    def __init__(self, giong="", mauSac="", tuoi=0, canNang=0):
        # __ : private
        self.__giong = giong
        self.__mauSac = mauSac
        self.__tuoi = tuoi
        self.__canNang = canNang

    def __str__(self) -> str:
        return f"VatNuoi: {self.__giong}, {self.__mauSac}, {self.__tuoi}, {self.__canNang}"

    # getter va setter (lay va cai dat gia tri thuoc tinh)
    # "get"/"set" + ten thuoc tinh
    def getGiong (self):
        return self.__giong

    def getMauSac (self):
        return self.__mauSac

    def gettuoi (self):
        return self.__tuoi

    def getCanNang (self):
        return self.__canNang

    def setGiong (self, giongMoi):
        self.__giong = giongMoi

    def setMauSac (self, mauSacmoi):
        self.__mauSac = mauSacmoi

    def settuoi (self, tuoiMoi):
        self.__tuoi = tuoiMoi

    def setCanNang (self, canNangMoi):
        self.__canNang = canNangMoi

# tao doi tuong
meo1 = Vatnuoi("meo", "den")
print(meo1)