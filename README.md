# __openBF__-db

[![openBF](https://img.shields.io/badge/-openBF-red.svg?colorA=ffffff&colorB=008080&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABQAAAAOCAQAAACFzfR7AAAA10lEQVQoz4XQIUvDARCG8R%2BCaUEEqwwMwyKCYbImLCp%2BAoPJpMWyYFnfN1BBP4IGk0FkYBkyDYJgkBXTUOcYbFM8g0M3t%2F98rhz3Pnfh6GfKg7bQ8exG1hh2xE%2B9SCeLuT4xlC39RkeKUr1%2B1uWAGMKF%2Be9wW7gzgzX1IS2EhhVIaQnnSj6HlEerCsKrObgeeSeEPfvy7oUzqCaKVzLy3oUnpnWFsi3txIUP6%2BwKdQvIuh2pvdmAUwcyvfdM2PwjNx0mvz3tRAgVOZPGciw0LfqXmprlwdEX%2F8%2BRhjBYrRoAAAAASUVORK5CYII%3D)](https://github.com/INSIGNEO/openBF)

[![INSIGNEO](https://img.shields.io/badge/-INSIGNEO-red.svg?colorA=ffffff&colorB=cf2020&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAABC1BMVEUAAAD%2FAAC%2FAADMGhrRFxfSHh7VHBzJGxvTISHKICDMHx%2FOHR3RJCTTIyPOISHPICDMHR3NIyPNICDRISHQHx%2FQHx%2FOHx%2FQISHOICDQICDQHx%2FOHx%2FPISHQISHQICDOICDQISHOICDQICDPISHPICDQISHPICDPICDOHx%2FPISHPISHQISHPICDPISHPISHQICDOICDOICDPHx%2FPICDPICDOICDPICDPICDPICDPHx%2FPICDPICDQICDPICDPHx%2FQISHOICDPICDPICDPICDPICDPHx%2FMISHOICDPICDQICDPICDPISHPHx%2FPICDPICDPICDPICDPICDPICDOICDPHx%2FPICDPICDPICDPICDi8V76AAAAWHRSTlMAAgQKCxESExcYGRocHR8gIyRITVFSU1ZYYWJjZGZnaWxucXV5fH%2BAg4SFjI%2BUlZeYqKuusbK2ubrDxcbHycvMzdHU2Nrb4uLl5%2Bnq6%2Bzt7u%2F09vf7%2FP3%2B%2FHERCQAAAKVJREFUeAEdx%2BVCg2AAhtHHAANDMQRD7ECwO7DDjViM7b3%2FK9n4zr9Dxdk6jjc4s02si46kK7tMLGDuW%2Fq%2FvdxZlt5shh7VWhsGTqWvTVYll0q4PjMyy7VuYHQ7nIL98oVMAey183sI9EtNPpzXfz7BV8aHIpi%2Fe3ch1iuHysYxnFxHTDf1bD7xpMKBxa6Kk6WVKFXPY8BLZTQWMMYOHvK%2FZHcS6AOapR0V%2FpSSVQAAAABJRU5ErkJggg%3D%3D)](https://insigneo.org/)
[![CompBioMed](https://img.shields.io/badge/-CompBioMed-yellow.svg?colorA=00&colorB=f4b540&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAAoAAAAQCAMAAAAYoR5yAAAA81BMVEUAAAD%2F%2F%2F%2Bqqqr%2F%2F8z%2FzLP%2FyKT%2F1ar%2F4KP%2F9dj%2F5L%2Fm1bP%2F3bv%2Fx4Dw4eHbzJn%2F26%2F52Zn%2FzobQypT%2F6LveyLH%2FyID63d3%2F05P%2Fx3nt19fZzbT%2Fv2Dx0sHk0NDPtX7%2Fxln207D53abEr3f8vFjx1Jz%2FxWP%2FvmL%2FwWT%2Fw0f8vk7t0aj12aLBsnzz0qbTvZritmTAq3vWtF6%2FrIHHr4rJsor6vGPYu3vCsIft17rewJLCq3nw267KtYn%2Fv1vKtJL%2FvFPzz5v547H536P9uE%2FLrG7LsnHGsHbyvmXexIzWq130qkP3y3%2F8tUr3yYD6s0T8sz78tETsoiaWAAAAUXRSTlMAAgMFCg4YGRocHh4gIiMjKCorLS4uNDQ3OT1ISkxPUFFTVldYXV5eYWJkZWdnaGlqamttbW9wcXN1dnh5e35%2Bf3%2BAgYSFio6Sl5ydn6GkqK2fR9KlAAAAd0lEQVQI1zXGRQKCABRAwWdhY3d3t9iJ3d7%2FNC74zmo4H%2FH4AGBxoWIzetKUnDFu321c2vtUrdLx0y5j8oj9u3sPzFL9Ps9K86%2FmSho5FK77sgmglGKamLUA6gH6rkzHDzTcBDfe6BJYO6A4DKdDFmpOQG2PuskfKZ4MqTH%2F64gAAAAASUVORK5CYII%3D)](http://www.compbiomed.eu/)


[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

The code in this repository can be used to generate physiological virtual population of vascular networks. The pulse wave propagation can be simulated with [openBF](https://github.com/INSIGNEO/openBF) solver. The network is based on [ADAN56 model](https://github.com/alemelis/openBF-hub/tree/master/models/boilleau2015benchmark/adan56).

__Requirements__:
- Python + [SALib](https://github.com/SALib/SALib) + NumPy
- Julia + [openBF](https://github.com/INSIGNEO/openBF)

### Usage

- First, the lower and upper bounds for each parameter should be defined. Fill `parameters/*.txt` with parameter ranges (min/max).
- Create SALib input files as

```bash
$ cd parameters
$ python write_ranges.py
$ cd ..
```

- SALib is used to sample input points via the Latin Hypercube method

```bash
$ python setup_simulations.py <N, number of samples>
```

This will generate a folder with as many input sub-folder as `N`.

- Simulations can be run as

```bash
$ julia run_simulations.jl 1 <N>
```

Alternatively, on SGE systems, use the batch script

```bash
$ qsub run_array.sh
```

- :clock1: Wait...

<!-- ### Results

Explore the dataset with the interactive GUI

![img](gui.png) -->
