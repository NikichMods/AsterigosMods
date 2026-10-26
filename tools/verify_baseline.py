from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
env=json.loads((root/'.local/environment.json').read_text(encoding='utf-8'))
manifest=json.loads((root/'docs/BASELINE.json').read_text(encoding='utf-8'))
game=Path(env['gameRoot'])
for entry in manifest['files']:
    relative=entry['path']
    if relative.startswith('mods/'):
        source=root/relative
        _,mod,_,name=Path(relative).parts
        installed=Path(env['ue4ssMods'])/mod/'Scripts'/name
        assert hashlib.sha256(source.read_bytes()).hexdigest()==entry['sha256'],relative
    else:
        installed=game/'Genesis/Content/Paks/~mods'/relative
    assert hashlib.sha256(installed.read_bytes()).hexdigest()==entry['sha256'],str(installed)
print('PASS: all 8 accepted runtime/payload hashes unchanged; game not modified.')
