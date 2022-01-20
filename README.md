# Physiological Data Collection using LabStream

Prerequisites
============
- **Every Platform:** make sure that you have Miniconda installed and that the
  `conda` command-line interface is on your path

Config File
============

config.ini contains the following parameters:

### File info
These parameters set-up the file save directory for the .csv files

### Zephyr Info
These parameters are used to set functions for the Zephyr BioHarness
- macAddress : device mac address or "unknown". 

    --Unknown will search for available BioHarnesses

### Reed Info
These parameters are used for the Reed Decibel Meter
- Application Path: the R8080.exe path. 

    --This application must be running in order to obtain the sensor readings

Installing/Running
==================

- **Windows:** Invoke the script `run.cmd`, which will, if necessary, create a fresh Python 
  environment and install the necessary dependencies into it
- **Linux/MacOS:** Not yet supported
- **Alternative manual install:** you can also follow the instructions in 
  `conda-environment.yml` to install a Python environment yourself or to add the
  necessary requirements to an existing environment, and then you can use that
  interpreter to run `main.py`
