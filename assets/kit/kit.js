/* ==========================================================================
   kit.js — utilitários reutilizáveis para todos os MVPs (3SemVG)
   Sem dependências externas. Usa localStorage e APIs nativas do navegador.
   ========================================================================== */

/* ---------- namespace do grupo (isola localStorage por MVP) ---------- */
const NS = window.__kitNS || 'kit';
function _key(k) { return NS + ':' + k; }

export const store = {
  get(k, fallback) {
    try {
      const v = localStorage.getItem(_key(k));
      return v === null ? fallback : JSON.parse(v);
    } catch { return fallback; }
  },
  set(k, v) {
    try { localStorage.setItem(_key(k), JSON.stringify(v)); return true; } catch { return false; }
  },
  remove(k) { localStorage.removeItem(_key(k)); },
  clear() { Object.keys(localStorage).forEach(k => { if (k.startsWith(NS + ':')) localStorage.removeItem(k); }); }
};

/* ---------- router hash (#/pagina) ---------- */
export const router = {
  init(onRoute) {
    this._cb = onRoute;
    window.addEventListener('hashchange', () => this._cb(this.route()));
    this._cb(this.route());
  },
  route() {
    const h = window.location.hash || '#/';
    const [, path, ...parts] = h.match(/^#(\/[^?]*)(\?.*)?$/) || ['#/', '/', ''];
    const params = {};
    if (parts.length) {
      new URLSearchParams(parts[0].slice(1)).forEach((v, k) => { params[k] = v; });
    }
    return { path: path || '/', params };
  },
  navigate(path) { window.location.hash = path; }
};

/* ---------- formatação ---------- */
export function fmtBRL(v) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v || 0);
}
export function fmtData(d, opts = {}) {
  if (!d) return '';
  const dt = d instanceof Date ? d : new Date(d);
  return dt.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric', ...opts });
}
export function fmtDataInput(d) {
  if (!d) return '';
  const dt = d instanceof Date ? d : new Date(d);
  return dt.toISOString().slice(0, 10);
}
export function uid() {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
}

/* ---------- toast ---------- */
export function toast(msg, tipo = 'default', dur = 2800) {
  let c = document.querySelector('.toast-container');
  if (!c) {
    c = document.createElement('div');
    c.className = 'toast-container';
    document.body.appendChild(c);
  }
  const el = document.createElement('div');
  el.className = `toast ${tipo}`;
  el.textContent = msg;
  el.style.setProperty('--dur', dur + 'ms');
  c.appendChild(el);
  setTimeout(() => el.remove(), dur + 300);
}

/* ---------- modal ---------- */
export function modal({ title, body, footer, onClose } = {}) {
  let overlay = document.querySelector('.modal-overlay');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.className = 'modal-overlay';
    overlay.innerHTML = `<div class="modal"><div class="modal-header"><span class="modal-title"></span><button class="modal-close" aria-label="Fechar">×</button></div><div class="modal-body"></div><div class="modal-footer"></div></div>`;
    document.body.appendChild(overlay);
    overlay.querySelector('.modal-close').addEventListener('click', () => close());
    overlay.addEventListener('click', e => { if (e.target === overlay) close(); });
  }
  const close = () => {
    overlay.classList.remove('open');
    setTimeout(() => { overlay.remove(); }, 350);
    if (onClose) onClose();
  };
  overlay.querySelector('.modal-title').textContent = title || '';
  overlay.querySelector('.modal-body').innerHTML = typeof body === 'string' ? body : (body ? body.outerHTML : '');
  const foot = overlay.querySelector('.modal-footer');
  foot.innerHTML = '';
  if (footer) {
    if (typeof footer === 'string') foot.innerHTML = footer;
    else if (Array.isArray(footer)) {
      footer.forEach(b => foot.appendChild(typeof b === 'string' ? createEl(b) : b));
    }
  }
  requestAnimationFrame(() => overlay.classList.add('open'));
  return { close };
}
export function createEl(tag, attrs = {}, children = []) {
  const el = document.createElement(tag);
  Object.entries(attrs).forEach(([k, v]) => { if (k === 'className') el.className = v; else el.setAttribute(k, v); });
  children.forEach(c => { if (typeof c === 'string') el.appendChild(document.createTextNode(c)); else if (c) el.appendChild(c); });
  return el;
}

/* ---------- confirmar ---------- */
export function confirmar(msg, onSim, onNao) {
  const btnSim = createEl('button', { className: 'btn btn-primary', 'data-action': 'yes' }, [msg + '?']);
  const btnNao = createEl('button', { className: 'btn btn-secondary', 'data-action': 'no' }, ['Cancelar']);
  modal({
    title: 'Confirmar',
    body: `<p style="font-size:15px">${msg}?</p>`,
    footer: [btnSim, btnNao]
  });
  document.querySelector('.modal').dataset.onClose = 'true';
  document.querySelector('[data-action="yes"]').onclick = () => { store._modalClose && store._modalClose(); if (onSim) onSim(); };
  document.querySelector('[data-action="no"]').onclick = () => { store._modalClose && store._modalClose(); if (onNao) onNao(); };
  const mo = document.querySelector('.modal-overlay');
  store._modalClose = () => { mo.classList.remove('open'); setTimeout(() => mo.remove(), 350); };
}

