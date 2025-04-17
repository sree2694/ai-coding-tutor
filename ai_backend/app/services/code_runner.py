import subprocess

def execute_code(language: str, code: str, user_input: str) -> dict:
    """
    Execute the given code in a sandboxed environment.
    Currently supports Python only, but can be extended for other languages.
    """
    if language.lower() == "python":
        try:
            process = subprocess.Popen(
                ['python3', '-c', code],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output, error = process.communicate(user_input)
            return {"output": output, "error": error}
        except Exception as e:
            return {"output": "", "error": str(e)}
    else:
        return {"output": "", "error": f"Unsupported language: {language}"}
