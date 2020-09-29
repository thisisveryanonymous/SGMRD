<meta name="robots" content="noindex">

# SGMRD 
# Streaming Greedy Maximum Random Deviation

Welcome to this anonymous GitHub repository for the paper ```Efficient Subspace Search in Data Streams```. 
You will find all the required code, data, and documentation to reproduce the results from our study. 
This repository will be de-anonymised after acceptance of the paper. 

This repository is released under the AGPLv3 license. Please see the [LICENSE.md](LICENSE.md) file. 

See the README of the subfolders `StreamHiCS` and `xStream` for information about the licensing of those units. 

## Data

Our benchmark data sets are in the folder `/data`. Please decompress `data.7z` to set up this folder. 

## Quick Start

### Build it and run it 

**Requirements** : ([Oracle JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
or [OpenJDK 8](http://openjdk.java.net/install/)) and [sbt](https://www.scala-sbt.org/1.0/docs/Setup.html)

The project is built with sbt (version 1.2.8). You can compile, package or run the project as follows:

```
sbt compile
sbt package 
sbt "run <arguments>"
```

In case you need to adjust the amount of memory assigned to the JVM, you can set the `javaOptions` (`-Xmx` and `-Xms`) in `build.sbt`.

## Reproducing the experiments

The results of the experiments are stored in `.csv` files in separate folders in `experiments/`.

### SGMRD

Parameter sensitivity study (we use the pyro dataset)

```
sbt "run experiments.SGMRDsearchers_pi" # Run with various update strategies and v (step size)
sbt "run experiments.SGMRDsearchers_gold" # Run the "golden" baseline
sbt "run experiments.SGMRDsearchers_L" # Let L (the number of plays per round) vary
sbt "run experiments.SGMRDsearchers_runtime" # Runtime evaluation
```

Perform the search for the synthetic and the real-world data

```
sbt "run experiments.SGMRDsearchers"
```

Copy all the resulting `*-subspaces-0.txt` files into `data/subspaces`, then run the outlier detection:

```
sbt "run experiments.SGMRDminers"
```

Run the outlier detection on the subspaces from StreamHiCS (execute the StreamHiCS section below first)

```
sbt "run experiments.StreamHiCSminers"
```

### StreamHiCS

**Requirements** :  ([Oracle JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
                    or [OpenJDK 8](http://openjdk.java.net/install/))

```
cd StreamHiCS/
bash run_experiments.sh
```

This will run the subspace search from StreamHiCS with default parameters. 
The results are then available in `StreamHiCS/results`. To run the outlier detection based on those subspaces, see the experiment `StreamHiCSminers` in the section SGMRD. 

### xStream

**Requirements**: g++, Python3, numpy, pandas, sklearn (e.g., Anaconda distribution)

#### Build 

```
cd xStream/cpp/
make clean
make optimized
```

#### Run the experiment 

```
cd xStream/
python run_experiments.py
```
This will run the xStream outlier detection (parameters: ```--initsample=1000 --nwindows=100 --scoringbatch=100 --rowstream```). 
The results are then available in `xStream/reports`. 

## Visualize the results, create figures

**Requirements**: Jupyter notebook, Python3, numpy, pandas

We provide in folder `visualize/` a set of Jupyter notebooks to reproduce the figures in our study

- `SGMRDsearchers_pi.ipynb`: Reproduces Figure 7,8,9,10. 
- `SGMRD_runtime.ipynb`: Reproduces Figure 14. 
- `SGMRD_success.ipynb`: Reproduces Figure 11. 
- `SGMRDsearchers_L.ipynb`: Reproduces Figure 12.
- `SGMRDsearchers_runtime.ipynb`: Reproduces Figure 13.
- `SGMRDminers.ipynb`: Fetch the outlier detection results for SGMRD. 
- `StreamHiCSminers.ipynb`: Fetch the outlier detection results for StreamHiCS. 

