"""v14: compact pre-purchase v2, clear success on click, unchanged v1 behavior."""
from pathlib import Path
from html.parser import HTMLParser
r=Path(__file__).resolve().parents[1]
html=(r/'public/index.html').read_text(encoding='utf-8')
css=(r/'public/style.css').read_text(encoding='utf-8')
v2=(r/'public/main.js').read_text(encoding='utf-8')
v1=(r/'demo/v1/main.js').read_text(encoding='utf-8')
assert html.count('?ui=v14')==3
assert 'FLOWBASE_UI_V14' in css
assert 'checkout-card[data-flow-version="v2"]' in css
assert 'width:auto' in css and 'max-width:100%' in css
assert 'min-height:205px' in css
assert 'background:#ffffff' in css and 'padding:25px' in css
assert "feature.textContent = 'ワンクリック購入'" in v2
assert 'もっとスムーズな購入体験' not in v2
assert '<span class="one-click-symbol" aria-hidden="true">→</span>' in v2
assert '<span class="order-success-icon" aria-hidden="true">✓</span>' in v2
assert 'card.dataset.flowVersion = \'v2\'' in v2
assert 'button.hidden = true' in v2 and "result.classList.add('order-success')" in v2
assert '注文デモが完了しました！' in v2
for forbidden in ('NEW FEATURE','NEW FUTURE','操作回数','必要な回数'):
    assert forbidden not in v2
assert '3ステップ' in v1
assert 'flowVersion' not in v1
assert '決済・個人情報送信' in html
print('[PASS] v14 compact card, no pre-purchase checkmark, click-to-success, v1 unchanged')
