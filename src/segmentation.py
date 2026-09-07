import open3d as o3d
import numpy as np


def segment_plane_ransac(pcd, distance_threshold, ransac_n=3, ransac_iterations=100):
    # 调用o3d API实现平面分割
    plane_model, inliers = pcd.segment_plane(distance_threshold=distance_threshold, ransac_n=ransac_n, num_iterations=ransac_iterations)
    plane_pcd = pcd.select_by_index(inliers)
    non_plane_pcd = pcd.select_by_index(inliers, invert=True)

    return plane_model, plane_pcd, non_plane_pcd


def cluster_dbscan(pcd, eps=0.01, min_points=10):
    # 调用 Open3D API 聚类
    labels = np.asarray(pcd.cluster_dbscan(eps=eps, min_points=min_points, print_progress=False))
    return labels