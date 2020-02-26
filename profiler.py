# file that runs the python profiler on specified script

import profile
import os
import pstats

f=open(str(os.getcwd())+"profile.tmp", 'w')
f.close()

profile.run('import multiDimensionalSpheres;\
            multiDimensionalSpheres.sphere_dict(100, 1)', 'profile.tmp')

p=pstats.Stats('profile.tmp')
p.sort_stats('tottime').print_stats(20)
