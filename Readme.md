This repository is built for the deployment of machine learning model on Kubeflow as a part of MLOPS architecture.(Please refer to SETUP for a complete overview and step-by-step guide. )

code.py is the ml model built on the iris dataset available in sklearn library.

The trained model is then converted into .pkl file.

The inference_script.py can be then used to deploy the following model as a serverless model using kserve and python flask.

Then the ml model and inference script is then dockerised and push into dockerhub and then pulled in the yaml file

performance.py is the python script to test the deployed model's performance using the Kserve REST API.(make sure you edit the endpoint URL with your enpoint URL)
