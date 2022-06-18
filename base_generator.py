import random
import datetime
import time

menu_board = {"아메리카노":1500, "꿀아메리카노":2500, "카페라떼":3700, "카라멜마끼야또":3500, 
"바닐라라떼":3200, "카페모카":3700, "민트카페모카":4500, "카푸치노":2700, "티라미수라떼":3900, 
"연유라떼":3700, "헤이즐럿아메리카노":2500, "바닐라아메리카노":2500, "헤이즐럿라떼":3200, 
"콜드 브루": 3300, "콜드 브루라떼": 3800, "흑당버블라떼": 3500, "흑당버블그린티":3500,
"흑당라떼":3000,"흑당밀크티라떼":3300,"토피넛라떼":3800,"녹차라떼":3200,"오레오초코라떼":3900,
"메가초코":3800,"딸기라떼":3500,"민트크림초코":3500,"고구마라떼":3500,"녹차":2500,"얼그레이":2500,
"캐모마일":2500,"페퍼민트":2500,"사과유자차":3500, "유자차":3000,"레몬차":3000,"자몽차":3000,
"허니자몽블랙티":3500,"복숭아아이스티":3000,"오곡바나나주스":3800,"초코바나나주스":3800,"딸기주스":3800,
"딸기바나나주스":3800,"레몬에이드":3500,"블루레몬에이드":3500,"자몽에이드":3500,"체리콕":3000,
"메가에이드":3900,"자몽모히또":3800,"청포토모히또":3800,"라임모히또":3800,"청포도에이드":3500,
"쿠키프라페":3900,"딸기쿠키프라페":3900,"민트프라페":3900,"녹차프라페":3900,"리얼초코프라페":3900,
"커피프라페":3900,"유니콘프라페":4800,"스트로베리 치즈홀릭":4500,"플레인 요거트스무디":3900,
"망고 요거트스무디":3900,"딸기 요거트스무디":3900}

catid_dic = {"716047376":"3408394001", "111111111":"1231231231", "222222222":"4564564564",
"333333333":"7897897897", "444444444":"3213213213"}

serial_dic = {"716047376":"NS220511170254386422", "111111111":"QW111111111111111111", "222222222": "TY111111111111111111",
"333333333":"ZX111111111111111111", "444444444":"JH111111111111111111"}

def sampleDate():
    month = random.randint(5, 6)
    if month == 5:
        day = random.randint(28, 31)
    else:
        day = random.randint(1, 7)

    temp = random.randint(1, 100)
    if temp <= 20:
        hour = 8
    elif temp <= 25:
        hour = 9
    elif temp <= 30:
        hour = 10
    elif temp <= 35:
        hour = 11
    elif temp <= 55:
        hour = 12
    elif temp <= 60:
        hour = 13
    elif temp <= 65:
        hour = 14
    elif temp <= 70:
        hour = 15
    elif temp <= 75:
        hour = 16
    elif temp <= 80:
        hour = 17
    elif temp <= 85:
        hour = 18
    elif temp <= 90:
        hour = 19
    elif temp <= 95:
        hour = 20
    else:
        hour = 21
    # hour = random.randint(8, 22)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    return datetime.datetime(2022, month, day, hour, minute, second)

def ServiceAmount(): #사용 안함
    return "0" * 12

def Point():
    return random.randint(1, 100)

def Vat(): #부과세 범위 1~300
    num = random.randint(1, 100)
    if num < 10:
        return "0" * 11 + str(num)
    elif num >= 10 and num < 100:
        return "0" * 10 + str(num)
    else:
        return "0" * 9 + str(num)

def CardType():
    return str(random.randint(0, 2))

def accumulatedPoint(): #사용 안함
    return "         "

def acquisitionCode():
    return "01"

def Classification():
    n = random.randint(0, 1)

    if n == 0:
        return "0210"
    else:
        return "0430"

def DeviceNumber(): #기기번호
    return "          "

def CashBackStore():
    return "               "

def CatId(businessNumber): #단말기 번호
    return catid_dic[businessNumber]

def Code():
    return "0000"

def OccurPoint(): #사용안함
    return "        "

def Amount(menu): #결제금액
    price = []

    for k in menu:
        price.append(menu_board[k])
    return price

def PointType(): # 1:포인트적립 2포인트사용
    return random.randint(1, 2)

def SerialNumber(businessNumber): # 카드단말기 시리얼 번호
    return serial_dic[businessNumber]

def AvailablePoint(): #사용 안함
    return "         "

def IssuerName():
    cardName = ['카카오페이체크','대구은행체크','신한은행체크','농협은행체크','기업은행체크','국민은행체크']
    n = random.randint(0,5)
    return cardName[n]

def Menus():
    menu = []
    n = random.randint(1, 5)
    temp = list(menu_board.keys())

    for i in range(n): 
        k = random.randint(1, len(menu_board) - 1)
        menu.append(temp[k])

    return menu

