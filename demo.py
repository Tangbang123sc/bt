class SinhVien:
    def __init__(self, id, name, sex, age, diemToan, diemLy, diemHoa):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age
        self._diemToan = diemToan
        self._diemLy = diemLy
        self._diemHoa = diemHoa
        self._diemTB = 0
        self._hocLuc = ""
    listSinhVien = []

    # Hàm tạo ID
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()


    def nhapSinhVien(self):
        # Khởi tạo một sinh viên mới
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        diemToan = float(input("Nhập điểm Toán: "))
        diemLy = float(input("Nhập điểm Lý: "))
        diemHoa = float(input("Nhập điểm Hóa: "))
        sv = SinhVien(svId, name, sex, age, diemToan, diemLy, diemHoa)
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
 
    # def updateSinhVien(self, ID):
    #     # Tìm kiếm sinh viên trong danh sách listSinhVien
    #     sv:SinhVien = self.findByID(ID)
    #     # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
    #     if (sv != None):
    #         # nhập thông tin sinh viên
    #         name = input("Nhập tên sinh viên: ")
    #         sex = input("Nhập giới tính sinh viên: ")
    #         age = int(input("Nhập tuổi sinh viên: "))
    #         diemToan = float(input("Nhập điểm Toán: "))
    #         diemLy = float(input("Nhập điểm Lý: "))
    #         diemHoa = float(input("Nhập điểm Hóa: "))
    #         # cập nhật thông tin sinh viên
    #         sv._name = name
    #         sv._sex = sex
    #         sv._age = age
    #         sv._diemToan = diemToan
    #         sv._diemLy = diemLy
    #         sv._diemHoa = diemHoa
    #         self.tinhDTB(sv)
    #         self.xepLoaiHocLuc(sv)
    #     else:
    #         print("Sinh viên có ID = {} không tồn tại.".format(ID))
 
    # # Hàm xóa sinh viên theo ID
    # def deleteById(self, ID):
    #     isDeleted = False
    #     # tìm kiếm sinh viên theo ID
    #     sv = self.findByID(ID)
    #     if (sv != None):
    #         self.listSinhVien.remove(sv)
    #         isDeleted = True
    #     return isDeleted

    # # Hàm tìm kiếm sinh viên theo tên
    # # Trả về một danh sách sinh viên
    # def findByName(self, keyword):
    #     listSV = []
    #     if (self.soLuongSinhVien() > 0):
    #         for sv in self.listSinhVien:
    #             if (keyword.upper() in sv._name.upper()):
    #                 listSV.append(sv)
    #     return listSV

    # Hàm tính điểm TB cho sinh viên
    def tinhDTB(self, sv):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
        # làm tròn điểm trung binh với 2 chữ số thập phân
        sv._diemTB = math.ceil(diemTB * 100) / 100
    #Hàm xếp loại học lực cho nhân viên
    def xepLoaiHocLuc(self, sv):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"
    
    # # Hàm sắp xếp danh sach sinh vien theo điểm TB tăng dần
    # def sortByDiemTB(self):
    #     self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    # #Hàm sắp xếp danh sach sinh vien theo tên tăng dần
    # def sortByName(self):
    #     self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    # Hàm hiển thị danh sách sinh viên ra màn hình console
    def showSinhVien(self, listSV):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
            .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        # hien thi danh sach sinh vien
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                    .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                            sv._diemHoa,sv._diemTB, sv._hocLuc))
        print("\n")

import math
class QuanLySinhVien:
    listSinhVien = []
    # Hàm tạo ID 
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
 
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
 
    def nhapSinhVien(self):
        # Khởi tạo một sinh viên mới
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        diemToan = float(input("Nhập điểm Toán: "))
        diemLy = float(input("Nhập điểm Lý: "))
        diemHoa = float(input("Nhập điểm Hóa: "))
        sv = SinhVien(svId, name, sex, age, diemToan, diemLy, diemHoa)
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        sv:SinhVien = self.findByID(ID)
        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if (sv != None):
            # nhập thông tin sinh viên
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            age = int(input("Nhập tuổi sinh viên: "))
            diemToan = float(input("Nhập điểm Toán: "))
            diemLy = float(input("Nhập điểm Lý: "))
            diemHoa = float(input("Nhập điểm Hóa: "))
            # cập nhật thông tin sinh viên
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._diemToan = diemToan
            sv._diemLy = diemLy
            sv._diemHoa = diemHoa
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại.".format(ID))
 
    # Hàm sắp xếp danh sach sinh vien theo ID tăng dần
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
 
    #Hàm sắp xếp danh sach sinh vien theo tên tăng dần
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
 
    # Hàm sắp xếp danh sach sinh vien theo điểm TB tăng dần
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
 
    # Hàm tìm kiếm sinh viên theo ID
    # Trả về một sinh viên
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
 
    # Hàm tìm kiếm sinh viên theo tên
    # Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
 
    # Hàm xóa sinh viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    # Hàm tính điểm TB cho sinh viên
    def tinhDTB(self, sv):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
        # làm tròn điểm trung binh với 2 chữ số thập phân
        sv._diemTB = math.ceil(diemTB * 100) / 100
 
    #Hàm xếp loại học lực cho nhân viên
    def xepLoaiHocLuc(self, sv):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"

    # Hàm hiển thị danh sách sinh viên ra màn hình console
def showSinhVien(self, listSV):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Điểm TB", "Học Lực"))
        # hien thi danh sach sinh vien
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                              sv._diemHoa,sv._diemTB, sv._hocLuc))
        print("\n")
 
    # Hàm trả về danh sách sinh viên hiện tại
def getListSinhVien(self):
        return self.listSinhVien

# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ###")
    print("*************************MENU**************************")
    print("**  1. Thêm sinh viên.                               **")
    print("**  2. Cập nhật thông tin sinh viên bởi ID.          **")
    print("**  3. Xóa sinh viên bởi ID.                         **")
    print("**  4. Tìm kiếm sinh viên theo tên.                  **")
    print("**  5. Sắp xếp sinh viên theo điểm trung bình (GPA). **")
    print("**  6. Sắp xếp sinh viên theo tên.                   **")
    print("**  7. Sắp xếp sinh viên theo ID.                    **")
    print("**  8. Hiển thị danh sách sinh viên.                 **")
    print("**  0. Thoát chương trình.                           **")
    print("*******************************************************")
     
    key = int(input("Mời bạn chọn chức năng: "))
    if (key == 1):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên. ")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có id = ", ID, " đã bị xóa.")
            else:
                print("\nSinh viên có id = ", ID ," không tồn tại.")
        else:
            print("\nDanh sách sinh viên trong!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trong!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trong!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trong!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo ID.")
            qlsv.sortByID()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trong!")
    elif (key == 8):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trong!!")
    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình!")
        break
    else:
        print("\nKhông có chức năng này!")
        print("\nHãy chọn chức năng trong menu.")
