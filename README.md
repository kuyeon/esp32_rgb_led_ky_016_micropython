# ESP32 S3 MicroPython RGB LED KY-016 라이브러리

ESP32 S3용 MicroPython으로 RGB LED KY-016 모듈을 제어하는 라이브러리입니다.

## 원본 코드 출처

이 라이브러리는 다음 Arduino 코드를 MicroPython으로 포팅한 것입니다:

```
//*******************************************************************************
// Project : 13_LED in Sensor Kit
// Board : Arduino Uno 
// By : Kit Plus
//*******************************************************************************
```

**원저작자**: COMPASS  
**원본 프로젝트**: 13_LED in Sensor Kit  
**원본 보드**: Arduino Uno

## 특징

- 공통 캐소드 타입 RGB LED 지원
- 기본 디지털 제어와 PWM 밝기 조절 모두 지원
- 간단한 색상 제어 메서드 제공
- 페이드 인/아웃, 호흡 효과, 무지개 순환 등 다양한 효과
- 직관적인 API 설계

## 파일 구성

- `rgb_led_ky016.py`: RGB LED 제어 라이브러리 (기본 + PWM)
- `example.py`: 기본 사용 예제 코드
- `pwm_example.py`: PWM 밝기 조절 예제 코드

## 하드웨어 연결

RGB LED KY-016 모듈을 ESP32 S3에 다음과 같이 연결하세요:

| RGB LED KY-016 | ESP32 S3 |
|----------------|----------|
| R (빨강)       | GPIO 6   |
| G (초록)       | GPIO 7   |
| B (파랑)       | GPIO 5   |
| VCC            | 3.3V     |
| GND            | GND      |

## 사용법

### 기본 사용법

```python
from rgb_led_ky016 import RGBLedKY016

# RGB LED 객체 생성
rgb_led = RGBLedKY016(red_pin=6, green_pin=7, blue_pin=5)

# 빨간색 켜기
rgb_led.red_on()

# 초록색 켜기
rgb_led.green_on()

# 파란색 켜기
rgb_led.blue_on()

# 흰색 켜기
rgb_led.white_on()

# 모든 LED 끄기
rgb_led.off()
```

### 직접 색상 설정

```python
# 빨강과 초록 동시 켜기 (노랑)
rgb_led.set_color(red=True, green=True, blue=False)

# 모든 색상 켜기 (흰색)
rgb_led.set_color(red=True, green=True, blue=True)
```

### 데모 시퀀스

```python
# 색상 순차 변경 데모 (각 색상 1초씩)
rgb_led.demo_sequence(1000)
```

## PWM 밝기 조절 사용법

### PWM 클래스 사용

```python
from rgb_led_ky016 import RGBLedKY016PWM

# PWM RGB LED 객체 생성
rgb_led = RGBLedKY016PWM(red_pin=6, green_pin=7, blue_pin=5, freq=1000)

# 밝기 조절 (0-100%)
rgb_led.set_brightness(red_brightness=50, green_brightness=75, blue_brightness=25)

# RGB 값으로 색상 설정 (0-255)
rgb_led.set_color_rgb(255, 128, 64)  # 주황색

# 페이드 효과
rgb_led.fade_in(100, 0, 0, duration_ms=2000)  # 빨간색 페이드 인
rgb_led.fade_out(duration_ms=2000)  # 페이드 아웃

# 호흡 효과
rgb_led.breathing_effect((0, 255, 0), cycles=3, duration_ms=2000)  # 초록색 호흡

# 무지개 색상 순환
rgb_led.rainbow_cycle(duration_ms=5000, steps=100)

# PWM 객체 정리
rgb_led.deinit()
```

## 예제 실행

- `example.py`: 기본 디지털 제어 예제
- `pwm_example.py`: PWM 밝기 조절 및 다양한 효과 예제

각 파일을 ESP32 S3에 업로드하고 실행하면 다양한 사용법을 확인할 수 있습니다.

## 주의사항

- RGB LED KY-016은 공통 캐소드 타입입니다
- 각 색상 핀에 HIGH 신호를 보내면 해당 색상이 켜집니다
- 핀 번호는 실제 연결에 맞게 수정하세요
- 3.3V 전원을 사용하세요