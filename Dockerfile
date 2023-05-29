# base image
FROM python:3.9-slim-buster

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ../app . 

# expose port 2222
EXPOSE 2222

# run the command to start the Flask app
CMD ["python", "app.py"]