import torch.nn as nn
import torch.nn.init as init

class SigntoText(nn.Module):
    """Container module with an encoder, a recurrent module, and a decoder."""

    def __init__(self, nclasses, ninp, nhid, nlayers, dropout=0.5):
        super(RNNModel, self).__init__()
        self.drop = nn.Dropout(dropout)
        self.encoder = nn.Linear(ntoken, ninp)
        self.rnn = nn.GRU(ninp, nhid, nlayers, dropout=dropout)
        self.decoder = nn.Linear(nhid, ntoken)

        # # Optionally tie weights as in:
        # # "Using the Output Embedding to Improve Language Models" (Press & Wolf 2016)
        # # https://arxiv.org/abs/1608.05859
        # # and
        # # "Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling" (Inan et al. 2016)
        # # https://arxiv.org/abs/1611.01462
        # if tie_weights:
        #     if nhid != ninp:
        #         raise ValueError('When using the tied flag, nhid must be equal to emsize')
        #     self.decoder.weight = self.encoder.weight

        self.init_weights()
        self.nhid = nhid
        self.nlayers = nlayers

    def init_weights(self):
        initrange = 0.1
        self.encoder.bias.data.zero_()
        self.encoder.weight.data.uniform_(-initrange, initrange)
        self.decoder.bias.data.zero_()
        self.decoder.weight.data.uniform_(-initrange, initrange)

    def forward(self, input, hidden):
        emb = self.drop(self.encoder(input))
        output, hidden = self.rnn(emb, hidden)
        output = self.drop(output)
        # decoded = self.decoder(output.view(output.size(0)*output.size(1), output.size(2)))
        output = self.decoder(output)
        return decoded.view(output.size(0), output.size(1), decoded.size(1)), hidden

    def init_hidden(self, bsz):
        weight = next(self.parameters())
        # if self.rnn_type == 'LSTM':
        #     return (weight.new_zeros(self.nlayers, bsz, self.nhid),
        #             weight.new_zeros(self.nlayers, bsz, self.nhid))
        # else:
        return weight.new_zeros(self.nlayers, bsz, self.nhid)


def getSequential(n_in, enc_h, rnn_h, n_rnnlayers, n_signs, dropout=0.2):
    print(rnn_h)
    net = nn.Sequential(
        nn.Linear(n_in, enc_h),
        # nn.BatchNorm1d(enc_h),
        nn.ReLU(),
        nn.Dropout(dropout),
        nn.GRU(enc_h, rnn_h, n_rnnlayers, dropout=dropout),
        nn.Linear(rnn_h, n_signs),
        # nn.BatchNorm1d(rnn_h),
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