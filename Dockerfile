FROM python:3.9.7

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app

RUN pip install --upgrade pip

#We use the pip install command to install the packages listed in the requirements.txt file.
RUN pip install --no-cache-dir --upgrade -r requirements.txt 

RUN pip install fastapi uvicorn

RUN [ "python3", "-c", "import nltk; nltk.download('punkt', download_dir='/usr/local/nltk_data')" ]

COPY . /app

#This is the command that will be executed when a container is created from this image.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]