## Start Real-World Tests with ANYmal

### Start Hardware
1. Install all components like the below figure, including computers, battery, camera, and others
2. Connect the battery with the Intel NUC and Jetson Orin. And turn on these computers and the battery.
3. Connect the monitor with the Intel NUC.
4. Check whether the NUC starts, the network switch starts, and monitor starts
5. Login the **jjiao** account with the password.
6. Check whether the network connection of the NUC is **Anymal_Shared_Network**.
7. Turn on the Anymal and swith its mode as **walking mode**.
<div align="center">
  <a href="">
    <img align="center" src="image/anymal_d_hardware.jpeg" width="50%" alt="anymal_d_hardware">
  </a> 
</div>

### Start VNC
1. (NUC) settings -> sharing -> scene sharing (turn on)
2. (Another PC) open Remmina Remote Destkop -> create a VNC setting -> click connect
<div align="center">
  <a href="">
    <img align="center" src="image/anymal_d_vnc_setting.png" width="30%" alt="anymal_d_vnc_setting">
  </a> 
</div>

### Start Sensor Setup and Record Data (NUC)
1. Open a terminal and enter: ```bash /home/jjiao/setup_sensor.sh```
2. Check the output of RVIZ
3. Record data: ```bash /home/jjiao/record_rosbag_anymal_message_noimage.sh```. 
4. Check data ```rosbag info /Rocket_ssd/dataset/data_anymal/anymal_real_message_xxx.bag```

### RUN FastLIO2 (NUC)
1. Open a terminal and enter: ```rostopiz hz /lidar/point_cloud```, and check output (should output **10 Hz** if correct).
2. Start the docker: ```docker start robohike_anymal && docker exec -it robohike_anymal /bin/bash```.
3. Launch the fastlio program: ```cd /Titan/code/RPL-RoboHike/config_launch_anymal/scipt && bash run_anymal_fastlio2_velodyne```
5. Move the robot slowly and check whether the rviz shows something.


