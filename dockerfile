FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# 1. Create the data directory first
RUN mkdir -p /app/data

# 2. Install dependencies
ENV UV_COMPILE_BYTECODE=1
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# 3. Copy the scripts
COPY scripts/ ./scripts/

# 2. Copy the main pipeline script
COPY pipeline.py ./pipeline.py

# 4. Setup Paths
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/scripts:$PYTHONPATH"

ENTRYPOINT ["python", "pipeline.py"]
