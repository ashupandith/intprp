# .NET 10 Interview Answers - 500

Format: each answer is written for interview preparation. Use it as a base answer, then add your own project example.

Suggested answer style: definition → why it matters → practical example/trade-off.


## 01 .NET 10 Overview & Platform

### 1. What is .NET 10, and how is it different from .NET Framework?

**Answer:** .NET 10 is the modern Microsoft developer platform for building APIs, web apps, cloud services, desktop apps, background workers, and containers. In interviews, explain it as cross-platform, high-performance, cloud-ready, and suitable for enterprise workloads.

### 2. Why is .NET 10 important for modern enterprise application development?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 3. What are the major runtime improvements introduced in .NET 10?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 4. How does .NET 10 improve performance compared with earlier .NET versions?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 5. What does LTS mean in the context of .NET releases?

**Answer:** LTS means Long-Term Support. For enterprise systems, LTS releases are preferred because they receive longer support, security fixes, and a safer upgrade window.

### 6. How do you decide whether to migrate an application to .NET 10?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 7. What compatibility checks would you perform before upgrading to .NET 10?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 8. What is the difference between .NET SDK, runtime, and hosting bundle?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 9. How do you check the installed .NET SDK version?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 10. What is the role of global.json in .NET projects?

**Answer:** global.json pins the .NET SDK version for a repository. It prevents build differences between developer machines and CI/CD agents.

### 11. How does .NET support cross-platform application development?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 12. What are the major application types you can build with .NET 10?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 13. What is the difference between .NET runtime and CoreCLR?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.

### 14. What is the role of Base Class Library in .NET?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 15. How does .NET 10 support cloud-native development?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 16. What is NativeAOT and when would you use it?

**Answer:** NativeAOT compiles a .NET app ahead-of-time into a native binary. It improves startup time and memory usage, but reflection-heavy libraries, dynamic loading, and some serializers need careful testing.

### 17. What are the risks of NativeAOT in enterprise applications?

**Answer:** NativeAOT compiles a .NET app ahead-of-time into a native binary. It improves startup time and memory usage, but reflection-heavy libraries, dynamic loading, and some serializers need careful testing.

### 18. What is trimming in .NET and why is it useful?

**Answer:** Trimming removes unused code during publish to reduce application size. It is useful for containers and serverless apps, but reflection-based code must be validated because required code may be removed.

### 19. How do you handle breaking changes during .NET migration?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 20. How would you explain .NET 10 to a non-technical stakeholder?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.


## 02 C# 14 Language Features

### 21. What are the important C# language features used with .NET 10?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 22. What is the difference between record, class, and struct?

**Answer:** A class is general-purpose reference type behavior, a record is optimized for immutable data/value-style equality, and a struct is a value type. Records are useful for DTOs, events, and immutable models.

### 23. How do init-only properties improve immutability?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 24. What are required properties in C#?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 25. What is pattern matching in C# and where do you use it?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 26. Explain switch expressions with a practical example.

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 27. What are nullable reference types and why are they important?

**Answer:** Nullable reference types help detect possible null reference errors at compile time. In production code, they improve API contracts and reduce runtime NullReferenceException issues.

### 28. How do you handle nullable warnings in production code?

**Answer:** Nullable reference types help detect possible null reference errors at compile time. In production code, they improve API contracts and reduce runtime NullReferenceException issues.

### 29. What is the difference between var, dynamic, and object?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 30. What is the purpose of using statements and using declarations?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 31. How do extension methods work in C#?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 32. What are extension members and why are they useful?

**Answer:** With .NET 10, C# 14 adds productivity features such as enhanced extension members. In interviews, mention that modern C# improves readability, reduces boilerplate, and supports cleaner domain/application code.

### 33. What are collection expressions in modern C#?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 34. What is the difference between primary constructors and normal constructors?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 35. How does C# support functional-style programming?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 36. What are lambdas and expression-bodied members?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 37. What is the difference between Func, Action, and Predicate?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 38. What is tuple deconstruction in C#?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 39. How do you write clean and maintainable C# code?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 40. What C# features help reduce boilerplate code?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.


## 03 ASP.NET Core Fundamentals

### 41. What is ASP.NET Core?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 42. What is the ASP.NET Core request pipeline?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 43. What is middleware in ASP.NET Core?

**Answer:** Middleware is a component in the ASP.NET Core request pipeline. Each middleware can inspect, modify, pass, or stop the request; examples include authentication, logging, CORS, exception handling, and routing.

### 44. How do you create custom middleware?

**Answer:** Middleware is a component in the ASP.NET Core request pipeline. Each middleware can inspect, modify, pass, or stop the request; examples include authentication, logging, CORS, exception handling, and routing.

### 45. What is the difference between Use, Run, and Map middleware?

**Answer:** Middleware is a component in the ASP.NET Core request pipeline. Each middleware can inspect, modify, pass, or stop the request; examples include authentication, logging, CORS, exception handling, and routing.

### 46. What is endpoint routing?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 47. What is the role of Program.cs in minimal hosting model?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 48. What is dependency injection in ASP.NET Core?

