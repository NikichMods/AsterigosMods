from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
known={'CombatHUD','SoulsEnemyHUD','ProfileRender','SubtitleSoftEdges','AnimationRate'}
selected=sys.argv[1:]
if set(selected)-known:
    raise SystemExit('Unknown mod: '+', '.join(sorted(set(selected)-known)))
tests=sorted(p for mod in selected or sorted(known) for p in (root/mod/'tests').glob('*.py'))
if not tests:
    raise SystemExit('No automated Python tests for this selection; inspect the mod documentation.')
for test in tests:
    print(test.relative_to(root),flush=True)
    subprocess.run([sys.executable,str(test)],cwd=root,check=True)
