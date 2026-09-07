import numpy as np


def crop_roi(pcd, x_range=None, y_range=None, z_range=None):
    # 1. 获取点坐标
    pos = np.asarray(pcd.points)

    # 2. 根据 xyz 范围构造 mask
    mask = np.ones(len(pos), dtype=bool)
    if x_range is not None:
        mask &= (pos[:, 0]>=x_range[0]) & (pos[:, 0]<=x_range[1])
    if y_range is not None:
        mask &= (pos[:, 1]>=y_range[0]) & (pos[:, 1]<=y_range[1])
    if z_range is not None:
        mask &= (pos[:, 2]>=z_range[0]) & (pos[:, 2]<=z_range[1])

    # 3. 获取满足条件的 index
    index = np.where(mask)[0]

    # 4. 根据 index 返回裁剪后的 pcd
    cropped_pcd = pcd.select_by_index(index)

    return cropped_pcd


def voxel_downsample(pcd, voxel_size):
    # 调用o3d API实现降采样
    downsampled_pcd = pcd.voxel_down_sample(voxel_size)
    return downsampled_pcd


def statistical_denoise(pcd, nb_neighbors=5, std_ratio=2):
    # 调用o3d API实现统计去噪
    denoised_pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    return denoised_pcd