**Answer:** Dependency Injection provides dependencies from the container instead of creating them manually. It improves testability, loose coupling, and clean architecture.

### 49. What are the default services registered in ASP.NET Core?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 50. What is the difference between appsettings.json and environment variables?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 51. How do you manage configuration in ASP.NET Core?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 52. What is IWebHostEnvironment used for?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 53. What are filters in ASP.NET Core MVC?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 54. What is model binding?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 55. What is model validation?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 56. What is the difference between controller-based API and minimal API?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 57. When would you choose minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 58. How do you handle global errors in ASP.NET Core?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 59. What is ProblemDetails in ASP.NET Core?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 60. How do you structure a production-ready ASP.NET Core application?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.


## 04 Web API Design

### 61. What are REST principles?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 62. What is the difference between REST and RPC-style APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 63. How do you design resource-based URLs?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 64. What are correct HTTP methods for CRUD operations?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 65. What is the difference between PUT and PATCH?

**Answer:** PUT usually replaces the full resource and should be idempotent. PATCH partially updates selected fields and is used when only part of the resource changes.

### 66. What are idempotent HTTP methods?

**Answer:** Idempotent operations give the same result even if repeated multiple times. GET, PUT, and DELETE should be idempotent; POST is generally not unless designed with an idempotency key.

### 67. How do you design API versioning?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 68. What is content negotiation?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 69. What status code would you return for validation failure?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 70. What status code would you return for unauthorized access?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 71. What is the difference between 401 and 403?

**Answer:** 401 means the caller is not authenticated or token is invalid/missing. 403 means the caller is authenticated but does not have permission for the resource.

### 72. How do you design pagination in APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 73. How do you implement filtering and sorting in APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 74. What is HATEOAS and do you use it in enterprise APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 75. How do you handle correlation IDs in APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 76. What is OpenAPI/Swagger?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 77. How do you secure Swagger in production?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 78. How do you design APIs for backward compatibility?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 79. What is rate limiting and where do you implement it?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 80. What makes an API production-ready?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.


## 05 Dependency Injection & Lifetimes

### 81. What is dependency injection?

**Answer:** Dependency Injection provides dependencies from the container instead of creating them manually. It improves testability, loose coupling, and clean architecture.

### 82. What problem does dependency injection solve?

**Answer:** Dependency Injection provides dependencies from the container instead of creating them manually. It improves testability, loose coupling, and clean architecture.

### 83. What is the difference between constructor injection and property injection?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 84. What are Singleton, Scoped, and Transient lifetimes?

**Answer:** A Singleton depending on a Scoped service is a lifetime mismatch because Singleton lives for the app lifetime while Scoped is per request. Fix it by changing lifetimes or creating scopes using IServiceScopeFactory.

### 85. When should you use Singleton lifetime?

**Answer:** Singleton creates one instance for the entire application lifetime. Use it for stateless services, caches, or expensive shared objects, but avoid storing request/user-specific state.

### 86. When should you use Scoped lifetime?

**Answer:** Scoped creates one instance per request scope. It is commonly used for DbContext and request-specific services.

### 87. When should you use Transient lifetime?

**Answer:** Transient creates a new instance every time it is requested. Use it for lightweight stateless services.

### 88. What happens if a Singleton service depends on a Scoped service?

**Answer:** A Singleton depending on a Scoped service is a lifetime mismatch because Singleton lives for the app lifetime while Scoped is per request. Fix it by changing lifetimes or creating scopes using IServiceScopeFactory.

### 89. How do you resolve services manually using IServiceProvider?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 90. What is IServiceScopeFactory?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 91. How do you register generic services?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 92. How do you register multiple implementations of the same interface?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 93. What is keyed service registration?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 94. How do you test services that use dependency injection?

**Answer:** Dependency Injection provides dependencies from the container instead of creating them manually. It improves testability, loose coupling, and clean architecture.

### 95. What is the service locator anti-pattern?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 96. How do you avoid circular dependencies?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 97. How do you inject configuration options?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 98. What is the Options pattern?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 99. What is IOptionsMonitor?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 100. How do you design DI for clean architecture?

**Answer:** Dependency Injection provides dependencies from the container instead of creating them manually. It improves testability, loose coupling, and clean architecture.


## 06 EF Core & Dapper

### 101. What is Entity Framework Core?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 102. What is Dapper?

**Answer:** Dapper is a lightweight micro ORM for .NET. It executes SQL or stored procedures and maps results to C# objects with very low overhead.

### 103. What is the difference between EF Core and Dapper?

**Answer:** EF Core is a full ORM with change tracking, LINQ, relationships, and migrations. Dapper is a micro ORM where we write SQL manually and get fast object mapping; use Dapper for optimized queries and EF Core for productivity/domain CRUD.

### 104. When would you use Dapper instead of EF Core?

**Answer:** EF Core is a full ORM with change tracking, LINQ, relationships, and migrations. Dapper is a micro ORM where we write SQL manually and get fast object mapping; use Dapper for optimized queries and EF Core for productivity/domain CRUD.

