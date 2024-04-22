# llamacpp

Repo to experiment with llama cpp use cases.

LLama cpp currently supports cuda 12.1, 12.2, 12.3 but not 12.4

Older versions of cuda can be used with conda environments e.g.:
$ conda create -n cuda122 cuda=12.2
$ conda activate cuda122

* The .ipynb file demonstrates how to run a 7bn parameter model on llamacpp on colab
* The makefile shows the commands used to serve the model as an endpoint using docker.
* We query that end point using the scripts in test_scripts/ 