# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port that the application will run on
EXPOSE 8080

# Run the command to start the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

