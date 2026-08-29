# Step 1: Use an official lightweight python image as the foundation
FROM python:3.11-slim

#Step 2:  Set the working directory inside the container to/app
WORKDIR /app

# Step 3: Copy only the requirements file first to optimize installation caching
COPY requirements.txt .

# Step 4: Install streamlit and your other packages inside the container
RUN pip install --no-cache-dir -r requirements.txt

#Step 5: Copy all your local project files into the container 
COPY . .

#Step 6: Inform Docker that the container listens to port 8501 at runtime
EXPOSE 8501

#Step 7: Define the command to launch your streamlit app automatically
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]