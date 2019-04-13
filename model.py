import torch.nn as nn
import torch.nn.init as init

def getModel(n_in, enc_h, rnn_h, n_rnnlayers, n_signs, dropout=0.2):
    print(rnn_h)
    net = nn.Sequential(
        nn.Linear(n_in, enc_h),
        nn.BatchNorm1d(enc_h),
        nn.ReLU(),
        nn.Dropout(dropout),
        nn.GRU(enc_h, rnn_h, n_rnnlayers, dropout=dropout),
        nn.Linear(rnn_h, n_signs),
        nn.BatchNorm1d(rnn_h),
        nn.Sigmoid()
    )

    return net

# class SignToText(nn.Module):

#     def __init__(self, dropout=0.2, n_input, n_hidden, n_signs, n_layers, afn):
#         self.encoder = nn.Linear(n_in, enc_dim)
#         self.rnn = nn.GRU(enc_dim, n_hidden, n_layers, nonlinearity=afn, dropout=dropout)
#         self.rnn_bn = nn.BatchNorm2d(n_hidden)
#         self.decoder = nn.Linear(n_hidden, n_signs)
#         self.sigmoid = nn.Sigmoid()
#         self.init_weights()

#     def init_weights(self):
#         init.xavier_normal(self.rnn)