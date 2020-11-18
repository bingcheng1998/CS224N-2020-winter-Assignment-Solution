#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2019-20: Homework 5
"""

import torch
import torch.nn as nn

class Highway(nn.Module):
    ### YOUR CODE HERE for part 1f
    def __init__(self, e_word):
        super(Highway, self).__init__()
        self.W_proj = nn.Linear(e_word, e_word)
        self.W_gate = nn.Linear(e_word, e_word)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        # self.X_conv_out = X_conv_out

    def forward(self, X_conv_out):
        # map from x_conv_out to x_highway.
        X_proj = self.relu(self.W_proj(X_conv_out))
        X_gate = self.sigmoid(self.W_gate(X_conv_out))
        X_highway = X_gate.mul(X_proj) + (1 - X_gate).mul(X_conv_out)
        return X_highway




    ### END YOUR CODE

