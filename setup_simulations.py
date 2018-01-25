import os, sys
import numpy as np
from SALib.sample import latin
from SALib.util import read_param_file

def writeModelCSV(file_name, template, input_point, mesh_type):

    with open(file_name+".csv", 'w') as f:
        header = "name, sn, tn, wkn, L, M, Rp, Rd, E, Pext, R, Cc,\n"
        f.write(header)

        j = 0
        for i in range(len(template)):
            l = template[i].split('\t')

            name = 'v'+l[0]+'_'+l[1]
            sn = l[2]
            tn = l[3]
            L = float(input_point[j])
            j += 1

            if mesh_type == "normal":
                M = np.max([5, int(L*1e3)])
            elif mesh_type == "fine":
                M = np.max([5, 2*int(L*1e3)])
            elif mesh_type == "coarse":
                M = np.max([5, int(0.5*L*1e3)])
            M = int(M)

            Rp = float(input_point[j])
            j += 1

            Rd = float(input_point[j])
            j += 1

            if Rd > Rp:
                Rd = Rp

            E  = float(input_point[j])
            j += 1

            if l[8] == '0':
            	R = '0.'
            	Cc = '0.'
            else:
                R  = float(input_point[j])
                j += 1

                Cc = float(input_point[j])
                j += 1

            # wkn and Pext are always zero for this application
            line = ("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\n"%
            	(name, sn, tn, '0', L, M, Rp, Rd, E, '0.', R, Cc))
            f.write(line)

def writeConstants(file_name, input_point):
	rho = 1060.*input_point[-2]
	mu  = 4.e-3*input_point[-1]

	with open(file_name+"_constants.jl", 'w') as f:
		f.write('const inlet_type = "Q"\n')
		f.write('const inlet_BC_switch = 3\n')
		f.write('const Ccfl = 0.9\n')
		f.write('const cycles = 100\n')
		f.write('const rho = %s\n'% rho)
		f.write('const mu = %s\n'% mu)
		f.write('const gamma_profile = 9\n')
		f.write('const initial_pressure = 0.\n')

#=============================================================================

if __name__ == "__main__":

    mesh_type = "normal"

    # load template file
    with open("network_template.dat", 'r') as f:
        template = f.readlines()
        template = template[1:] # skip first line

    # Latin hypercube design with N samples
    if not os.path.isfile("model_input.txt"):
        params_file = "parameters/parameters.txt"
        N = np.int(sys.argv[1])
        params = read_param_file(params_file)
        design = latin.sample(params, N)
        np.savetxt("model_input.txt", design, delimiter=' ')
    else:
        design = np.loadtxt("model_input.txt")

    # create new directory to save all the results
    try:
    	os.mkdir("results-"+mesh_type)
    except:
    	pass

    os.chdir("results-"+mesh_type)

    for i in range(design.shape[0]):

        if not i%100: print(i)

        d = design[i, :]

        # create simulation subfolder
        idx = str(i+1)
        try:
        	os.mkdir(idx)
        except:
        	pass

        os.chdir(idx)

        writeModelCSV(idx, template, d, mesh_type)
        writeConstants(idx, d)

        os.system("cp ../../_inlet.dat %s" %(idx+"_inlet.dat"))

        os.chdir("..")
    os.chdir("..")
