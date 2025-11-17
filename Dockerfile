FROM python:3.13-slim

WORKDIR /app

# Install uv (fast Python package manager)
RUN pip install --no-cache-dir uv

# Copy dependency files first to use Docker layer caching
COPY pyproject.toml uv.lock ./

# Install production dependencies (no dev)
RUN uv sync --frozen --no-dev

# Copy source code and model
COPY predict.py model_xgb.pkl ./

EXPOSE 9696

# Start FastAPI
ENTRYPOINT ["uv", "run", "uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]