# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /src

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Default command to run the CLI app
ENTRYPOINT ["python3", "/src/app/app.py"]