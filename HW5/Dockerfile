FROM agrigorev/zoomcamp-model:2025

# Install UV for dependency management
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml .

# Install dependencies using UV with --system flag
RUN uv pip install --system -r pyproject.toml

# Copy the FastAPI application
COPY app.py .
COPY assets/ ./assets/

# Expose the port
EXPOSE 9696

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9696"]