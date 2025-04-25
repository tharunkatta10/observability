# Observability Project

This project demonstrates the implementation of an integrated monitoring system using **Prometheus**, **Grafana**, **Loki**, **Jaeger**, and a sample **Python/Node.js** app. The system provides observability with metrics, logs, and traces for monitoring the app's performance.

## Technologies Used
- **Prometheus**: For metrics collection and monitoring.
- **Grafana**: For visualizing metrics and dashboards.
- **Loki**: For collecting and viewing logs.
- **Jaeger**: For tracing requests across microservices.
- **Docker**: To containerize the app and monitoring tools.
- **Docker Compose**: To manage multi-container Docker applications.

## Project Structure
- **docker-compose.yml**: Defines and runs multi-container Docker applications for Prometheus, Grafana, Loki, Jaeger, and the sample app.
- **prometheus.yml**: Prometheus configuration for scraping metrics.
- **promtail-config.yml**: Configuration for Promtail (Loki agent) to collect logs.
- **App**: A Python/Node.js application that exposes metrics for Prometheus and logs for Loki.
- **Dashboards**: Pre-configured Grafana dashboards for metrics, logs, and traces.

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/tharunkatta10/observability.git
cd observability
2. Build and Start the Containers
Run the following command to start all containers using Docker Compose:

bash
Copy
Edit
docker-compose up --build
This will start the following services:

Prometheus: Metrics collection

Grafana: Dashboards for visualizing metrics

Loki: Log collection

Jaeger: Distributed tracing

App: Sample Python/Node.js app that exposes metrics and logs

3. Access the Services
Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (default username: admin, default password: admin)

Jaeger: http://localhost:16686

Loki: http://localhost:3100

4. Import Dashboards
You can import Grafana dashboards using the provided JSON files in the repository.

Author Details
Author: Tharun Katta

GitHub: tharunkatta10

Email: tharunkatta10@gmail.com
