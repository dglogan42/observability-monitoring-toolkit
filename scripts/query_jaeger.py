import requests
import time
import json
from datetime import datetime

def query_jaeger(service="backend", limit=50, max_pages=5, export_file=None):
    traces = []
    # ... (pagination + error handling as before)
    
    if export_file:
        export_data = {
            "query_time": datetime.now().isoformat(),
            "service": service,
            "total_traces": len(traces),
            "traces": traces
        }
        with open(export_file, 'w') as f:
            json.dump(export_data, f, indent=2)
        print(f"Exported to {export_file}")
    return traces

# Example
if __name__ == "__main__":
    query_jaeger("anomaly-detector", limit=30, export_file=f"jaeger_traces_{datetime.now().strftime('%Y%m%d_%H%M')}.json")
