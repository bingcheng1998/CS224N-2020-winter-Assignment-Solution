#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2019-20: Homework 5
"""

import torch
import torch.nn as nn

class CNN(nn.Module):
    ### YOUR CODE HERE for part 1g
    def __init__(self, in_channels, out_channels, kernel_size = 5, padding = 1, stride = 1):
        super(CNN, self).__init__()
        self.conv = nn.Conv1d(in_channels, out_channels,  kernel_size, stride, padding)

    def forward(self, x_reshaped):
        #  map from x_reshaped to x_conv_out
        # x_reshaped (N, e_char, m_word)
        # x_conv (N, e_word, (m_word - kernel_size + 2*padding)/stride + 1)
        # x_conv_out (N, e_word)
        x_conv = self.conv(x_reshaped)
        x_conv_out = torch.max(x_conv, 2)[0]
        return x_conv_out

    ### END YOUR CODE

