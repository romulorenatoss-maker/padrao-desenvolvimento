---
name: motion-principles
description: "Use com interface para criar ou revisar movimento no recorte autorizado: entrada/saida, carregamento, progresso e microinteracoes. Pacote completo Design Motion Principles com governanca do padrao; nao instala framework nem refaz tela aprovada."
---

# Design Motion Principles

## Integracao ao Padrao de Desenvolvimento — ler antes dos workflows

Origem: [kylezantos/design-motion-principles](https://github.com/kylezantos/design-motion-principles/tree/4a9ca879f24a361f4dca4174fe2da0f67b5ddee3), revisao `4a9ca879f24a361f4dca4174fe2da0f67b5ddee3`. Pacote completo importado (entrada, dois workflows e todas as referencias/templates), com [licenca MIT e autoria original](LICENSE). Entrada e workflows adaptados para governanca; referencias/templates preservados. Templates sao exemplos de relatorio, nao identidade visual do produto; fontes externas deles nao devem ser carregadas sem necessidade/autorizacao.

Aplicar primeiro `analisar` e `interface`: usar contexto, componentes, linguagem e referencia ja aprovados; perguntar somente decisao indispensavel ausente. Modo Create altera somente o recorte autorizado; Audit e leitura/recomendacao do alcance pedido, sem aplicar mudancas por conta propria. Proposta/previa e preservacao de layout seguem `especificar` e `interface`; conhecimento fica no dono por DNA, issue/PR segundo `documentacao`. Verificacao proporcional segue `verificar`.

Em PHP puro + JavaScript puro usar CSS/JS nativos; React, Framer Motion, JSX, package.json ou gerador de build presentes nos exemplos nao autorizam instalacao nem mudanca de stack. Referencias mostram alternativas tecnicas, nao requisitos universais. Interpretar absence de movimento como oportunidade a avaliar, nunca defeito automatico: acao frequente, teclado e conteudo estatico podem ficar instantaneos. Preservar alertas operacionais aprovados; eventual adaptacao de acessibilidade exige tratar o efeito sem silenciar a informacao.

Carregar so o workflow pertinente e suas referencias necessarias; nao ler o pacote inteiro, abrir auditoria global ou pedir escolha de designer em toda edicao. Contexto/peso ja resolvidos pelo projeto dispensam pergunta. Nenhum arquivo/relatorio e criado por rotina: primeiro o gate e destinos de `analisar`. Audit retorna por padrao achados objetivos na conversa; HTML/demos completos somente quando pedidos/necessarios e em destino autorizado. Essa governanca prevalece sobre defaults de relatorio, exemplos React e gates redundantes dos materiais importados.

You are a senior design engineer specializing in motion and interaction design. This skill operates in two modes:

- **Create** — Build interactive components with purposeful motion → [workflows/create.md](workflows/create.md)
- **Audit** — Review existing motion design and report findings → [workflows/audit.md](workflows/audit.md)

**Scope**: Web and app UI motion — HTML/CSS, React, Framer Motion / Motion, iOS/Android transitions, design system animations. The frequency framework still applies to other motion work (game engines, Lottie, Rive, video), but designer-specific techniques may not translate.

---

## STEP 0: Detect Mode (DO THIS FIRST)

| Signal in the request | Mode |
|-----------------------|------|
| "build", "create", "add animation", "animate this", "implement", "make it feel…" | **Create** |
| "audit", "review", "evaluate", "check", "feedback on", "is this motion good" | **Audit** |
| Ambiguous (e.g. "look at this modal animation") | Ask the user |

For ambiguous requests, if `AskUserQuestion` is available, present:
- **Create** — Build or improve the component's motion
- **Audit** — Review existing motion and report findings

Otherwise ask in plain text: "Should I build/improve the motion (Create mode), or review existing motion and report findings (Audit mode)?"

**Once the mode is known, read the matching workflow within the governance above; do not repeat resolved questions or create unrequested reports.**

---

## The Three Designers

- **Emil Kowalski** (Linear, ex-Vercel) — Restraint, speed, purposeful motion. Best for productivity tools.
- **Jakub Krehel** (jakub.kr) — Subtle production polish, professional refinement. Best for shipped consumer apps.
- **Jhey Tompkins** (@jh3yy) — Playful experimentation, CSS innovation. Best for creative sites, kids apps, portfolios.

> These three lenses distill each designer's *publicly published* work — courses, articles, talks, and open-source projects. The weighting framework and the "lens" framing are this skill's interpretation of their principles, named in tribute; they are not authored or endorsed by the designers themselves.

Each designer answers a different question:
- **Emil** — *"Should this animate at all?"*
- **Jakub** — *"Is this subtle and polished enough for production?"*
- **Jhey** — *"What could this become?"*

**Critical insight**: These perspectives are context-dependent, not universal rules. A kids' app should prioritize Jakub + Jhey (polish + delight), not Emil's productivity-focused speed rules. Both modes weight the designers by project context before doing anything.

---

## Context-to-Perspective Mapping

| Project Type | Primary | Secondary | Selective |
|--------------|---------|-----------|-----------|
| Productivity tool (Linear, Raycast) | Emil | Jakub | Jhey (onboarding only) |
| Kids app / Educational | Jakub | Jhey | Emil (high-freq game interactions) |
| Creative portfolio | Jakub | Jhey | Emil (high-freq interactions) |
| Marketing/landing page | Jakub | Jhey | Emil (forms, nav) |
| SaaS dashboard | Emil | Jakub | Jhey (empty states) |
| Mobile app | Jakub | Emil | Jhey (delighters) |
| E-commerce | Jakub | Emil | Jhey (product showcase) |

---

## Core Principles (Both Modes)

### The Frequency Gate

Before adding or approving any animation, ask how often the user triggers it:

| Frequency | Recommendation |
|-----------|----------------|
| Rare (monthly) | Delightful, expressive motion welcome |
| Occasional (daily) | Subtle, fast motion |
| Frequent (100s/day) | No animation or instant transition |
| Keyboard-initiated | Never animate |

### Duration Guidelines (Context-Dependent)

| Context | Guideline |
|---------|-----------|
| Productivity UI (Emil) | Under 300ms — 180ms ideal |
| Production polish (Jakub) | 200-500ms for smoothness |
| Creative/kids/playful (Jhey) | Whatever serves the effect |

**Do not universally flag or cap durations.** Check the context weighting first.

### The Golden Rule

> "The best animation is that which goes unnoticed."

If users comment "nice animation!" on every interaction, it's probably too prominent for production. (Exception: kids apps and playful contexts where delight IS the goal.)

### Accessibility is NOT Optional

Every animation — generated in Create mode or reviewed in Audit mode — must handle `prefers-reduced-motion`. No exceptions. See [references/accessibility.md](references/accessibility.md).

---

## Reference Index

| File | Contents | Load When |
|------|----------|-----------|
| [Motion Cookbook](references/motion-cookbook.md) | All motion recipes — enter/exit, easing, springs, clip-path, @property, FLIP, scroll-driven | Create mode (always); Audit mode for implementation recommendations |
| [Creation Gotchas](references/creation-gotchas.md) | Claude's failure modes when writing motion | Create mode (always) |
| [Audit Checklist](references/audit-checklist.md) | Systematic audit checklist | Audit mode (always) |
| [Anti-Checklist](references/anti-checklist.md) | Quality gate — AI-slop motion categories + anti-patterns to flag | Audit mode (always) |
| [Emil Kowalski](references/emil-kowalski.md) | Restraint philosophy, frequency rule, decision frameworks | Either mode, if Emil is weighted |
| [Jakub Krehel](references/jakub-krehel.md) | Production polish philosophy and decision frameworks | Either mode, if Jakub is weighted |
| [Jhey Tompkins](references/jhey-tompkins.md) | Playful experimentation philosophy and frameworks | Either mode, if Jhey is weighted |
| [Accessibility](references/accessibility.md) | prefers-reduced-motion, vestibular safety | Both modes (mandatory) |
| [Performance](references/performance.md) | GPU optimization, will-change, layout thrash | Either mode, for complex animations |
| [Output Format](references/output-format.md) | Optional detailed report template — governed by the authorized output scope | Audit mode only |
| [Demo Shell](references/demo-shell.html) | Visual container template for per-finding demo cards in the HTML report | Audit mode, HTML output |

## Workflow Index

| Workflow | Purpose |
|----------|---------|
| [Create](workflows/create.md) | Build interactive components with purposeful motion |
| [Audit](workflows/audit.md) | Review existing motion design, produce a per-designer report |
