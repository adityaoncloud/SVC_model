# Use a base image with Python pre-installed
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the inference script and trained model into the container
COPY inference_script.py /app/
COPY trained_model.pkl /app/

# Install dependencies
RUN pip install Flask numpy scikit-learn matplotlib seaborn joblib

# Expose the port your application will listen on
EXPOSE 8080

# Define the command to run when the container starts
CMD ["python", "inference_script.py"]

