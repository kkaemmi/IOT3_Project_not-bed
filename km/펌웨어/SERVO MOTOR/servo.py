import Adafruit_PCA9685
import requests
import time

# 클라이언트 요청코드
url = "http://192.168.1.180/dashboard/cont.php" 

response = requests.get(url)

ch = response.text

class MG90_96R_Class:
    def __init__(self, Channel, ZeroOffset):
        self.servo_num = Channel
        self.servo_offset = ZeroOffset

        # 원하는 주소 및/또는 버스를 사용하여 PCA9685를 초기화합니다.
        self.Pwm = Adafruit_PCA9685.PCA9685(address = 0x40, busnum = 1)

        # 주파수를 60[Hz]로 설정
        self.Pwm.set_pwm_freq(60)

    # 최소 및 최대 서보 펄스 길이 구성
    # 150 최소 펄스 길이
    # 650 최대 펄스 길이
    def SetPos(self, pos):
        pulse = (650 - 150) * pos / 180 + 150 + self.servo_offset
        self.Pwm.set_pwm(self.servo_num, 0, int(pulse))

    def Cleanup(self):
        self.SetPos(90)
        time.sleep(1)

# 클레스 선언
# up
class motor_Class:
    def motor0_up_q():
        if ch == 'q':   # 왼쪽
            Servo0.SetPos(100)
            time.sleep(1)

    def motor1_up_w():
        if ch == 'w':   # 오른쪽 
            Servo1.SetPos(90)
            time.sleep(1)

    def motor2_up_r():
        if ch == 'r':   # 다리
            Servo2.SetPos(160)
            Servo3.SetPos(160)
            time.sleep(1)

    def motor3_up_t():
        if ch == 't':   # 등받이
            Servo4.SetPos(140)
            Servo5.SetPos(40)
            Servo6.SetPos(60)
            time.sleep(1)

    def motor4_up_y():
        if ch == 'y':   # 범퍼
            Servo7.SetPos(65)
            Servo8.SetPos(20)
            Servo9.SetPos(65)
            Servo10.SetPos(165)
            time.sleep(1)

# down
class motor1_Class:
    def motor5_down_a():
        if ch == 'a':   # 왼쪽
            Servo0.SetPos(0)
            time.sleep(1)

    def motor6_down_s():
        if ch == 's':   # 오른쪽
            Servo1.SetPos(180)
            time.sleep(1)

    def motor7_down_f():
        if ch == 'f':   # 다리
            Servo2.SetPos(50)
            Servo3.SetPos(50)
            time.sleep(1)
  
    def motor8_down_g():
        if ch == 'g':   # 등받이
            Servo4.SetPos(180)
            Servo5.SetPos(0)
            Servo6.SetPos(15)
            time.sleep(1)

    def motor9_down_h():
        if ch == 'h':   # 범퍼
            Servo7.SetPos(130)
            Servo8.SetPos(0)
            Servo9.SetPos(130)
            Servo10.SetPos(100)
            time.sleep(1)

# 서보 모터 사용할 채널 설정
if __name__ == '__main__':
    Servo0 = MG90_96R_Class(Channel = 0, ZeroOffset = -10)
    Servo1 = MG90_96R_Class(Channel = 1, ZeroOffset = -10)
    Servo2 = MG90_96R_Class(Channel = 2, ZeroOffset = -10)
    Servo3 = MG90_96R_Class(Channel = 3, ZeroOffset = -10)
    Servo4 = MG90_96R_Class(Channel = 4, ZeroOffset = -10)
    Servo5 = MG90_96R_Class(Channel = 5, ZeroOffset = -10)
    Servo6 = MG90_96R_Class(Channel = 6, ZeroOffset = -10)
    Servo7 = MG90_96R_Class(Channel = 7, ZeroOffset = -10)
    Servo8 = MG90_96R_Class(Channel = 8, ZeroOffset = -10)
    Servo9 = MG90_96R_Class(Channel = 9, ZeroOffset = -10)
    Servo10 = MG90_96R_Class(Channel = 10, ZeroOffset = -10)

# 서보모터 클래스 콜 및 동작 실행
    try:
        while True:
            if ch == motor_Class.motor0_up_q():
                print("motor0 up-q")
            if ch == motor_Class.motor1_up_w():
                print("motor1 up-w")
            if ch == motor_Class.motor2_up_r():
                print("motor2 up-r")
            if ch == motor_Class.motor3_up_t():
                print("motor3 up-t")
            if ch == motor_Class.motor4_up_y():
                print("motor4 up-y")
            if ch == motor1_Class.motor5_down_a():
                print("motor5 up-a")
            if ch == motor1_Class.motor6_down_s():
                print("motor6 up-s")
            if ch == motor1_Class.motor7_down_f():
                print("motor7 up-f")
            if ch == motor1_Class.motor8_down_g():
                print("motor8 up-g")
            if ch == motor1_Class.motor9_down_h():
                print("motor9 up-h")
            
    except KeyboardInterrupt:
        print("Ctrl + C")

    finally:
        print("exit program")


