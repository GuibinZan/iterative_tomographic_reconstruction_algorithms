import os
import shutil


if os.path.exists('build'):
    shutil.rmtree('build')

if os.path.isfile( 'radon_distance_driven.c' ) is True:
    os.remove( 'radon_distance_driven.c' ) 

os.system('python create_module.py build_ext --inplace')