### 105. When would you use EF Core instead of Dapper?

**Answer:** EF Core is a full ORM with change tracking, LINQ, relationships, and migrations. Dapper is a micro ORM where we write SQL manually and get fast object mapping; use Dapper for optimized queries and EF Core for productivity/domain CRUD.

### 106. What is change tracking in EF Core?

**Answer:** EF Core is Microsoft's ORM for .NET. It maps domain objects to relational data and supports LINQ, migrations, transactions, and change tracking.

### 107. What is AsNoTracking and why is it useful?

**Answer:** AsNoTracking disables EF Core change tracking for read-only queries. It improves performance and memory usage when you do not plan to update the returned entities.

### 108. What is DbContext lifetime best practice?

**Answer:** EF Core is Microsoft's ORM for .NET. It maps domain objects to relational data and supports LINQ, migrations, transactions, and change tracking.

### 109. What is migration in EF Core?

**Answer:** EF Core is Microsoft's ORM for .NET. It maps domain objects to relational data and supports LINQ, migrations, transactions, and change tracking.

### 110. How do you handle database transactions in EF Core?

**Answer:** EF Core is Microsoft's ORM for .NET. It maps domain objects to relational data and supports LINQ, migrations, transactions, and change tracking.

### 111. How do you handle transactions with Dapper?

**Answer:** Dapper is a lightweight micro ORM for .NET. It executes SQL or stored procedures and maps results to C# objects with very low overhead.

### 112. What is lazy loading and why can it be dangerous?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 113. What is eager loading?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 114. What is explicit loading?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 115. What is the N+1 query problem?

**Answer:** N+1 happens when one query loads parent data and then additional queries load child data per row. Fix it using Include, projection, joins, batching, or optimized SQL.

### 116. How do you optimize EF Core queries?

**Answer:** EF Core is Microsoft's ORM for .NET. It maps domain objects to relational data and supports LINQ, migrations, transactions, and change tracking.

### 117. How do you execute stored procedures using Dapper?

**Answer:** Dapper is a lightweight micro ORM for .NET. It executes SQL or stored procedures and maps results to C# objects with very low overhead.

### 118. How do you prevent SQL injection with Dapper?

**Answer:** Dapper is a lightweight micro ORM for .NET. It executes SQL or stored procedures and maps results to C# objects with very low overhead.

### 119. How do you implement repository pattern with EF Core or Dapper?

**Answer:** EF Core is a full ORM with change tracking, LINQ, relationships, and migrations. Dapper is a micro ORM where we write SQL manually and get fast object mapping; use Dapper for optimized queries and EF Core for productivity/domain CRUD.

### 120. How do you choose between ORM and raw SQL in architecture?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.


## 07 Authentication & Authorization

### 121. What is authentication?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 122. What is authorization?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 123. What is JWT?

**Answer:** JWT is a signed token containing header, payload, and signature. APIs validate issuer, audience, expiry, signature, and claims before allowing access.

### 124. What are the parts of a JWT token?

**Answer:** JWT is a signed token containing header, payload, and signature. APIs validate issuer, audience, expiry, signature, and claims before allowing access.

### 125. What is OAuth 2.0?

**Answer:** OAuth 2.0 is an authorization framework for delegated access. OpenID Connect adds authentication and identity information on top of OAuth 2.0.

### 126. What is OpenID Connect?

**Answer:** Authentication proves who the caller is; authorization decides what the caller can do. In .NET APIs, this is commonly implemented using JWT bearer authentication, claims, roles, and policies.

### 127. What is the difference between access token and ID token?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 128. What is refresh token rotation?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 129. What is token validation in ASP.NET Core?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 130. How do you configure JWT bearer authentication?

**Answer:** JWT is a signed token containing header, payload, and signature. APIs validate issuer, audience, expiry, signature, and claims before allowing access.

### 131. What are claims?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 132. What are roles?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 133. What is policy-based authorization?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 134. What is resource-based authorization?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 135. How do you secure APIs with Entra ID?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 136. What is Managed Identity?

**Answer:** Authentication proves who the caller is; authorization decides what the caller can do. In .NET APIs, this is commonly implemented using JWT bearer authentication, claims, roles, and policies.

### 137. What is the difference between Managed Identity and Service Principal?

**Answer:** Managed Identity is an Azure-managed identity for Azure resources, so secrets are not stored by the app. Service Principal is an application identity usually managed with credentials/certificates and used across automation or external workloads.

### 138. How do you protect APIs behind Azure API Management?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 139. What are common authentication mistakes?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 140. How do you secure machine-to-machine APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.


## 08 Security & OWASP

### 141. What is OWASP API Security Top 10?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 142. How do you prevent SQL injection?

**Answer:** Prevent SQL injection by using parameterized queries, ORM parameters, stored procedure parameters, input validation, and least-privilege DB accounts. Never concatenate user input into SQL.

### 143. How do you prevent XSS?

