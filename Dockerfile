FROM python:3.9.7

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app

RUN pip install --upgrade pip

#We use the pip install command to install the packages listed in the requirements.txt file.
RUN pip install --no-cache-dir --upgrade -r requirements.txt 

RUN pip install fastapi uvicorn

#We then copy the rest of our application’s source code from our host to the image’s working directory.
COPY . /app

#This is the command that will be executed when a container is created from this image.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]