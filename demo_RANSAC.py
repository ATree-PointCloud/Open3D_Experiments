import open3d as o3d

def main():
    ply_point_cloud = o3d.data.PLYPointCloud()
    pcd = o3d.io.read_point_cloud(ply_point_cloud.path)

    # 对点云数据进行RANSAC平面分割，返回最优平面参数和内点坐标
    plane_model, inlier = pcd.segment_plane(
        distance_threshold=0.08,
        ransac_n=3,
        num_iterations=1000,
    )

    # 打印平面方程
    a, b, c, d = plane_model
    print(f"平面方程：{a}x + {b}y + {c}z + {d} = 0")

    # 划分内点和外点
    ground = pcd.select_by_index(inlier)
    non_ground = pcd.select_by_index(inlier, invert=True)

    # 染色
    ground.paint_uniform_color([0.765, 0.475, 0.384])
    non_ground.paint_uniform_color([0.361, 0.545, 0.631])

    # 可视化
    o3d.visualization.draw_geometries([ground, non_ground],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024]
                                      )


if __name__ == '__main__':
    main()