**Answer:** Security should include input validation, output encoding, authentication, authorization, secret management, secure headers, logging, rate limits, and OWASP API risk review.

### 144. How do you prevent CSRF?

**Answer:** Security should include input validation, output encoding, authentication, authorization, secret management, secure headers, logging, rate limits, and OWASP API risk review.

### 145. How do you secure secrets in .NET applications?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 146. Why should secrets not be stored in appsettings.json?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 147. How do you use Azure Key Vault with .NET?

**Answer:** Secrets should be stored in a secure secret manager such as Azure Key Vault and accessed using Managed Identity. Avoid storing passwords, keys, or connection strings in source control.

### 148. What is secure configuration management?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 149. What is input validation?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 150. What is output encoding?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 151. What is rate limiting as a security control?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 152. What is CORS and how do you configure it safely?

**Answer:** CORS controls which browser origins can call your API. Configure explicit allowed origins, methods, and headers; avoid wildcard origins with credentials.

### 153. What is HTTPS redirection?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 154. What is HSTS?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 155. How do you secure cookies?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 156. What is data protection API in ASP.NET Core?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 157. How do you handle PII data?

**Answer:** Security should include input validation, output encoding, authentication, authorization, secret management, secure headers, logging, rate limits, and OWASP API risk review.

### 158. How do you implement audit logging?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 159. What are security headers?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 160. How do you perform threat modeling for a .NET API?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.


## 09 Performance & Scalability

### 161. What is the difference between performance and scalability?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 162. How do you improve ASP.NET Core API performance?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 163. What is async/await and how does it help scalability?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 164. What is thread pool starvation?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 165. How do you identify memory leaks in .NET?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 166. What is garbage collection in .NET?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.

### 167. What are Gen 0, Gen 1, and Gen 2 collections?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 168. What is LOH in .NET?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 169. What are Span<T> and Memory<T>?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.

### 170. How do you reduce allocations in hot paths?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 171. What is response caching?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 172. What is distributed caching?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 173. How do you use Redis with .NET?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 174. What is output caching?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 175. How do you handle high-throughput APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 176. What is backpressure?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 177. How do you design retry policies safely?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 178. What is circuit breaker pattern?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 179. How do you measure p95 and p99 latency?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 180. How do you tune APIs for production traffic?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.


## 10 Async, Multithreading & TPL

### 181. What is the difference between Task and Thread?

**Answer:** Thread is an OS execution unit; Task is a higher-level abstraction for asynchronous or parallel work. In web APIs, Task with async/await is preferred for IO-bound operations.

### 182. What is async/await?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 183. What happens when you await a Task?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 184. What is Task.WhenAll?

**Answer:** Task.WhenAll is awaitable and non-blocking; Task.WaitAll blocks the current thread and can cause deadlocks or thread starvation in async applications.

### 185. What is Task.WaitAll and why should you avoid it in async code?

**Answer:** Task.WhenAll is awaitable and non-blocking; Task.WaitAll blocks the current thread and can cause deadlocks or thread starvation in async applications.

### 186. What is ConfigureAwait?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 187. What is CancellationToken?

**Answer:** CancellationToken allows cooperative cancellation when a client disconnects, timeout occurs, or the system shuts down. Pass it to database, HTTP, and long-running operations.

### 188. How do you implement cancellation in APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 189. What is deadlock in async programming?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 190. What is fire-and-forget and why is it risky?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 191. What is Parallel.ForEachAsync?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 192. What is the difference between CPU-bound and IO-bound work?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 193. How do you handle background tasks in ASP.NET Core?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 194. What is IHostedService?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 195. What is BackgroundService?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 196. What is Channel<T>?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 197. What is SemaphoreSlim used for?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 198. How do you limit concurrency in .NET?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 199. What are race conditions?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 200. How do you make code thread-safe?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.


## 11 Logging, Monitoring & Observability

### 201. What is structured logging?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 202. What is ILogger in .NET?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 203. What is the difference between log levels?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 204. What should you not log?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 205. What is correlation ID?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 206. What is distributed tracing?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 207. What is OpenTelemetry?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 208. How do you integrate Application Insights with .NET?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 209. What are metrics?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 210. What are traces?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 211. What are logs?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 212. What is health check middleware?

**Answer:** Middleware is a component in the ASP.NET Core request pipeline. Each middleware can inspect, modify, pass, or stop the request; examples include authentication, logging, CORS, exception handling, and routing.

### 213. How do you create custom health checks?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 214. What is readiness vs liveness probe?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 215. How do you monitor dependency failures?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 216. What is sampling in telemetry?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 217. How do you troubleshoot high latency in production?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 218. What is centralized logging?

**Answer:** Authentication proves who the caller is; authorization decides what the caller can do. In .NET APIs, this is commonly implemented using JWT bearer authentication, claims, roles, and policies.

### 219. How do you define SLI, SLO, and SLA?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 220. How do you make observability useful for support teams?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.


## 12 Testing

