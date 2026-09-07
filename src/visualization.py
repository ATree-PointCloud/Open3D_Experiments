import copy

import open3d as o3d
import numpy as np

import matplotlib.pyplot as plt


def visualize_pcd(pcd):
    # 调用o3d API对输入点云进行可视化
    o3d.visualization.draw_geometries([pcd])


def visualize_clusters(pcd, labels):
    # 长度检查：
    if len(labels) != len(pcd.points):
        raise ValueError("labels and pcd must have same length")

    # 1. 根据 labels 生成每个点对应的颜色
    unique_labels = np.unique(labels)
    cluster_labels = unique_labels[unique_labels >= 0]
    cmap = plt.get_cmap("tab20")

    colors = np.zeros((len(labels), 3))

    for i, label in enumerate(cluster_labels):
        mask = labels == label
        colors[mask] = cmap(i % cmap.N)[:3]

    # 2. noise(label=-1) 单独处理
    mask = labels == -1
    colors[mask] = [0.5, 0.5, 0.5]

    # 3. 将颜色赋给 pcd（使用copy数据避免覆盖原始数据的语义信息）
    vis_pcd = copy.deepcopy(pcd)
    vis_pcd.colors = o3d.utility.Vector3dVector(colors)

    # 4. 调用 Open3D 可视化
    o3d.visualization.draw_geometries([vis_pcd])