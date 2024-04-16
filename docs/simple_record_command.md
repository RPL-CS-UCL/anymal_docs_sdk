## Record of Commands
This document will reocrd commends that are usually be used

### Cheat Sheet
<div align="center">
  <a href="">
    <img align="center" src="image/screenshot_chatsheet.png" width="80%" alt="screenshot_chatsheet">
  </a> 
</div>

### Commands of using CMU Navigation
1. Setup CMU navigation environment: ```roslaunch vehicle_simulator system_env.launch``` (env: indoor, garage, matterport, ...)
2. Running CMU far planner: ```roslaunch far_planner far_planner.launch```
3. Install Habitat and render rgb, depth, and semantic images using the Habitat with Matterport3D
    ```shell script
    conda create -n habitat python=3.8 cmake=3.14.0 && \
    conda activate habitat && \
    conda install habitat-sim=0.2.1 -c conda-forge -c aihabitat && \
    conda install -c conda-forge -c robostack ros-noetic-desktop
    git clone --branch v.0.2.1 https://github.com/facebookresearch/habitat-sim.git &&
    cd habitat-sim/examples
    ```
    * Test the render
    ```shell script
    python3 example.py --scene path_to_mp3d/environment_id.glb --semantic_sensor --depth_sensor --save_png
    ```
    * Test the offline render (trajectory_timestamp.txt file in the 'src/vehicle_simulator/log' folder)
    ```shell script
    python3 habitat_offline_v0.2.1.py --scene extracted_mp3d_habitat_dir/environment_id.glb \
      --trajectory trajectory_file_dir/trajectory_timestamp.txt --save_dir image_saving_dir
    ```
    * Test the online render (trajectory_timestamp.txt file in the 'src/vehicle_simulator/log' folder)
    ```shell script
    python3 habitat_online_v0.2.1.py --scene extracted_mp3d_habitat_dir/environment_id.glb
    ```

### Other Commands
1. Setup lpc and npc server: ```anymal_setup -a d014```
2. 


### Experimental Tools
1. Case: if you want your anymal to walk outside and remotely control the PC desktop without the reliance of Internet, please refer [VNC-Viewer within WLAN](vnc-connection.md)