def Type(): #신용카드10 현금영수증21
    k = random.randint(1, 100)

    if k <= 80:
        return 10
    else:
        return 21

def CashBackApprovalNumber(): #사용 안함
    return "         "

def ManageNumber(): #전문번호
    return "34083940010511170251"

def MyPoint(point): #적립자 잔여 포인트
    return str(point + random.randint(0, 10000))

def AcquisitionName(): #매입사명
    return "비씨카드 EDC       "

def isDc():
    return ""

def myHp():
    a = random.randint(1000, 9999)
    b = random.randint(1000, 9999)
    return "010" + str(a) + str(b)

def OrderId(i): #주문번호
    return str(i)

def CardBin(): #카드번호
    return "944192" + str(random.randint(1000000000, 9999999999))

def install(): #할부개월
    return "0" + str(random.randint(0, 3))

def ApprovalDate(date): #승인날짜   
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second 

    return str(year) + str(month) + str(day) + str(hour) + str(minute) + str(second)

def Balance(): #카드잔액
    return str(random.randint(0, 100000))

def Refunded(): #취소여부 T(취소)
    return "T"

def ApprovalNumber(): #승인번호
    return str(random.randint(10000000, 99999999))

def IssuerCode(): #발급사 코드
    return "01"

def RecordedTime(date): #기록날짜
    return date

def Message(anum): #데몬앱 리턴 메세지
    return "IC카드 정상승인" + str(anum)

def BusinessNumber(k): #사업자번호
    business_num = list(catid_dic.keys())
    return business_num[k]

def output():
    log = []
    f = open("C:/Users/Boat/Desktop/ㅈㅂ/종프2/sample.log", "w+")#파일경로설정

    for k in range(len(catid_dic)):
        n = random.randint(480, 720)
        businessNumber = BusinessNumber(k)

        for i in range(n):
            point = Point()
            mdate = sampleDate()
            anum = ApprovalNumber()
            menu = Menus()
            amount = Amount(menu)

            olog = str(mdate) + ' : { "serviceAmount":"' + ServiceAmount() + '", '
            olog += '"point":"' + str(Point()) + '", '
            olog += '"vat":"' + Vat() + '", '
            olog += '"cardType":"' + CardType() + '", '
            olog += '"accumulatedPoint":"' + accumulatedPoint() + '", '
            olog += '"acquisitionCode":"' + acquisitionCode() + '", '
            olog += '"classification":"' + Classification() + '", '
            olog += '"deviceNumber":"' + DeviceNumber() + '", '
            olog += '"cashbackStore":"' + CashBackStore() + '", '
            olog += '"catId":"' + CatId(businessNumber) + '", '
            olog += '"code":"' + Code() + '", '
            olog += '"occurPoint":"' + OccurPoint() + '", '

            olog += '"amount":"'
            for  i in range(len(amount)):
                if i == len(amount) - 1:
                    olog += str(amount[i])
                else:  
                    olog += str(amount[i]) + ","
            olog += '", '

            olog += '"pointType":"' + str(PointType()) + '", '
            olog += '"serialNumber":"' + SerialNumber(businessNumber) + '", '
            olog += '"availablePoint":"' + AvailablePoint() + '", '
            olog += '"issuerName":"' + IssuerName() + '", '
        
            olog += '"Menus":"'  
            for i in range(len(menu)):
                if i == len(menu) - 1:
                    olog += menu[i]
                else:  
                    olog += menu[i] + ","
            olog += '", '

            # olog += '"type":"' + Type() + '", '
            olog += '"cashbackApprovalNumber":"' + CashBackApprovalNumber() + '", '
            olog += '"manageNumber":"' + ManageNumber() + '", '
            olog += '"myPoint":"' + MyPoint(point) + '", '
            olog += '"accquisitionName":"' + AcquisitionName() + '", '
            olog += '"isDc":"' + isDc() + '", '
            olog += '"myHp":"' + myHp() + '", '
            olog += '"orderId":"' + OrderId(i) + '", '
            olog += '"cardBin":"' + CardBin() + '", '
            olog += '"install":"' + install() + '", '
            olog += '"approvalDate":"' + ApprovalDate(mdate) + '", '
            olog += '"balance":"' + Balance() + '", '
            olog += '"Refunded":"' + Refunded() + '", '
            olog += '"approvalNumber":"' + anum + '", '
            olog += '"issuerCode":"' + IssuerCode() + '", '
            olog += '"recordedTime":"' + RecordedTime(str(mdate)) + '", '
            olog += '"message":"' + Message(anum) + '", '
            olog += '"businessNumber":"' + businessNumber + '"}\n'

            log.append(olog)
        
    log.sort()
    for i in range(len(log)):
        f.write(log[i])
        # print(log[i])
    f.close()
    
    
output()