# Observability & Monitoring Toolkit

A full-stack observability and monitoring platform with Sentry, Jaeger, Loki, Prometheus, OpenTelemetry, Grafana, SHAP anomaly detection, and async trace processing.

> Rebranded from the original EV-focused prototype. Core functionality and deployment tooling preserved.

## Stack

- **Frontend**: React PWA with Plotly SHAP visualizations
- **Backend**: Python anomaly detection service with OpenTelemetry instrumentation
- **Observability**: Sentry, Jaeger, Loki, Prometheus, Grafana, OTEL Collector
- **Deployment**: Docker Compose, Render Blueprint, Kubernetes (OTEL Operator)

## Quick Start

```bash
docker-compose up
```

## Key Directories

- `client/` – React frontend components
- `scripts/` – Jaeger query/parsing utilities, screenshot automation
- `grafana/` – Alerting rules and dashboard provisioning
- `k8s/` – Kubernetes instrumentation manifests
- `anomaly_detector.py` – Python service with OTEL metrics/traces and SHAP

## Grafana Dashboard Import

1. Open Grafana → Dashboards → Import
2. Upload sample dashboard JSON from `grafana/dashboards/`
3. Select Prometheus/Loki/Jaeger data sources

## Render Deployment

Use `render.yaml` for one-click Blueprint deployment.

## License

MIT
