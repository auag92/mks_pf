Apaar please look at the descriptions for each of the files

* generate_coeff.py
  - The script generates initial micro-structures runs them through a
  Cahn-Hillard simulation. During the simulation it calibrates the influence
  kernels every 10 steps saves the kernels with the data. You need to
  create a directories titled `coef` and `data` to run the script.

* filter.py and mks_localization_model_sparse.py
  - This files are need to run generate_coef.py. I found that I had to
  use a sparse linear solver when running the experiments.

* pca_of_coef.py
  - This script loads the influence coefficients generated with
  generate_coef.py and save the pca model and scores.

* dynamic_coeff.pbs
  - This pbs script can be used to run a job on the cluster pace.

    $ qsub dynamic_coeff.pbs
