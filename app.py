from flask import Flask
from prometheus_client import Counter, generate_latest
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import logging

# Logs
logging.basicConfig(filename='/var/log/app.log', level=logging.INFO)

# Tracing
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# App
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    logging.info("Request received at /")
    return "Hello from Flask"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

