# docker_runner/executor.py
import subprocess
import uuid
import os


def run_python_code(code: str) -> str:
    run_id = str(uuid.uuid4())
    code_file_path = f"./temp/{run_id}.py"

    os.makedirs("temp", exist_ok=True)
    with open(code_file_path, "w") as f:
        f.write(code)

    try:
        result = subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{os.path.abspath(code_file_path)}:/runner/python3_runner.py",
            "python-runner"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)

        output = result.stdout.decode() or result.stderr.decode()
        return output.strip()
    except subprocess.TimeoutExpired:
        return "Execution timed out."
    except Exception as e:
        return str(e)
    finally:
        os.remove(code_file_path)
