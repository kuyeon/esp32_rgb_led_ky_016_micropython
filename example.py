"""
RGB LED KY-016 사용 예제
ESP32 S3 MicroPython용

이 예제는 RGB LED KY-016 라이브러리의 사용법을 보여줍니다.
"""

from rgb_led_ky016 import RGBLedKY016
import time

# RGB LED 핀 설정 (ESP32 S3 기준)
# 실제 연결된 핀 번호에 맞게 수정하세요
RED_PIN = 6
GREEN_PIN = 7
BLUE_PIN = 5

def main():
    """메인 함수"""
    print("RGB LED KY-016 예제 시작")
    
    # RGB LED 객체 생성
    rgb_led = RGBLedKY016(RED_PIN, GREEN_PIN, BLUE_PIN)
    
    # 잠시 대기
    time.sleep(1)
    
    print("\n=== 기본 색상 테스트 ===")
    
    # 빨간색 켜기
    rgb_led.red_on()
    time.sleep(1)
    
    # 초록색 켜기
    rgb_led.green_on()
    time.sleep(1)
    
    # 파란색 켜기
    rgb_led.blue_on()
    time.sleep(1)
    
    # 흰색 켜기
    rgb_led.white_on()
    time.sleep(1)
    
    # 모든 LED 끄기
    rgb_led.off()
    time.sleep(1)
    
    print("\n=== 직접 색상 설정 테스트 ===")
    
    # 다양한 색상 조합 테스트
    color_combinations = [
        (True, False, False),   # 빨강
        (False, True, False),   # 초록
        (False, False, True),   # 파랑
        (True, True, False),    # 노랑 (빨강+초록)
        (True, False, True),    # 마젠타 (빨강+파랑)
        (False, True, True),    # 시안 (초록+파랑)
        (True, True, True),     # 흰색
        (False, False, False),  # 꺼짐
    ]
    
    for red, green, blue in color_combinations:
        rgb_led.set_color(red, green, blue)
        time.sleep(0.5)
    
    print("\n=== 데모 시퀀스 시작 ===")
    print("Ctrl+C를 눌러서 중지하세요")
    
    try:
        # 데모 시퀀스 실행 (각 색상 1초씩)
        rgb_led.demo_sequence(1000)
    except KeyboardInterrupt:
        print("\n데모 중지됨")
        rgb_led.off()
        print("프로그램 종료")

if __name__ == "__main__":
    main()
