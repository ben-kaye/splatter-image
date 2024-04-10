
srn_failed, co3d_failed = False, False

try:
    from .srn import SRNDataset
except ImportError as e:
    srn_failed = True
try:
    from .co3d import CO3DDataset
except ImportError as e:
    co3d_failed = True

def get_dataset(cfg, name):
    if cfg.data.category == "cars" or cfg.data.category == "chairs":
        if srn_failed:
            raise ImportError('srn.py failed to import!')
        return SRNDataset(cfg, name)
    elif cfg.data.category == "hydrants" or cfg.data.category == "teddybears":
        if co3d_failed:
            raise ImportError('co3d.py failed to import!')
        return CO3DDataset(cfg, name)