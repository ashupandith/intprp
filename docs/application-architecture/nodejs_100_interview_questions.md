# Node.js Interview Questions (100)

## Node.js Fundamentals
1. What is Node.js, and how is it different from browser JavaScript?
2. How does the V8 engine relate to Node.js?
3. What is the Node.js event loop?
4. What are the phases of the event loop?
5. What is non-blocking I/O in Node.js?
6. What is the difference between synchronous and asynchronous APIs?
7. What are callbacks and callback hell?
8. What are Promises, and why are they better than raw callbacks?
9. How does `async/await` work in Node.js?
10. What is the difference between microtasks and macrotasks?
11. What is `process.nextTick` and when should you avoid it?
12. What is `setImmediate` and how does it differ from `setTimeout(fn, 0)`?
13. What are CommonJS modules?
14. What are ES Modules in Node.js?
15. What is the difference between `require` and `import`?

## Runtime and Performance
16. Why is CPU-intensive work problematic in Node.js?
17. How do worker threads help in Node.js?
18. What is the cluster module used for?
19. How do you scale a Node.js app vertically vs horizontally?
20. How do you measure event loop lag?
21. What is backpressure in streams?
22. How do Node.js streams work?
23. What is the difference between readable, writable, duplex, and transform streams?
24. How do you avoid memory leaks in Node.js?
25. What causes high memory usage in long-running Node.js processes?
26. How do you profile Node.js CPU and memory?
27. What is garbage collection behavior in Node.js?
28. What are common Node.js performance anti-patterns?
29. How do you optimize JSON serialization/deserialization overhead?
30. How do you handle large file processing efficiently in Node.js?

## Express and API Design
31. What is Express.js and why is it widely used?
32. What is middleware in Express?
33. How does middleware order affect behavior?
34. What is error-handling middleware in Express?
35. How do you structure routes/controllers/services in Node APIs?
36. What is RESTful API design in Node.js?
37. What are idempotent HTTP methods and why do they matter?
38. How do you version APIs in Node.js applications?
39. How do you implement pagination efficiently?
40. How do you design filtering and sorting APIs safely?
41. What is HATEOAS and is it practical?
42. How do you document Node APIs (OpenAPI/Swagger)?
43. How do you validate request payloads in Node.js?
44. How do you handle partial failures in API orchestration?
45. How do you design health endpoints for Node services?

## Security
46. What are common Node.js web security vulnerabilities?
47. How do you prevent SQL injection in Node.js?
48. How do you prevent NoSQL injection?
49. How do you prevent XSS and CSRF in Node backends?
50. How do you secure authentication and authorization in Node apps?
51. JWT vs session-based auth in Node: when to use which?
52. How do you securely manage secrets in Node.js?
53. What is helmet and how does it improve security?
54. How do rate limiting and throttling work in Node APIs?
55. How do you secure file upload endpoints?
56. How do you implement audit logging securely?
57. How do you protect against dependency supply chain attacks?

## Databases and Data Access
58. How do you choose between SQL and NoSQL for Node apps?
59. What are ORMs/ODMs in Node.js?
60. TypeORM vs Prisma vs Sequelize: how do you choose?
61. How do you design connection pooling in Node.js?
62. How do you handle transaction boundaries in Node services?
63. How do you avoid N+1 query issues?
64. How do you design caching with Redis in Node architectures?
65. How do you implement distributed locking in Node systems?
66. How do you design idempotency keys in payment/order APIs?
67. How do you handle eventual consistency in distributed Node services?

## Messaging and Distributed Systems
68. When should you use queues in Node.js systems?
69. How do you design retry and DLQ behavior for message consumers?
70. How do you implement idempotent consumers in Node?
71. How do you choose between RabbitMQ, Kafka, and Service Bus patterns?
72. What is saga orchestration in Node microservices?
73. How do you manage distributed tracing across Node services?
74. How do you handle service-to-service communication timeouts and circuit breakers?
75. How do you design graceful degradation in Node backends?

## Testing and Quality
76. How do you structure unit tests in Node.js?
77. How do you test Express routes and middleware?
78. How do you mock external dependencies in Node tests?
79. What should be integration-tested in backend services?
80. How do you run contract testing between services?
81. How do you set up end-to-end API tests?
82. How do you prevent flaky backend tests?
83. How do you enforce linting, formatting, and static analysis in Node projects?

## DevOps and Operations
84. How do you containerize a Node.js application?
85. What should be in a production-ready Node Dockerfile?
86. How do you run Node.js apps in Kubernetes safely?
87. How do you implement readiness and liveness probes for Node containers?
88. How do you do zero-downtime deployments for Node services?
89. How do you handle config management across environments?
90. How do you rotate secrets and certificates in production?
91. How do you perform blue-green/canary release for Node APIs?

## Observability and Reliability
92. What metrics should every Node service expose?
93. How do structured logs improve operations?
94. How do you implement distributed tracing in Node.js?
95. How do you define SLI/SLO for Node services?
96. How do you design incident response playbooks for backend services?
97. How do you debug intermittent production issues in Node?

## Advanced Architecture and Interview Discussion
98. How do you design multi-tenant Node.js applications?
99. How do you prepare Node.js architecture for enterprise scale?
100. How do you explain Node.js architectural trade-offs in a senior interview?
