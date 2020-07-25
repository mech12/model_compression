# -*- coding: utf-8 -*-
"""Configurations for slimming simple network.

- Author: Curt-Park
- Email: jwpark@jmarple.ai
"""

from config.train.simplenet.cifar100 import simplenet

train_config = simplenet.config
train_config.update({"REGULARIZER": "BnWeight", "REGULARIZER_PARAMS": dict(coeff=1e-5)})
config = {
    "TRAIN_CONFIG": train_config,
    "N_PRUNING_ITER": 5,
    "EPOCHS": 20,
    "PRUNE_METHOD": "NetworkSlimming",
    "PRUNE_PARAMS": dict(
        PRUNE_AMOUNT=0.2, STORE_PARAM_BEFORE=20, PRUNE_START_FROM=0, PRUNE_AT_BEST=False
    ),
}
