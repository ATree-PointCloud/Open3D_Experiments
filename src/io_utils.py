import open3d as o3d
import yaml


def load_point_cloud(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    return pcd


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config