### 221. What are unit tests?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 222. What are integration tests?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 223. What are contract tests?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 224. What are end-to-end tests?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 225. How do you test ASP.NET Core controllers?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 226. How do you test minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 227. What is WebApplicationFactory?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 228. What is mocking?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 229. What is the difference between mock, stub, and fake?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 230. How do you test EF Core code?

**Answer:** EF Core is Microsoft's ORM for .NET. It maps domain objects to relational data and supports LINQ, migrations, transactions, and change tracking.

### 231. How do you test Dapper code?

**Answer:** Dapper is a lightweight micro ORM for .NET. It executes SQL or stored procedures and maps results to C# objects with very low overhead.

### 232. What is Testcontainers?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 233. How do you test authentication and authorization?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 234. How do you test middleware?

**Answer:** Middleware is a component in the ASP.NET Core request pipeline. Each middleware can inspect, modify, pass, or stop the request; examples include authentication, logging, CORS, exception handling, and routing.

### 235. What is code coverage?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 236. Why is 100% code coverage not always meaningful?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 237. What is TDD?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 238. What is BDD?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 239. How do you write maintainable tests?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 240. What should be included in a CI test pipeline?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.


## 13 Clean Architecture & DDD

### 241. What is Clean Architecture?

**Answer:** Clean Architecture separates domain, application, infrastructure, and presentation layers. The core business logic remains independent of frameworks, databases, and UI, making the system testable and maintainable.

### 242. What are the layers of Clean Architecture?

**Answer:** Clean Architecture separates domain, application, infrastructure, and presentation layers. The core business logic remains independent of frameworks, databases, and UI, making the system testable and maintainable.

### 243. What is Domain-Driven Design?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 244. What is an aggregate?

**Answer:** Clean Architecture separates domain, application, infrastructure, and presentation layers. The core business logic remains independent of frameworks, databases, and UI, making the system testable and maintainable.

### 245. What is an entity?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 246. What is a value object?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 247. What is a domain service?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 248. What is an application service?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 249. What is an infrastructure service?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 250. What is repository pattern?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 251. What is unit of work pattern?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 252. What is CQRS?

**Answer:** CQRS separates read and write models. It is useful when read and write workloads have different complexity, scale, or optimization needs, but it should not be used unnecessarily for simple CRUD.

### 253. When should you use CQRS?

**Answer:** CQRS separates read and write models. It is useful when read and write workloads have different complexity, scale, or optimization needs, but it should not be used unnecessarily for simple CRUD.

### 254. What is MediatR used for?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 255. What is domain event?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 256. What is integration event?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 257. What is bounded context?

**Answer:** Clean Architecture separates domain, application, infrastructure, and presentation layers. The core business logic remains independent of frameworks, databases, and UI, making the system testable and maintainable.

### 258. How do you avoid anemic domain model?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 259. How do you structure a .NET solution for Clean Architecture?

**Answer:** Clean Architecture separates domain, application, infrastructure, and presentation layers. The core business logic remains independent of frameworks, databases, and UI, making the system testable and maintainable.

### 260. How do you explain Clean Architecture in an interview?

**Answer:** Clean Architecture separates domain, application, infrastructure, and presentation layers. The core business logic remains independent of frameworks, databases, and UI, making the system testable and maintainable.


## 14 Microservices & Distributed Systems

### 261. What is microservices architecture?

**Answer:** Microservices split a system into independently deployable services around business capabilities. They improve autonomy and scalability but add complexity in networking, observability, data consistency, and operations.

### 262. What is the difference between microservices and modular monolith?

**Answer:** Microservices split a system into independently deployable services around business capabilities. They improve autonomy and scalability but add complexity in networking, observability, data consistency, and operations.

### 263. When should you avoid microservices?

**Answer:** Microservices split a system into independently deployable services around business capabilities. They improve autonomy and scalability but add complexity in networking, observability, data consistency, and operations.

### 264. What is service boundary identification?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 265. What is database per service?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 266. What is distributed transaction problem?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 267. What is Saga pattern?

**Answer:** Saga manages distributed transactions using a sequence of local transactions and compensating actions. It avoids two-phase commit in microservices.

### 268. What is choreography-based saga?

**Answer:** Saga manages distributed transactions using a sequence of local transactions and compensating actions. It avoids two-phase commit in microservices.

### 269. What is orchestration-based saga?

**Answer:** Saga manages distributed transactions using a sequence of local transactions and compensating actions. It avoids two-phase commit in microservices.

### 270. What is eventual consistency?

**Answer:** Microservices split a system into independently deployable services around business capabilities. They improve autonomy and scalability but add complexity in networking, observability, data consistency, and operations.

### 271. What is idempotency?

**Answer:** Idempotency ensures repeated processing of the same request/message does not create duplicate side effects. Use idempotency keys, unique constraints, processed-message tables, or natural business keys.

### 272. What is outbox pattern?

**Answer:** Outbox pattern stores business data and integration events in the same database transaction, then publishes events asynchronously. It prevents data-update-success but event-publish-failure scenarios.

