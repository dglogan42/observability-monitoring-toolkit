import asyncio
import json
from pathlib import Path
import aiofiles
from asyncio import Semaphore

async def parse_single_file_async(file_path, sem):
    async with sem:
        try:
            async with aiofiles.open(file_path, 'r') as f:
                content = await f.read()
                data = json.loads(content)
            print(f"Processed {file_path.name}: {len(data.get('traces', []))} traces")
            return data
        except Exception as e:
            print(f"Error {file_path}: {e}")
            return None

async def parse_jaeger_files_async(pattern="**/*jaeger_traces_*.json", max_concurrent=20):
    root = Path(".")
    files = list(root.rglob(pattern.split("**/", 1)[-1] if "**/" in pattern else pattern))
    print(f"Found {len(files)} files.")
    
    sem = Semaphore(max_concurrent)
    tasks = [parse_single_file_async(f, sem) for f in files]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    valid = [r for r in results if isinstance(r, dict)]
    print(f"Successfully processed {len(valid)} files.")
    return valid

if __name__ == "__main__":
    asyncio.run(parse_jaeger_files_async(max_concurrent=10))
