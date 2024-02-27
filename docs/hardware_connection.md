## Hardware Connection
This document will reocrd commends that are usually be used

### Interfaces
<div align="center">
  <a href="">
    <img align="center" src="image/anymal_d014_hardware_interface.png" width="60%" alt="anymal_d014_hardware_interface">
  </a> 
</div>

</br>

<div align="center">
  <a href="">
    <img align="center" src="image/anymal_d014_network_connection.png" width="60%" alt="anymal_d014_network_connection">
  </a> 
</div>
**NOTE:** Connect to the Robot: Green line is connected to the robot. Black line is connected to the PC with internet. 

### Common Operations
1. [Link to share the WIFI network with the robot](https://anymal-research.docs.anymal.com/user_manual/anymal_d100_operators_manual-workforce_app/release-23.12/html/Operators_Manual/Service_and_maintenance/Upgrade_the_software_and_firmware_of_the_Robot/Share_the_internet_connection_from_the_OPC_to_the_Robot.htm), and use ssh to check the connection.

### Note
1. [Livox-Mid360](https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/livox%20mid%20360%20%E7%94%A8%E6%88%B7%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C240222/Livox_Mid-360_User_Manual_EN.pdf)
   - The working voltage is from 9V to 27V, the recommended voltage is 12V
2. Jetson Orin
   - Power Supply: It is 7~20V, 5A for type-C or DC jack. The P/N of DC jack is AC0002-0011-001-HH, you can get its spec by searching online. [how to power on](https://developer.nvidia.com/embedded/learn/jetson-agx-orin-devkit-user-guide/howto.html)
3. [Azure Kinect DK](https://learn.microsoft.com/en-us/azure/kinect-dk/hardware-specification)
   - Power Supply:
     - USB-C: It consumes up to 5.9 W; specific power consumption is use-case dependent. A passive cable should be less than 1.5m in length. If longer, use an active cable.
The cable needs to support at least 1.5A. Otherwise you need to connect an external power supply. The USB certified cable must support both power and data.
     - Others: The in-box power supply cable is a USB Type-A to single post barrel connector. Use the provided wall power supply with this cable. The device is capable of drawing more power than two standard USB Type-A ports can provide.



  




 
