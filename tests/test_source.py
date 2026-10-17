from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
p=r/'public'
d=json.loads((p/'version.json').read_text())
assert d['version'] in {'v1','v2'}
assert (d['mode']=='one-click') == (d['version']=='v2')
assert "fetch('/version.json'" in (p/'main.js').read_text()
assert 'https://' not in (p/'main.js').read_text()
assert '決済・個人情報送信は行いません' in (p/'index.html').read_text()
assert not any((r/n).exists() for n in ['.env','.env.local','credentials.json'])
print('[PASS] App source checks:',d)
