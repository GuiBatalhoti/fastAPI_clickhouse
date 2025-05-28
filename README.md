# fastAPI_clickhouse

## Docker:

```bash
docker run -d -p 18123:8123 -p19000:9000 -e CLICKHOUSE_PASSWORD=changeme --name some-clickhouse-server --ulimit nofile=262144:262144 clickhouse/clickhouse-server
```

## UVICORN:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Clickhouse client:

```bash
docker exec -it some-clickhouse-server clickhouse-client
```

## Default SQL

```sql
CREATE DATABSE db;
USE db;
CREATE TABLE IF NOT EXISTS vit(
    no_fantasia String,
    placa String,
    data String,
    PRIMARY KEY (placa)
)
```