##  In this test a volume of sinograms of Shepp-Logan is reconstructed with the
##  Separable Paraboloidal Surrogate (-a sps) the gridding
##  projectors with minimal oversampling (-pr grid-kb), 30 iterations
##  (-n 100).

from __future__ import division , print_function
import os

os.chdir( '../algorithms' )
command = 'python -W ignore sir.py -a sps -Di ../data/sl3d/sl3d_256_sino_ang0304/ -Do ../data/sl3d/sl3d_256_reco_ang0304/ -o shepp_logan_pix0256_ang0304_sino_reco.DMP -pr grid-pswf -r huber -hc 0.1 -n 10 -p'
print( '\n\nCommand line:\n', command )
os.system( command )