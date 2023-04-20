CONFIG = {
    "data_dir": None,
    "extension": "jpg",
    "regression_key": "value",
    "starting_channels": 1,

    "wandb": False,
    "wandb_print":
    [
        "use_existing",
        "lr",
        "pool",
    ],
    "keyfile": "/hdd/wandb.json",
    "train": True,
    # Option to log images during training to the /tmp/ dir for visualization.
    # This is likely a slowdown so should be used for debugging.
    "log_images": False,

    "models": [],
    # "models": ["checkpoint.pth"],
    # "models": [{"name": "checkpoint.pth", "run_path": "diplernerz/hw3p2-ablations/3q34k58v", "replace": True}],
    # "models": [{"name": "checkpoint.pth", "run_path": "diplernerz/hw3p2-ablations/fqsx3zdk", "replace": True},
    #            {"name": "checkpoint.pth", "run_path": "diplernerz/hw3p2-ablations/37z196qx", "replace": True},
    #            {"name": "checkpoint.pth", "run_path": "diplernerz/hw3p2-ablations/phan45yu", "replace": True}],
    # "models": ["checkpoint.pth",
    #            {"name": "checkpoint.pth", "run_path": "diplernerz/hw2p3-ablations/sk5209ak", "replace": True}],

    "lr": 5e-2,
    "scheduler": "constant",
    "StepLR_kwargs": {"step_size": 5, "gamma": 0.2},
    "LRTest_kwargs": {"min_per_epoch": 5, "runtime_min": 20, "start": 1e-6, "end": 0.5},
    "OneCycleLR_kwargs": {"max_lr": 2.5e-3, "min_lr": 2.5e-6},
    "CosMulti_kwargs": {"epoch_per_cycle": 20, "eta_min": 1.5e-6},

    # Augmentations are stored in a json file as (name, kwargs). They are
    # applied in the loader phase. The way to experiment with augmentations is
    # to make a copy of the file, set those that you want, and then select the
    # files one-by-one as a command-line argument.
    "train_augmentation_path": "./train_augmentations.json",
    "test_augmentation_path": "./test_augmentations.json",

    "batch_size": 32,  # Increase if you can handle it, generally
    "epochs": 20,
    "wd": 0.01,

    # TODO: Try out all of these models on bigger input pictures
    # None
    # resnet18, resnet34, resnet50, resnet101, resnet152,
    # vgg11, vgg11_bn, vgg13, vgg13_bn, vgg16, vgg16_bn, vgg19, vgg19_bn
    # DON'T USE FOR NOW: inception_v3
    # densenet121, densenet161, densenet169, densenet201
    # mobilenet_v2, mobilenet_v3_large, mobilenet_v3_small
    # efficientnet_b0, efficientnet_b1, efficientnet_b2, efficientnet_b3,
    # efficientnet_b4, efficientnet_b5, efficientnet_b6, efficientnet_b7,
    # efficientnet_v2_s, efficientnet_v2_m, efficientnet_v2_l
    "use_existing": None,
    "pretrained": True,
    "frozen_embedding": False,

    # Used only when not using an existing encoder
    "cnn_depth": 3,
    "cnn_kernel": 3,
    "cnn_width": 256,
    "cnn_outdim": 128,
    "cnn_downsample": 4,
    "cnn_batchnorm": True,
    "cnn_dropout": None,
    "pool": "max", # "avg",
    "lin_depth": 3,
    "lin_width": 256,
    "lin_batchnorm": True,
    "lin_dropout": None,

    # How many epochs between validation checks (can take a while)
    "eval_report_iter": 1,
    # How many batches between wandb logs if we are logging batch stats
    "train_report_iter": 10,
}