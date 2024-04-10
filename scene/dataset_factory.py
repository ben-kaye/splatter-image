
srn_failed, co3d_failed = False, False

try:
    from .srn import SRNDataset
except AssertionError as e:
    srn_failed = True
try:
    from .co3d import CO3DDataset
except AssertionError as e:
    co3d_failed = True

def get_dataset(cfg, name):
    if cfg.data.category == "cars" or cfg.data.category == "chairs":
        if srn_failed:
            raise ImportError('SRN dataset not found. Update env.yaml')
        return SRNDataset(cfg, name)
    elif cfg.data.category == "hydrants" or cfg.data.category == "teddybears":
        if co3d_failed:
            raise ImportError('CO3D dataset not found. Update env.yaml')
        return CO3DDataset(cfg, name)