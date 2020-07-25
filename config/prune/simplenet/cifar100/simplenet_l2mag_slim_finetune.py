# -*- coding: utf-8 -*-
"""Configurations for slimming simple network.

- Author: Curt-Park
- Email: jwpark@jmarple.ai
"""

from config.train.simplenet.cifar100 import simplenet, simplenet_finetune

regularizer_params = {
    "REGULARIZER": "BnWeight",
    "REGULARIZER_PARAMS": dict(coeff=1e-5),
    "EPOCHS": 20,
}

train_config = simplenet.config
finetune_config = simplenet_finetune.config
train_config.update(regularizer_params)
finetune_config.update(regularizer_params)


config = {
    "TRAIN_CONFIG": train_config,
    "TRAIN_CONFIG_AT_PRUNE": finetune_config,
    "N_PRUNING_ITER": 15,
    "PRUNE_METHOD": "SlimMagnitude",
    "PRUNE_PARAMS": dict(
        PRUNE_AMOUNT=0.1,
        NORM=2,
        STORE_PARAM_BEFORE=10,
        PRUNE_START_FROM=0,
        PRUNE_AT_BEST=False,
    ),
}
