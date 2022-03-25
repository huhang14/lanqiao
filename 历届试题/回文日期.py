import time

def is_date(s):
    try:
        time.strptime(s,"%Y%m%d")
        return True
    except:
        return False


def cal_hw(hw_year,date):
    hw_m=hw_year[3]+hw_year[2]
    hw_d=hw_year[1]+hw_year[0]
    if is_date(hw_year+hw_m+hw_d) and int(hw_year+hw_m+hw_d)>int(date):
        print(hw_year+hw_m+hw_d)
    else:
        while int(hw_year)<=9999:    
            hw_year=int(hw_year)+1
            hw_year=str(hw_year)
            hw_m=hw_year[3]+hw_year[2]
            hw_d=hw_year[1]+hw_year[0]
            if is_date(hw_year+hw_m+hw_d):
                print(hw_year+hw_m+hw_d)
                break

def cal_ab(ab_year,date):
    ba=ab_year[1]+ab_year[0]
    if is_date(ab_year+ab_year+ba+ba) and int(ab_year+ab_year+ba+ba)>int(date):
        print(ab_year+ab_year+ba+ba)
    else:
        while int(ab_year)<=99:
            ab_year=int(ab_year)+1
            ab_year=str(ab_year)
            ba=ab_year[1]+ab_year[0]
            if is_date(ab_year+ab_year+ba+ba):
                print(ab_year+ab_year+ba+ba)
                break

date=input()
hw_year=date[:4]
ab_year=date[:2]
cal_hw(hw_year,date)
cal_ab(ab_year,date)
