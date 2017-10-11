using openBF

istart = parse(Int, ARGS[1])
iend = parse(Int, ARGS[2])
mesh_type = ARGS[3]

timelog = open("times/time$istart.log", "w")
errorslog = open("errors/errors$istart.log", "w")
tic()
for i = istart:iend

	try
		i = string(i)
		cd("results-$mesh_type/$i/")

		project_name = string(i)

		openBF.projectPreamble(project_name)

		println("Load project $project_name files")
		include(join(["results-$mesh_type/$i/", project_name, "_constants.jl"]))

		model = openBF.readModelData(join([project_name, ".csv"]))

		heart, blood_prop, total_time = openBF.loadGlobalConstants(project_name,
			inlet_BC_switch, inlet_type, cycles, rho, mu, gamma_profile)

        vessels = [openBF.initialiseVessel(model[1,:], 1, heart, blood_prop,
          initial_pressure, Ccfl)]
        edge_list = zeros(Int8, length(model[:,1]), 3)
        edge_list[1,1] = vessels[1].ID
        edge_list[1,2] = vessels[1].sn
        edge_list[1,3] = vessels[1].tn

        for i in 2:length(model[:,1])
          push!(vessels, openBF.initialiseVessel(model[i,:], i, heart, blood_prop,
            initial_pressure, Ccfl))
          edge_list[i,1] = vessels[i].ID
          edge_list[i,2] = vessels[i].sn
          edge_list[i,3] = vessels[i].tn
        end

		println("Start simulation \n")
		current_time = 0

        dts  = zeros(Float64, length(edge_list[:,1]))
        dt = openBF.calculateDeltaT(vessels, dts)

        # prog = ProgressMeter.Progress(Int(ceil(total_time/dt)), 1, "Running ", 50)

		passed_cycles = 0

		tic()
		counter = 1
        jump = 100
        timepoints = linspace(0, heart.cardiac_T, jump)
		while true
			dt = openBF.calculateDeltaT(vessels, dts)

			current_time += dt
			openBF.solveModel(vessels, heart, edge_list, blood_prop, dt, current_time)

			openBF.updateGhostCells(vessels)

            if current_time >= timepoints[counter]
              openBF.saveTempData(current_time, vessels)
              counter += 1
            end

			# ProgressMeter.next!(prog)

			if (current_time - heart.cardiac_T*passed_cycles) >= heart.cardiac_T &&
				(current_time - heart.cardiac_T*passed_cycles + dt) > heart.cardiac_T

                openBF.closeTempFiles(vessels)

                err = openBF.checkConvergence(edge_list, vessels, passed_cycles)
                println("Iteration: ", passed_cycles, " Error: ", err,"%")

                openBF.transferLastToOut(vessels)
                openBF.openCloseLastFiles(vessels)
                openBF.transferTempToLast(vessels)
                openBF.openTempFiles(vessels)

                if err < 5.
                    break
                end

			    passed_cycles += 1
                timepoints += heart.cardiac_T
                counter = 1
			end

			if current_time >= total_time
                break
			end
		end
		@printf "\n"
		toc()

		openBF.closeTempFiles(vessels)
		openBF.transferTempToOut(vessels)

		# run(`sh ../cleaner-d.sh`)

		cd("../../../")

	catch err
		write(errorslog, "$i\n")
		write(errorslog, string(err))
		write(errorslog, "\n\n")
		continue
	end

end
tt = toc()
write(timelog, "$tt")
close(timelog)
close(errorslog)
