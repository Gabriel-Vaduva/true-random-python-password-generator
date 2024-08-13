FROM python:3.9-slim-buster

# Set woking directory 
WORKDIR /app

# install dependencies 
RUN pip install flask && pip install --upgrade semiphemeral

# Copy app
COPY . .

# Expose app port
EXPOSE 5000

# Command to run app in container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
