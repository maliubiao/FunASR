
def get_padding(kernel_size, dilation=1):
    return int((kernel_size * dilation - dilation) / 2)


def init_weights(m, mean=0.0, std=0.01):
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        m.weight.data.normal_(mean, std)


from cosyvoice.modules.hifigan_module.generator import HifiGenerator, NsfHifiGenerator, HiFTGenerator
from cosyvoice.modules.hifigan_module.discriminator import MultipleDiscriminator
from cosyvoice.modules.hifigan_module.nsf_utils import ConvRNNF0Predictor
