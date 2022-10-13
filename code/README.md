# Marathon Docker Template
Docker Template sample submission format using Python.

## Running sample code
Build the container from within the `/code` folder by
`docker build -t docker-template .`

Launch the container with
`docker run -it docker-template`

Verify that training works:
`./train.sh ./data/training.csv`

This should overwrite the `./model/dummy-model.pickle` file, so subsequent testing will use the new model instead of the one shipped with the submission.

Verify that testing works out of the box. Within the container, run
`./test.sh ./data/testing.csv ./data/solution.csv`

This should create a `solution.csv` file within the `/data` folder. This should be identical that is already present in the submission's `/solution` folder.
