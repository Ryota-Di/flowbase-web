'use strict';
(async () => {
  const [versionRes, environmentRes] = await Promise.all([
    fetch('/version.json', {cache: 'no-store'}),
    fetch('/environment.json', {cache: 'no-store'})
  ]);
  if (!versionRes.ok || !environmentRes.ok) throw new Error('Display metadata unavailable');
  const [version, environment] = await Promise.all([versionRes.json(), environmentRes.json()]);
  if (!['v1', 'v2'].includes(version.version)) throw new Error('Unexpected version');
  if (!['prod', 'staging'].includes(environment.environment)) throw new Error('Unexpected environment');
  const bar = document.getElementById('environment-bar');
  bar.dataset.environment = environment.environment;
  document.getElementById('environment-name').textContent = environment.environment === 'prod' ? 'PRODUCTION' : 'STAGING';
  document.getElementById('app-version').textContent = version.version;
})().catch(() => {
  document.getElementById('environment-name').textContent = '環境情報エラー';
  document.getElementById('app-version').textContent = 'ERROR';
});
