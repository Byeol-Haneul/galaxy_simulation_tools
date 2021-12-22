import sys
import h5py
import numpy as np

inputfilename = sys.argv[1]
f = h5py.File(inputfilename,'r')
ptype = dict()
particle_list = ["gas", "halo", "disk", "bulge", "stars"]
for i in range(0,5):
    ptype["PartType"+str(i)] = particle_list[i]
print(ptype)

for key in list(f.keys()):
    #try key
    try: 
        ptype[key]
    except KeyError:
        continue
    pnum = f[key]['ParticleIDs'].size
    column_num = 8 if f[key]=="gas" else 7 
    pdata = np.empty([pnum,column_num])
    
    for i in range(0,column_num):
        if i<3:
            pdata[:,i] = f[key]['Coordinates'][:,i]
        elif i<6:
            pdata[:,i] = f[key]['Velocities'][:,i-3]
        elif i==6:
            pdata[:,i] = f[key]['Masses']
        else:
            pdata[:,i] = f[key]['InternalEnergy']
    
    filename = ptype[key]+".data"
    np.savetxt(filename,pdata,delimiter=" ")
    
