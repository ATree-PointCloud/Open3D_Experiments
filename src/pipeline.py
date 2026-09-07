from .io_utils import load_point_cloud
from .filters import crop_roi, voxel_downsample, statistical_denoise
from .segmentation import segment_plane_ransac, cluster_dbscan
from .visualization import visualize_pcd, visualize_clusters


def run_pipeline(config):
    pcd = load_point_cloud(config["input"]["path"])

    if config["roi"]["enabled"]:
        pcd = crop_roi(
            pcd,
            x_range=config["roi"]["x_range"],
            y_range=config["roi"]["y_range"],
            z_range=config["roi"]["z_range"]
        )

    if config["voxel"]["enabled"]:
        pcd = voxel_downsample(pcd, config["voxel"]["voxel_size"])

    if config["denoise"]["enabled"]:
        pcd = statistical_denoise(
            pcd,
            config["denoise"]["nb_neighbors"],
            config["denoise"]["std_ratio"]
        )

    if config["ransac"]["enabled"]:
        plane_model, plane_pcd, non_plane_pcd = segment_plane_ransac(
            pcd,
            config["ransac"]["distance_threshold"],
            config["ransac"]["ransac_n"],
            config["ransac"]["num_iterations"]
        )
    else:
        plane_model, plane_pcd, non_plane_pcd = None, None, pcd

    if config["dbscan"]["enabled"]:
        labels = cluster_dbscan(non_plane_pcd, config["dbscan"]["eps"], config["dbscan"]["min_points"])
    else:
        labels = None

    if config["visualization"]["enabled"]:
        if labels is not None:
            visualize_clusters(non_plane_pcd, labels)
        else:
            visualize_pcd(non_plane_pcd)

    return {
        "pcd": pcd,
        "non_plane_pcd": non_plane_pcd,
        "plane_model": plane_model,
        "labels": labels
    }