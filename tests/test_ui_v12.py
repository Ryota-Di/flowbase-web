"""Offline demo UI checks; run in the app repo and GitHub Actions."""
from pathlib import Path
from html.parser import HTMLParser

root = Path(__file__).resolve().parents[1]
html = (root/'public/index.html').read_text(encoding='utf-8')
css = (root/'public/style.css').read_text(encoding='utf-8')
v1 = (root/'demo/v1/main.js').read_text(encoding='utf-8')
v2 = (root/'public/main.js').read_text(encoding='utf-8')
env = (root/'public/environment-banner.js').read_text(encoding='utf-8')

class IDs(HTMLParser):
    def __init__(self): super().__init__();self.ids=[]
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:self.ids.append(a['id'])

p = IDs();p.feed(html)
for x in ('environment-bar','environment-name','app-version','feature','flow-preview','next','result'):
    assert p.ids.count(x) == 1,(x,p.ids)
assert 'FLOWBASE_UI_V12' in css
assert '/style.css?ui=v12' in html
assert '/main.js?ui=v12' in html
assert '/environment-banner.js?ui=v12' in html
assert '[data-environment="prod"]' in css and '[data-environment="staging"]' in css
assert '.environment-pill' in css and '.version-pill' in css
assert 'background:' in css and '.checkout-card' in css
assert 'v1' in v1 and '3ステップ' in v1
assert 'v2' in v2 and 'ワンクリック' in v2
assert 'environment.json' in env and 'version.json' in env
assert '決済・個人情報送信' in html
print('[PASS] v12 UI structure, styling, cache busting and version-specific flows')
