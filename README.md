# __openBF__-db

---

### Usage

- Fill `parameters/*.txt` with parameter ranges (min/max)

- Run
```bash
$ cd paramters
$ python write_ranges.py
$ cd ..
$ python setup_simulations.py
$ qsub run_array.sh
```

- Wait...

### Results

Explore the dataset with the interactive GUI (tbf)

![img](gui.png)
