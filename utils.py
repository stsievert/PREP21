import skorch
import torch.optim as optim
import seaborn as sns
import torch.nn as nn


def Optimizer(max_epochs=200, **kwargs):
    to_pass = dict(
        verbose=False,
        train_split=None,
        max_epochs=max_epochs,
        batch_size=-1,
        optimizer=optim.LBFGS,
        criterion=nn.MSELoss,
#         optimizer=optim.SGD,
#         optimizer__lr=0.05,
#         optimizer__t0=int(max_epochs * 0.5)
    )
    to_pass.update(kwargs)
    return skorch.NeuralNet(**to_pass)


def plot(data, model):
    sns.scatter(
        x="weight",
        y="max_running_speed",
        hue="type",
        data=data,
    )