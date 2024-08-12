# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory in the container
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
