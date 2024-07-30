import pickle
import numpy as np
np.set_printoptions(threshold=np.inf) #
#import torch
#torch.set_printoptions(threshold=np.inf)
#pytorch

f = open("path", 'rb')
inf = pickle.load(f)
f.close()
inf = str(inf)
ft = open("path", 'w')
ft.write(inf)