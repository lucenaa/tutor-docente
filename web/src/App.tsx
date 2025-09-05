import { BrowserRouter, Routes, Route, Link, useNavigate, useParams } from "react-router-dom";
import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { BookOpenCheck, GraduationCap, Sparkles } from "lucide-react";
import "./index.css";

function Avatar({ label, color }: { label: string; color?: string }) {
	return (
		<div className={`w-8 h-8 rounded-full flex items-center justify-center text-xs font-semibold ${color ?? "bg-primary text-primary-foreground"}`}>{label}</div>
	);
}

function Navbar() {
	return (
		<nav className="sticky top-0 z-30 border-b bg-background/60 backdrop-blur supports-[backdrop-filter]:bg-background/50">
			<div className="mx-auto max-w-6xl px-4 h-14 flex items-center justify-between">
				<Link className="font-semibold tracking-tight" to="/">Verbum • Catálogo</Link>
				<div className="text-sm text-muted-foreground">Ambiente de Treinamento Docente</div>
			</div>
		</nav>
	);
}

function Footer() {
	return (
		<footer className="border-t mt-10">
			<div className="mx-auto max-w-6xl px-4 py-8 text-xs text-muted-foreground">© 2025 Verbum — Demo de treinamento docente</div>
		</footer>
	);
}

function Button(
	props: React.PropsWithChildren<{ variant?: "default" | "secondary" | "outline"; to?: string; onClick?: () => void; disabled?: boolean }>
) {
	const clsBase =
		"inline-flex items-center justify-center font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 rounded-full h-11 px-5 text-sm";
	const map: Record<string, string> = {
		default: "bg-primary text-primary-foreground hover:bg-primary/90",
		secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
		outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
	};
	const cls = `${clsBase} ${map[props.variant ?? "default"]}`;
	if (props.to) return <Link className={cls} to={props.to}>{props.children}</Link>;
	return (
		<button className={cls} onClick={props.onClick} disabled={props.disabled}>
			{props.children}
		</button>
	);
}

function Card(props: { title?: string; description?: string; footer?: React.ReactNode; children?: React.ReactNode; disabled?: boolean }) {
	return (
		<div className={`rounded-2xl border bg-card text-card-foreground card-hover ${props.disabled ? "opacity-60" : ""}`}>
			{(props.title || props.description) && (
				<div className="p-5 border-b">
					{props.title && <h3 className="text-lg font-semibold leading-none tracking-tight">{props.title}</h3>}
					{props.description && <p className="text-sm text-muted-foreground mt-1">{props.description}</p>}
				</div>
			)}
			<div className="p-5 space-y-3">{props.children}</div>
			{props.footer && <div className="p-4 border-t flex items-center justify-end gap-2">{props.footer}</div>}
		</div>
	);
}

function Home() {
	const lessons = [
		{ id: "1", title: "Aula 1 — Situação-problema", desc: "Dimensão 1 — Práticas para o Desenvolvimento Integral", enabled: true, icon: <Sparkles className="w-5 h-5" /> },
		{ id: "2", title: "Aula 2 — Fundamentação", desc: "Trilho 2 — Fundamentos Verbum", enabled: true, icon: <Sparkles className="w-5 h-5" /> },
		{ id: "3", title: "Aula 3 — Integração e Aplicação", desc: "Trilho 3 — Mini-plano integral", enabled: true, icon: <Sparkles className="w-5 h-5" /> },
		{ id: "4", title: "Aula 4 — Curadoria Complementar", desc: "Trilho 4 — Repertório e aplicação", enabled: true, icon: <Sparkles className="w-5 h-5" /> },
	];
	return (
		<div className="mx-auto max-w-6xl px-4 py-8">
			<div className="mb-6 flex items-center gap-3">
				<GraduationCap className="w-6 h-6 text-primary" />
				<h1 className="text-2xl font-semibold">Catálogo de Aulas</h1>
			</div>
			<div className="grid gap-6 md:grid-cols-2">
				{lessons.map((l) => (
					<Card key={l.id} title={l.title} description={l.desc} disabled={!l.enabled} footer={<Button variant={l.enabled ? "default" : "outline"} to={l.enabled ? `/chat/${l.id}` : undefined} disabled={!l.enabled}>Entrar</Button>}>
						<div className="flex items-center gap-3 text-sm text-muted-foreground"><BookOpenCheck className="w-4 h-4" />
							<span>Treinamento Docente</span>
						</div>
						<div className="flex items-center gap-2 text-xs text-muted-foreground">
							{l.icon}
							<span>{l.enabled ? "Disponível" : "Bloqueada"}</span>
						</div>
					</Card>
				))}
			</div>
		</div>
	);
}

function AssistantBubble({ children }: { children: React.ReactNode }) {
	return (
		<div className="flex items-start gap-2">
			<Avatar label="AI" />
			<div className="max-w-[80ch] md:max-w-[70%] rounded-2xl border border-border bg-card px-4 py-3 text-sm shadow-card">
				{children}
			</div>
		</div>
	);
}

