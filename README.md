# Open3D Point Cloud Preprocessing Pipeline

A lightweight point cloud preprocessing pipeline based on Open3D.

## Pipeline

```text
Load
→ ROI Filtering
→ Voxel Downsampling
→ Optional Statistical Denoising
→ RANSAC Plane Segmentation
→ DBSCAN Clustering
→ Visualization
```

## Project Structure

```text
Open3D_Experiments/
├── configs/
│   └── default.yaml
├── data/
│   └── fragment.ply
├── outputs/
├── scripts/
│   └── run_pipeline.py
├── src/
│   ├── io_utils.py
│   ├── filters.py
│   ├── segmentation.py
│   ├── visualization.py
│   └── pipeline.py
└── README.md
```

## Configuration

Pipeline parameters are managed in `configs/default.yaml`.

Example:

```yaml
roi:
  enabled: true
  x_range: [1.0, 3.5]
  y_range: [1.0, 2.2]
  z_range: [0.8, 2.3]

voxel:
  enabled: true
  voxel_size: 0.01

denoise:
  enabled: false
  nb_neighbors: 5
  std_ratio: 2.0

ransac:
  enabled: true
  distance_threshold: 0.02
  ransac_n: 3
  num_iterations: 100

dbscan:
  enabled: true
  eps: 0.05
  min_points: 10
```

## Run

```bash
python scripts/run_pipeline.py
```

The entry script loads the YAML configuration, resolves project-relative paths, and runs the preprocessing pipeline.

## Design

* Parameters are separated from implementation through YAML configuration.
* Denoising is optional to reduce the risk of removing sparse structures.
* RANSAC returns both plane and non-plane point clouds.
* DBSCAN is applied to the non-plane point cloud.
* Visualization works on copied point clouds to avoid modifying original point attributes.

## Known Limitations

Current version is a V0 prototype.

* Parameters are currently tuned on the sample point cloud.
* RANSAC detects the dominant plane, which is not necessarily the ground.
* Fixed DBSCAN parameters may perform poorly when point density varies significantly.
* Logging, unit tests, CLI arguments, and systematic experiment tracking are not implemented yet.
