"""
RGB LED KY-016 라이브러리
ESP32 S3 MicroPython용

이 라이브러리는 RGB LED KY-016 모듈을 제어하기 위한 클래스를 제공합니다.
공통 캐소드 타입의 RGB LED를 지원합니다.

원본 Arduino 코드 출처:
//*******************************************************************************
// Project : 13_LED in Sensor Kit
// Board : Arduino Uno 
// By : Kit Plus
//*******************************************************************************

원저작자: Kit Plus
원본 프로젝트: 13_LED in Sensor Kit
원본 보드: Arduino Uno

이 코드는 원본 Arduino 코드를 MicroPython으로 포팅한 것입니다.
"""

from machine import Pin, PWM
import time

class RGBLedKY016:
    """
    RGB LED KY-016 제어 클래스
    
    공통 캐소드 타입의 RGB LED를 제어합니다.
    각 색상 핀에 HIGH 신호를 보내면 해당 색상이 켜집니다.
    """
    
    def __init__(self, red_pin, green_pin, blue_pin):
        """
        RGB LED 초기화
        
        Args:
            red_pin (int): 빨간색 LED 핀 번호
            green_pin (int): 초록색 LED 핀 번호  
            blue_pin (int): 파란색 LED 핀 번호
        """
        self.red = Pin(red_pin, Pin.OUT)
        self.green = Pin(green_pin, Pin.OUT)
        self.blue = Pin(blue_pin, Pin.OUT)
        
        # 초기 상태: 모든 LED 끄기 (LOW = 꺼짐, HIGH = 켜짐)
        self.red.value(0)
        self.green.value(0)
        self.blue.value(0)
        
        print("RGB LED KY-016 초기화 완료")
        print(f"빨강 핀: {red_pin}, 초록 핀: {green_pin}, 파랑 핀: {blue_pin}")
    
    def off(self):
        """모든 LED 끄기"""
        self.red.value(0)
        self.green.value(0)
        self.blue.value(0)
        print("모든 LED 꺼짐")
    
    def red_on(self):
        """빨간색 LED 켜기"""
        self.red.value(1)
        self.green.value(0)
        self.blue.value(0)
        print("빨간색 LED 켜짐")
    
    def green_on(self):
        """초록색 LED 켜기"""
        self.red.value(0)
        self.green.value(1)
        self.blue.value(0)
        print("초록색 LED 켜짐")
    
    def blue_on(self):
        """파란색 LED 켜기"""
        self.red.value(0)
        self.green.value(0)
        self.blue.value(1)
        print("파란색 LED 켜짐")
    
    def white_on(self):
        """흰색 LED 켜기 (모든 색상 혼합)"""
        self.red.value(1)
        self.green.value(1)
        self.blue.value(1)
        print("흰색 LED 켜짐")
    
    def set_color(self, red, green, blue):
        """
        RGB 색상 직접 설정
        
        Args:
            red (bool): 빨간색 켜기/끄기
            green (bool): 초록색 켜기/끄기
            blue (bool): 파란색 켜기/끄기
        """
        self.red.value(1 if red else 0)
        self.green.value(1 if green else 0)
        self.blue.value(1 if blue else 0)
        
        color_name = []
        if red: color_name.append("빨강")
        if green: color_name.append("초록")
        if blue: color_name.append("파랑")
        
        if not color_name:
            print("모든 LED 꺼짐")
        else:
            print(f"색상 설정: {'+'.join(color_name)}")
    
    def demo_sequence(self, delay_ms=1000):
        """
        색상 순차 변경 데모
        
        Args:
            delay_ms (int): 각 색상 지속 시간 (밀리초)
        """
        print("RGB LED 데모 시작")
        
        while True:
            # 빨간색
            self.red_on()
            time.sleep_ms(delay_ms)
            
            # 초록색
            self.green_on()
            time.sleep_ms(delay_ms)
            
            # 파란색
            self.blue_on()
            time.sleep_ms(delay_ms)
            
            # 흰색
            self.white_on()
            time.sleep_ms(delay_ms)


