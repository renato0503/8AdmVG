# App de Coleta — Customer Discovery · 8AdmVG

Formulário de campo **offline** em arquivo único (`index.html`), usado na **Parte 3**
(ida ao shopping). Roda no navegador do celular, **sem instalar nada** e **sem internet**.

---

## Como usar

1. Abra o app no navegador do celular `https://renato0503.github.io/8AdmVG/coleta/`
   - **Dica:** no Chrome, menu → *Adicionar à tela inicial* para virar ícone de app.
2. Escolha o **grupo da dupla** (G1–G5) — fica salvo no aparelho.
3. Toque em **Iniciar nova coleta** → **selecione o aluno** que está fazendo a pesquisa →
   marque o **Bloco 0 (perfil) por observação** → responda as **20 perguntas** (escala 1–5,
   com confirmação em cada resposta).
4. Ao salvar, aparece o **CÓDIGO** (`G<n>-<nnn>`). **Leia o código no início do áudio do WhatsApp.**
5. Ao final, pergunte se a pessoa quer **deixar o e-mail** para receber o TCLE —
   campo opcional, não entra nas notas.
6. No fim do dia, use **Exportar dados** → **CSV** (Excel) ou **JSON** (backup/correlação).
7. Se configurou a sincronização, cada resposta sobe sozinha para a planilha Google.

---

## Fluxo de coleta

```
Grupo → Iniciar coleta → Selecionar aluno → Perfil (observação) →
20 perguntas (confirmação em cada) → E-mail (opcional) → Código G<n>-<nnn>
```

---

## Protocolo (fixo, vale para todos os grupos)

- **Bloco 0 — Perfil** é a **exceção**: marcado **por observação** (não se pergunta).
  - Faixa etária · Sexo · Classe social (estimada) · Raça/cor (estimada). Em dúvida, **"Não sei estimar"**.
  - **Nunca** pergunte raça nem renda.
- As **demais 20 perguntas** são marcadas de **1 a 5**: `1` = um polo, `5` = polo oposto
  (todos os cinco rótulos aparecem na tela: 1·2·3·4·5 com descrições intermediárias).
- **Sem resposta aberta.** Falas/justificativas vão no **áudio** (quanti = app · quali = áudio).
- Cada resposta salva gera um **código** `G<n>-<nnn>` para correlacionar com o áudio.
- Em campo: **dupla** com 2 celulares (um do formulário, um do áudio).

---

## Os 5 grupos e seus membros

| # | Projeto | Professor | Integrantes |
|---|---|---|---|
| G1 | HoraCerta | Prof. Renato | José Arlindo da Cunha Filho · Taynara Luana de Oliveira · Luana da Silva Araújo · Leticia Leydiane de Oliveira · Samara de Campos Henrique |
| G2 | GuiaMobi | Prof. Renato | Cinthia Ferreira da Silva Oliveira · Danielly Gomes de Souza Pinto · Leandro Teodoro de Santana · Guilherme Henrique Xavier Sampaio · Esther Rodrigues da Conceição |
| G3 | VozGuia | Profa. Sandra | Karla Moema Henning Pitaluga · Victor Hugo Gomes de Almeida dos Passos · Nicolas Alexandre Freitas Moraes · Fabio Teyllor Tatehira do Couto · Yasmim Quéren Rodrigues Feitosa |
| G4 | CasaPiloto | Profa. Polyana | Aliny Suquerê Guimarães · André Henrique Magalhães Duarte · Michelly de Jesus Pereira Silva · Everson Alencar de Souza |
| G5 | CasaHumanizada | Prof. Heitor | Bianca Veronez Dias · Geovanna Shara Soares da Silveira · Estefane Souza da Costa |

---

## Estrutura do código (manutenção)

- `PERFIL` — campos do Bloco 0 (comuns a todos os grupos).
- `GRUPOS` — dados por grupo: `nome`, `prof`, `cor`/`corDark`/`rgb`, `alunos[]`, `triagem`,
  `sensivel`/`aviso`, `blocos[]` com `perguntas[]` no formato `{ q, a, b }`
  (`a` = polo 1 · `b` = polo 5). **Cada grupo tem exatamente 20 perguntas.**
- `localStorage` — chaves `cd8admvg_respostas`, `cd8admvg_seq`, `cd8admvg_grupo`, `cd8admvg_sheet_url`.

### Formato do CSV e do JSON exportado

```
codigo; aluno; grupo; grupo_nome; data; faixaEtaria; sexo; classe; raca; orgao; Q1; Q2; …; Q20; email_contato
```

