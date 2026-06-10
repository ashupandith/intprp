# Interview Question Bank

# .NET 10 Interview Questions


## 01 .NET 10 Overview & Platform

1. What is .NET 10, and how is it different from .NET Framework?
2. Why is .NET 10 important for modern enterprise application development?
3. What are the major runtime improvements introduced in .NET 10?
4. How does .NET 10 improve performance compared with earlier .NET versions?
5. What does LTS mean in the context of .NET releases?
6. How do you decide whether to migrate an application to .NET 10?
7. What compatibility checks would you perform before upgrading to .NET 10?
8. What is the difference between .NET SDK, runtime, and hosting bundle?
9. How do you check the installed .NET SDK version?
10. What is the role of global.json in .NET projects?
11. How does .NET support cross-platform application development?
12. What are the major application types you can build with .NET 10?
13. What is the difference between .NET runtime and CoreCLR?
14. What is the role of Base Class Library in .NET?
15. How does .NET 10 support cloud-native development?
16. What is NativeAOT and when would you use it?
17. What are the risks of NativeAOT in enterprise applications?
18. What is trimming in .NET and why is it useful?
19. How do you handle breaking changes during .NET migration?
20. How would you explain .NET 10 to a non-technical stakeholder?

## 02 C# 14 Language Features

21. What are the important C# language features used with .NET 10?
22. What is the difference between record, class, and struct?
23. How do init-only properties improve immutability?
24. What are required properties in C#?
25. What is pattern matching in C# and where do you use it?
26. Explain switch expressions with a practical example.
27. What are nullable reference types and why are they important?
28. How do you handle nullable warnings in production code?
29. What is the difference between var, dynamic, and object?
30. What is the purpose of using statements and using declarations?
31. How do extension methods work in C#?
32. What are extension members and why are they useful?
33. What are collection expressions in modern C#?
34. What is the difference between primary constructors and normal constructors?
35. How does C# support functional-style programming?
36. What are lambdas and expression-bodied members?
37. What is the difference between Func, Action, and Predicate?
38. What is tuple deconstruction in C#?
39. How do you write clean and maintainable C# code?
40. What C# features help reduce boilerplate code?

## 03 ASP.NET Core Fundamentals

41. What is ASP.NET Core?
42. What is the ASP.NET Core request pipeline?
43. What is middleware in ASP.NET Core?
44. How do you create custom middleware?
45. What is the difference between Use, Run, and Map middleware?
46. What is endpoint routing?
47. What is the role of Program.cs in minimal hosting model?
48. What is dependency injection in ASP.NET Core?
49. What are the default services registered in ASP.NET Core?
50. What is the difference between appsettings.json and environment variables?
51. How do you manage configuration in ASP.NET Core?
52. What is IWebHostEnvironment used for?
53. What are filters in ASP.NET Core MVC?
54. What is model binding?
55. What is model validation?
56. What is the difference between controller-based API and minimal API?
57. When would you choose minimal APIs?
58. How do you handle global errors in ASP.NET Core?
59. What is ProblemDetails in ASP.NET Core?
60. How do you structure a production-ready ASP.NET Core application?

## 04 Web API Design

61. What are REST principles?
62. What is the difference between REST and RPC-style APIs?
63. How do you design resource-based URLs?
64. What are correct HTTP methods for CRUD operations?
65. What is the difference between PUT and PATCH?
66. What are idempotent HTTP methods?
67. How do you design API versioning?
68. What is content negotiation?
69. What status code would you return for validation failure?
70. What status code would you return for unauthorized access?
71. What is the difference between 401 and 403?
72. How do you design pagination in APIs?
73. How do you implement filtering and sorting in APIs?
74. What is HATEOAS and do you use it in enterprise APIs?
75. How do you handle correlation IDs in APIs?
76. What is OpenAPI/Swagger?
77. How do you secure Swagger in production?
78. How do you design APIs for backward compatibility?
79. What is rate limiting and where do you implement it?
80. What makes an API production-ready?

## 05 Dependency Injection & Lifetimes

