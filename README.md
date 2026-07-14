# Fraud Detection Pipeline

## Docker Compose

### 1. Build the images
```bash
docker compose build
```

### 2. Start the stack
```bash
docker compose up -d
```

### 3. View running containers
```bash
docker compose ps
```

### 4. Check logs
```bash
docker compose logs -f producer-python
```

### 5. Stop everything
```bash
docker compose down
```

### 6. Remove volumes too
```bash
docker compose down -v
```

This setup includes:
- Zookeeper
- Kafka
- PostgreSQL
- Redis
- A Python producer container
