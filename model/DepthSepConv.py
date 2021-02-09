import torch
import torch.nn as nn

class DepthSepConvBlock(nn.Module):
    """
        Depth wise Separable Convolution Block for MobileNet
        Used in PFLD backbone
    """
    def __init__(self, in_channels, out_chanels):
        super(DepthSepConvBlock, self).__init__()
        """
            groups parameter: perform a groups of conv 
            https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html
        """
        self.depth_wise_conv = nn.Conv2d(in_channels, in_channels, kernel_size=3, stride=1, groups=in_channels,padding=1)
        self.bn1 = nn.BatchNorm2d(in_channels)
        self.relu = nn.ReLU()
        self.point_wise_conv = nn.Conv2d(in_channels, out_chanels, kernel_size=1, stride=1)
        self.bn2 = nn.BatchNorm2d(out_chanels)

    def forward(self, x):
        # depth wise
        x = self.depth_wise_conv(x)
        x = self.bn1(x)
        x = self.relu(x)
        # point wise
        x = self.point_wise_conv(x)
        x = self.bn2(x)
        x = self.relu(x)

        return x


if __name__ == "__main__":
    depth_conv = DepthSepConvBlock(3,10)
    print(depth_conv)
    x = torch.randn((4, 3,112,112)) # batch, Channels, W, H
    print(x.shape)
    y = depth_conv(x)
    print(y.shape)