81. What is dependency injection?
82. What problem does dependency injection solve?
83. What is the difference between constructor injection and property injection?
84. What are Singleton, Scoped, and Transient lifetimes?
85. When should you use Singleton lifetime?
86. When should you use Scoped lifetime?
87. When should you use Transient lifetime?
88. What happens if a Singleton service depends on a Scoped service?
89. How do you resolve services manually using IServiceProvider?
90. What is IServiceScopeFactory?
91. How do you register generic services?
92. How do you register multiple implementations of the same interface?
93. What is keyed service registration?
94. How do you test services that use dependency injection?
95. What is the service locator anti-pattern?
96. How do you avoid circular dependencies?
97. How do you inject configuration options?
98. What is the Options pattern?
99. What is IOptionsMonitor?
100. How do you design DI for clean architecture?

## 06 EF Core & Dapper

101. What is Entity Framework Core?
102. What is Dapper?
103. What is the difference between EF Core and Dapper?
104. When would you use Dapper instead of EF Core?
105. When would you use EF Core instead of Dapper?
106. What is change tracking in EF Core?
107. What is AsNoTracking and why is it useful?
108. What is DbContext lifetime best practice?
109. What is migration in EF Core?
110. How do you handle database transactions in EF Core?
111. How do you handle transactions with Dapper?
112. What is lazy loading and why can it be dangerous?
113. What is eager loading?
114. What is explicit loading?
115. What is the N+1 query problem?
116. How do you optimize EF Core queries?
117. How do you execute stored procedures using Dapper?
118. How do you prevent SQL injection with Dapper?
119. How do you implement repository pattern with EF Core or Dapper?
120. How do you choose between ORM and raw SQL in architecture?

## 07 Authentication & Authorization

121. What is authentication?
122. What is authorization?
123. What is JWT?
124. What are the parts of a JWT token?
125. What is OAuth 2.0?
126. What is OpenID Connect?
127. What is the difference between access token and ID token?
128. What is refresh token rotation?
129. What is token validation in ASP.NET Core?
130. How do you configure JWT bearer authentication?
131. What are claims?
132. What are roles?
133. What is policy-based authorization?
134. What is resource-based authorization?
135. How do you secure APIs with Entra ID?
136. What is Managed Identity?
137. What is the difference between Managed Identity and Service Principal?
138. How do you protect APIs behind Azure API Management?
139. What are common authentication mistakes?
140. How do you secure machine-to-machine APIs?

## 08 Security & OWASP

141. What is OWASP API Security Top 10?
142. How do you prevent SQL injection?
143. How do you prevent XSS?
144. How do you prevent CSRF?
145. How do you secure secrets in .NET applications?
146. Why should secrets not be stored in appsettings.json?
147. How do you use Azure Key Vault with .NET?
148. What is secure configuration management?
149. What is input validation?
150. What is output encoding?
151. What is rate limiting as a security control?
152. What is CORS and how do you configure it safely?
153. What is HTTPS redirection?
154. What is HSTS?
155. How do you secure cookies?
156. What is data protection API in ASP.NET Core?
157. How do you handle PII data?
158. How do you implement audit logging?
159. What are security headers?
160. How do you perform threat modeling for a .NET API?

## 09 Performance & Scalability

161. What is the difference between performance and scalability?
162. How do you improve ASP.NET Core API performance?
163. What is async/await and how does it help scalability?
164. What is thread pool starvation?
165. How do you identify memory leaks in .NET?
166. What is garbage collection in .NET?
167. What are Gen 0, Gen 1, and Gen 2 collections?
168. What is LOH in .NET?
169. What are Span<T> and Memory<T>?
170. How do you reduce allocations in hot paths?
171. What is response caching?
172. What is distributed caching?
173. How do you use Redis with .NET?
174. What is output caching?
175. How do you handle high-throughput APIs?
176. What is backpressure?
177. How do you design retry policies safely?
178. What is circuit breaker pattern?
179. How do you measure p95 and p99 latency?
180. How do you tune APIs for production traffic?

## 10 Async, Multithreading & TPL

