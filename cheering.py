#近づいたら旗を振るプログラム

import ev3dev.ev3 as ev3
import time

# モータクラスとカラーセンサクラスをインスタンス化
hmr = ev3.LargeMotor('outA') #右手モータを有効化
hml = ev3.LargeMotor('outB') #左手モータを有効化
lmr = ev3.LargeMotor('outC') #右足モータを有効化
lml = ev3.LargeMotor('outD') #左足モータを有効化

ts = ev3.TouchSensor('in1') #タッチセンサを有効化
ir = ev3.InfraredSensor('in2') #赤外線センサを有効化
ir.mode='IR-PROX'

previous_time=time.time()
while 1:
    infrared = ir.value()
    print(infrared)
    if infrared<70:
        current_time=time.time()
        t0 = time.time()
        if current_time-previous_time > 1.0:
            previous_time=current_time
            while  time.time()-t0 < 3:
                hmr.run_to_rel_pos(position_sp=60, speed_sp=1000, stop_action='hold')
                hml.run_to_rel_pos(position_sp=-60, speed_sp=-1000, stop_action='hold')
                time.sleep(0.5)
                hmr.stop()
                hml.stop()
                hmr.run_to_rel_pos(position_sp=-60, speed_sp=-1000, stop_action='hold')
                hml.run_to_rel_pos(position_sp=60, speed_sp=1000, stop_action='hold')
                time.sleep(0.5)
                hmr.stop()
                hml.stop()
            lmr.run_to_rel_pos(position_sp=1500, speed_sp=500, stop_action='hold')
            lml.run_to_rel_pos(position_sp=-1500, speed_sp=-500, stop_action='hold')
            time.sleep(2.23)
            lmr.stop()
            lml.stop()

    if ts.value()==1:
        break
hmr.stop(stop_action='brake') #右モータを停止
hml.stop(stop_action='brake') #左モータを停止
lmr.stop(stop_action='brake') #右モータを停止
lml.stop(stop_action='brake') #左モータを停止
