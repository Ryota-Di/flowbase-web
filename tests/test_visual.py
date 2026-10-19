from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
v1=json.loads((r/'demo/v1/version.json').read_text()); v2=json.loads((r/'public/version.json').read_text())
assert v1=={'version':'v1','mode':'multi-step'}
assert v2=={'version':'v2','mode':'one-click'}
html=(r/'public/index.html').read_text(); css=(r/'public/style.css').read_text(); js=(r/'public/environment-banner.js').read_text()
for x in ('environment-name','app-version','flow-preview'):
 assert f'id="{x}"' in html, x
assert 'PRODUCTION' in js and 'STAGING' in js and 'environment.json' in js
assert 'data-environment="prod"' in css and 'data-environment="staging"' in css
assert '3ステップ' in (r/'demo/v1/main.js').read_text()
assert 'ワンクリック' in (r/'public/main.js').read_text()
assert 'COPY demo/v1/main.js' in (r/'Dockerfile.v1').read_text()
print('[PASS] v1 and v2 display sources and environment/version banner')
