from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
for test in sorted((root/'tests').glob('*.py')):
    print(test.name,flush=True)
    subprocess.run([sys.executable,str(test)],cwd=root,check=True)
