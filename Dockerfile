# Use the official Python 3.9 image
FROM python:3.9
 
# Set the working directory to /code
WORKDIR /app
 
# Copy the current directory contents into the container at /code
COPY ./requirements.txt /app/requirements.txt
 
# Install requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
 
# Set up a new user named "user" with user ID 1000
#RUN useradd -m -u 1000 user
# Switch to the "user" user
#USER user
# Set home to the user's home directory
#ENV HOME=/home/user \\
#    PATH=/home/user/.local/bin:$PATH
 
# Set the working directory to the user's home directory
WORKDIR /app
 
# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY . /app
 
# Start the FastAPI app on port 7860, the default port expected by Spaces
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]