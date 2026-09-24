const CACHE = '8admvg-hub-v1';
const PRE = ['./', './index.html', './assets/landing.css'];
self.addEventListener('install', e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRE)).then(() => self.skipWaiting())));
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(k => Promise.all(k.filter(v => v !== CACHE).map(v => caches.delete(v)))).then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(fetch(e.request).then(res => {
    if (res && res.ok && new URL(e.request.url).origin === location.origin) { const c = res.clone(); caches.open(CACHE).then(x => x.put(e.request, c)); }
    return res;
  }).catch(() => caches.match(e.request).then(r => r || caches.match('./index.html'))));
});
