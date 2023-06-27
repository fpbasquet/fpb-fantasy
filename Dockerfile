# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Set environment variables, if necessary
ENV DJANGO_SETTINGS_MODULE=fpbasquet.settings

# Expose the port on which the Django development server will run
EXPOSE 8000

RUN apt-get update && apt-get install -y postgresql-client

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
