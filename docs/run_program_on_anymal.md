## Run Program On Anymal

### Start Hardware
1. Connect the battery with the Intel NUC. And turn on the Intel NUC and the battery.
2. Connect the monitor with the Intel NUC.
3. Check whether the NUC starts, the network switch starts, and monitor starts
4. Login the **jjiao** account with the password.
5. Check whether the network connection of the NUC is **Anymal_Shared_Network**.
6. Turn on the Anymal and swith its mode as **walking mode**.

### RUN FastLIO2 on Anymal
1. Open a terminal and enter ```rostopiz hz /lidar/point_cloud```, and check output (should output **x Hz** if correct).
2. Start the docker and enter the docker ```docker start robohike_anymal && docker exec -it robohike_anymal /bin/bash```.
3. Launch the fastlio program ```cd /Titan/code/RPL-RoboHike/config_launch_anymal/launch/cmu_exploration && roslaunch anymal_real_fastlio2.launch```
4. Open another terminal and run rviz ```rviz -d RPL-RoboHike/config_launch_anymal/fastlio2.rviz```. (If you restart the fastlio program, please remember to open the rviz again).
5. Move the robot slowly and check whether the rviz shows something.


