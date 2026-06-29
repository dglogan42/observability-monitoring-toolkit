from pathlib import Path
import json
from concurrent.futures import ThreadPoolExecutor
import time

def parse_single_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        # Quick analysis
        print(f"Parsed {file_path.name}: {len(data.get('traces', []))} traces")
        return data
    except Exception as e:
        print(f"Error {file_path}: {e}")
        return None

def parse_jaeger_files(pattern="**/*jaeger_traces_*.json", max_workers=8):
    root = Path(".")
    files = list(root.rglob(pattern.split("**/", 1)[-1] if "**/" in pattern else pattern))
    print(f"Found {len(files)} files with rglob.")
    
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(parse_single_file, files))
    
    print(f"Processed in {time.time() - start:.2f}s with {max_workers} workers.")
    return [r for r in results if r]

if __name__ == "__main__":
    parse_jaeger_files()
