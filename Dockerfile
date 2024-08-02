# Use the official Python 3.9 image
FROM python:3.9
 
# Set the working directory to /app
WORKDIR /app
 
# Copy the current directory contents into the container
COPY ./requirements.txt /app/requirements.txt
 
# Install requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
 
# Set the working directory to /app
WORKDIR /app
 
# Copy the source directory contents into the container at /app
COPY ./src /app

# Copy the models to locally.
RUN /app/downloadModels.py
 
# Start the FastAPI app on port 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]