181. What is the difference between Task and Thread?
182. What is async/await?
183. What happens when you await a Task?
184. What is Task.WhenAll?
185. What is Task.WaitAll and why should you avoid it in async code?
186. What is ConfigureAwait?
187. What is CancellationToken?
188. How do you implement cancellation in APIs?
189. What is deadlock in async programming?
190. What is fire-and-forget and why is it risky?
191. What is Parallel.ForEachAsync?
192. What is the difference between CPU-bound and IO-bound work?
193. How do you handle background tasks in ASP.NET Core?
194. What is IHostedService?
195. What is BackgroundService?
196. What is Channel<T>?
197. What is SemaphoreSlim used for?
198. How do you limit concurrency in .NET?
199. What are race conditions?
200. How do you make code thread-safe?

## 11 Logging, Monitoring & Observability

201. What is structured logging?
202. What is ILogger in .NET?
203. What is the difference between log levels?
204. What should you not log?
205. What is correlation ID?
206. What is distributed tracing?
207. What is OpenTelemetry?
208. How do you integrate Application Insights with .NET?
209. What are metrics?
210. What are traces?
211. What are logs?
212. What is health check middleware?
213. How do you create custom health checks?
214. What is readiness vs liveness probe?
215. How do you monitor dependency failures?
216. What is sampling in telemetry?
217. How do you troubleshoot high latency in production?
218. What is centralized logging?
219. How do you define SLI, SLO, and SLA?
220. How do you make observability useful for support teams?

## 12 Testing

221. What are unit tests?
222. What are integration tests?
223. What are contract tests?
224. What are end-to-end tests?
225. How do you test ASP.NET Core controllers?
226. How do you test minimal APIs?
227. What is WebApplicationFactory?
228. What is mocking?
229. What is the difference between mock, stub, and fake?
230. How do you test EF Core code?
231. How do you test Dapper code?
232. What is Testcontainers?
233. How do you test authentication and authorization?
234. How do you test middleware?
235. What is code coverage?
236. Why is 100% code coverage not always meaningful?
237. What is TDD?
238. What is BDD?
239. How do you write maintainable tests?
240. What should be included in a CI test pipeline?

## 13 Clean Architecture & DDD

241. What is Clean Architecture?
242. What are the layers of Clean Architecture?
243. What is Domain-Driven Design?
244. What is an aggregate?
245. What is an entity?
246. What is a value object?
247. What is a domain service?
248. What is an application service?
249. What is an infrastructure service?
250. What is repository pattern?
251. What is unit of work pattern?
252. What is CQRS?
253. When should you use CQRS?
254. What is MediatR used for?
255. What is domain event?
256. What is integration event?
257. What is bounded context?
258. How do you avoid anemic domain model?
259. How do you structure a .NET solution for Clean Architecture?
260. How do you explain Clean Architecture in an interview?

## 14 Microservices & Distributed Systems

261. What is microservices architecture?
262. What is the difference between microservices and modular monolith?
263. When should you avoid microservices?
264. What is service boundary identification?
265. What is database per service?
266. What is distributed transaction problem?
267. What is Saga pattern?
268. What is choreography-based saga?
269. What is orchestration-based saga?
270. What is eventual consistency?
271. What is idempotency?
272. What is outbox pattern?
273. What is inbox pattern?
274. What is API gateway pattern?
275. What is service discovery?
276. What is circuit breaker pattern?
277. What is bulkhead pattern?
278. What is retry storm?
279. What is schema evolution?
280. How do you design microservices for reliability?

## 15 Azure for .NET Developers

281. How do you deploy .NET APIs to Azure App Service?
282. What is Azure App Service?
283. What is Azure Functions?
284. What is the difference between App Service and Azure Functions?
285. What is Azure API Management?
286. What is Azure Key Vault?
287. What is Azure Service Bus?
288. What is Azure Event Grid?
289. What is Azure Event Hubs?
290. What is Azure Storage Account?
291. What is Azure Cosmos DB?
292. What is Managed Identity in Azure?
293. How do you connect .NET app to Azure SQL securely?
294. How do you use Key Vault references in App Service?
295. What is private endpoint?
296. What is VNet integration?
297. What is Application Insights?
298. How do you deploy .NET containers to AKS?
299. What is Azure Container Apps?
300. How do you design Azure hosting for enterprise .NET APIs?

