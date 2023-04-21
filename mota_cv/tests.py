 di =32
        min1 = 105
        min2 = min1 +di +1

        min3 = min2+di +1
        min4 = min3 +di +1
        min5 = min4 +di +1
        print(min1,min2, min3, min4, min5)
        min6 = min5 +di +1
        min7 = min6 +di +1
        min8 = min7 +di +1
        min9 = min8 +di +1
        min10 = min9 +di +1
        print(min6,min7, min8, min9, min10)
        min11 = min10 +di +1
        min12 = min11 +di +1
        min13 = min12+ di +1
        min14 = min13 +di +1
        min15 = min14 +di +1
        min16 = min15 +di +1
        print(min11,min12, min13, min14, min15)

        min17 = min16 +di +1
        min18 = min17 +di +1
        min19 = min18 +di +1
        min20 = min19 +di +1
        print(min16, min17, min18, min19,min20)
        min21 = min20+di +1
        min22 = min21+di +1

        min23 = min22+di +1
        min24 = min23 +di +1
        min25 = min24 +di +1
        min26 = min25 +di +1
        min27 = min26 +di +1
 if self.tong_diem7 < min1:

            self.Nhom_luong = 1

        elif self.tong_diem7  > min2 and self.tong_diem7 < min2+ di :
            self.Nhom_luong = 2

        elif self.tong_diem7 > min3 and self.tong_diem7 < min3+ di :
            self.Nhom_luong = 3

        if self.tong_diem7 > min4 and self.tong_diem7 < min4+ di :
            self.Nhom_luong = 4
        if self.tong_diem7 > min5 and self.tong_diem7 < min5+ di :
            self.Nhom_luong = 5

        if self.tong_diem7 > 105 :
           self.Nhom_luong = 2
        if self.tong_diem7 > 138 :
           self.Nhom_luong = 2
        if self.tong_diem7 > 171 :
           self.Nhom_luong = 3
        if self.tong_diem7 > 204 :
           self.Nhom_luong = 4
        if self.tong_diem7 > 238 :
           self.Nhom_luong = 5