/* ---------- download ---------- */
export function baixarJSON(data, nome = 'dados') {
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href = url; a.download = nome + '.json'; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
export function baixarCSV(rows, colunas, nome = 'dados') {
  const hdr = colunas.map(c => typeof c === 'string' ? c : c.label).join(';');
  const body = rows.map(r => colunas.map(c => {
    const v = typeof c === 'object' ? r[c.key] : r[c];
    return String(v ?? '').replace(/;/g, ',');
  }).join(';')).join('\n');
  const blob = new Blob(['\uFEFF' + hdr + '\n' + body], { type: 'text/csv;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href = url; a.download = nome + '.csv'; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

/* ---------- import ---------- */
export function importarJSON(onLoaded) {
  const inp = document.createElement('input'); inp.type = 'file'; inp.accept = '.json';
  inp.onchange = () => {
    const file = inp.files[0]; if (!file) return;
    const reader = new FileReader();
    reader.onload = e => {
      try {
        const data = JSON.parse(e.target.result);
        if (onLoaded) onLoaded(data);
        toast('Dados importados com sucesso!', 'success');
      } catch { toast('Arquivo inválido', 'error'); }
    };
    reader.readAsText(file);
  };
  inp.click();
}

/* ---------- seed (dados de exemplo) ---------- */
export function seed(key, fn) {
  const existing = store.get(key);
  if (!existing) {
    const data = fn();
    store.set(key, data);
    return data;
  }
  return existing;
}

/* ---------- gráfico SVG simples (barras / rosca) ---------- */
export function graficoBarras(container, dados, opts = {}) {
  const { titulo, formatoY } = opts;
  if (!dados || !dados.length) return '';
  const w = container.offsetWidth || 320;
  const h = Math.min(200, w * 0.5);
  const max = Math.max(...dados.map(d => d.v));
  const barW = Math.floor((w - 40) / dados.length) - 4;
  const svg = ['<svg viewBox="0 0 ' + w + ' ' + h + '" xmlns="http://www.w3.org/2000/svg">'];
  svg.push('<style>text{font-family:system-ui,sans-serif;font-size:11px;fill:#666} .bar{fill:var(--accent,#7c3aed)}</style>');
  if (titulo) svg.push('<text x="4" y="14">' + titulo + '</text>');
  dados.forEach((d, i) => {
    const bh = Math.max(4, ((d.v / max) * (h - 40)));
    const x = 20 + i * (barW + 4);
    const y = h - 20 - bh;
    svg.push('<rect class="bar" x="' + x + '" y="' + y + '" width="' + barW + '" height="' + bh + '" rx="4"/>');
    svg.push('<text x="' + (x + barW / 2) + '" y="' + (h - 4) + '" text-anchor="middle">' + (formatoY ? formatoY(d.v) : d.v) + '</text>');
    if (d.label) svg.push('<text x="' + (x + barW / 2) + '" y="' + (h - 4) + '" text-anchor="middle" dy="-6">' + d.label + '</text>');
  });
  svg.push('</svg>');
  return svg.join('');
}

export function graficoRosca(container, dados, opts = {}) {
  const { titulo } = opts;
  if (!dados || !dados.length) return '';
  const size = Math.min(container.offsetWidth || 200, 200);
  const r = size / 2 - 10;
  const cx = size / 2, cy = size / 2;
  let startAngle = -90;
  const total = dados.reduce((s, d) => s + d.v, 0);
  const colors = ['#7c3aed', '#facc15', '#16a34a', '#ea580c', '#3b82f6', '#ec4899', '#8b5cf6'];
  const slices = dados.map((d, i) => {
    const angle = (d.v / total) * 360;
    const endAngle = startAngle + angle;
    const x1 = cx + r * Math.cos(startAngle * Math.PI / 180);
    const y1 = cy + r * Math.sin(startAngle * Math.PI / 180);
    const x2 = cx + r * Math.cos(endAngle * Math.PI / 180);
    const y2 = cy + r * Math.sin(endAngle * Math.PI / 180);
    const large = angle > 180 ? 1 : 0;
    const path = 'M ' + cx + ' ' + cy + ' L ' + x1 + ' ' + y1 + ' A ' + r + ' ' + r + ' 0 ' + large + ' 1 ' + x2 + ' ' + y2 + ' Z';
    startAngle = endAngle;
    return '<path d="' + path + '" fill="' + (d.color || colors[i % colors.length]) + '"/>';
  }).join('');
  const svg = ['<svg viewBox="0 0 ' + size + ' ' + size + '" xmlns="http://www.w3.org/2000/svg" style="max-width:' + size + 'px">'];
  svg.push('<style>text{font-family:system-ui,sans-serif;font-size:11px;fill:#666}</style>');
  if (titulo) svg.push('<text x="' + (cx) + '" y="14" text-anchor="middle">' + titulo + '</text>');
  svg.push(slices);
  svg.push('<circle cx="' + cx + '" cy="' + cy + '" r="' + (r * 0.55) + '" fill="#fff"/>');
  svg.push('</svg>');
  return svg.join('');
}

/* ---------- SW registration (opcional) ---------- */
export async function registerSW(url = 'sw.js') {
  if ('serviceWorker' in navigator) {
    try {
      const reg = await navigator.serviceWorker.register(url);
      return reg;
    } catch (e) { console.warn('SW registration failed', e); }
  }
}

/* ---------- install prompt ---------- */
export function setupInstallPrompt(btnId) {
  let deferredPrompt;
  const btn = document.getElementById(btnId);
  if (!btn) return;
  window.addEventListener('beforeinstallprompt', e => {
    e.preventDefault();
    deferredPrompt = e;
    btn.style.display = '';
  });
  btn.addEventListener('click', async () => {
    if (!deferredPrompt) return;
    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    deferredPrompt = null;
    btn.style.display = 'none';
  });
}

/* ---------- screen orientation lock ---------- */
export async function lockPortrait() {
  if (screen.orientation && screen.orientation.lock) {
    try { await screen.orientation.lock('portrait'); } catch {}
  }
}

/* ---------- vibrate (haptic feedback) ---------- */
export function vibra(ms = 10) {
  if (navigator.vibrate) navigator.vibrate(ms);
}