## 16 Containers, Kubernetes & KEDA

301. What is Docker?
302. What is a Dockerfile?
303. How do you containerize a .NET API?
304. What is Kubernetes?
305. What is a pod?
306. What is deployment in Kubernetes?
307. What is service in Kubernetes?
308. What is ingress?
309. What is ConfigMap?
310. What is Secret?
311. What is Horizontal Pod Autoscaler?
312. What is KEDA?
313. How does KEDA scale .NET workers?
314. What is event-driven autoscaling?
315. How do you scale based on Azure Service Bus queue length?
316. What is readiness probe?
317. What is liveness probe?
318. How do you manage configuration in Kubernetes?
319. How do you secure container images?
320. What are best practices for .NET on AKS?

## 17 Minimal APIs

321. What are minimal APIs in ASP.NET Core?
322. When should you use minimal APIs?
323. When should you avoid minimal APIs?
324. How do you define routes in minimal API?
325. How do you inject dependencies in minimal API handlers?
326. How do you validate input in minimal APIs?
327. How do you group endpoints?
328. What is RouteGroupBuilder?
329. How do you apply authorization to route groups?
330. How do you return typed results?
331. What are Results and TypedResults?
332. How do you document minimal APIs using OpenAPI?
333. How do you version minimal APIs?
334. How do you handle errors in minimal APIs?
335. How do filters work in minimal APIs?
336. How do you test minimal APIs?
337. How do you organize minimal APIs in large projects?
338. What is endpoint filter?
339. What are the limitations of minimal APIs?
340. How do minimal APIs compare with controllers?

## 18 gRPC, SignalR & Realtime

341. What is gRPC?
342. When would you use gRPC instead of REST?
343. What is Protocol Buffers?
344. What is unary call in gRPC?
345. What is server streaming?
346. What is client streaming?
347. What is bidirectional streaming?
348. What is SignalR?
349. When would you use SignalR?
350. What is WebSocket?
351. What is long polling?
352. How does SignalR manage connections?
353. What is a SignalR hub?
354. How do you scale SignalR in Azure?
355. What is Azure SignalR Service?
356. How do you secure SignalR endpoints?
357. What is message ordering challenge in realtime systems?
358. How do you handle reconnects?
359. How do you monitor realtime systems?
360. What are common realtime architecture mistakes?

## 19 Configuration & Options

361. What are configuration providers in .NET?
362. What is the order of configuration loading?
363. How do environment variables override appsettings.json?
364. What is User Secrets?
365. What is the Options pattern?
366. What is IOptions?
367. What is IOptionsSnapshot?
368. What is IOptionsMonitor?
369. When do you use IOptionsMonitor?
370. How do you validate options at startup?
371. How do you manage feature flags?
372. What is Azure App Configuration?
373. How do you handle secrets in local development?
374. How do you handle secrets in production?
375. How do you configure per-environment settings?
376. What is strongly typed configuration?
377. What is reloadOnChange?
378. How do you manage connection strings securely?
379. How do you configure logging per environment?
380. How do you design configuration for cloud-native apps?

## 20 Messaging & Event-Driven Architecture

381. What is event-driven architecture?
382. What is the difference between command and event?
383. What is a queue?
384. What is a topic?
385. What is pub/sub?
386. What is Azure Service Bus?
387. What is the difference between Service Bus Queue and Topic?
388. What is dead-letter queue?
389. What is message lock?
390. What is duplicate detection?
391. What is session-enabled queue?
392. What is Kafka?
393. What is consumer group?
394. What is event ordering?
395. What is poison message?
396. How do you implement retries safely?
397. What is exponential backoff?
398. What is outbox pattern?
399. What is idempotent consumer?
400. How do you monitor message-based systems?

