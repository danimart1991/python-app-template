# Use official Python 3.11 slim image
FROM python:3.11-slim

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Configure apt and install packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    # Essential tools
    build-essential \
    ca-certificates \
    curl \
    sudo \
    wget \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid "$USER_GID" "$USERNAME" \
    && useradd --uid "$USER_UID" --gid "$USER_GID" -m "$USERNAME" \
    && echo "$USERNAME" ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/"$USERNAME" \
    && chmod 0440 /etc/sudoers.d/"$USERNAME"

# Switch to vscode user and install Poetry
USER $USERNAME
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && echo 'export PATH="/home/vscode/.local/bin:$PATH"' >> /home/vscode/.bashrc \
    && /home/vscode/.local/bin/poetry config virtualenvs.in-project true

# Set PATH for Poetry
ENV PATH="/home/vscode/.local/bin:$PATH"

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# Set working directory
WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
