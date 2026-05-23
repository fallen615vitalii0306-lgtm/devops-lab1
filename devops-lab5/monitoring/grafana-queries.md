# Grafana PromQL queries

## Использование CPU

```promql
sum(rate(node_cpu_seconds_total{mode!="idle"}[5m]))
```

## Доступная оперативная память

```promql
node_memory_MemAvailable_bytes
```
