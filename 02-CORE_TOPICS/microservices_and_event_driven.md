# Microservices and Event-Driven Architecture

## Architecture Design Principles

- Decompose services by business capability, not technical layers
- Keep ownership boundaries clear: code, data, and runtime accountability
- Prefer asynchronous communication for resilience and decoupling
- Design for failure: retries, timeouts, circuit breaking, fallback

## Common Interview Scenarios

### Scenario 1: Monolith to Microservices

Answer approach:
- Start with bounded context identification
- Prioritize extraction by business value and risk
- Introduce API gateway and anti-corruption layer
- Apply strangler pattern and phased cutover
- Include observability and operational readiness

### Scenario 2: High-Throughput Order Processing

Answer approach:
- Use command/query separation where appropriate
- Implement outbox pattern for reliable event publishing
- Ensure idempotent consumers and deduplication keys
- Introduce saga for distributed transaction orchestration

## .NET / .NET Core Discussion Points

- Clean architecture for testability and separation of concerns
- Dependency inversion and interface-driven domain boundaries
- Vertical slice architecture for feature ownership
- Resiliency middleware (Polly policies, retries, bulkheads)
- Structured logging + distributed tracing standards

## Event-Driven Patterns to Mention

- Pub/sub for domain and integration events
- Event sourcing only when clear audit/replay need exists
- CQRS when read/write scalability and model separation are required
- Dead-letter queues and replay pipelines for recovery

## Pitfalls to Avoid in Answers

- Over-splitting services too early
- Ignoring data consistency semantics
- No strategy for observability and operations
- Treating async as "eventual correctness" without controls