function UserBubble({ children }: { children: React.ReactNode }) {
	return (
		<div className="flex items-start gap-2 justify-end">
			<div className="max-w-[80ch] md:max-w-[70%] rounded-2xl bg-primary text-primary-foreground px-4 py-2 text-sm shadow">
				{children}
			</div>
			<Avatar label="Você" color="bg-secondary text-secondary-foreground" />
		</div>
	);
}

function Chat() {
	const { id } = useParams();
	const navigate = useNavigate();
	function normalizeApiBase(value?: string): string {
		if (!value) return "";
		let v = value.trim();
		if (v.endsWith("/")) v = v.slice(0, -1);
		try {
			const u = new URL(v);
			const pathname = u.pathname.endsWith("/") ? u.pathname.slice(0, -1) : u.pathname;
			return `${u.protocol}//${u.host}${pathname}`;
		} catch {
			try {
				const u2 = new URL(`https://${v}`);
				const pathname = u2.pathname.endsWith("/") ? u2.pathname.slice(0, -1) : u2.pathname;
				return `${u2.protocol}//${u2.host}${pathname}`;
			} catch {
				return "";
			}
		}
	}
	const API_BASE = normalizeApiBase((import.meta as any).env?.VITE_API_URL); // ex.: https://seu-backend.onrender.com
	const [messages, setMessages] = React.useState<{ role: "user" | "assistant"; content: string }[]>([
		{ role: "assistant", content: Number(id) === 2 ? "Bem-vindo ao Trilho 2 — vamos começar pelo enquadramento inicial?" : Number(id) === 3 ? "Bem-vindo ao Trilho 3 — pronto para transformar princípios em ações?" : Number(id) === 4 ? "Bem-vindo ao Trilho 4 — vamos começar pela sua necessidade formativa de hoje?" : "Olá! Vamos começar a Aula 1. Posso iniciar a introdução?" },
	]);
	const [pending, setPending] = React.useState(false);
	const inputRef = React.useRef<HTMLInputElement>(null);
	const scrollRef = React.useRef<HTMLDivElement>(null);

	React.useEffect(() => {
		if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
	}, [messages, pending]);

	async function send(message: string) {
		setMessages((prev) => [...prev, { role: "user", content: message }]);
		setPending(true);
		try {
			const resp = await fetch(`${API_BASE}/api/chat`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({ lesson_id: id, messages: [...messages, { role: "user", content: message }] }),
			});
			const data = await resp.json();
			if (!resp.ok) throw new Error(data.detail || "Erro");
			setMessages((prev) => [...prev, { role: "assistant", content: data.reply }]);
		} catch (e) {
			setMessages((prev) => [...prev, { role: "assistant", content: "Desculpe, ocorreu um erro ao gerar a resposta." }]);
		} finally {
			setPending(false);
		}
	}

	return (
		<div className="mx-auto max-w-5xl px-4 py-8">
			<div className="mb-4 flex items-center justify-between">
				<div className="flex items-center gap-3">
					<Sparkles className="w-5 h-5 text-primary" />
					<div>
						<h1 className="text-xl font-semibold">Aula {id} — Chat Tutor</h1>
						<p className="text-xs text-muted-foreground">Converse com o tutor passo a passo (LLM).</p>
					</div>
				</div>
				<Button variant="outline" onClick={() => navigate("/")}>Voltar</Button>
			</div>
			<div className="rounded-2xl border bg-card shadow-card">
				<div id="chat-scroll" ref={scrollRef} className="h-[65vh] overflow-y-auto p-4 space-y-4">
					{messages.map((m, idx) => (
						m.role === "user" ? (
							<UserBubble key={idx}>{m.content}</UserBubble>
						) : (
							<AssistantBubble key={idx}>
								<ReactMarkdown remarkPlugins={[remarkGfm]}>{m.content}</ReactMarkdown>
							</AssistantBubble>
						)
					))}
					{pending && (
						<AssistantBubble>
							<span className="inline-flex gap-1">
								<span className="w-2 h-2 rounded-full bg-foreground/50 animate-bounce"></span>
								<span className="w-2 h-2 rounded-full bg-foreground/50 animate-bounce [animation-delay:0.15s]"></span>
								<span className="w-2 h-2 rounded-full bg-foreground/50 animate-bounce [animation-delay:0.3s]"></span>
							</span>
						</AssistantBubble>
					)}
				</div>
				<form
					id="chat-form"
					className="border-t p-3 flex items-center gap-2 sticky bottom-0 bg-card"
					onSubmit={(e) => {
						e.preventDefault();
						const value = (inputRef.current?.value || "").trim();
						if (!value) return;
						if (inputRef.current) inputRef.current.value = "";
						send(value);
					}}
				>
					<input ref={inputRef} id="chat-input" placeholder="Digite sua mensagem..." className="flex-1 h-11 rounded-full border px-4 text-sm shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring bg-background" />
					<button id="chat-send" type="submit" className="inline-flex items-center justify-center h-11 px-6 rounded-full bg-primary text-primary-foreground hover:bg-primary/90 font-medium" disabled={pending}>
						{pending ? "Enviando..." : "Enviar"}
					</button>
				</form>
			</div>
		</div>
	);
}

export default function App() {
	return (
		<BrowserRouter>
			<Navbar />
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/chat/:id" element={<Chat />} />
			</Routes>
			<Footer />
		</BrowserRouter>
	);
}
