import odrive
import time
import keyboard

# ODriveを接続
odrv0 = odrive.find_any()

# ODrive設定
odrv0.axis0.controller.config.control_mode = odrive.utils.ControlMode.POSITION_CONTROL
odrv0.axis0.controller.config.input_mode = odrive.utils.InputMode.POS_FILTER
odrv0.axis0.requested_state = odrive.utils.AxisState.CLOSED_LOOP_CONTROL

odrv0.axis1.controller.config.control_mode = odrive.utils.ControlMode.POSITION_CONTROL
odrv0.axis1.controller.config.input_mode = odrive.utils.InputMode.POS_FILTER
odrv0.axis1.requested_state = odrive.utils.AxisState.CLOSED_LOOP_CONTROL

# 初期位置設定
current_position_axis0 = 0
current_position_axis1 = 0

while True:
    # 矢印キーの入力を監視
    if keyboard.is_pressed('up'):  # 上矢印キー
        current_position_axis0 += 1  # axis0を1単位前進
        current_position_axis1 += 1  # axis1を1単位前進
        odrv0.axis0.controller.input_pos = current_position_axis0
        odrv0.axis1.controller.input_pos = current_position_axis1
        print(f'Axis 0 Position: {current_position_axis0}, Axis 1 Position: {current_position_axis1}')
    elif keyboard.is_pressed('down'):  # 下矢印キー
        current_position_axis0 -= 1  # axis0を1単位後退
        current_position_axis1 -= 1  # axis1を1単位後退
        odrv0.axis0.controller.input_pos = current_position_axis0
        odrv0.axis1.controller.input_pos = current_position_axis1
        print(f'Axis 0 Position: {current_position_axis0}, Axis 1 Position: {current_position_axis1}')
    
    time.sleep(0.1)  # 0.1秒待機して連続入力を防止
