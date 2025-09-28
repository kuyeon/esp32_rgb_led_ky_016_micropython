"""
RGB LED KY-016 PWM 사용 예제
ESP32 S3 MicroPython용

이 예제는 PWM을 사용한 RGB LED 밝기 조절과 다양한 효과를 보여줍니다.
"""

from rgb_led_ky016 import RGBLedKY016PWM
import time

# RGB LED 핀 설정 (ESP32 S3 기준)
# 실제 연결된 핀 번호에 맞게 수정하세요
RED_PIN = 6
GREEN_PIN = 7
BLUE_PIN = 5

def main():
    """메인 함수"""
    print("RGB LED KY-016 PWM 예제 시작")
    
    # PWM RGB LED 객체 생성
    rgb_led = RGBLedKY016PWM(RED_PIN, GREEN_PIN, BLUE_PIN, freq=1000)
    
    try:
        # 잠시 대기
        time.sleep(1)
        
        print("\n=== 기본 밝기 조절 테스트 ===")
        
        # 빨간색 밝기 조절 (0% -> 50% -> 100%)
        print("빨간색 밝기 조절 테스트")
        for brightness in [0, 25, 50, 75, 100]:
            rgb_led.red_on(brightness)
            time.sleep(0.5)
        
        time.sleep(1)
        
        # 초록색 밝기 조절
        print("초록색 밝기 조절 테스트")
        for brightness in [0, 25, 50, 75, 100]:
            rgb_led.green_on(brightness)
            time.sleep(0.5)
        
        time.sleep(1)
        
        # 파란색 밝기 조절
        print("파란색 밝기 조절 테스트")
        for brightness in [0, 25, 50, 75, 100]:
            rgb_led.blue_on(brightness)
            time.sleep(0.5)
        
        time.sleep(1)
        
        print("\n=== RGB 값으로 색상 설정 테스트 ===")
        
        # 다양한 RGB 색상 테스트
        colors = [
            (255, 0, 0),    # 빨강
            (0, 255, 0),    # 초록
            (0, 0, 255),    # 파랑
            (255, 255, 0),  # 노랑
            (255, 0, 255),  # 마젠타
            (0, 255, 255),  # 시안
            (255, 255, 255), # 흰색
            (128, 64, 192), # 보라색
            (255, 128, 0),  # 주황색
        ]
        
        for r, g, b in colors:
            print(f"RGB 색상 설정: ({r}, {g}, {b})")
            rgb_led.set_color_rgb(r, g, b)
            time.sleep(1)
        
        print("\n=== 페이드 효과 테스트 ===")
        
        # 빨간색 페이드 인/아웃
        print("빨간색 페이드 인")
        rgb_led.fade_in(100, 0, 0, 2000, 50)
        time.sleep(1)
        
        print("빨간색 페이드 아웃")
        rgb_led.fade_out(2000, 50)
        time.sleep(1)
        
        # 초록색 페이드 인/아웃
        print("초록색 페이드 인")
        rgb_led.fade_in(0, 100, 0, 2000, 50)
        time.sleep(1)
        
        print("초록색 페이드 아웃")
        rgb_led.fade_out(2000, 50)
        time.sleep(1)
        
        # 파란색 페이드 인/아웃
        print("파란색 페이드 인")
        rgb_led.fade_in(0, 0, 100, 2000, 50)
        time.sleep(1)
        
        print("파란색 페이드 아웃")
        rgb_led.fade_out(2000, 50)
        time.sleep(1)
        
        print("\n=== 호흡 효과 테스트 ===")
        
        # 빨간색 호흡 효과
        rgb_led.breathing_effect((255, 0, 0), cycles=2, duration_ms=3000)
        time.sleep(1)
        
        # 초록색 호흡 효과
        rgb_led.breathing_effect((0, 255, 0), cycles=2, duration_ms=3000)
        time.sleep(1)
        
        # 파란색 호흡 효과
        rgb_led.breathing_effect((0, 0, 255), cycles=2, duration_ms=3000)
        time.sleep(1)
        
        print("\n=== 무지개 색상 순환 테스트 ===")
        print("무지개 효과를 2회 실행합니다")
        
        for i in range(2):
            print(f"무지개 순환 {i+1}/2")
            rgb_led.rainbow_cycle(duration_ms=3000, steps=60)
            time.sleep(1)
        
        print("\n=== 사용자 정의 색상 그라데이션 ===")
        
        # 빨강 -> 초록 그라데이션
        print("빨강에서 초록으로 그라데이션")
        for i in range(21):
            red = int(255 * (1 - i/20))
            green = int(255 * (i/20))
            rgb_led.set_color_rgb(red, green, 0)
            time.sleep(0.1)
        
        time.sleep(1)
        
        # 초록 -> 파랑 그라데이션
        print("초록에서 파랑으로 그라데이션")
        for i in range(21):
            green = int(255 * (1 - i/20))
            blue = int(255 * (i/20))
            rgb_led.set_color_rgb(0, green, blue)
            time.sleep(0.1)
        
        time.sleep(1)
        
        # 파랑 -> 빨강 그라데이션
        print("파랑에서 빨강으로 그라데이션")
        for i in range(21):
            blue = int(255 * (1 - i/20))
            red = int(255 * (i/20))
            rgb_led.set_color_rgb(red, 0, blue)
            time.sleep(0.1)
        
        print("\n=== 모든 테스트 완료 ===")
        rgb_led.off()
        
    except KeyboardInterrupt:
        print("\n프로그램 중단됨")
        rgb_led.off()
    
    finally:
        # PWM 객체 정리
        rgb_led.deinit()
        print("프로그램 종료")

if __name__ == "__main__":
    main()
