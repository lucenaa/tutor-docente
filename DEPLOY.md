# 🚀 Roteiro de Deploy: Railway + Netlify

Guia completo para fazer deploy do **Tutor Docente Verbum** em produção.

---

## 📐 Arquitetura do Projeto

```
┌─────────────────────┐         ┌─────────────────────┐
│      NETLIFY        │         │      RAILWAY        │
│   (Frontend React)  │  ───►   │   (Backend FastAPI) │
│                     │  HTTPS  │                     │
│   web/dist/         │         │   app/main.py       │
└─────────────────────┘         └─────────────────────┘
         │                               │
         │                               │
         ▼                               ▼
    Usuário final              Google Generative AI
                                   (Gemini API)
```

- **Frontend**: React + Vite + Tailwind → hospedado no **Netlify** (arquivos estáticos)
- **Backend**: FastAPI + Uvicorn → hospedado no **Railway** (servidor Python)
- **AI**: Google Gemini 2.5 via API

---

## 📋 Pré-requisitos

1. Conta no [GitHub](https://github.com) com o repositório do projeto
2. Conta no [Railway](https://railway.app) (grátis com cartão ou $5/mês)
3. Conta no [Netlify](https://netlify.com) (grátis)
4. Chave de API do [Google AI Studio](https://aistudio.google.com/apikey)

---

## 🔧 PARTE 1: Deploy do Backend no Railway

### 1.1. Conectar Repositório

1. Acesse [railway.app](https://railway.app) e faça login
2. Clique em **"New Project"**
3. Selecione **"Deploy from GitHub repo"**
4. Autorize o Railway no GitHub e selecione o repositório `tutor-docente`
5. O Railway detectará automaticamente que é um projeto Python

### 1.2. Configurar Variáveis de Ambiente

No painel do Railway, vá em **Variables** e adicione:

| Variável | Valor | Descrição |
|----------|-------|-----------|
| `GOOGLE_API_KEY` | `sua-chave-aqui` | Chave da API do Google Generative AI |
| `FRONTEND_ORIGIN` | `https://seu-site.netlify.app` | URL do frontend (após deploy no Netlify) |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Modelo do Gemini (opcional, default: gemini-2.5-flash) |

> ⚠️ **Importante**: `FRONTEND_ORIGIN` deve ser a URL exata do Netlify, sem barra no final.

### 1.3. Arquivos de Configuração (já existentes)

O projeto já possui os arquivos necessários:

**`railway.json`** - Comando de inicialização:
```json
{
    "deploy": {
        "startCommand": "uvicorn app.main:app --host 0.0.0.0 --port $PORT",
        "numReplicas": 1
    }
}
```

**`Procfile`** - Alternativa (Railway aceita ambos):
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**`requirements.txt`** - Dependências Python:
```
fastapi>=0.112
uvicorn[standard]>=0.30
google-generativeai>=0.8.0
python-dotenv>=1.0
httpx>=0.27
```

### 1.4. Deploy Automático

- O Railway faz deploy automático a cada `git push` na branch `main`
- Aguarde o build completar (1-3 minutos)
- Copie a URL pública gerada (ex: `https://tutor-docente-production.up.railway.app`)

### 1.5. Testar o Backend

Acesse `https://sua-url-railway.up.railway.app/` no navegador:
```json
{
  "status": "ok",
  "trilho": "01",
  "steps": 20
}
```

---

## 🌐 PARTE 2: Deploy do Frontend no Netlify

### 2.1. Conectar Repositório

1. Acesse [app.netlify.com](https://app.netlify.com) e faça login
2. Clique em **"Add new site"** → **"Import an existing project"**
3. Conecte com GitHub e selecione o repositório `tutor-docente`

### 2.2. Configurar Build Settings

Na tela de configuração, defina:

| Campo | Valor |
|-------|-------|
| **Base directory** | `web` |
| **Build command** | `npm run build` |
| **Publish directory** | `web/dist` |

### 2.3. Configurar Variáveis de Ambiente

Vá em **Site settings** → **Environment variables** e adicione:

| Variável | Valor | Descrição |
|----------|-------|-----------|
| `VITE_API_URL` | `https://sua-url-railway.up.railway.app` | URL do backend no Railway |

> ⚠️ **Importante**: Sem barra no final da URL!

### 2.4. Deploy

1. Clique em **"Deploy site"**
2. Aguarde o build (1-2 minutos)
3. Copie a URL gerada (ex: `https://seu-site.netlify.app`)

### 2.5. Atualizar CORS no Railway

Volte ao Railway e atualize a variável:
```
FRONTEND_ORIGIN=https://seu-site.netlify.app
```

Isso permite que o frontend faça requisições ao backend.

---

## 🔄 PARTE 3: Fluxo de Deploy Contínuo

Após configurar, o deploy é automático:

```
git add .
git commit -m "feat: nova funcionalidade"
git push origin main
```

1. **Railway** detecta o push → rebuild do backend
2. **Netlify** detecta o push → rebuild do frontend

---

## 🐛 PARTE 4: Troubleshooting

### Erro: "CORS policy blocked"

**Causa**: `FRONTEND_ORIGIN` não está configurado corretamente no Railway.

**Solução**: 
1. Verifique se a URL está exata (sem barra final, com https)
2. Redeploy o backend após alterar a variável

### Erro: "f-string expression cannot include backslash"

**Causa**: Python 3.11+ não aceita `\` dentro de `{}` em f-strings.

**Solução**: Troque `\"` por `'` dentro das expressões. Exemplo:
```python
# ❌ Errado
f"{'<iframe src=\"url\">' if x else 'texto'}"

# ✅ Correto  
f"{'<iframe src='url'>' if x else 'texto'}"
```

### Erro: "GOOGLE_API_KEY não configurada"

**Causa**: Variável de ambiente não definida no Railway.

**Solução**: Adicione `GOOGLE_API_KEY` nas variáveis do Railway.

### Erro: "google-generativeai FutureWarning"

**Causa**: O pacote `google-generativeai` está depreciado.

**Status**: É apenas um aviso, não impede o funcionamento. Migração futura para `google-genai` é recomendada.

### Frontend não conecta ao backend

**Checklist**:
1. `VITE_API_URL` está definido no Netlify?
2. A URL termina sem `/`?
3. O backend está rodando? (testar URL diretamente)
4. `FRONTEND_ORIGIN` no Railway está correto?

---

## 📊 PARTE 5: Monitoramento

### Railway
- Logs: Dashboard → Deployments → View Logs
- Métricas: Dashboard → Metrics (CPU, RAM, Network)

### Netlify
- Logs de build: Deploys → Deploy log
- Analytics: Analytics (requer plano Pro)

---

## 💰 PARTE 6: Custos Estimados

| Serviço | Plano | Custo |
|---------|-------|-------|
| Railway | Hobby | ~$5/mês (ou grátis com trial) |
| Netlify | Free | $0/mês (100GB bandwidth) |
| Google AI | Pay-as-you-go | ~$0.01-0.10 por 1k tokens |

**Total estimado**: $5-10/mês para uso moderado.

---

## 📁 Estrutura de Arquivos Relevantes

```
tutor-docente/
├── app/                    # Backend FastAPI
│   ├── main.py            # Endpoints da API
│   ├── prompts/           # System prompts do tutor
│   └── content/           # Conteúdos das trilhas (.md)
├── web/                    # Frontend React
│   ├── src/
│   │   └── App.tsx        # Componente principal
│   ├── dist/              # Build de produção (gerado)
│   ├── package.json       # Dependências Node
│   └── vite.config.ts     # Config do Vite
├── railway.json           # Config do Railway
├── Procfile               # Alternativa ao railway.json
├── requirements.txt       # Dependências Python
└── README.md              # Documentação geral
```

---

## ✅ Checklist Final

- [ ] Repositório no GitHub
- [ ] Backend no Railway com `GOOGLE_API_KEY` e `FRONTEND_ORIGIN`
- [ ] Frontend no Netlify com `VITE_API_URL`
- [ ] Testar URL do backend retorna `{"status": "ok"}`
- [ ] Testar frontend carrega e inicia o chat
- [ ] Verificar logs se houver erros

---

## 🔗 Links Úteis

- [Railway Docs](https://docs.railway.app/)
- [Netlify Docs](https://docs.netlify.com/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Vite Build Guide](https://vitejs.dev/guide/build.html)
- [Google AI Studio](https://aistudio.google.com/)
