import os
from aeon import Dataloader


pdir = os.path.dirname(os.path.abspath(__file__))
manifest_root = os.path.join(pdir, '..', 'loader', 'test', 'test_data')

manifest_file = os.path.join(manifest_root, 'manifest.csv')
cache_root = ""

cfg = {
           'manifest_filename': manifest_file,
           'manifest_root': manifest_root,
           'batch_size': 20,
           'block_size': 40,
           'cache_directory': cache_root,
           'type': 'image,label',
           'image': {'height': 28,
                     'width': 28,
                     'channels': 1},
           'label': {'binary': False}
        }

d1 = Dataloader(config=cfg)
print("d1 length {0}").format(len(d1))

shapes = d1.shapes()

print("shapes {}".format(shapes))

for x in d1:
    print("d1, v1: {0}").format(x.keys())

# d1.reset()

# for x in d1:
#     print("d1 {0}").format(x.keys())