### 273. What is inbox pattern?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 274. What is API gateway pattern?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 275. What is service discovery?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 276. What is circuit breaker pattern?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 277. What is bulkhead pattern?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 278. What is retry storm?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 279. What is schema evolution?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 280. How do you design microservices for reliability?

**Answer:** Microservices split a system into independently deployable services around business capabilities. They improve autonomy and scalability but add complexity in networking, observability, data consistency, and operations.


## 15 Azure for .NET Developers

### 281. How do you deploy .NET APIs to Azure App Service?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 282. What is Azure App Service?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 283. What is Azure Functions?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 284. What is the difference between App Service and Azure Functions?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 285. What is Azure API Management?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 286. What is Azure Key Vault?

**Answer:** Secrets should be stored in a secure secret manager such as Azure Key Vault and accessed using Managed Identity. Avoid storing passwords, keys, or connection strings in source control.

### 287. What is Azure Service Bus?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 288. What is Azure Event Grid?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 289. What is Azure Event Hubs?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 290. What is Azure Storage Account?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 291. What is Azure Cosmos DB?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 292. What is Managed Identity in Azure?

**Answer:** Authentication proves who the caller is; authorization decides what the caller can do. In .NET APIs, this is commonly implemented using JWT bearer authentication, claims, roles, and policies.

### 293. How do you connect .NET app to Azure SQL securely?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 294. How do you use Key Vault references in App Service?

**Answer:** Secrets should be stored in a secure secret manager such as Azure Key Vault and accessed using Managed Identity. Avoid storing passwords, keys, or connection strings in source control.

### 295. What is private endpoint?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 296. What is VNet integration?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 297. What is Application Insights?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 298. How do you deploy .NET containers to AKS?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 299. What is Azure Container Apps?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 300. How do you design Azure hosting for enterprise .NET APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.


## 16 Containers, Kubernetes & KEDA

### 301. What is Docker?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 302. What is a Dockerfile?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 303. How do you containerize a .NET API?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 304. What is Kubernetes?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 305. What is a pod?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 306. What is deployment in Kubernetes?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 307. What is service in Kubernetes?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 308. What is ingress?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 309. What is ConfigMap?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 310. What is Secret?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 311. What is Horizontal Pod Autoscaler?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 312. What is KEDA?

**Answer:** KEDA provides event-driven autoscaling for Kubernetes workloads. For example, a .NET Worker can scale based on Azure Service Bus queue length instead of only CPU.

### 313. How does KEDA scale .NET workers?

**Answer:** KEDA provides event-driven autoscaling for Kubernetes workloads. For example, a .NET Worker can scale based on Azure Service Bus queue length instead of only CPU.

### 314. What is event-driven autoscaling?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 315. How do you scale based on Azure Service Bus queue length?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 316. What is readiness probe?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 317. What is liveness probe?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 318. How do you manage configuration in Kubernetes?

**Answer:** Containers package the .NET app with its runtime dependencies. Kubernetes/AKS manages deployment, scaling, service discovery, health probes, config, secrets, and rolling updates.

### 319. How do you secure container images?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 320. What are best practices for .NET on AKS?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.


## 17 Minimal APIs

### 321. What are minimal APIs in ASP.NET Core?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 322. When should you use minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 323. When should you avoid minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 324. How do you define routes in minimal API?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 325. How do you inject dependencies in minimal API handlers?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 326. How do you validate input in minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 327. How do you group endpoints?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 328. What is RouteGroupBuilder?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 329. How do you apply authorization to route groups?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 330. How do you return typed results?

**Answer:** LTS means Long-Term Support. For enterprise systems, LTS releases are preferred because they receive longer support, security fixes, and a safer upgrade window.

### 331. What are Results and TypedResults?

**Answer:** LTS means Long-Term Support. For enterprise systems, LTS releases are preferred because they receive longer support, security fixes, and a safer upgrade window.

### 332. How do you document minimal APIs using OpenAPI?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 333. How do you version minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 334. How do you handle errors in minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 335. How do filters work in minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 336. How do you test minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 337. How do you organize minimal APIs in large projects?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 338. What is endpoint filter?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 339. What are the limitations of minimal APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 340. How do minimal APIs compare with controllers?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.


## 18 gRPC, SignalR & Realtime

### 341. What is gRPC?

**Answer:** gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers. It is useful for internal service-to-service communication where strong contracts and performance matter.

### 342. When would you use gRPC instead of REST?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 343. What is Protocol Buffers?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 344. What is unary call in gRPC?

**Answer:** gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers. It is useful for internal service-to-service communication where strong contracts and performance matter.

### 345. What is server streaming?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 346. What is client streaming?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 347. What is bidirectional streaming?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 348. What is SignalR?

**Answer:** SignalR enables realtime server-to-client communication using WebSockets with fallbacks. Use it for notifications, dashboards, chat, and live updates.

### 349. When would you use SignalR?

**Answer:** SignalR enables realtime server-to-client communication using WebSockets with fallbacks. Use it for notifications, dashboards, chat, and live updates.

