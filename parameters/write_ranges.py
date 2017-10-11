import numpy as np

lengths = np.loadtxt("lengths.txt")
radii_min = np.loadtxt("radii_min.txt")
radii_max = np.loadtxt("radii_max.txt")
young = np.loadtxt("young.txt")
resistance = np.loadtxt("resistance.txt")
compliance = np.loadtxt("compliance.txt")

params = ["l", "Rp", "Rd", "E", "R", "C"]
with open("parameters.txt", 'w') as f:
    for v in range(1,lengths.shape[0]+1):
        for p in params:
            if p == "R" and resistance[v-1,0] == 0:
                break
            else:
                if p == 'l':
                    min_value = lengths[v-1,0]
                    max_value = lengths[v-1,1]
                elif p == "Rp":
                    min_value = radii_min[v-1,0]
                    max_value = radii_max[v-1,0]
                elif p == "Rd":
                    min_value = radii_min[v-1,1]
                    max_value = radii_max[v-1,1]
                elif p == 'E':
                    min_value = young[v-1,0]
                    max_value = young[v-1,1]
                elif p == "R":
                    min_value = resistance[v-1,0]
                    max_value = resistance[v-1,1]
                elif p == "C":
                    min_value = compliance[v-1,0]
                    max_value = compliance[v-1,1]

                f.write("v{0}_{1} {2} {3}\n".format(v, p, min_value, max_value))
    f.write("rho 0.7 1.3\n")
    f.write("mu 0.7 1.3\n")