> **Importante:** o app envia `aluno` com o nome completo do membro selecionado na tela
> "Quem está coletando?". Esse campo também vai para a planilha Google na coluna `aluno`.

### Adicionar/editar perguntas

Edite o objeto do grupo em `GRUPOS`. Cada grupo **precisa ter exatamente 20 perguntas**
com os dois polos (`a` e `b`). Depois de editar:

```powershell
Copy-Item .\App\index.html .\coleta\index.html -Force
git add App/index.html coleta/index.html && git commit -m "msg" && git push
```

---

## Onde os dados ficam salvos

O app **não tem backend** — é só HTML/JS local. Os dados moram em duas camadas:

1. **`localStorage` do navegador** daquele celular — automático, mas preso àquele aparelho.
2. **Arquivo exportado** (CSV/JSON) — só existe quando alguém clica em exportar/compartilhar.

Para consolidar respostas de várias duplas em um só lugar:

- **Compartilhar + Importar/Mesclar** (já pronto no app): cada dupla manda seu JSON
  por WhatsApp para o celular "central" e usa **Importar/mesclar JSON** — junta tudo
  sem duplicar (mescla pelo código `G<n>-<nnn>`).
- **Backup automático (Google Sheets)** — descrito abaixo.

---

## Backup automático — Google Apps Script + Google Sheets

Cada resposta salva tenta um `POST` automático para uma planilha Google.
Exige internet no momento do salvamento; sem internet, fica **pendente** e sincroniza
sozinha quando o celular reconectar (ou ao tocar em **"Sincronizar pendentes agora"**).

### 1. Criar a planilha e o script

1. Crie uma planilha nova em [sheets.google.com](https://sheets.google.com) (ex.: `Coleta 8AdmVG`).
2. Menu **Extensões → Apps Script**.
3. Apague o conteúdo padrão e cole o código abaixo (versão com campo `aluno`).

```javascript
function doPost(e) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName("Respostas") || ss.insertSheet("Respostas");
  const dados = JSON.parse(e.postData.contents);

  if (sheet.getLastRow() === 0) {
    const cab = ["recebidoEm","codigo","aluno","grupo","grupoNome","criadoEm",
      "faixaEtaria","sexo","classe","raca","orgao"];
    for (let i = 1; i <= 20; i++) cab.push("Q" + i);
    cab.push("email_contato");
    sheet.getRange(1, 1, 1, cab.length).setValues([cab]);
  }

  const linha = [
    new Date().toISOString(),
    dados.codigo || "",
    dados.aluno || "",
    dados.grupo || "",
    dados.grupoNome || "",
    dados.criadoEm || "",
    (dados.perfil||{}).faixaEtaria || "",
    (dados.perfil||{}).sexo || "",
    (dados.perfil||{}).classe || "",
    (dados.perfil||{}).raca || "",
    (dados.perfil||{}).orgao || "",
  ];
  for (let i = 0; i < 20; i++) linha.push((dados.respostas||{})[i] ?? "");
  linha.push(dados.email || "");

  sheet.appendRow(linha);
  return ContentService.createTextOutput(JSON.stringify({ok:true}))
    .setMimeType(ContentService.MimeType.JSON);
}
```

4. **Implantar → Nova implantação → tipo "App da Web"**.
   - Executar como: **Eu**.
   - Quem pode acessar: **Qualquer pessoa** (não "com uma Conta do Google").
5. Copie a **URL do app da Web** (termina em `/exec`).

### 2. Configurar no app de coleta

1. Abra o app → **Exportar dados**.
2. Cole a URL em **"Sincronização automática"** → **Salvar URL de sincronização**.
3. Pronto — cada resposta nova tenta subir sozinha. O status mostra quantas ficaram pendentes.

> **Nota:** a URL `/exec` está **pré-configurada** (`DEFAULT_SHEET_URL`) e aponta para a **mesma planilha do AdmCBA**
> (mesma estrutura de colunas). Os registros se distinguem por `grupoNome`; atenção: os códigos `G<n>-<nnn>` se repetem entre turmas.

---

## Observações técnicas

- **Offline por completo** para a coleta em si — sem CDN, sem fonte externa, sem build.
  A sincronização automática é o único ponto que pede internet, e é opcional.
- `localStorage` funciona em `file://` no Chrome/Safari; se o navegador bloquear, o app avisa.
- O app trata o CORS do Apps Script com `mode:"no-cors"`; o POST é enviado uma única vez
  por resposta e marcado como `sincronizado` localmente para evitar duplicação.
