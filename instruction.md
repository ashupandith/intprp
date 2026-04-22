# Permanent Content Instructions

Use this file as the default standard for all topic pages and question answers in this repository.

## Documentation Quality Standard

Every topic page must be deep, structured, and self-contained. Content should read like Microsoft Learn style technical documentation adapted for senior architect interviews.

Required sections (detailed, not shallow):
- Overview
- Why this topic matters
- Core concepts
- Detailed explanation of each concept
- Evaluation (how to assess design quality)
- Architecture / flow diagram + flow explanation
- Real-world example
- Best practices
- Common mistakes / misconceptions
- Industry relevance
- Interview discussion points
- Related/dependent links

## Depth Expectations

- Each section should explain both architecture reasoning and operational impact.
- Include trade-offs, governance implications, and real-world failure patterns.
- Explain how the topic connects to security, cost, reliability, and delivery speed.
- Keep explanations practical and interview-useful.
- Do not stop at definitions; explain when to use, when not to use, and why.
- Every deep explanation must include decision criteria, risks, mitigations, and production implications.
- Prefer scenario-driven explanation style over generic statements.
- Mention measurable architecture signals where relevant (latency, RTO/RPO, cost, blast radius, failure rate).

## Question Answer Format (Mandatory)

For every question in every topic file, use this exact structure:

1. Question summary (1-2 lines that clarifies what interviewer is testing)  
2. Crisp answer (7-8 lines, speakable in 30-60 seconds)  
3. Deep explanation (rich paragraph style with architecture flow, trade-offs, risks, mitigations, and operations impact)  
4. Answer summary (minimum 3 strong bullet points; include decision, risk, mitigation)  
5. Practical example (real enterprise scenario, not generic)  
6. Simple diagram (mermaid or text flow)  
7. Trusted reference links

## Writing Constraints

- Do not use numbered line-style explanations in deep answer sections.
- Keep crisp answers concise and speakable in interviews.
- Keep deep explanations detailed and architecture-oriented.
- Deep explanation must include practical scenario context, trade-offs, and decision criteria.
- Use plain, professional language.
- Avoid generic one-line bullets for complex sections.
- Answer summary must be multi-line with concise actionable takeaways.
- Add at least one practical example for every answer.
- Diagram explanation should describe control points and fallback path where relevant.
- Avoid shallow textbook phrasing; use senior-architect decision language.
- Include explicit trade-off framing in answers (speed vs control, cost vs resilience, centralization vs autonomy).

## Priority Topic Order (Current)

### Most important
- Azure Landing Zone
- Hub-spoke networking
- ExpressRoute / VPN / peering / private endpoints
- Azure Firewall + NVA integration
- Migration strategies + Azure Migrate
- Entra ID / RBAC / Policy / governance
- Terraform + Bicep
- HA/DR
- TCO / OLA

### Second priority
- Documentation and blueprinting
- Stakeholder workshops
- Delivery governance
- Operational readiness
- Cost optimization

### Third priority
- Advanced compliance discussions
- Multi-region enterprise design patterns
- Complex hybrid scenarios

## Execution Mode

- Continue automatically across all files and all questions unless explicitly told to stop.
- Complete one topic file fully (all 50 questions) before moving to next topic file.
- Preserve consistent formatting across all topic files.
- Do NOT ask repetitive continuation prompts such as "Should I proceed to next question?"
- Default behavior: proceed to next question automatically.
- After finishing all 50 questions of current topic, automatically move to next topic file.
- Ask for confirmation only if there is a blocker, conflict, or ambiguity that prevents safe progress.
