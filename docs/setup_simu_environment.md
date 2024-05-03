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

### Case 2: Use the matterport3D
1. Download [havitat-sim](https://github.com/facebookresearch/habitat-sim) and follow this [tutorial](https://drive.google.com/file/d/1xV3L2xW4JtPMZpY8t43aqlXDhraZYLDi/view) for the usage.

### Case 3: Import 3D Mesh from the Google Map into Gazebo
1. Tutorial:
    * Bilibili (Chinese): [tutorial video](https://www.bilibili.com/video/BV1fv411s7cc/?spm_id_from=333.337.search-card.all.click)
    * Youtube: [tutorial video](https://www.youtube.com/watch?v=X6Q7dbtXVZQ)
2. Download the [MapsModelsImporter](https://github.com/eliemichel/MapsModelsImporter?tab=readme-ov-file) and follow the tutorial
    * Click the [MapsModelsImporter download link](https://github.com/eliemichel/MapsModelsImporter/releases)
    * Steps: ```launch chrome``` - ```launch RenderDoc``` - ```open google map``` - ```press PrtSc``` - ```save capture in RenderDoc``` - ```launch blender and install MapsModelsImporter``` - ```load .rdc``` - ```export models as obj```
    <div align="center">
      <a href="">
        <img align="center" src="image/environment_blender_model_wotexture.png" width="40%" alt="image/environment_blender_model_wotexture">
      </a> 
      <a href="">
        <img align="center" src="image/environment_blender_model_wtexture.png" width="41%" alt="image/environment_blender_model_wtexture">
      </a>     
    </div>
3. Launch Meshlab, open ```*obj```, and then save ```*.ply```, ```*.dae```, ```*_pointcloud.ply```