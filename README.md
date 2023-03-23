
An independent verification of the DEF formulas of SDIA
====================================

This project is a simple experiment that stresses a server to certain fixed loads to measure energy consumption. Later, the obtained results are compared against the predictions from the DEF (Digital Environmental Formulas) from SDIA for that particular server.

The aim of this experiment is to independently verify the validity of DEF formulas to model real systems.

Explanatory slides
----------------------
You can find here the [slides](https://docs.google.com/presentation/d/18TdcRDZyTFe_NGjTVC7JJMNeW0zNQJP_5W00Oa4zBIg/edit?usp=sharing)

Experiment Description
----------------------

The experiment aims to measure the energy consumption of a server under different loads. The server is subjected to fixed loads using a set of Linux tools. The energy consumption data is obtained via WattsupPro, while the CPU data is obtained via 'lm-sensors' and 'mpstat'. The obtained data is then preprocessed using Python and analysed using Excel.

Workflow
--------

The experiment workflow consists of the following steps:

1.  The bash scripts are used to subject the server to different fixed loads.
2.  The energy consumption data is collected via WattsupPro.
3.  The CPU data is collected via 'lm-sensors' and 'mpstat'.
4.  The collected data is preprocessed using Python.
5.  The cleaned data is analysed using Excel

Running the Experiment
----------------------

To run the experiment, follow these steps:

1.  Clone the repository.
2.  Install the necessary dependencies (e.g., stress-ng, WattsupPro, lm-sensors, mpstat).
3.  Run the bash scripts to subject the server to different loads.
4.  Collect the energy consumption and CPU data using the respective tools.
5.  Preprocess the data using the provided Python scripts.

Repository Structure
--------------------

The repository contains the following files and directories:

-   `bash_scripts/`: contains the bash scripts used to subject the server to different loads.
-   `preprocessing/`: contains the Python scripts used to preprocess the obtained data.
-   `experiment.log`: info about the experiment.
-   `README.md`: this file.


Feel free to adapt this README file to suit your project's specific needs.
