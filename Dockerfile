# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
