# Use the lightweight version of Python 3.11
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Expose port 8000
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]