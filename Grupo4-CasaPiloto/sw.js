const CACHE = 'casapiloto-v2';
const PRE = ['./', './index.html', './app.html', '../assets/logos/g4.svg'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(k => Promise.all(k.filter(v => v !== CACHE).map(v => caches.delete(v)))).then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  // rede primeiro (conteúdo sempre atualizado); sem internet, usa o cache
  e.respondWith(fetch(e.request).then(res => {
    if (res && res.ok && new URL(e.request.url).origin === location.origin) {
      const copia = res.clone();
      caches.open(CACHE).then(c => c.put(e.request, copia));
    }
    return res;
  }).catch(() => caches.match(e.request).then(r => r || caches.match('./app.html'))));
});
