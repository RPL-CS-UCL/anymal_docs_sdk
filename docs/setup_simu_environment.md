## Setup Your Own Simulated Environment

### Case 1: Import RGB-D Point Cloud into Gazebo
#### Requirement:
1. Install meshlab
2. PCD file: scene.pcd

#### Steps:
1. Terminal-convert pcd to ply: ```pcl_pcd2ply scene.pcd scene.ply```
2. Meshlab:
    * Open scene.ply
      <div align="center">
        <a href="">
          <img align="center" src="image/setup_simu_import_pc.png" width="40%" alt="setup_simu_import_pc">
        </a> 
      </div>
    * **Compute normal:** Filters → normals, curvature, operation → compute normals for pointset → neighbor: 100
      * Visualize normla: Render → show normal
    * **Compute mesh:** Remeshing, simplification, reconstruction → surface reconstruction: screened poisson/ **VGG**
      * Save mesh: Export mesh as dae and ply

3. CloudCompare
  <div align="center">
    <a href="">
      <img align="center" src="image/setup_simu_start_end_point.png" width="40%" alt="setup_simu_start_end_point">
    </a> 
  </div>

#### Reference link:
1. Use matterport3d: [https://drive.google.com/file/d/1xV3L2xW4JtPMZpY8t43aqlXDhraZYLDi/view](https://drive.google.com/file/d/1xV3L2xW4JtPMZpY8t43aqlXDhraZYLDi/view)