### 350. What is WebSocket?

**Answer:** SignalR enables realtime server-to-client communication using WebSockets with fallbacks. Use it for notifications, dashboards, chat, and live updates.

### 351. What is long polling?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 352. How does SignalR manage connections?

**Answer:** SignalR enables realtime server-to-client communication using WebSockets with fallbacks. Use it for notifications, dashboards, chat, and live updates.

### 353. What is a SignalR hub?

**Answer:** SignalR enables realtime server-to-client communication using WebSockets with fallbacks. Use it for notifications, dashboards, chat, and live updates.

### 354. How do you scale SignalR in Azure?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 355. What is Azure SignalR Service?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 356. How do you secure SignalR endpoints?

**Answer:** SignalR enables realtime server-to-client communication using WebSockets with fallbacks. Use it for notifications, dashboards, chat, and live updates.

### 357. What is message ordering challenge in realtime systems?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 358. How do you handle reconnects?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 359. How do you monitor realtime systems?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 360. What are common realtime architecture mistakes?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.


## 19 Configuration & Options

### 361. What are configuration providers in .NET?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 362. What is the order of configuration loading?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 363. How do environment variables override appsettings.json?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 364. What is User Secrets?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 365. What is the Options pattern?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 366. What is IOptions?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 367. What is IOptionsSnapshot?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 368. What is IOptionsMonitor?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 369. When do you use IOptionsMonitor?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 370. How do you validate options at startup?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 371. How do you manage feature flags?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 372. What is Azure App Configuration?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 373. How do you handle secrets in local development?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 374. How do you handle secrets in production?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 375. How do you configure per-environment settings?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 376. What is strongly typed configuration?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.

### 377. What is reloadOnChange?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 378. How do you manage connection strings securely?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 379. How do you configure logging per environment?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 380. How do you design configuration for cloud-native apps?

**Answer:** .NET configuration is loaded from providers such as appsettings.json, environment variables, command line, and secret stores. The Options pattern maps settings to strongly typed classes and supports validation.


## 20 Messaging & Event-Driven Architecture

### 381. What is event-driven architecture?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 382. What is the difference between command and event?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 383. What is a queue?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 384. What is a topic?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 385. What is pub/sub?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 386. What is Azure Service Bus?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 387. What is the difference between Service Bus Queue and Topic?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 388. What is dead-letter queue?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 389. What is message lock?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 390. What is duplicate detection?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 391. What is session-enabled queue?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 392. What is Kafka?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 393. What is consumer group?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 394. What is event ordering?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 395. What is poison message?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 396. How do you implement retries safely?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 397. What is exponential backoff?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 398. What is outbox pattern?

**Answer:** Outbox pattern stores business data and integration events in the same database transaction, then publishes events asynchronously. It prevents data-update-success but event-publish-failure scenarios.

### 399. What is idempotent consumer?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 400. How do you monitor message-based systems?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.


## 21 Files, Streams & Serialization

### 401. What is Stream in .NET?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 402. What is MemoryStream?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 403. What is FileStream?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 404. What is async file IO?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 405. What is JSON serialization?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 406. What is System.Text.Json?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 407. What is Newtonsoft.Json and when do you still use it?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 408. What is custom converter?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 409. How do you handle large file uploads?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 410. How do you stream large responses from API?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 411. What is multipart/form-data?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 412. How do you validate uploaded files?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 413. How do you prevent file upload attacks?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 414. What is compression middleware?

**Answer:** Middleware is a component in the ASP.NET Core request pipeline. Each middleware can inspect, modify, pass, or stop the request; examples include authentication, logging, CORS, exception handling, and routing.

### 415. What is Brotli compression?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 416. What is response buffering?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 417. What is UTF-8 encoding?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 418. What is Base64 encoding?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 419. How do you serialize circular references?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 420. How do you design APIs for large payloads?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.


## 22 Build, CI/CD & DevOps

### 421. What is dotnet CLI?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 422. What is dotnet restore?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 423. What is dotnet build?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 424. What is dotnet publish?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 425. What is self-contained deployment?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 426. What is framework-dependent deployment?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 427. What is single-file deployment?

**Answer:** Streams process data sequentially without loading everything into memory. For large uploads/downloads, use streaming, validation, content-type checks, and secure storage.

### 428. What is ReadyToRun compilation?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 429. What is CI/CD?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 430. How do you build .NET applications in Azure DevOps?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 431. How do you create a YAML pipeline for .NET?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 432. What steps should be in a .NET CI pipeline?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 433. How do you run tests in pipeline?

**Answer:** Testing should cover unit tests for business logic, integration tests for APIs/database, and contract tests for service boundaries. In ASP.NET Core, WebApplicationFactory is commonly used to test APIs end-to-end in memory.

### 434. How do you perform static code analysis?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 435. What is SonarQube?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 436. How do you deploy to Azure App Service?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 437. How do you deploy containers?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 438. How do you handle rollback?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 439. How do you manage environment approvals?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 440. What is blue-green deployment?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.


## 23 Memory Management & Runtime

