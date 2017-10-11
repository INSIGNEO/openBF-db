#!/bin/bash
#$ -l h_rt=03:00:00
#$ -l rmem=1G
#$ -t 1-5000
#$ -N openBF-db
#$ -j y
#$ -o ja/

~/julia0.6/bin/julia run_simulations.jl $SGE_TASK_ID $SGE_TASK_ID normal
