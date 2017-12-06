# __openBF__-db

[![INSIGNEO](https://img.shields.io/badge/-INSIGNEO-red.svg?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAQAAAC1QeVaAAABGElEQVQY012QvyvEcRzGH12p4%2BRHKW6Rugz%2BAnUWGQyUVYRBFuVMBgmL%2BBdsZzBQymT1YyDJxiaTG3RX576f1%2FubXPE23I8uz7M9z7vn6XlLkiRPhFmOuObK8t7BbpRRA19D3OF1Rt7GG%2B91Oxojwnm1jZAN49F0ZRjHKYQRFVMUcE4%2BOhs5YYUqt2wzqrCJc%2B%2BJZoeiTKkrTrNuiwqPeJiRJG8Pq%2BzQL0k2hduDiPFytyTZMj%2F2FY4lqdKLE4lv3JOSRI5qgAtJKqZwYvGM22RNsAPL1yaELM6LwhbOuf4hXOJ2qDhthrPWapHDKUV9kmyJX5xTJjz52ROynOH8Mle%2FtAVovs9xsPmWoHiQPW4oU%2BCJfRuoqX8d8dI8uuCeiQAAAABJRU5ErkJggg%3D%3D)](https://insigneo.org/)
[![CompBioMed](https://img.shields.io/badge/-CompBioMed-yellow.svg?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAAoAAAAQCAMAAAAYoR5yAAAA81BMVEUAAAD%2F%2F%2F%2Bqqqr%2F%2F8z%2FzLP%2FyKT%2F1ar%2F4KP%2F9dj%2F5L%2Fm1bP%2F3bv%2Fx4Dw4eHbzJn%2F26%2F52Zn%2FzobQypT%2F6LveyLH%2FyID63d3%2F05P%2Fx3nt19fZzbT%2Fv2Dx0sHk0NDPtX7%2Fxln207D53abEr3f8vFjx1Jz%2FxWP%2FvmL%2FwWT%2Fw0f8vk7t0aj12aLBsnzz0qbTvZritmTAq3vWtF6%2FrIHHr4rJsor6vGPYu3vCsIft17rewJLCq3nw267KtYn%2Fv1vKtJL%2FvFPzz5v547H536P9uE%2FLrG7LsnHGsHbyvmXexIzWq130qkP3y3%2F8tUr3yYD6s0T8sz78tETsoiaWAAAAUXRSTlMAAgMFCg4YGRocHh4gIiMjKCorLS4uNDQ3OT1ISkxPUFFTVldYXV5eYWJkZWdnaGlqamttbW9wcXN1dnh5e35%2Bf3%2BAgYSFio6Sl5ydn6GkqK2fR9KlAAAAd0lEQVQI1zXGRQKCABRAwWdhY3d3t9iJ3d7%2FNC74zmo4H%2FH4AGBxoWIzetKUnDFu321c2vtUrdLx0y5j8oj9u3sPzFL9Ps9K86%2FmSho5FK77sgmglGKamLUA6gH6rkzHDzTcBDfe6BJYO6A4DKdDFmpOQG2PuskfKZ4MqTH%2F64gAAAAASUVORK5CYII%3D)](http://www.compbiomed.eu/)

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
