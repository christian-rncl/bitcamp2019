import torch.nn as nn
import torch.nn.init as init

# def getModel(n_in, enc_h, rnn_h, n_rnnlayers, n_signs, dropout=0.2):
    # print(rnn_h)
    # net = nn.Sequential(
    #     nn.Linear(n_in, enc_h),
    #     # nn.BatchNorm1d(num_features=enc_h),
    #     nn.ReLU(),
    #     nn.Dropout(dropout),
    #     nn.GRU(enc_h, rnn_h),
    #     nn.Linear(rnn_h, n_signs),
    #     # nn.BatchNorm1d(rnn_h),
    #     nn.Sigmoid()
    # )

    # return net

class SignToText(nn.Module):

    def __init__(self, n_in, enc_h, rnn_h, n_rnnlayers, n_signs, dropout=0.2):
        super(SignToText, self).__init__()

        self.encoder = nn.Linear(n_in, enc_h)
        self.enc_bn = nn.BatchNorm1d(enc_h)
        self.dropout = nn.Dropout(dropout)
        self.rnn = nn.GRU(enc_h, rnn_h)
        self.rnn_bn = nn.BatchNorm1d(rnn_h)
        self.decoder = nn.Linear(rnn_h, n_signs)
        self.sigmoid = nn.Sigmoid()
        self.init_weights()

    def init_weights(self):
        init.xavier_normal(self.encoder)
        init.xavier_normal(self.rnn)
        init.xavier_normal(self.rnn_bn)
        init.xavier_normal(self.decoder)

    def forward()