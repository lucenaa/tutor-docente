import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkBreaks from "remark-breaks";
import { Sparkles, Send, Loader2 } from "lucide-react";
import "./index.css";

// ══════════════════════════════════════════════════════════════
// Types
// ══════════════════════════════════════════════════════════════

interface Message {
	role: "user" | "assistant";
	content: string;
}

interface ChatState {
	current_step?: string;
	caminho_escolhido?: "A" | "B" | null;
	completed_steps?: string[];
	lesson_completed?: boolean;
}

// Lista de steps (espelho do backend)
const STEPS_ORDER = [
	"t01_s1_intro",
	"t01_s2_video01",
	"t01_s3_texto_abertura",
	"t01_s4_pergunta_abertura",
	"t01_s5_competencias",
	"t01_s6_texto_articulacao",
	"t01_s7_q1",
	"t01_s8_q2",
	"t01_s9_q3",
	"t01_s10_q4",
	"t01_s11_q5",
	"t01_s12_video02",
	"t01_s13_texto_complementar",
	"t01_s14_perguntas_video02",
	"t01_s15_pausa_intencional",
	"t01_s16_escolha_caminho",
	"t01_s17_video03_escolhido",
	"t01_s18_video03_outro",
	"t01_s19_reflexao_caminhos",
	"t01_s20_conclusao_encerramento",
];

// ══════════════════════════════════════════════════════════════
// Components
// ══════════════════════════════════════════════════════════════

function Avatar({ label, color }: { label: string; color?: string }) {
	return (
		<div className={`w-8 h-8 rounded-full flex items-center justify-center text-xs font-semibold ${color ?? "bg-primary text-primary-foreground"}`}>
			{label}
		</div>
	);
}

function Navbar() {
	return (
		<nav className="sticky top-0 z-30 border-b bg-background/60 backdrop-blur supports-[backdrop-filter]:bg-background/50">
			<div className="mx-auto max-w-6xl px-4 h-14 flex items-center justify-between">
				<div className="flex items-center gap-2">
					<Sparkles className="w-5 h-5 text-primary" />
					<span className="font-semibold tracking-tight">Verbum • Trilho 01</span>
				</div>
				<div className="text-sm text-muted-foreground">Desenvolvimento Integral</div>
			</div>
		</nav>
	);
}

function Footer() {
	return (
		<footer className="border-t mt-auto">
			<div className="mx-auto max-w-6xl px-4 py-4 text-xs text-muted-foreground">
				© 2025 Verbum Educação — Formação Docente
			</div>
		</footer>
	);
}

