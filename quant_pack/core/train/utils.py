# -*- coding: utf-8 -*-

from . import lr_policies
from . import qat_policies
from . import loss

__all__ = ["build_qat_policies", "build_lr_policies", "build_losses"]


def build_qat_policies(*cfgs):
    ret_policies = []
    for cfg in cfgs:
        policy = qat_policies.__dict__[cfg["name"]](**cfg["args"])
        ret_policies.append(policy)
    return ret_policies


def build_lr_policies(*cfgs):
    ret_policies = []
    for cfg in cfgs:
        lr_policy_cls = cfg["name"]
        if lr_policy_cls not in lr_policies.__dict__:
            lr_policy_cls += "LrUpdateHook"
        policy = lr_policies.__dict__[lr_policy_cls](**cfg["args"])
        ret_policies.append(policy)
    return ret_policies


def build_losses(cfg):
    loss_cls = cfg["name"]
    if loss_cls not in loss.__dict__:
        loss_cls += "Loss"
    loss_hook = loss.__dict__[loss_cls](**cfg["args"])
    return loss_hook