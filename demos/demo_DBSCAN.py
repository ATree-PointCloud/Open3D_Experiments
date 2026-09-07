import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

def main():
    ply_pcd = o3d.data.PLYPointCloud()
    pcd = o3d.io.read_point_cloud(ply_pcd.path)

    # 利用RANSAC去除地面和墙面，降低目标物粘连情况
    model, inliers = pcd.segment_plane(distance_threshold=0.02, ransac_n=3, num_iterations=1000)
    pcd = pcd.select_by_index(inliers, invert=True)
    model, inliers = pcd.segment_plane(distance_threshold=0.02, ransac_n=3, num_iterations=1000)
    pcd = pcd.select_by_index(inliers, invert=True)
    #
    # o3d.visualization.draw_geometries([pcd],
    #                                   zoom=0.3412,
    #                                   front=[0.4257, -0.2125, -0.8795],
    #                                   lookat=[2.6172, 2.0475, 1.532],
    #                                   up=[-0.0694, -0.9768, 0.2024]
    #                                   )

    labels = np.array(
        pcd.cluster_dbscan(
            eps=0.02,
            min_points=10,
            print_progress=True
        )
    )

    max_label = labels.max()
    print(f"cluster nums: {max_label + 1}")

    # 返回RGBA颜色
    colors = plt.get_cmap("tab20")(
        labels / (max_label if max_label > 0 else 1)
    )

    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcd],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024]
                                      )

if __name__ == '__main__':
    main()