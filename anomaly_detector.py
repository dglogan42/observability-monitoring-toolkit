from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.view import View, ExplicitBucketHistogramAggregation
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

# Resource
resource = Resource.create({
    "service.name": "anomaly-detector",
    "app.version": "1.0",
    "deployment.region": "nz",
    "k8s.pod.name": os.getenv("POD_NAME", "local")
})

# Traces
trace.set_tracer_provider(TracerProvider(resource=resource))
otlp_trace = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_trace))
tracer = trace.get_tracer(__name__)

# Metrics with Views & Exemplars support
metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter(endpoint="http://otel-collector:4317", insecure=True))
meter_provider = MeterProvider(
    resource=resource,
    views=[
        View(instrument_name="thermal.duration", aggregation=ExplicitBucketHistogramAggregation([50, 200, 500, 1000]))
    ]
)
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)

# Example instruments
anomaly_counter = meter.create_counter("anomalies.detected")
thermal_histogram = meter.create_histogram("thermal.duration")

# Usage example
with tracer.start_as_current_span("detect_anomaly", attributes={"ev.battery_kwh": 75.2}):
    anomaly_counter.add(1, {"ev.model": "Custom"})
    thermal_histogram.record(320, {"ev.temp": "cold"})
