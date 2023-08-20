This repository is built for the deployment of machine learning model on Kubeflow as a part of MLOPS architecture.
code.py is the ml model built on the iris dataset available in sklearn library.
The trained model is then converted into .pkl file.
The inference_script.py can be then used to deploy the following model as a serverless model using kserve and python flask.
performance.py is the python script to test the deployed model's performance using the Kserve REST API.
