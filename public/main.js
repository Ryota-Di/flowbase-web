'use strict';
(async () => {
  const response = await fetch('/version.json', {cache:'no-store'});
  if (!response.ok) throw new Error('Version metadata unavailable');
  const config = await response.json();
  if (config.version !== 'v2' || config.mode !== 'one-click') throw new Error('Unexpected image content');

  const card = document.querySelector('.checkout-card');
  const title = card?.querySelector('.checkout-title');
  const feature = document.getElementById('feature');
  const preview = document.getElementById('flow-preview');
  const button = document.getElementById('next');
  const result = document.getElementById('result');
  if (!card || !title || !feature || !preview || !button || !result) {
    throw new Error('Missing Checkout UI element');
  }

  // Restrict the v14 appearance to v2. The v1 script remains unchanged.
  card.dataset.flowVersion = 'v2';
  feature.textContent = 'ワンクリック購入';
  preview.innerHTML = `
    <div class="one-click-panel">
      <span class="one-click-symbol" aria-hidden="true">→</span>
      <div class="one-click-copy">
        <p>この画面から、そのまま購入手続きを完了できます。</p>
      </div>
    </div>`;
  button.textContent = 'この商品を購入する';
  result.textContent = '購入手続きはまだ完了していません';

  button.addEventListener('click', () => {
    button.disabled = true;
    card.classList.add('is-complete');
    title.hidden = true;
    feature.hidden = true;
    preview.hidden = true;
    button.hidden = true;
    result.classList.add('order-success');
    result.innerHTML = `
      <span class="order-success-icon" aria-hidden="true">✓</span>
      <strong>注文デモが完了しました！</strong>
      <span class="order-success-message">ご購入ありがとうございます。</span>
      <span class="order-success-note">※ デモ画面のため、実際の決済・注文は発生していません。</span>`;
  });
})().catch(() => {
  const result = document.getElementById('result');
  if (result) result.textContent='画面を読み込めませんでした';
});
