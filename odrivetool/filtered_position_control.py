import odrive
import time
import keyboard # 実行できない場合，sudo -E python3 position.py

odrv0 = odrive.find_any()

odrv0.axis0.controller.config.control_mode=odrive.utils.ControlMode.POSITION_CONTROL
odrv0.axis0.controller.config.input_mode=odrive.utils.InputMode.POS_FILTER
odrv0.axis0.requested_state=odrive.utils.AxisState.CLOSED_LOOP_CONTROL

# 初期位置設定
current_position = 0

while True:
    # 矢印キーの入力を監視
    if keyboard.is_pressed('up'):  # 上矢印キー
        current_position += 0.5  # 位置を0.5単位前進
        odrv0.axis0.controller.input_pos = current_position
        print(f'Position: {current_position}')
    elif keyboard.is_pressed('down'):  # 下矢印キー
        current_position -= 0.5  # 位置を0.5単位後退
        odrv0.axis0.controller.input_pos = current_position
        print(f'Position: {current_position}')
    
    time.sleep(0.1)  # 0.1秒待機して連続入力を防止