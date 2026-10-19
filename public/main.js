'use strict';
(async () => {
  const response = await fetch('/version.json', {cache:'no-store'});
  if (!response.ok) throw new Error('Version metadata unavailable');
  const config = await response.json();
  if (config.version !== 'v2' || config.mode !== 'one-click') throw new Error('Unexpected image content');
  const button = document.getElementById('next');
  const result = document.getElementById('result');
  document.getElementById('feature').textContent = 'NEW：ワンクリック購入';
  document.getElementById('flow-preview').innerHTML = '<span class="step highlight">1クリックで購入完了</span>';
  button.textContent='ワンクリックで購入';
  button.addEventListener('click', () => {
    result.textContent='注文デモ完了（1クリック）';
    button.disabled = true;
  });
})().catch(() => {document.getElementById('result').textContent='画面を読み込めませんでした';});
