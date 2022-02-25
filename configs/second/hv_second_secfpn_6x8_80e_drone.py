_base_ = [
    '../_base_/models/hv_second_secfpn_drone.py',
    '../_base_/datasets/drone-data.py', '../_base_/schedules/cyclic_40e.py',
    '../_base_/default_runtime.py'
]
point_cloud_range = [-5, -5, -0.5, 5, 5, 5]
model = dict(
    bbox_head=dict(
        type='Anchor3DHead',
        num_classes=1,
        anchor_generator=dict(
            _delete_=True,
            type='Anchor3DRangeGenerator',
            ranges=[[-5.0, -5.0, -0.45, 5.0, 5.0, 2.95]],
            sizes=[[0.46, 0.46, 0.11]],
            rotations=[0, 1.57],
            reshape_out=True)),
    # model training and testing settings
    train_cfg=dict(
        _delete_=True,
        assigner=dict(
            type='MaxIoUAssigner',
            iou_calculator=dict(type='BboxOverlapsNearest3D'),
            pos_iou_thr=0.35,
            neg_iou_thr=0.2,
            min_pos_iou=0.2,
            ignore_iof_thr=-1),
        allowed_border=0,
        pos_weight=-1,
        debug=False))