class RGBLedKY016PWM:
    """
    RGB LED KY-016 PWM 제어 클래스
    
    공통 캐소드 타입의 RGB LED를 PWM으로 제어하여 밝기 조절이 가능합니다.
    각 색상의 밝기를 0-100% 범위에서 조절할 수 있습니다.
    """
    
    def __init__(self, red_pin, green_pin, blue_pin, freq=1000):
        """
        RGB LED PWM 초기화
        
        Args:
            red_pin (int): 빨간색 LED 핀 번호
            green_pin (int): 초록색 LED 핀 번호  
            blue_pin (int): 파란색 LED 핀 번호
            freq (int): PWM 주파수 (기본값: 1000Hz)
        """
        self.freq = freq
        self.max_duty = 1023  # ESP32의 최대 duty cycle
        
        # PWM 객체 생성 (공통 캐소드이므로 초기 duty는 0)
        self.red_pwm = PWM(Pin(red_pin), freq=freq, duty=0)
        self.green_pwm = PWM(Pin(green_pin), freq=freq, duty=0)
        self.blue_pwm = PWM(Pin(blue_pin), freq=freq, duty=0)
        
        print("RGB LED KY-016 PWM 초기화 완료")
        print(f"빨강 핀: {red_pin}, 초록 핀: {green_pin}, 파랑 핀: {blue_pin}")
        print(f"PWM 주파수: {freq}Hz")
    
    def set_brightness(self, red_brightness, green_brightness, blue_brightness):
        """
        RGB 밝기 설정 (0-100%)
        
        Args:
            red_brightness (float): 빨간색 밝기 (0-100)
            green_brightness (float): 초록색 밝기 (0-100)
            blue_brightness (float): 파란색 밝기 (0-100)
        """
        # 0-100 범위를 0-1023 duty cycle로 변환
        # 공통 캐소드이므로 정상 (100% = 1023 duty, 0% = 0 duty)
        red_duty = int(self.max_duty * max(0, min(100, red_brightness)) / 100)
        green_duty = int(self.max_duty * max(0, min(100, green_brightness)) / 100)
        blue_duty = int(self.max_duty * max(0, min(100, blue_brightness)) / 100)
        
        self.red_pwm.duty(red_duty)
        self.green_pwm.duty(green_duty)
        self.blue_pwm.duty(blue_duty)
        
        print(f"밝기 설정 - 빨강: {red_brightness:.1f}%, 초록: {green_brightness:.1f}%, 파랑: {blue_brightness:.1f}%")
    
    def set_color_rgb(self, red, green, blue):
        """
        RGB 값으로 색상 설정 (0-255)
        
        Args:
            red (int): 빨간색 값 (0-255)
            green (int): 초록색 값 (0-255)
            blue (int): 파란색 값 (0-255)
        """
        # 0-255 범위를 0-100%로 변환
        red_brightness = (red / 255) * 100
        green_brightness = (green / 255) * 100
        blue_brightness = (blue / 255) * 100
        
        self.set_brightness(red_brightness, green_brightness, blue_brightness)
    
    def off(self):
        """모든 LED 끄기"""
        self.set_brightness(0, 0, 0)
        print("모든 LED 꺼짐")
    
    def red_on(self, brightness=100):
        """빨간색 LED 켜기"""
        self.set_brightness(brightness, 0, 0)
        print(f"빨간색 LED 켜짐 (밝기: {brightness}%)")
    
    def green_on(self, brightness=100):
        """초록색 LED 켜기"""
        self.set_brightness(0, brightness, 0)
        print(f"초록색 LED 켜짐 (밝기: {brightness}%)")
    
    def blue_on(self, brightness=100):
        """파란색 LED 켜기"""
        self.set_brightness(0, 0, brightness)
        print(f"파란색 LED 켜짐 (밝기: {brightness}%)")
    
    def white_on(self, brightness=100):
        """흰색 LED 켜기 (모든 색상 혼합)"""
        self.set_brightness(brightness, brightness, brightness)
        print(f"흰색 LED 켜짐 (밝기: {brightness}%)")
    
    def fade_in(self, red_brightness, green_brightness, blue_brightness, duration_ms=1000, steps=50):
        """
        페이드 인 효과
        
        Args:
            red_brightness (float): 목표 빨간색 밝기 (0-100)
            green_brightness (float): 목표 초록색 밝기 (0-100)
            blue_brightness (float): 목표 파란색 밝기 (0-100)
            duration_ms (int): 페이드 지속 시간 (밀리초)
            steps (int): 페이드 단계 수
        """
        print(f"페이드 인 시작 - 목표 밝기: R{red_brightness}% G{green_brightness}% B{blue_brightness}%")
        
        step_delay = duration_ms // steps
        
        for i in range(steps + 1):
            progress = i / steps
            current_red = red_brightness * progress
            current_green = green_brightness * progress
            current_blue = blue_brightness * progress
            
            self.set_brightness(current_red, current_green, current_blue)
            time.sleep_ms(step_delay)
    
    def fade_out(self, duration_ms=1000, steps=50):
        """
        페이드 아웃 효과
        
        Args:
            duration_ms (int): 페이드 지속 시간 (밀리초)
            steps (int): 페이드 단계 수
        """
        print("페이드 아웃 시작")
        
        # 현재 밝기 저장 (공통 캐소드이므로 정상)
        current_red = self.red_pwm.duty() / self.max_duty * 100
        current_green = self.green_pwm.duty() / self.max_duty * 100
        current_blue = self.blue_pwm.duty() / self.max_duty * 100
        
        step_delay = duration_ms // steps
        
        for i in range(steps + 1):
            progress = 1 - (i / steps)
            target_red = current_red * progress
            target_green = current_green * progress
            target_blue = current_blue * progress
            
            self.set_brightness(target_red, target_green, target_blue)
            time.sleep_ms(step_delay)
    
    def rainbow_cycle(self, duration_ms=5000, steps=100):
        """
        무지개 색상 순환 효과
        
        Args:
            duration_ms (int): 전체 순환 시간 (밀리초)
            steps (int): 색상 변화 단계 수
        """
        print("무지개 색상 순환 시작")
        
        step_delay = duration_ms // steps
        
        for i in range(steps):
            # HSV 색상 공간에서 Hue 값 계산 (0-360도)
            hue = (i / steps) * 360
            
            # HSV를 RGB로 변환
            rgb = self._hsv_to_rgb(hue, 100, 100)
            
            self.set_color_rgb(rgb[0], rgb[1], rgb[2])
            time.sleep_ms(step_delay)
    
    def breathing_effect(self, color_rgb, cycles=3, duration_ms=2000):
        """
        호흡 효과 (밝기가 천천히 변하는 효과)
        
        Args:
            color_rgb (tuple): RGB 색상 (r, g, b) 0-255
            cycles (int): 호흡 사이클 수
            duration_ms (int): 한 사이클 지속 시간 (밀리초)
        """
        print(f"호흡 효과 시작 - 색상: RGB{color_rgb}, 사이클: {cycles}회")
        
        for cycle in range(cycles):
            # 페이드 인
            self.fade_in(
                (color_rgb[0] / 255) * 100,
                (color_rgb[1] / 255) * 100,
                (color_rgb[2] / 255) * 100,
                duration_ms // 2,
                25
            )
            
            # 페이드 아웃
            self.fade_out(duration_ms // 2, 25)
    
    def _hsv_to_rgb(self, h, s, v):
        """
        HSV 색상 공간을 RGB로 변환
        
        Args:
            h (float): Hue (0-360)
            s (float): Saturation (0-100)
            v (float): Value (0-100)
            
        Returns:
            tuple: RGB 값 (0-255)
        """
        h = h / 360.0
        s = s / 100.0
        v = v / 100.0
        
        if s == 0:
            r = g = b = v
        else:
            i = int(h * 6)
            f = h * 6 - i
            p = v * (1 - s)
            q = v * (1 - s * f)
            t = v * (1 - s * (1 - f))
            
            if i % 6 == 0:
                r, g, b = v, t, p
            elif i % 6 == 1:
                r, g, b = q, v, p
            elif i % 6 == 2:
                r, g, b = p, v, t
            elif i % 6 == 3:
                r, g, b = p, q, v
            elif i % 6 == 4:
                r, g, b = t, p, v
            else:
                r, g, b = v, p, q
        
        return (int(r * 255), int(g * 255), int(b * 255))
    
    def deinit(self):
        """PWM 객체 정리"""
        self.red_pwm.deinit()
        self.green_pwm.deinit()
        self.blue_pwm.deinit()
        print("PWM 객체 정리 완료")
