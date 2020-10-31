# Use the official Python image from the Docker Hub
FROM python:3.8.5

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Make a new directory to put the code in.
RUN mkdir /app_grupo1

# Change the working directory. 
# Every command after this will be run from the /app_grupo1 directory.
WORKDIR /app_grupo1

# Copy the requirements.txt file.
COPY requirements.txt /app_grupo1/

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt

# Copy the rest of the code that isn't on the ".dockerignore" file.
COPY . /app_grupo1/

# Make a new directory to put the database in.
RUN mkdir /app_grupo1/data

# Use environment variable to detect Database on BASE_DIR/data
ENV EN_DOCKER = True

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]