### 441. What is CLR?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.

### 442. What is JIT compilation?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.

### 443. What is tiered compilation?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 444. What is garbage collection?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.

### 445. What is workstation GC?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 446. What is server GC?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 447. What is LOH?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 448. What is object allocation?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 449. What is boxing and unboxing?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 450. How do you avoid unnecessary allocations?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 451. What is IDisposable?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 452. What is IAsyncDisposable?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 453. What is using statement?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 454. What is finalizer?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 455. What is memory leak in managed code?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.

### 456. How do events cause memory leaks?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 457. What is weak reference?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 458. What is stack vs heap?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 459. What is Span<T>?

**Answer:** In interview, define the concept clearly, explain why it is used, give a practical .NET example, and mention trade-offs such as performance, maintainability, security, and operational complexity.

### 460. How do you troubleshoot high memory usage?

**Answer:** The CLR manages execution, JIT compilation, memory, garbage collection, exceptions, and type safety. Performance tuning involves reducing allocations, avoiding leaks, profiling, and understanding GC behavior.


## 24 Advanced .NET Interview Scenarios

### 461. How would you design a high-throughput order API in .NET 10?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 462. How would you migrate a monolith to .NET 10 microservices?

**Answer:** Microservices split a system into independently deployable services around business capabilities. They improve autonomy and scalability but add complexity in networking, observability, data consistency, and operations.

### 463. How would you troubleshoot intermittent 500 errors in ASP.NET Core?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 464. How would you handle 10x traffic increase?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 465. How would you design a secure file upload API?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 466. How would you process one million messages per day?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 467. How would you design retry and dead-letter handling?

**Answer:** Messaging decouples producers and consumers. Queues are point-to-point, topics are publish/subscribe, and dead-letter queues store messages that cannot be processed after retries.

### 468. How would you implement multi-tenant APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 469. How would you handle per-tenant database isolation?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 470. How would you design role-based and policy-based authorization?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 471. How would you optimize slow EF Core queries?

**Answer:** EF Core is Microsoft's ORM for .NET. It maps domain objects to relational data and supports LINQ, migrations, transactions, and change tracking.

### 472. How would you replace EF Core with Dapper for hot paths?

**Answer:** EF Core is a full ORM with change tracking, LINQ, relationships, and migrations. Dapper is a micro ORM where we write SQL manually and get fast object mapping; use Dapper for optimized queries and EF Core for productivity/domain CRUD.

### 473. How would you implement audit logging?

**Answer:** Observability combines logs, metrics, and traces to understand production behavior. In .NET, use structured ILogger logs, correlation IDs, health checks, OpenTelemetry/Application Insights, and dashboards for latency, errors, and dependency health.

### 474. How would you build observability for distributed APIs?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 475. How would you detect and fix thread pool starvation?

**Answer:** Async/await improves scalability for IO-bound work by releasing the thread while waiting. It does not make CPU-bound code faster; CPU work needs parallelism or background processing.

### 476. How would you design zero-downtime deployment?

**Answer:** A production .NET CI/CD pipeline should restore, build, run tests, scan code/dependencies, publish artifacts/container images, deploy with approvals, and support rollback.

### 477. How would you secure APIs exposed to partners?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 478. How would you implement API throttling?

**Answer:** A production API should use correct HTTP verbs, clear resource URLs, validation, consistent status codes, versioning, authentication, logging, rate limits, and backward-compatible contracts.

### 479. How would you manage secrets across environments?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 480. How would you explain your .NET architecture to an interviewer?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.


## 25 Scenario-Based Final Round

### 481. Tell me about a complex .NET system you designed.

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 482. How do you decide between monolith, modular monolith, and microservices?

**Answer:** Microservices split a system into independently deployable services around business capabilities. They improve autonomy and scalability but add complexity in networking, observability, data consistency, and operations.

### 483. How do you decide between SQL and NoSQL?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 484. How do you handle stakeholder-driven changing requirements?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 485. How do you convert business requirements into technical architecture?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 486. How do you define non-functional requirements?

**Answer:** For Azure-hosted .NET systems, choose services based on workload: App Service for APIs, Functions for event/serverless jobs, Service Bus for reliable messaging, Cosmos DB for globally distributed NoSQL, Key Vault for secrets, and Application Insights for monitoring.

### 487. How do you design for availability?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 488. How do you design for disaster recovery?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 489. How do you design for cost optimization?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 490. How do you design for security by default?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 491. How do you review code as an architect?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 492. How do you mentor junior developers?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 493. How do you handle production incidents?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 494. How do you communicate technical risks?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 495. How do you choose libraries and frameworks?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 496. How do you prevent over-engineering?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 497. How do you document architecture decisions?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 498. What are ADRs?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 499. How do you measure architecture success?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.

### 500. What is your final .NET 10 architecture checklist?

**Answer:** Answer using architecture flow: clarify requirements, identify NFRs, define boundaries, select technology, cover security/scalability/observability, explain trade-offs, and connect it to a real project example.


---
Total answers: 500
