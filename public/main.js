'use strict';
(async () => {
  const response = await fetch('/version.json', {cache:'no-store'});
  if (!response.ok) throw new Error('Version metadata unavailable');
  const config = await response.json();
  if (config.version !== 'v1' || config.mode !== 'multi-step') throw new Error('Unexpected image content');
  const button = document.getElementById('next');
  const result = document.getElementById('result');
  document.getElementById('feature').textContent = '従来の3ステップ購入';
  const labels = ['配送先の確認','支払方法の確認','注文内容の確認'];
  let step = 0;
  button.textContent = '1. ' + labels[0];
  button.addEventListener('click', () => {
    step++;
    if (step === 3) {result.textContent='注文デモ完了（3ステップ）';button.disabled=true;return;}
    result.textContent=`ステップ${step}完了`;
    button.textContent = `${step+1}. ${labels[step]}`;
  });
})().catch(() => {document.getElementById('result').textContent='画面を読み込めませんでした';});
