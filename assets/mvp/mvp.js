/* ==========================================================================
   mvp.js — utilitários dos MVPs do 8AdmVG (script clássico, funciona em file:// e no Pages).
   Uso: <script src="../assets/mvp/mvp.js"></script>  →  window.MVP
   ========================================================================== */
(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  function esc(s) {
    return String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  /* ---------- estado persistido (um objeto JSON por app) ---------- */
  function criarEstado(chave, semente) {
    let dados;
    try { dados = JSON.parse(localStorage.getItem(chave)); } catch (e) { dados = null; }
    if (!dados) dados = semente();
    const api = {
      get d() { return dados; },
      salvar() { try { localStorage.setItem(chave, JSON.stringify(dados)); return true; } catch (e) { toast('Sem espaço no aparelho para salvar.'); return false; } },
      substituir(novo) { dados = novo; api.salvar(); },
      resetar() { dados = semente(); api.salvar(); },
    };
    api.salvar();
    return api;
  }

  /* ---------- formatação ---------- */
  const fmtBRL = v => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL', maximumFractionDigits: 0 }).format(v || 0);
  const fmtNum = (v, c = 0) => new Intl.NumberFormat('pt-BR', { maximumFractionDigits: c, minimumFractionDigits: c }).format(v || 0);
  const fmtData = d => d ? new Date(d.length === 10 ? d + 'T12:00:00' : d).toLocaleDateString('pt-BR') : '';
  const hoje = () => new Date().toISOString().slice(0, 10);
  const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 6);

  /* ---------- toast / modal ---------- */
  let tt;
  function toast(msg) {
    let el = $('#toast');
    if (!el) { el = document.createElement('div'); el.id = 'toast'; el.className = 'toast'; el.setAttribute('role', 'status'); el.setAttribute('aria-live', 'polite'); document.body.appendChild(el); }
    el.textContent = msg; el.classList.add('on');
    clearTimeout(tt); tt = setTimeout(() => el.classList.remove('on'), 2600);
  }

  function modal(html, aoAbrir) {
    const fundo = document.createElement('div');
    fundo.className = 'modal-fundo';
    fundo.innerHTML = `<div class="modal" role="dialog" aria-modal="true">${html}</div>`;
    const fechar = () => { fundo.classList.remove('on'); setTimeout(() => fundo.remove(), 200); document.removeEventListener('keydown', esc_); };
    const esc_ = ev => { if (ev.key === 'Escape') fechar(); };
    fundo.addEventListener('click', ev => { if (ev.target === fundo || ev.target.closest('[data-fechar]')) fechar(); });
    document.addEventListener('keydown', esc_);
    document.body.appendChild(fundo);
    requestAnimationFrame(() => fundo.classList.add('on'));
    const m = $('.modal', fundo);
    const foco = m.querySelector('input,select,textarea,button');
    if (foco) setTimeout(() => foco.focus(), 50);
    if (aoAbrir) aoAbrir(m, fechar);
    return fechar;
  }

  function confirmar(msg, sim, rotulo = 'Confirmar') {
    modal(`<h2>Confirmar</h2><p>${esc(msg)}</p><div class="btns"><button class="btn sec" data-fechar>Cancelar</button><button class="btn perigo" id="mvp-sim">${esc(rotulo)}</button></div>`,
      (m, fechar) => $('#mvp-sim', m).addEventListener('click', () => { fechar(); sim(); }));
  }

  /* ---------- arquivos ---------- */
  function baixar(nome, texto, tipo = 'application/json') {
    const url = URL.createObjectURL(new Blob([texto], { type: tipo + ';charset=utf-8' }));
    const a = Object.assign(document.createElement('a'), { href: url, download: nome });
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function escolherArquivo(accept, cb) {
    const inp = Object.assign(document.createElement('input'), { type: 'file', accept });
    inp.addEventListener('change', () => { if (inp.files[0]) cb(inp.files[0]); });
    inp.click();
  }
  function lerComoDataURL(arquivo, limiteKB = 900) {
    return new Promise((ok, erro) => {
      if (arquivo.size > limiteKB * 1024 && !arquivo.type.startsWith('image/')) return erro(new Error('grande'));
      const r = new FileReader();
      r.onload = () => {
        if (!arquivo.type.startsWith('image/')) return ok(r.result);
        const img = new Image();
        img.onload = () => { // reduz a foto para caber no localStorage
          const esc_ = Math.min(1, 900 / Math.max(img.width, img.height));
          const c = document.createElement('canvas'); c.width = img.width * esc_; c.height = img.height * esc_;
          c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
          ok(c.toDataURL('image/jpeg', 0.7));
        };
        img.onerror = erro; img.src = r.result;
      };
      r.onerror = erro; r.readAsDataURL(arquivo);
    });
  }

  /* Exportar / importar / apagar — liga os botões com data-acao nos apps */
  function ligarDados(estado, nomeArquivo, aoMudar) {
    document.addEventListener('click', ev => {
      const b = ev.target.closest('[data-acao]');
      if (!b) return;
      const acao = b.dataset.acao;
      if (acao === 'exportar') {
        baixar(`${nomeArquivo}-${hoje()}.json`, JSON.stringify({ app: nomeArquivo, exportadoEm: new Date().toISOString(), dados: estado.d }, null, 2));
        toast('Backup baixado.');
      } else if (acao === 'importar') {
        escolherArquivo('application/json,.json', f => f.text().then(t => {
          try {
            const j = JSON.parse(t);
            if (j.app !== nomeArquivo || !j.dados) throw new Error('outro app');
            estado.substituir(j.dados); aoMudar(); toast('Backup importado.');
          } catch (e) { toast('Arquivo inválido para este app.'); }
        }));
      } else if (acao === 'resetar') {
        confirmar('Apagar todos os dados deste app neste aparelho e voltar ao exemplo inicial?', () => { estado.resetar(); aoMudar(); toast('Dados apagados.'); }, 'Apagar tudo');
      }
    });
  }

  /* ---------- abas (hash #aba) ---------- */
  function abas(aoTrocar) {
    const ir = nome => {
      const alvo = $(`.view[data-view="${nome}"]`) ? nome : $('.view').dataset.view;
      $$('.view').forEach(v => v.classList.toggle('ativa', v.dataset.view === alvo));
      $$('.nav-inf [data-aba]').forEach(b => { const on = b.dataset.aba === alvo; b.classList.toggle('on', on); b.setAttribute('aria-current', on ? 'page' : 'false'); });
      if (aoTrocar) aoTrocar(alvo);
      window.scrollTo(0, 0);
    };
    document.addEventListener('click', ev => {
      const b = ev.target.closest('[data-aba]');
      if (b) { ev.preventDefault(); if (location.hash === '#' + b.dataset.aba) ir(b.dataset.aba); else location.hash = b.dataset.aba; }
    });
    window.addEventListener('hashchange', () => ir(location.hash.slice(1)));
    ir(location.hash.slice(1));
    return ir;
  }

  /* ---------- voz e vibração ---------- */
  function falar(texto, opts = {}) {
    if (!('speechSynthesis' in window)) { toast(texto); return false; }
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(texto);
    u.lang = 'pt-BR'; u.rate = opts.rate || 1;
    const voz = speechSynthesis.getVoices().find(v => v.lang && v.lang.toLowerCase().startsWith('pt'));
    if (voz) u.voice = voz;
    speechSynthesis.speak(u);
    return true;
  }
  const vibrar = p => { try { navigator.vibrate && navigator.vibrate(p); } catch (e) { /* sem suporte */ } };

  /* ---------- geografia ---------- */
  function distanciaM(a, b) {
    const R = 6371000, r = x => x * Math.PI / 180;
    const dLat = r(b.lat - a.lat), dLng = r(b.lng - a.lng);
    const h = Math.sin(dLat / 2) ** 2 + Math.cos(r(a.lat)) * Math.cos(r(b.lat)) * Math.sin(dLng / 2) ** 2;
    return 2 * R * Math.asin(Math.sqrt(h));
  }
  const fmtDist = m => m < 1000 ? `${Math.round(m)} m` : `${fmtNum(m / 1000, 1)} km`;

  /* ---------- PWA ---------- */
  function pwa() {
    if ('serviceWorker' in navigator && location.protocol.startsWith('http')) navigator.serviceWorker.register('sw.js').catch(() => {});
    let pedido = null;
    const btn = $('#btn-instalar');
    window.addEventListener('beforeinstallprompt', ev => { ev.preventDefault(); pedido = ev; if (btn) btn.hidden = false; });
    if (btn) btn.addEventListener('click', async () => { if (!pedido) return; pedido.prompt(); await pedido.userChoice; pedido = null; btn.hidden = true; });
  }

  window.MVP = { $, $$, esc, criarEstado, fmtBRL, fmtNum, fmtData, hoje, uid, toast, modal, confirmar, baixar, escolherArquivo, lerComoDataURL, ligarDados, abas, falar, vibrar, distanciaM, fmtDist, pwa };
})();
