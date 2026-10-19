"""Checkout v13 release impact checks: no new feature labels or operation counts."""
from pathlib import Path
r = Path(__file__).resolve().parents[1]
html=(r/'public/index.html').read_text(encoding='utf-8')
css=(r/'public/style.css').read_text(encoding='utf-8')
v2=(r/'public/main.js').read_text(encoding='utf-8')
v1=(r/'demo/v1/main.js').read_text(encoding='utf-8')
for src in ('/style.css?ui=v13','/main.js?ui=v13','/environment-banner.js?ui=v13'):
    assert src in html, src
assert 'FLOWBASE_UI_V13' in css
assert 'checkout-card[data-flow-version="v2"]' in css
assert '.one-click-panel' in css and '.order-success' in css
assert "card.dataset.flowVersion = 'v2'" in v2
assert 'ワンクリック購入' in v2 and '注文デモが完了しました' in v2
assert 'button.hidden = true' in v2 and 'result.innerHTML' in v2
assert "config.version !== 'v2' || config.mode !== 'one-click'" in v2
assert "fetch('/version.json'" in v2
assert "config.version !== 'v1' || config.mode !== 'multi-step'" in v1
assert '3ステップ' in v1 and 'flowVersion' not in v1
for forbidden in ('NEW FEATURE','NEW FUTURE','操作回数','必要な回数'):
    assert forbidden not in v2, forbidden
assert '決済・個人情報送信' in html
print('[PASS] v13: v2-specific visual difference, success screen, v1 unchanged by JS')