// Componente para renderizar markdown com suporte a iframes de vídeo
function MarkdownWithVideos({ content }: { content: string }) {
	const processContent = (text: string) => {
		const iframeRegex = /<iframe([^>]*)><\/iframe>/gi;
		const parts: (string | JSX.Element)[] = [];
		let lastIndex = 0;
		let match;

		while ((match = iframeRegex.exec(text)) !== null) {
			if (match.index > lastIndex) {
				const beforeText = text.substring(lastIndex, match.index);
				if (beforeText.trim()) {
					parts.push(beforeText);
				}
			}

			const attrs = match[1];
			const srcMatch = attrs.match(/src=["']([^"']+)["']/);
			const widthMatch = attrs.match(/width=["']?(\d+)["']?/);
			const heightMatch = attrs.match(/height=["']?(\d+)["']?/);

			const src = srcMatch ? srcMatch[1] : "https://example.com/video-placeholder";
			const width = widthMatch ? widthMatch[1] : "560";
			const height = heightMatch ? heightMatch[1] : "315";

			parts.push(
				<div key={`iframe-${match.index}`} className="my-4 flex justify-center">
					<iframe
						src={src}
						width={width}
						height={height}
						frameBorder="0"
						allowFullScreen
						className="rounded-lg max-w-full"
						title="Vídeo embeddado"
					/>
				</div>
			);

			lastIndex = match.index + match[0].length;
		}

		if (lastIndex < text.length) {
			const remainingText = text.substring(lastIndex);
			if (remainingText.trim()) {
				parts.push(remainingText);
			}
		}

		if (parts.length === 0) {
			return text;
		}

		return parts;
	};

	const processedContent = processContent(content);

	const mdComponents = {
		p: ({ ...props }: React.HTMLAttributes<HTMLParagraphElement>) => <p className="mb-3 leading-relaxed" {...props} />,
		ul: ({ ...props }: React.HTMLAttributes<HTMLUListElement>) => <ul className="list-disc ml-5 mb-3" {...props} />,
		ol: ({ ...props }: React.HTMLAttributes<HTMLOListElement>) => <ol className="list-decimal ml-5 mb-3" {...props} />,
		li: ({ ...props }: React.HTMLAttributes<HTMLLIElement>) => <li className="mb-1" {...props} />,
		strong: ({ ...props }: React.HTMLAttributes<HTMLElement>) => <strong className="font-semibold" {...props} />,
		em: ({ ...props }: React.HTMLAttributes<HTMLElement>) => <em className="italic" {...props} />,
		blockquote: ({ ...props }: React.HTMLAttributes<HTMLQuoteElement>) => (
			<blockquote className="border-l-4 border-primary/30 pl-3 italic text-muted-foreground mb-3" {...props} />
		),
		hr: ({ ...props }: React.HTMLAttributes<HTMLHRElement>) => <hr className="my-4 border-border" {...props} />,
		a: ({ ...props }: React.AnchorHTMLAttributes<HTMLAnchorElement>) => (
			<a className="text-primary underline hover:text-primary/80" target="_blank" rel="noreferrer" {...props} />
		),
		h1: ({ ...props }: React.HTMLAttributes<HTMLHeadingElement>) => <h1 className="text-xl font-bold mb-3" {...props} />,
		h2: ({ ...props }: React.HTMLAttributes<HTMLHeadingElement>) => <h2 className="text-lg font-semibold mb-2" {...props} />,
		h3: ({ ...props }: React.HTMLAttributes<HTMLHeadingElement>) => <h3 className="text-base font-semibold mb-2" {...props} />,
	};

	return (
		<div>
			{Array.isArray(processedContent) ? (
				processedContent.map((part, idx) => {
					if (typeof part === "string") {
						return (
							<ReactMarkdown key={`md-${idx}`} remarkPlugins={[remarkGfm, remarkBreaks]} components={mdComponents}>
								{part}
							</ReactMarkdown>
						);
					}
					return part;
				})
			) : (
				<ReactMarkdown remarkPlugins={[remarkGfm, remarkBreaks]} components={mdComponents}>
					{processedContent}
				</ReactMarkdown>
			)}
		</div>
	);
}

function ProgressBar({ currentStep }: { currentStep: string }) {
	const currentIndex = STEPS_ORDER.indexOf(currentStep);
	const progress = currentIndex >= 0 ? ((currentIndex + 1) / STEPS_ORDER.length) * 100 : 0;

	return (
		<div className="w-full bg-secondary rounded-full h-2 mb-4">
			<div
				className="bg-primary h-2 rounded-full transition-all duration-500 ease-out"
				style={{ width: `${progress}%` }}
			/>
		</div>
	);
}

function StepIndicator({ currentStep }: { currentStep: string }) {
	const currentIndex = STEPS_ORDER.indexOf(currentStep);
	const stepLabels: Record<string, string> = {
		"t01_s1_intro": "Introdução",
		"t01_s2_video01": "Vídeo 01",
		"t01_s3_texto_abertura": "Texto de Abertura",
		"t01_s4_pergunta_abertura": "Reflexão Inicial",
		"t01_s5_competencias": "Competências",
		"t01_s6_texto_articulacao": "Articulação",
		"t01_s7_q1": "Pergunta 1/5",
		"t01_s8_q2": "Pergunta 2/5",
		"t01_s9_q3": "Pergunta 3/5",
		"t01_s10_q4": "Pergunta 4/5",
		"t01_s11_q5": "Pergunta 5/5",
		"t01_s12_video02": "Vídeo Situação-Problema",
		"t01_s13_texto_complementar": "Texto Complementar",
		"t01_s14_perguntas_video02": "Reflexão do Vídeo",
		"t01_s15_pausa_intencional": "Pausa Intencional",
		"t01_s16_escolha_caminho": "Escolha de Caminho",
		"t01_s17_video03_escolhido": "Vídeo do Caminho",
		"t01_s18_video03_outro": "Vídeo Alternativo",
		"t01_s19_reflexao_caminhos": "Reflexão Final",
		"t01_s20_conclusao_encerramento": "Conclusão",
	};

	return (
		<div className="flex items-center gap-2 text-sm text-muted-foreground mb-2">
			<span className="font-medium text-foreground">
				Etapa {currentIndex + 1} de {STEPS_ORDER.length}
			</span>
			<span>•</span>
			<span>{stepLabels[currentStep] || currentStep}</span>
		</div>
	);
}

function AssistantBubble({ children }: { children: React.ReactNode }) {
	return (
		<div className="flex items-start gap-3">
			<Avatar label="AI" />
			<div className="max-w-[85ch] md:max-w-[75%] rounded-2xl border border-border bg-card px-4 py-3 text-sm shadow-sm">
				{children}
			</div>
		</div>
	);
}

function UserBubble({ children }: { children: React.ReactNode }) {
	return (
		<div className="flex items-start gap-3 justify-end">
			<div className="max-w-[85ch] md:max-w-[75%] rounded-2xl bg-primary text-primary-foreground px-4 py-3 text-sm shadow">
				{children}
			</div>
			<Avatar label="Você" color="bg-secondary text-secondary-foreground" />
		</div>
	);
}

// ══════════════════════════════════════════════════════════════
// ADK API Helper
// ══════════════════════════════════════════════════════════════

const APP_NAME = "tutor_docente";
const USER_ID = "web_user";

// Gerar session ID único
function generateSessionId(): string {
	return `session_${Date.now()}_${Math.random().toString(36).substring(2, 11)}`;
}

// Criar sessão no ADK
async function createSession(sessionId: string): Promise<boolean> {
	try {
		const response = await fetch(`/apps/${APP_NAME}/users/${USER_ID}/sessions`, {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ session_id: sessionId }),
		});
		
		if (response.ok) {
			console.log("Session created:", sessionId);
			return true;
		}
		
		const data = await response.json();
		console.log("Create session response:", data);
		
		// Se a sessão já existe, tudo bem
		if (response.status === 500 && data.detail?.includes("UNIQUE constraint")) {
			console.log("Session already exists:", sessionId);
			return true;
		}
		
		return false;
	} catch (e) {
		console.error("Error creating session:", e);
		return false;
	}
}

// Enviar mensagem via /run
async function sendMessageToADK(sessionId: string, message: string): Promise<string> {
	const response = await fetch(`/run`, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({
			app_name: APP_NAME,
			user_id: USER_ID,
			session_id: sessionId,
			new_message: {
				role: "user",
				parts: [{ text: message }]
			},
		}),
	});
	
	if (!response.ok) {
		const errorText = await response.text();
		console.error("ADK Error Response:", errorText);
		throw new Error(`Erro HTTP ${response.status}: ${errorText}`);
	}
	
	const data = await response.json();
	console.log("ADK Response:", data);
	
	// Extrair texto da resposta do ADK
	// O formato é um array de eventos: [{ content: { parts: [{ text: "..." }] } }]
	let fullResponse = '';
	
	if (Array.isArray(data)) {
		for (const event of data) {
			if (event.content?.parts) {
				for (const part of event.content.parts) {
					if (part.text) {
						fullResponse += part.text;
					}
				}
			}
		}
	} else if (data.events && Array.isArray(data.events)) {
		for (const event of data.events) {
			if (event.content?.parts) {
				for (const part of event.content.parts) {
					if (part.text) {
						fullResponse += part.text;
					}
				}
			}
		}
	}
	
	// Fallback para outros formatos
	if (!fullResponse) {
		if (data.response) fullResponse = data.response;
		else if (data.text) fullResponse = data.text;
		else if (data.output) fullResponse = data.output;
	}
	
	return fullResponse || "Não foi possível obter resposta.";
}

// ══════════════════════════════════════════════════════════════
// Main App
// ══════════════════════════════════════════════════════════════

export default function App() {
	// State
	const [sessionId, setSessionId] = React.useState<string>("");
	const [sessionReady, setSessionReady] = React.useState(false);
	const [messages, setMessages] = React.useState<Message[]>([]);
	const [stepId, setStepId] = React.useState<string>(STEPS_ORDER[0]);
	const [chatState, setChatState] = React.useState<ChatState>({});
	const [pending, setPending] = React.useState(false);

	const inputRef = React.useRef<HTMLInputElement>(null);
	const scrollRef = React.useRef<HTMLDivElement>(null);

	// Inicializar sessão
	React.useEffect(() => {
		async function initSession() {
			// Gerar novo session ID (sempre criar nova sessão)
			const newSessionId = generateSessionId();
			setSessionId(newSessionId);
			
			// Criar sessão no ADK
			const created = await createSession(newSessionId);
			
			if (created) {
				setSessionReady(true);
				// Enviar mensagem inicial para começar a trilha
				sendMessageWithSession(newSessionId, "Olá, quero começar a trilha de formação.", true);
			} else {
				console.error("Failed to create session");
			}
		}
		
		initSession();
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, []);

	// Auto-scroll
	React.useEffect(() => {
		if (scrollRef.current) {
			scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
		}
	}, [messages, pending]);

	// Detectar escolha de caminho A/B
	function detectPathChoice(message: string): "A" | "B" | null {
		const msg = message.trim().toUpperCase();
		if (["A", "CAMINHO A", "OPÇÃO A", "ESCOLHO A"].includes(msg)) return "A";
		if (["B", "CAMINHO B", "OPÇÃO B", "ESCOLHO B"].includes(msg)) return "B";
		
		const msgLower = message.toLowerCase();
		if (msgLower.includes("inclusão solidária") || msgLower.includes("inclusao solidaria")) return "A";
		if (msgLower.includes("protagonismo ativo")) return "B";
		
		return null;
	}

	// Enviar mensagem com session ID específico
	async function sendMessageWithSession(sid: string, message: string, isInit = false) {
		if (!isInit) {
			setMessages(prev => [...prev, { role: "user" as const, content: message }]);
		}
		
		setPending(true);

		// Detectar escolha de caminho
		if (stepId === "t01_s16_escolha_caminho" && !isInit) {
			const choice = detectPathChoice(message);
			if (choice) {
				setChatState(prev => ({ ...prev, caminho_escolhido: choice }));
			}
		}

		try {
			const responseText = await sendMessageToADK(sid, message);
			
			const assistantMessage: Message = { role: "assistant", content: responseText };
			setMessages(prev => [...prev, assistantMessage]);

		} catch (e) {
			console.error("Falha ao gerar resposta:", e);
			setMessages(prev => [
				...prev,
				{ role: "assistant", content: "Desculpe, ocorreu um erro ao gerar a resposta. Tente novamente." },
			]);
		} finally {
			setPending(false);
		}
	}

	// Enviar mensagem usando session ID do estado
	async function sendMessage(message: string) {
		if (!sessionId || !sessionReady) {
			console.error("Session not ready");
			return;
		}
		await sendMessageWithSession(sessionId, message, false);
	}

	// Submit handler
	function handleSubmit(e: React.FormEvent) {
		e.preventDefault();
		const value = (inputRef.current?.value || "").trim();
		if (!value || pending || !sessionReady) return;
		if (inputRef.current) inputRef.current.value = "";
		
		sendMessage(value);
	}

	// Reiniciar sessão
	function handleResetSession() {
		window.location.reload();
	}

	return (
		<div className="min-h-screen flex flex-col bg-background">
			<Navbar />
			
			<main className="flex-1 mx-auto max-w-5xl w-full px-4 py-6">
				{/* Progress & Step Indicator */}
				<div className="mb-6">
					<StepIndicator currentStep={stepId} />
					<ProgressBar currentStep={stepId} />
				</div>

				{/* Chat Container */}
				<div className="rounded-2xl border bg-card shadow-sm">
					{/* Messages */}
					<div
						ref={scrollRef}
						className="h-[60vh] overflow-y-auto p-4 space-y-4"
					>
						{!sessionReady && (
							<AssistantBubble>
								<div className="flex items-center gap-2">
									<Loader2 className="w-4 h-4 animate-spin" />
									<span className="text-muted-foreground">Conectando ao tutor...</span>
								</div>
							</AssistantBubble>
						)}
						{messages.map((m, idx) =>
							m.role === "user" ? (
								<UserBubble key={idx}>{m.content}</UserBubble>
							) : (
								<AssistantBubble key={idx}>
									<MarkdownWithVideos content={m.content} />
								</AssistantBubble>
							)
						)}
						{pending && (
							<AssistantBubble>
								<div className="flex items-center gap-2">
									<Loader2 className="w-4 h-4 animate-spin" />
									<span className="text-muted-foreground">Pensando...</span>
								</div>
							</AssistantBubble>
						)}
					</div>

					{/* Input Area */}
					<div className="border-t p-4 bg-card rounded-b-2xl">
						<form onSubmit={handleSubmit} className="flex items-center gap-3">
							<input
								ref={inputRef}
								type="text"
								placeholder={sessionReady ? "Digite sua mensagem..." : "Aguarde..."}
								className="flex-1 h-11 rounded-full border px-4 text-sm shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring bg-background"
								disabled={pending || !sessionReady}
							/>
							<button
								type="submit"
								disabled={pending || !sessionReady}
								className="inline-flex items-center justify-center h-11 w-11 rounded-full bg-primary text-primary-foreground hover:bg-primary/90 disabled:opacity-50 transition-colors"
							>
								{pending ? (
									<Loader2 className="w-4 h-4 animate-spin" />
								) : (
									<Send className="w-4 h-4" />
								)}
							</button>
						</form>
					</div>
				</div>

				{/* State info & Reset button */}
				<div className="mt-4 flex items-center justify-between">
					{chatState.caminho_escolhido && (
						<div className="text-xs text-muted-foreground">
							Caminho escolhido: {chatState.caminho_escolhido === "A" ? "Inclusão Solidária" : "Protagonismo Ativo"}
						</div>
					)}
					<button
						onClick={handleResetSession}
						className="text-xs text-muted-foreground hover:text-foreground underline ml-auto"
					>
						Reiniciar trilha
					</button>
				</div>
			</main>

			<Footer />
		</div>
	);
}
