## Tutor Docente Verbum — Catálogo e Chat (Aulas 1–4)

Aplicação web com backend em FastAPI e frontend em React (Vite + TypeScript + Tailwind v4), que oferece um catálogo de aulas e um chat tutor com prompts específicos para cada trilho (Aulas 1–4). O tutor utiliza o modelo `gemini-2.5-pro` (Google Generative AI).

### Arquitetura
- Backend: FastAPI (`app/main.py`) com endpoint `/api/chat` e prompts por `lesson_id` (1, 2, 3, 4)
- Frontend: React + Vite em `web/` com Tailwind v4, UI com ícones e renderização de Markdown
- CORS habilitado para `http://localhost:5173`

### Requisitos
- Python 3.10+
- Node.js 18+
- Uma chave de API do Google Generative AI (`GOOGLE_API_KEY`)

### Configuração do Backend (Windows PowerShell)
1) Criar/usar venv e instalar dependências:
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
venv\Scripts\python -m pip install -r requirements.txt
```
2) Definir a variável de ambiente (ou use um arquivo `.env`):
```powershell
setx GOOGLE_API_KEY "SUA_CHAVE_AQUI"
```
Feche e reabra o terminal após `setx`. Alternativa: crie `.env` na raiz com:
```
GOOGLE_API_KEY=coloque_sua_chave_aqui
```
3) Rodar o servidor FastAPI:
```powershell
venv\Scripts\python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Configuração do Frontend
1) Instalar dependências do app React:
```powershell
cd web
npm install
```
2) Executar o Vite:
```powershell
npm run dev
```
3) Acessar o frontend em `http://localhost:5173` (o backend fica em `http://localhost:8000`).

### Uso
- Página inicial: catálogo com as Aulas 1–4. Clique em uma aula para abrir o chat.
- O chat envia `lesson_id` para o backend que seleciona o prompt correto.
- Mensagens do tutor suportam Markdown.

### Prompts
- Aula 1 — Situação-problema (Dimensão 1 — Desenvolvimento Integral)
- Aula 2 — Fundamentação (Fundamentos/BNCC/valores)
- Aula 3 — Integração e Aplicação (mini-plano integral)
- Aula 4 — Curadoria Complementar (repertório + aplicação)

### Publicação no GitHub
Assumindo que você já tem um repositório remoto `https://github.com/lucenaa/tutor-docente-verbum`:

```powershell
cd C:\Users\GABRIEL-PC\Desktop\projetos\trilhas-docentes
git init
git remote add origin https://github.com/lucenaa/tutor-docente-verbum.git
git add .
git commit -m "feat: backend FastAPI + frontend React (Aulas 1–4, Gemini)"
git branch -M main
git push -u origin main
```

Se o repositório já possuir histórico, execute antes:
```powershell
git pull --rebase origin main
```

### Estrutura de Pastas (principal)
```
app/
  main.py
  templates/ (apenas para a versão server-side inicial — o front atual é React)
web/
  src/
  vite.config.ts
  package.json
requirements.txt
README.md
```

### Notas
- Tailwind v4 com `@tailwindcss/postcss`. Se vir erro de PostCSS, rode `npm install` dentro de `web/`.
- O chat usa `google-generativeai` e requer `GOOGLE_API_KEY` válida.
- Para produção, recomenda-se servir o build do React (`npm run build` e servir `web/dist`) por um servidor (Nginx) e apontar o backend FastAPI por WSGI/ASGI (uvicorn/gunicorn) atrás de um proxy.

