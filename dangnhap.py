X=['Duy', 'Thinh', 'Duong', 'Hung']
while "dang ki tai khoan thanh cong!":
  a=input("Ban da la thanh vien? ")
  if a=="Y":
    b=input("nhap ten tai khoan:")
    while not b in X:
      b=input("nhap lai:")
    else:
      c=input("vui long nhap mat khau:")
      while c!="h1":
        print("mat khau sai!")
        c=input("vui long nhap lai mat khau:")
      else:
        print("dang nhap thanh cong!")
    break
  if a=="N":
     d=input("nhap ten tai khoan cua ban:")
     while d in X:
       d=input("ten dang nhap da ton tai, vui long chon ten khac:")
     else:
       X.append(d)
       print("dang ki tai khoan thanh cong!")
       print("mat khau dang nhap cua ban la 'h1'")


