import subprocess

if __name__ == "__main__":
    subprocess.run(["black", "."])
    subprocess.run(["flake8", "."])
    subprocess.run(["mypy", "."])