## 21 Files, Streams & Serialization

401. What is Stream in .NET?
402. What is MemoryStream?
403. What is FileStream?
404. What is async file IO?
405. What is JSON serialization?
406. What is System.Text.Json?
407. What is Newtonsoft.Json and when do you still use it?
408. What is custom converter?
409. How do you handle large file uploads?
410. How do you stream large responses from API?
411. What is multipart/form-data?
412. How do you validate uploaded files?
413. How do you prevent file upload attacks?
414. What is compression middleware?
415. What is Brotli compression?
416. What is response buffering?
417. What is UTF-8 encoding?
418. What is Base64 encoding?
419. How do you serialize circular references?
420. How do you design APIs for large payloads?

## 22 Build, CI/CD & DevOps

421. What is dotnet CLI?
422. What is dotnet restore?
423. What is dotnet build?
424. What is dotnet publish?
425. What is self-contained deployment?
426. What is framework-dependent deployment?
427. What is single-file deployment?
428. What is ReadyToRun compilation?
429. What is CI/CD?
430. How do you build .NET applications in Azure DevOps?
431. How do you create a YAML pipeline for .NET?
432. What steps should be in a .NET CI pipeline?
433. How do you run tests in pipeline?
434. How do you perform static code analysis?
435. What is SonarQube?
436. How do you deploy to Azure App Service?
437. How do you deploy containers?
438. How do you handle rollback?
439. How do you manage environment approvals?
440. What is blue-green deployment?

## 23 Memory Management & Runtime

441. What is CLR?
442. What is JIT compilation?
443. What is tiered compilation?
444. What is garbage collection?
445. What is workstation GC?
446. What is server GC?
447. What is LOH?
448. What is object allocation?
449. What is boxing and unboxing?
450. How do you avoid unnecessary allocations?
451. What is IDisposable?
452. What is IAsyncDisposable?
453. What is using statement?
454. What is finalizer?
455. What is memory leak in managed code?
456. How do events cause memory leaks?
457. What is weak reference?
458. What is stack vs heap?
459. What is Span<T>?
460. How do you troubleshoot high memory usage?

## 24 Advanced .NET Interview Scenarios

461. How would you design a high-throughput order API in .NET 10?
462. How would you migrate a monolith to .NET 10 microservices?
463. How would you troubleshoot intermittent 500 errors in ASP.NET Core?
464. How would you handle 10x traffic increase?
465. How would you design a secure file upload API?
466. How would you process one million messages per day?
467. How would you design retry and dead-letter handling?
468. How would you implement multi-tenant APIs?
469. How would you handle per-tenant database isolation?
470. How would you design role-based and policy-based authorization?
471. How would you optimize slow EF Core queries?
472. How would you replace EF Core with Dapper for hot paths?
473. How would you implement audit logging?
474. How would you build observability for distributed APIs?
475. How would you detect and fix thread pool starvation?
476. How would you design zero-downtime deployment?
477. How would you secure APIs exposed to partners?
478. How would you implement API throttling?
479. How would you manage secrets across environments?
480. How would you explain your .NET architecture to an interviewer?

## 25 Scenario-Based Final Round

481. Tell me about a complex .NET system you designed.
482. How do you decide between monolith, modular monolith, and microservices?
483. How do you decide between SQL and NoSQL?
484. How do you handle stakeholder-driven changing requirements?
485. How do you convert business requirements into technical architecture?
486. How do you define non-functional requirements?
487. How do you design for availability?
488. How do you design for disaster recovery?
489. How do you design for cost optimization?
490. How do you design for security by default?
491. How do you review code as an architect?
492. How do you mentor junior developers?
493. How do you handle production incidents?
494. How do you communicate technical risks?
495. How do you choose libraries and frameworks?
496. How do you prevent over-engineering?
497. How do you document architecture decisions?
498. What are ADRs?
499. How do you measure architecture success?
500. What is your final .NET 10 architecture checklist?

**Total .NET 10 Interview Questions questions: 500**

---
Prepared as a separate part from the original 1500-question bank.
