"""
TODO
"""

import argparse
from pathlib import Path

import torch
from torch.nn import MSELoss

from image_regressor.loader import get_loaders
from image_regressor.model import get_models
from image_regressor.train import save_inference, run_train
from image_regressor.utils import load_config, login_wandb, system_check, wandb_run
from image_regressor.vis import vis_model


def main():
    num_cpus, device = system_check()
    config = load_config()
    models = get_models(config, None, device)
    run = None
    if config["wandb"]:
        login_wandb(config)
        run = wandb_run(config)
    train_loader, test_loader = get_loaders(config, debug=True)

    if config["train"]:
        assert len(models) == 1
        model = models[0]
        run_train(
            train_loader=train_loader,
            val_loader=test_loader,
            model=model,
            config=config,
            device=device,
            run=run,
        )
    else:
        save_inference(
            models, (train_loader, test_loader), ("train", "test"), config, device
        )


if __name__ == "__main__":
    main()
