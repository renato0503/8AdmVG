/* ============================================================================
   Motor do deck: palco 16:9, revelação por clique, janela do apresentador
   (notas + cronômetro), teclado, toque, barra de progresso e PDF.
   Teclas: →/espaço avança · ← volta · P apresentador · R zera · F tela cheia
           B tela preta · número + Enter pula para o slide · Home/End.
   ============================================================================ */
(function () {
  'use strict';

  /* ---------- ícones (sprite injetado para os decks ficarem autocontidos) ---------- */
  document.body.insertAdjacentHTML('afterbegin', `<svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="i-target" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></symbol>
    <symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 5a3 3 0 0 1 0 6"/><path d="M18 20a6 6 0 0 0-3-5.2"/></symbol>
    <symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></symbol>
    <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
    <symbol id="i-doc" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/></symbol>
    <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></symbol>
    <symbol id="i-chart" viewBox="0 0 24 24"><path d="M4 19V5"/><path d="M4 19h16"/><path d="M7 15l4-5 3 3 5-7"/></symbol>
    <symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></symbol>
    <symbol id="i-check" viewBox="0 0 24 24"><path d="M4 12l5 5L20 6"/></symbol>
    <symbol id="i-alert" viewBox="0 0 24 24"><path d="M12 3l10 18H2z"/><path d="M12 9v5"/><path d="M12 17h.01"/></symbol>
    <symbol id="i-phone" viewBox="0 0 24 24"><rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/></symbol>
    <symbol id="i-lock" viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></symbol>
    <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M4 12h16"/><path d="M14 6l6 6-6 6"/></symbol>
    <symbol id="i-layers" viewBox="0 0 24 24"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/><path d="M3 17l9 5 9-5"/></symbol>
    <symbol id="i-compass" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/></symbol>
    <symbol id="i-route" viewBox="0 0 24 24"><circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H15a3.5 3.5 0 0 0 0-7H9a3.5 3.5 0 0 1 0-7h6.5"/></symbol>
    <symbol id="i-building" viewBox="0 0 24 24"><path d="M4 21V9l8-5 8 5v12"/><path d="M2 21h20"/><path d="M9 21v-5h6v5"/><path d="M8 11h.01M12 11h.01M16 11h.01"/></symbol>
    <symbol id="i-flask" viewBox="0 0 24 24"><path d="M9 3h6"/><path d="M10 3v6L4.5 18.5A2 2 0 0 0 6.2 21.5h11.6a2 2 0 0 0 1.7-3L14 9V3"/><path d="M7 15h10"/></symbol>
    <symbol id="i-rocket" viewBox="0 0 24 24"><path d="M5 15c-1 1-2 4-2 6 2 0 5-1 6-2"/><path d="M9 15l-3-3c1-4 5-9 12-9 0 7-5 11-9 12z"/><circle cx="15" cy="9" r="1.5"/></symbol>
    <symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></symbol>
    <symbol id="i-loop" viewBox="0 0 24 24"><path d="M20 12a8 8 0 1 1-2.3-5.7"/><path d="M20 4v4h-4"/></symbol>
    <symbol id="i-eye" viewBox="0 0 24 24"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></symbol>
    <symbol id="i-heart" viewBox="0 0 24 24"><path d="M12 20s-8-5-8-10a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5-8 10-8 10z"/></symbol>
    <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5L21 21"/></symbol>
    <symbol id="i-grad" viewBox="0 0 24 24"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/></symbol>
    <symbol id="i-cloud" viewBox="0 0 24 24"><path d="M7 18a5 5 0 0 1-.5-10A6 6 0 0 1 18 9a4.5 4.5 0 0 1-.5 9z"/></symbol>
    <symbol id="i-hand" viewBox="0 0 24 24"><path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M11 11V3.5a1.5 1.5 0 0 1 3 0V11"/><path d="M14 11V5a1.5 1.5 0 0 1 3 0v7"/><path d="M17 9.5a1.5 1.5 0 0 1 3 0V14a8 8 0 0 1-8 8h-1a7 7 0 0 1-6-3.5L3 15a1.5 1.5 0 0 1 2.6-1.5L8 16"/></symbol>
    <symbol id="i-book" viewBox="0 0 24 24"><path d="M4 4h6a3 3 0 0 1 3 3v13a3 3 0 0 0-3-3H4z"/><path d="M20 4h-6a3 3 0 0 0-3 3v13a3 3 0 0 1 3-3h6z"/></symbol>
    <symbol id="i-code" viewBox="0 0 24 24"><polyline points="9 6 4 12 9 18"/><polyline points="15 6 20 12 15 18"/></symbol>
    <symbol id="i-database" viewBox="0 0 24 24"><ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/></symbol>
    <symbol id="i-cpu" viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10" rx="2"/><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></symbol>
    <symbol id="i-bulb" viewBox="0 0 24 24"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.8.6 1.5 1.6 1.5 2.6V17h4v-.5c0-1 .7-2 1.5-2.6A6 6 0 0 0 12 3z"/></symbol>
    <symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18"/></symbol>
    <symbol id="i-store" viewBox="0 0 24 24"><path d="M3 9l2-5h14l2 5"/><path d="M4 9v11h16V9"/><path d="M3 9h18"/><path d="M9 20v-6h6v6"/></symbol>
    <symbol id="i-coin" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .8-3 2s1.3 1.7 3 2 3 .8 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5"/><path d="M12 6v2M12 16v2"/></symbol>
    <symbol id="i-pulse" viewBox="0 0 24 24"><path d="M3 12h4l2-6 4 12 2-6h6"/></symbol>
    <symbol id="i-play" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 8.5l5.5 3.5-5.5 3.5z"/></symbol>
    <symbol id="i-package" viewBox="0 0 24 24"><path d="M3 8l9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v8"/></symbol>
    <symbol id="i-desktop" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></symbol>
    <symbol id="i-server" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="7" rx="2"/><rect x="3" y="14" width="18" height="7" rx="2"/><path d="M7 6.5h.01M7 17.5h.01"/></symbol>
    <symbol id="i-scale" viewBox="0 0 24 24"><path d="M12 3v18M5 7h14"/><path d="M5 7l-3 6h6z"/><path d="M19 7l-3 6h6z"/></symbol>
    <symbol id="i-leaf" viewBox="0 0 24 24"><path d="M4 20c0-8 6-14 16-14 0 10-6 15-16 14z"/><path d="M4 20c4-4 8-7 13-9"/></symbol>
    <symbol id="i-truck" viewBox="0 0 24 24"><path d="M3 6h11v10H3z"/><path d="M14 9h4l3 3v4h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></symbol>
    <symbol id="i-home" viewBox="0 0 24 24"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></symbol>
    <symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></symbol>
    <symbol id="i-message" viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 21l1.9-5.4A8 8 0 1 1 21 12z"/></symbol>
    <symbol id="i-flag" viewBox="0 0 24 24"><path d="M5 21V4"/><path d="M5 4h13l-3 5 3 5H5"/></symbol>
    <symbol id="i-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></symbol>
  </svg>`);

  const params = new URLSearchParams(location.search);
  const slides = [...document.querySelectorAll('.slide')];
  const total = slides.length;
  const palco = document.getElementById('palco');
  const reduzido = params.has('sem-anim') || matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduzido) document.documentElement.classList.add('sem-anim');

  const deckNome = document.body.dataset.deck || document.title;
  const logo = document.body.dataset.logo || '';
  const trilha = (document.body.dataset.blocos || '').split('|').filter(Boolean);

  /* ---------- rodapé automático ---------- */
  slides.forEach((s, i) => {
    const f = document.createElement('div');
    f.className = 'rodape';
    f.innerHTML =
      `<span class="marca">${logo ? `<img src="${logo}" alt="">` : ''}<b>${deckNome}</b></span>` +
      (trilha.length ? `<span class="trilha">${trilha.map((t, k) => `<span data-bloco="${k}">${t}</span>`).join('')}</span>` : '') +
      `<span class="pag"></span>`;
    s.appendChild(f);
  });

  /* ---------- escala ---------- */
  let escala = 1;
  function ajustar() {
    escala = Math.min(innerWidth / 1920, innerHeight / 1080);
    palco.style.setProperty('--escala', escala);
    document.querySelector('.progresso').style.width = ((atual + 1) / total * 100) + '%';
  }

  /* ---------- estado ---------- */
  let atual = -1, batida = 0;
  const maxB = s => Math.max(0, ...[...s.querySelectorAll('[data-b]')].map(e => +e.dataset.b || 0));
  const titulo = s => {
    if (!s) return 'Fim';
    const t = s.querySelector('h1, h2, .titulo, .mega');
    return t ? t.textContent.replace(/\s+/g, ' ').trim() : '';
  };

  function render(i, b) {
    i = Math.max(0, Math.min(total - 1, i));
    const s = slides[i];
    atual = i; batida = Math.max(0, Math.min(b || 0, maxB(s)));
    slides.forEach((x, j) => x.classList.toggle('ativo', j === i));
    s.querySelectorAll('[data-b]').forEach(e => e.classList.toggle('visivel', (+e.dataset.b || 0) <= batida));
    s.querySelectorAll('.rodape .pag').forEach(p => p.textContent = String(i + 1).padStart(2, '0') + ' / ' + total);
    const bloco = +(s.dataset.bloco || 0);
    s.querySelectorAll('.trilha [data-bloco]').forEach(p => p.classList.toggle('on', +p.dataset.bloco === bloco));
    history.replaceState(null, '', '#' + (i + 1));
    document.querySelector('.progresso').style.width = ((i + 1) / total * 100) + '%';
    atualizarApresentador();
  }
  function ir(i, b) { render(i, b || 0); }
  function avancar() {
    const s = slides[atual];
    if (batida < maxB(s)) return render(atual, batida + 1);
    if (atual < total - 1) return render(atual + 1, 1);
  }
  function voltar() {
    if (batida > 0) return render(atual, batida - 1);
    if (atual > 0) render(atual - 1, maxB(slides[atual - 1]));
  }

  /* ---------- controles ---------- */
  const prog = document.createElement('div'); prog.className = 'progresso';
  const dica = document.createElement('div'); dica.className = 'dica';
  dica.textContent = '→ avança · ← volta · P notas · F tela cheia';
  document.body.append(prog, dica);
  setTimeout(() => dica.classList.add('some'), 6500);

  let jan = null, inicio = null;
  function resumo(s) {
    if (!s) return '— fim —';
    const k = s.querySelector('.kicker');
    return (k ? k.textContent.trim() + ' — ' : '') + titulo(s);
  }
  function abrirApresentador() {
    if (jan && !jan.closed) { jan.focus(); return; }
    jan = window.open('', 'apresentador', 'width=1040,height=720');
    if (!jan) return;
    inicio = inicio || Date.now();
    jan.document.write(`<!doctype html><meta charset="utf-8"><title>Apresentador — ${deckNome}</title>
      <style>
      body{margin:0;background:#050b18;color:#e8eefc;font:19px/1.5 Inter,system-ui,sans-serif;padding:26px 34px}
      #top{display:flex;justify-content:space-between;align-items:baseline;gap:18px;font-variant-numeric:tabular-nums}
      #relogio{font:700 56px/1 'JetBrains Mono',monospace;color:#fecb00}#meta{color:#8fa3c2;font-size:17px}
      #n{font-weight:800}#tit{font-size:30px;font-weight:900;margin:18px 0 14px;line-height:1.18}
      #notas{background:rgba(255,255,255,.06);border-radius:14px;padding:18px 22px;font-size:25px;line-height:1.45;color:#e2e8f0}
      #prox{margin-top:18px;color:#8fa3c2;font-size:18px;border-top:1px solid rgba(255,255,255,.12);padding-top:12px}
      #prox b{color:#cbd5e1}#teclas{margin-top:8px;color:#64748b;font-size:14px}
      </style>
      <div id="top"><div><span id="n"></span> · <span id="clq"></span></div><div id="meta"></div><div id="relogio">00:00</div></div>
      <div id="tit"></div><div id="notas"></div><div id="prox"></div>
      <div id="teclas">→ avança · ← volta · R zera o tempo · B tela preta · F tela cheia · número + Enter pula</div>`);
    jan.document.close();
    jan.document.addEventListener('keydown', teclas);
    atualizarApresentador();
  }
  function atualizarApresentador() {
    if (!jan || jan.closed) return;
    const d = jan.document, s = slides[atual];
    if (!s) return;
    d.getElementById('n').textContent = 'Slide ' + (atual + 1) + ' de ' + total;
    d.getElementById('clq').textContent = 'clique ' + batida + ' de ' + maxB(s);
    d.getElementById('tit').textContent = titulo(s);
    d.getElementById('notas').innerHTML = s.querySelector('.notas') ? s.querySelector('.notas').innerHTML : '';
    d.getElementById('prox').innerHTML = '<b>Próximo:</b> ' + resumo(slides[atual + 1]).replace(/</g, '&lt;');
    d.getElementById('meta').textContent = 'alvo ao fim: ' + (s.dataset.alvo || '?') + ' min';
  }
  setInterval(() => {
    if (!jan || jan.closed || !inicio) return;
    const seg = Math.floor((Date.now() - inicio) / 1000);
    jan.document.getElementById('relogio').textContent =
      String(Math.floor(seg / 60)).padStart(2, '0') + ':' + String(seg % 60).padStart(2, '0');
  }, 1000);

  let buffer = '', bufT;
  function teclas(e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    if (/^[0-9]$/.test(e.key)) {
      buffer += e.key; clearTimeout(bufT); bufT = setTimeout(() => buffer = '', 2500); e.preventDefault(); return;
    }
    if (e.key === 'Enter' && buffer) { ir(parseInt(buffer, 10) - 1, 0); buffer = ''; e.preventDefault(); return; }
    switch (e.key) {
      case 'ArrowRight': case 'ArrowDown': case 'PageDown': case ' ': avancar(); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp': case 'Backspace': voltar(); break;
      case 'Home': ir(0, 0); break;
      case 'End': ir(total - 1, 0); break;
      case 'p': case 'P': abrirApresentador(); break;
      case 'r': case 'R': inicio = Date.now(); break;
      case 'b': case 'B': document.body.classList.toggle('preto'); break;
      case 'f': case 'F': document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen(); break;
      default: return;
    }
    e.preventDefault();
  }
  document.addEventListener('keydown', teclas);
  document.addEventListener('click', e => {
    if (e.target.closest('a,button')) return;
    e.clientX > innerWidth * .42 ? avancar() : voltar();
  });
  let x0 = null;
  document.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  document.addEventListener('touchend', e => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) dx < 0 ? avancar() : voltar();
    x0 = null;
  });
  let tCursor;
  document.addEventListener('mousemove', () => {
    document.documentElement.classList.remove('sem-cursor');
    clearTimeout(tCursor);
    tCursor = setTimeout(() => document.documentElement.classList.add('sem-cursor'), 2200);
  });
  addEventListener('resize', ajustar);
  addEventListener('hashchange', () => {
    const n = parseInt(location.hash.slice(1), 10);
    if (n && n - 1 !== atual) ir(n - 1, 1);
  });
  addEventListener('beforeprint', () => slides.forEach(s => s.querySelectorAll('[data-b]').forEach(e => e.classList.add('visivel'))));

  /* ---------- conferência de estouro (?check=1) ---------- */
  if (params.has('check')) {
    setTimeout(() => {
      let pior = 0, culpado = '';
      slides.forEach(s => {
        slides.forEach(x => x.classList.toggle('ativo', x === s));
        s.querySelectorAll('[data-b]').forEach(e => e.classList.add('visivel'));
        const base = s.getBoundingClientRect();
        s.querySelectorAll('*').forEach(el => {
          if (el.closest('.rodape') || el.closest('.notas') || el.classList.contains('notas')) return;
          const r = el.getBoundingClientRect();
          if (!r.height) return;
          const ex = Math.max(0, r.bottom - (base.bottom - 96), r.right - (base.right - 80), (base.left + 70) - r.left, (base.top + 54) - r.top);
          const vaz = el.scrollWidth > el.clientWidth + 4 && el.clientWidth > 0 ? el.scrollWidth - el.clientWidth : 0;
          const p = Math.max(ex, vaz);
          if (p > pior) { pior = p; culpado = (el.textContent || el.className || el.tagName).trim().slice(0, 46); }
        });
      });
      document.title = pior > 3 ? 'ESTOURO ' + Math.round(pior) + 'px: ' + culpado : 'OK';
    }, 700);
  }

  /* ---------- início ---------- */
  const pedido = parseInt(params.get('s'), 10) || parseInt(location.hash.slice(1), 10) || 1;
  const b0 = params.has('b') ? parseInt(params.get('b'), 10) : 1;
  document.fonts.ready.then(() => {
    ajustar();
    ir(pedido - 1, b0);
    window.deck = { ir, avancar, voltar, total, estado: () => ({ atual, batida }) };
    window.deckPronto = true;
  });
})();
