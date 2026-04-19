class Hocsinh:
    def __init__(self, hoTen="", diaChi="", chieuCao=0, canNang=0, hocLuc=""):
        self.__hoTen = hoTen
        self.__diaChi = diaChi
        self.__chieuCao = chieuCao
        self.__canNang = canNang
        self.__hocLuc = hocLuc

    def __str__(self) -> str:
        return f"Hocsinh: {self.__hoTen}, {self.__diaChi}, {self.__chieuCao}, {self.__canNang}, {self.__hocLuc}"

    def getHoTen (self):
        return self.__hoTen

    def getDiaChi (self):
        return self.__diaChi

    def getChieuCao (self):
        return self.__chieuCao

    def getCanNang (self):
        return self.__canNang
    
    def getHocLuc (self):
        return self.__hocLuc

    def setHoTen (self, hoTenMoi):
        if hoTenMoi == "": print("Gia tri khong duoc de trong")
        else: self.__hoTen = hoTenMoi
 
    def setDiaChi (self, diaChiMoi):
        if diaChiMoi == "": print("Gia tri khong duoc de trong")
        else: self.__diaChi = diaChiMoi

    def setChieuCao (self, chieuCaoMoi):
        if chieuCaoMoi == "": print("Gia tri khong duoc la so am")
        else: self.__chieuCao = chieuCaoMoi

    def setCanNang (self, canNangMoi):
        if canNangMoi == "": print("Gia tri khong duoc la so am")
        else: self.__canNang = canNangMoi

    def setHocLuc (self, hocLucMoi):
        if hocLucMoi == "": print("Gia tri khong duoc de trong")
        else: self.__hocLuc = hocLucMoi

Hocsinh1 = Hocsinh("Nguyen Van A", "TP.HO CHI MINH", "Gioi")

Hocsinh1.setChieuCao(chieuCaoMoi=150)

Hocsinh1.setCanNang(canNangMoi=45)

print(Hocsinh1)