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
	caminho_escolhido?: "A" | "B" | null;
	completed_steps?: string[];
	lesson_completed?: boolean;
}

interface ChatResponse {
	reply: string;
	step_id: string;
	next_step_id: string | null;
	state: ChatState | null;
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

// Steps que são apenas conteúdo (sem pergunta que exige resposta elaborada)
// Nota: Mantido para referência, mas o botão "Continuar" foi removido
const CONTENT_ONLY_STEPS = [
	"t01_s2_video01",
	"t01_s3_texto_abertura",
	"t01_s5_competencias",
	"t01_s6_texto_articulacao",
	"t01_s12_video02",
	"t01_s13_texto_complementar",
	"t01_s15_pausa_intencional",
	"t01_s17_video03_escolhido",
	"t01_s18_video03_outro",
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
	// Processar iframes embeddados no conteúdo
	const processContent = (text: string) => {
		// Regex para encontrar iframes no formato HTML
		const iframeRegex = /<iframe([^>]*)><\/iframe>/gi;
		const parts: (string | JSX.Element)[] = [];
		let lastIndex = 0;
		let match;

		while ((match = iframeRegex.exec(text)) !== null) {
			// Adicionar texto antes do iframe
			if (match.index > lastIndex) {
				const beforeText = text.substring(lastIndex, match.index);
				if (beforeText.trim()) {
					parts.push(beforeText);
				}
			}

			// Extrair atributos do iframe
			const attrs = match[1];
			const srcMatch = attrs.match(/src=["']([^"']+)["']/);
			const widthMatch = attrs.match(/width=["']?(\d+)["']?/);
			const heightMatch = attrs.match(/height=["']?(\d+)["']?/);

			const src = srcMatch ? srcMatch[1] : "https://example.com/video-placeholder";
			const width = widthMatch ? widthMatch[1] : "560";
			const height = heightMatch ? heightMatch[1] : "315";

			// Adicionar iframe como elemento React
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

		// Adicionar texto restante
		if (lastIndex < text.length) {
			const remainingText = text.substring(lastIndex);
			if (remainingText.trim()) {
				parts.push(remainingText);
			}
		}

		// Se não encontrou iframes, retornar conteúdo original
		if (parts.length === 0) {
			return text;
		}

		return parts;
	};

	const processedContent = processContent(content);

	return (
		<div>
			{Array.isArray(processedContent) ? (
				processedContent.map((part, idx) => {
					if (typeof part === "string") {
						return (
							<ReactMarkdown
								key={`md-${idx}`}
								remarkPlugins={[remarkGfm, remarkBreaks]}
								components={{
									p: ({ ...props }) => <p className="mb-3 leading-relaxed" {...props} />,
									ul: ({ ...props }) => <ul className="list-disc ml-5 mb-3" {...props} />,
									ol: ({ ...props }) => <ol className="list-decimal ml-5 mb-3" {...props} />,
									li: ({ ...props }) => <li className="mb-1" {...props} />,
									strong: ({ ...props }) => <strong className="font-semibold" {...props} />,
									em: ({ ...props }) => <em className="italic" {...props} />,
									blockquote: ({ ...props }) => (
										<blockquote className="border-l-4 border-primary/30 pl-3 italic text-muted-foreground mb-3" {...props} />
									),
									hr: ({ ...props }) => <hr className="my-4 border-border" {...props} />,
									a: ({ ...props }) => (
										<a className="text-primary underline hover:text-primary/80" target="_blank" rel="noreferrer" {...props} />
									),
									h1: ({ ...props }) => <h1 className="text-xl font-bold mb-3" {...props} />,
									h2: ({ ...props }) => <h2 className="text-lg font-semibold mb-2" {...props} />,
									h3: ({ ...props }) => <h3 className="text-base font-semibold mb-2" {...props} />,
								}}
							>
								{part}
							</ReactMarkdown>
						);
					}
					return part;
				})
			) : (
				<ReactMarkdown
					remarkPlugins={[remarkGfm, remarkBreaks]}
					components={{
						p: ({ ...props }) => <p className="mb-3 leading-relaxed" {...props} />,
						ul: ({ ...props }) => <ul className="list-disc ml-5 mb-3" {...props} />,
						ol: ({ ...props }) => <ol className="list-decimal ml-5 mb-3" {...props} />,
						li: ({ ...props }) => <li className="mb-1" {...props} />,
						strong: ({ ...props }) => <strong className="font-semibold" {...props} />,
						em: ({ ...props }) => <em className="italic" {...props} />,
						blockquote: ({ ...props }) => (
							<blockquote className="border-l-4 border-primary/30 pl-3 italic text-muted-foreground mb-3" {...props} />
						),
						hr: ({ ...props }) => <hr className="my-4 border-border" {...props} />,
						a: ({ ...props }) => (
							<a className="text-primary underline hover:text-primary/80" target="_blank" rel="noreferrer" {...props} />
						),
						h1: ({ ...props }) => <h1 className="text-xl font-bold mb-3" {...props} />,
						h2: ({ ...props }) => <h2 className="text-lg font-semibold mb-2" {...props} />,
						h3: ({ ...props }) => <h3 className="text-base font-semibold mb-2" {...props} />,
					}}
				>
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

// Botão Continuar removido - transições agora são feitas via mensagens de texto

// ══════════════════════════════════════════════════════════════
// Main App
// ══════════════════════════════════════════════════════════════

export default function App() {
	// Normalizar URL da API
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

	const API_BASE = normalizeApiBase((import.meta as any).env?.VITE_API_URL);

	// State
	const [messages, setMessages] = React.useState<Message[]>([]);
	const [stepId, setStepId] = React.useState<string>(STEPS_ORDER[0]);
	const [chatState, setChatState] = React.useState<ChatState>({});
	const [pending, setPending] = React.useState(false);
	const [initialized, setInitialized] = React.useState(false);

	const inputRef = React.useRef<HTMLInputElement>(null);
	const scrollRef = React.useRef<HTMLDivElement>(null);

	// Auto-scroll
	React.useEffect(() => {
		if (scrollRef.current) {
			scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
		}
	}, [messages, pending]);

	// Iniciar o trilho automaticamente
	React.useEffect(() => {
		if (!initialized) {
			setInitialized(true);
			sendMessage("Iniciar", true);
		}
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [initialized]);

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

	// Enviar mensagem
	async function sendMessage(message: string, isInit = false) {
		const newMessages: Message[] = isInit 
			? [] 
			: [...messages, { role: "user" as const, content: message }];
		
		if (!isInit) {
			setMessages(newMessages);
		}
		
		setPending(true);

		// Detectar escolha de caminho
		let updatedState = { ...chatState };
		if (stepId === "t01_s16_escolha_caminho" && !isInit) {
			const choice = detectPathChoice(message);
			if (choice) {
				updatedState.caminho_escolhido = choice;
				setChatState(updatedState);
			}
		}

		try {
			const resp = await fetch(`${API_BASE}/api/chat`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({
					lesson_id: "1",
					step_id: stepId,
					messages: isInit ? [] : newMessages,
					state: updatedState,
				}),
			});

			const data: ChatResponse = await resp.json();

			if (!resp.ok) {
				console.error("/api/chat error:", { status: resp.status, data });
				throw new Error((data as any).detail || `Erro HTTP ${resp.status}`);
			}

			// Atualizar mensagens
			const assistantMessage: Message = { role: "assistant", content: data.reply };
			setMessages((prev) => [...prev, assistantMessage]);

			// Atualizar state se retornado
			if (data.state) {
				setChatState(data.state);
			}

			// Detectar se o usuário está pronto para avançar para a próxima etapa
			// O modelo pergunta "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
			// E detecta palavras-chave como "sim", "pode prosseguir", "continuar", etc.
			if (!isInit) {
				const readyToAdvance = detectReadyToAdvance(message, data.reply);
				if (readyToAdvance && data.next_step_id && stepId !== data.next_step_id) {
					setStepId(data.next_step_id);
					// Enviar mensagem vazia para iniciar o próximo step
					setTimeout(() => {
						sendMessage("", true);
					}, 100);
				}
			}

		} catch (e) {
			console.error("Falha ao gerar resposta:", e);
			setMessages((prev) => [
				...prev,
				{ role: "assistant", content: "Desculpe, ocorreu um erro ao gerar a resposta. Tente novamente." },
			]);
		} finally {
			setPending(false);
		}
	}

	// Detectar se o usuário está pronto para avançar
	function detectReadyToAdvance(userMessage: string, assistantReply: string): boolean {
		if (!userMessage) return false;
		
		const message = userMessage.toLowerCase().trim();
		const readyKeywords = [
			"sim", "pode prosseguir", "continuar", "próxima etapa", "sem dúvidas",
			"pode seguir", "vamos em frente", "ok", "tudo certo", "pode continuar",
			"sem dúvida", "pode avançar", "vamos", "próximo", "próxima"
		];
		
		// Verificar se a resposta do assistente contém a pergunta de transição
		const hasTransitionQuestion = assistantReply.includes("Você tem alguma dúvida sobre esta etapa ou podemos prosseguir");
		
		// Se tem a pergunta de transição e o usuário respondeu com palavras-chave de prontidão
		if (hasTransitionQuestion) {
			return readyKeywords.some(keyword => message.includes(keyword));
		}
		
		return false;
	}

	// Submit handler
	function handleSubmit(e: React.FormEvent) {
		e.preventDefault();
		const value = (inputRef.current?.value || "").trim();
		if (!value || pending) return;
		if (inputRef.current) inputRef.current.value = "";
		
		sendMessage(value);
	}

	const isLastStep = stepId === STEPS_ORDER[STEPS_ORDER.length - 1];

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
						{/* Form de input */}
						<form onSubmit={handleSubmit} className="flex items-center gap-3">
							<input
								ref={inputRef}
								type="text"
								placeholder="Digite sua mensagem..."
								className="flex-1 h-11 rounded-full border px-4 text-sm shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring bg-background"
								disabled={pending}
							/>
							<button
								type="submit"
								disabled={pending}
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

				{/* State info (debug - remover em produção) */}
				{chatState.caminho_escolhido && (
					<div className="mt-4 text-xs text-muted-foreground text-center">
						Caminho escolhido: {chatState.caminho_escolhido === "A" ? "Inclusão Solidária" : "Protagonismo Ativo"}
					</div>
				)}
			</main>

			<Footer />
		</div>
	);
}
