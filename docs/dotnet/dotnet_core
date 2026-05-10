# .NET Core Interview Question & Answer List

> GitHub-friendly format: **Question Summary → Crisp Answer → Detailed Explanation → Final Interview Answer**


---


## Table of Contents

- [1. What is .NET Core?
](#1-what-is-net-core)
- [2. Difference between .NET Framework and .NET Core?
](#2-difference-between-net-framework-and-net-core)
- [3. What is middleware in ASP.NET Core?
](#3-what-is-middleware-in-aspnet-core)
- [4. Explain dependency injection and where it is used.
](#4-explain-dependency-injection-and-where-it-is-used)
- [5. Difference between Singleton, Scoped, and Transient services?
](#5-difference-between-singleton-scoped-and-transient-services)
- [6. What is routing in ASP.NET Core?
](#6-what-is-routing-in-aspnet-core)
- [7. What is model binding?
](#7-what-is-model-binding)
- [8. How do you validate model in .NET Core?
](#8-how-do-you-validate-model-in-net-core)
- [9. What is JWT authentication?
](#9-what-is-jwt-authentication)
- [10. What is authorization?
](#10-what-is-authorization)
- [11. What is EF Core?
](#11-what-is-ef-core)
- [12. What is DbContext?
](#12-what-is-dbcontext)
- [13. What is AsNoTracking() and where is it used?
](#13-what-is-asnotracking-and-where-is-it-used)
- [14. Difference between First, FirstOrDefault, Single, and SingleOrDefault?
](#14-difference-between-first-firstordefault-single-and-singleordefault)
- [15. What is async/await and why is it used?
](#15-what-is-asyncawait-and-why-is-it-used)
- [16. What is repository pattern?
](#16-what-is-repository-pattern)
- [17. What is Clean Architecture in .NET Core?
](#17-what-is-clean-architecture-in-net-core)
- [18. What is Minimal API?
](#18-what-is-minimal-api)
- [19. What is Swagger/OpenAPI?
](#19-what-is-swaggeropenapi)
- [20. What is CORS and how do you implement it?
](#20-what-is-cors-and-how-do-you-implement-it)
- [21. What is HttpClientFactory?
](#21-what-is-httpclientfactory)
- [22. What is caching in .NET Core?
](#22-what-is-caching-in-net-core)
- [23. What is rate limiting?
](#23-what-is-rate-limiting)
- [24. What is background service in .NET Core?
](#24-what-is-background-service-in-net-core)
- [25. How do you secure a .NET Core API?
](#25-how-do-you-secure-a-net-core-api)
- [26. How do you improve API performance?
](#26-how-do-you-improve-api-performance)
- [27. What is circuit breaker pattern?
](#27-what-is-circuit-breaker-pattern)
- [28. What is idempotency in API?
](#28-what-is-idempotency-in-api)
- [29. What is correlation ID?
](#29-what-is-correlation-id)
- [30. What is OpenTelemetry?
](#30-what-is-opentelemetry)
- [31. How do you deploy a .NET Core API?
](#31-how-do-you-deploy-a-net-core-api)

---


## 1. What is .NET Core?



### Question Summary

> Tests whether you understand the modern .NET platform and where it is used.


### Crisp Answer

- .NET Core is a cross-platform, open-source development platform from Microsoft.
- It is used to build web APIs, web apps, microservices, background services, and cloud-native applications.
- It runs on Windows, Linux, and macOS.
- It is lightweight, modular, high-performance, and container-friendly.
- Modern .NET versions evolved from .NET Core and are commonly used for enterprise application modernization.

### Detailed Explanation

- .NET Core was introduced as a modern alternative to the traditional .NET Framework.
- The biggest advantage is cross-platform support, which means the same application can run on Windows, Linux, and macOS.
- It is also open-source and optimized for performance.
- In enterprise projects, .NET Core is widely used for building REST APIs, microservices, cloud-native applications, worker services, and containerized applications.
- It supports dependency injection, middleware pipeline, configuration, logging, health checks, and modern deployment models like Docker and Kubernetes.

### Final Interview Answer

> .NET Core is a modern, cross-platform, open-source framework from Microsoft used for building APIs, microservices, web applications, and cloud-native systems. Compared to the older .NET Framework, it is lightweight, faster, modular, and container-friendly. In enterprise applications, I use it mainly for building scalable Web APIs, background services, and microservices that can run on Windows, Linux, containers, or cloud platforms like Azure.


---


## 2. Difference between .NET Framework and .NET Core?



### Question Summary

> Tests whether you know why modern projects prefer .NET Core/.NET over the older .NET Framework.


### Crisp Answer

- .NET Framework is Windows-only and mainly used for legacy ASP.NET MVC, WebForms, WCF, and Windows applications. .NET Core is cross-platform, open-source, lightweight, and cloud-friendly. .NET Core supports modern APIs, microservices, containers, and better performance.
- For new development, .NET/.NET Core is preferred unless there is a legacy dependency on .NET Framework.

### Detailed Explanation

- .NET Framework is the older Microsoft framework that runs only on Windows.
- It is still used in legacy enterprise applications, especially WebForms, older MVC applications, WCF, and Windows desktop applications. .NET Core was designed to be cross-platform, modular, and optimized for modern workloads.
- It supports containerization, cloud-native development, microservices, and high-performance APIs.
- Modern .NET versions are the continuation of .NET Core.
- For greenfield development, .NET is preferred because it supports modern deployment, better performance, and faster evolution.

### Final Interview Answer

> .NET Framework is Windows-only and mostly used in legacy enterprise applications. .NET Core, now evolved into modern .NET, is cross-platform, open-source, lightweight, and optimized for cloud-native applications. For new APIs and microservices, I prefer .NET because it supports Linux hosting, containers, better performance, dependency injection, middleware, and modern DevOps deployment.


---


## 3. What is middleware in ASP.NET Core?



### Question Summary

> Tests whether you understand the ASP.NET Core request processing pipeline.


### Crisp Answer

- Middleware is a component in the ASP.NET Core HTTP request pipeline.
- Each middleware can inspect, modify, pass, or short-circuit a request.
- It is used for cross-cutting concerns like exception handling, logging, routing, `CORS`, authentication, authorization, compression, and static files.
- Middleware order is important because requests flow through middleware sequentially.

### Detailed Explanation

- ASP.NET Core processes every request through a pipeline of middleware components.
- Each middleware receives the HttpContext and decides whether to process the request, pass it to the next middleware, or stop the pipeline.
- For example, exception middleware should come early, routing should happen before authorization, and authentication should run before authorization.
- Middleware is useful because it centralizes common concerns and avoids repeating logic inside controllers.

### Final Interview Answer

> Middleware is a component in the ASP.NET Core request pipeline that handles cross-cutting concerns. For example, logging, exception handling, routing, `CORS`, authentication, and authorization are implemented as middleware. The request passes through middleware in order, so ordering is important. I use middleware to keep controllers clean and centralize common request/response processing.


---


## 4. Explain dependency injection and where it is used.



### Question Summary

> Tests whether you understand loose coupling, testability, and built-in DI in .NET Core.


### Crisp Answer

- Dependency Injection is a design pattern where dependencies are provided from outside instead of being created inside the class.
- ASP.NET Core has built-in DI.
- It is used in controllers, services, repositories, `DbContext`, logging, configuration, and external API clients.
- It improves loose coupling, unit testing, maintainability, and lifetime management.

### Detailed Explanation

- Without DI, a class directly creates its dependencies using new, which creates tight coupling.
- With DI, dependencies are injected through constructor parameters.
- ASP.NET Core manages object creation through the service container.
- Services are registered with lifetimes such as `Singleton`, `Scoped`, or `Transient`.
- DI is heavily used in enterprise applications because it allows replacing implementations, mocking dependencies during unit testing, and managing service lifetimes centrally.

### Final Interview Answer

> Dependency Injection means injecting required dependencies into a class instead of creating them inside the class. In ASP.NET Core, DI is built in and used for controllers, services, repositories, `DbContext`, logging, configuration, and HTTP clients. It improves loose coupling, testability, and maintainability. For example, a controller depends on an interface like IEmployeeService, and the concrete implementation is registered in `Program.cs`.


---


## 5. Difference between Singleton, Scoped, and Transient services?



### Question Summary

> Tests whether you understand service lifetimes and object creation in ASP.NET Core DI.


### Crisp Answer

- `Singleton` creates one instance for the entire application lifetime.
- `Scoped` creates one instance per HTTP request.
- `Transient` creates a new instance every time the service is requested.
- `Singleton` is good for stateless shared services or cache.
- `Scoped` is good for `DbContext`, repositories, and business services.
- `Transient` is good for lightweight stateless services.

### Detailed Explanation

- Service lifetime is important because it controls how long an object lives.
- `Singleton` objects are shared across all requests, so they must be thread-safe and should not store request-specific data.
- `Scoped` objects are created once per request and are commonly used with EF Core `DbContext`.
- `Transient` objects are created every time they are injected.
- A common mistake is injecting a `Scoped` service into a `Singleton` service, which can cause lifetime and stale-data issues.

### Final Interview Answer

> `Singleton` means one instance for the whole application, `Scoped` means one instance per HTTP request, and `Transient` means a new instance every time. I use `Scoped` for `DbContext`, repositories, and request-level business services. I use `Singleton` for stateless, thread-safe services like cache or configuration helpers. I use `Transient` for lightweight stateless services. I avoid injecting `Scoped` services directly into `Singleton` services.


---


## 6. What is routing in ASP.NET Core?



### Question Summary

> Tests whether you understand how URLs map to endpoints or controller actions.


### Crisp Answer

- Routing maps incoming HTTP requests to controller actions or minimal API endpoints.
- It uses URL patterns, HTTP verbs, route parameters, and attributes.
- Attribute routing is commonly used in Web APIs.
- Routing helps define clean and predictable API endpoints.

### Detailed Explanation

- In ASP.NET Core, routing is responsible for matching an incoming request to the correct endpoint.
- For example, GET /api/employees/10 can map to an EmployeesController action with [HttpGet("{id}")].
- Routing can be conventional or attribute-based.
- Web APIs commonly use attribute routing because it gives explicit control over endpoint URLs and HTTP methods.

### Final Interview Answer

> Routing is the mechanism that maps an incoming URL and HTTP verb to a specific controller action or endpoint. In Web API, I usually use attribute routing like [Route("api/[controller]")] and [HttpGet("{id}")]. It makes APIs clear, REST-friendly, and easier to maintain.


---


## 7. What is model binding?



### Question Summary

> Tests whether you know how ASP.NET Core maps request data to action parameters.


### Crisp Answer

- Model binding maps HTTP request data to action parameters or model objects.
- It can bind data from route values, query strings, request body, headers, and form data.
- For APIs, [`FromBody`], [`FromQuery`], [`FromRoute`], and [`FromHeader`] can be used to specify the source.

### Detailed Explanation

- When a request comes to an action method, ASP.NET Core automatically tries to populate method parameters from the request.
- For example, route values can bind to id, query string can bind to filters, and JSON body can bind to a DTO.
- Model binding reduces manual parsing and helps keep action methods clean.
- In Web APIs, complex objects are usually read from the request body.

### Final Interview Answer

> Model binding automatically maps request data to action method parameters or DTOs. For example, route id, query parameters, headers, and JSON body can be bound to C# objects. This avoids manual parsing of request data. In APIs, I use [`FromBody`] for request payloads, [`FromRoute`] for route values, and [`FromQuery`] for filters.


---


## 8. How do you validate model in .NET Core?



### Question Summary

> Tests whether you understand request validation and API input safety.


### Crisp Answer

- Model validation checks whether incoming data satisfies validation rules.
- In .NET Core, we can use data annotations like [Required], [EmailAddress], [Range], and [StringLength].
- With [`ApiController`], invalid models automatically return 400 Bad Request.
- For complex rules, `FluentValidation` can be used.

### Detailed Explanation

- Input validation is important because APIs should not process invalid or incomplete data.
- Data annotations are simple and work well for common validations.
- ASP.NET Core stores validation errors in `ModelState`.
- In controllers with [`ApiController`], the framework automatically returns a validation error response when `ModelState` is invalid.
- For advanced validation involving multiple fields or business rules, `FluentValidation` is preferred.

### Final Interview Answer

> In .NET Core, I validate models using data annotations or `FluentValidation`. For basic validation, I use attributes like [Required], [EmailAddress], and [Range] on DTO properties. With [`ApiController`], ASP.NET Core automatically returns 400 Bad Request if validation fails. For complex business validations, I prefer `FluentValidation` because it keeps validation rules clean and testable.


---


## 9. What is JWT authentication?



### Question Summary

> Tests whether you understand token-based authentication in APIs.


### Crisp Answer

- `JWT` authentication uses a signed JSON Web Token to authenticate API requests.
- A `JWT` has three parts: header, payload, and signature.
- The client sends the token in the Authorization header as Bearer token.
- The API validates signature, issuer, audience, expiry, and claims before allowing access.

### Detailed Explanation

- `JWT` is commonly used in stateless APIs.
- After login, the identity provider issues an access token.
- The client sends this token with every API request.
- The API validates the token and reads claims such as user id, role, email, or permissions.
- `JWT` is useful in microservices and distributed systems because the server does not need to store session state.
- However, token expiry, refresh tokens, signing keys, and secure storage must be handled carefully.

### Final Interview Answer

> `JWT` is a token-based authentication mechanism used in Web APIs. The user logs in and receives a token containing claims. The client sends it as Authorization: Bearer token. The API validates the signature, issuer, audience, expiry, and claims. After authentication, authorization is applied using roles, policies, or claims.


---


## 10. What is authorization?



### Question Summary

> Tests whether you understand access control after authentication.


### Crisp Answer

- Authentication verifies who the user is.
- Authorization verifies what the user is allowed to do.
- In ASP.NET Core, authorization can be role-based, policy-based, claim-based, or resource-based.
- It is applied using [`Authorize`], roles, policies, and custom handlers.

### Detailed Explanation

- After a user is authenticated, the application must decide what resources or operations the user can access.
- For example, an Admin may access user management APIs, while a normal user cannot.
- ASP.NET Core supports role-based authorization with [`Authorize`(Roles="Admin")] and policy-based authorization for more complex rules.
- In enterprise systems, authorization should be enforced at the API and service layer, not only at UI level.

### Final Interview Answer

> Authorization controls what an authenticated user can access. In ASP.NET Core, I can use [`Authorize`], role-based authorization, claims, or policies. For enterprise applications, I prefer policy-based authorization because it is more flexible and supports business rules like department, permission, role, or resource ownership.


---


## 11. What is EF Core?



### Question Summary

> Tests whether you understand ORM-based data access in .NET Core.


### Crisp Answer

- Entity Framework Core is an Object Relational Mapper that allows developers to work with databases using C# objects.
- It supports LINQ queries, change tracking, relationships, migrations, and transactions.
- It reduces boilerplate SQL for common CRUD operations.

### Detailed Explanation

- EF Core maps database tables to C# entity classes.
- `DbContext` represents a database session, and `DbSet` represents a table.
- Developers can write LINQ queries instead of raw SQL.
- EF Core tracks entity changes and saves them using SaveChanges.
- It is useful for maintainable CRUD applications, but for highly optimized queries, raw SQL or Dapper may be preferred.

### Final Interview Answer

> EF Core is an ORM used to interact with databases using C# entities and LINQ instead of writing SQL for every operation. It provides `DbContext`, `DbSet`, change tracking, migrations, relationships, and transaction support. I use EF Core for maintainable CRUD operations, and I optimize read-heavy queries using `AsNoTracking`, projection, indexing, and pagination.


---


## 12. What is DbContext?



### Question Summary

> Tests whether you understand the central EF Core object used for data access.


### Crisp Answer

- `DbContext` represents a session with the database.
- It is used to query data, track changes, and save updates.
- It contains `DbSet` properties that represent database tables.
- In ASP.NET Core, `DbContext` is usually registered as `Scoped`.

### Detailed Explanation

- `DbContext` is the main class in EF Core.
- It manages database connection, entity tracking, change detection, query execution, and persistence.
- `DbSet`<TEntity> inside `DbContext` represents tables.
- Because `DbContext` tracks changes during a request, it should usually be registered as `Scoped`, meaning one instance per HTTP request.

### Final Interview Answer

> `DbContext` is the EF Core session object used to query and save data. It contains `DbSet` properties for tables and tracks entity changes. In Web APIs, I register `DbContext` as `Scoped` because it should live for one request. It also behaves like a Unit of Work because it tracks changes and commits them using SaveChanges.


---


## 13. What is AsNoTracking() and where is it used?



### Question Summary

> Tests whether you understand EF Core performance optimization for read-only queries.


### Crisp Answer

- `AsNoTracking`() tells EF Core not to track returned entities in the change tracker.
- It is used for read-only queries where the entity will not be updated.
- It improves performance and reduces memory usage.

### Detailed Explanation

- By default, EF Core tracks queried entities so it can detect changes and update them later.
- This tracking has memory and CPU overhead.
- For read-only APIs, reports, dropdowns, and list screens, tracking is unnecessary.
- `AsNoTracking` improves performance by skipping change tracking.
- However, if we want to update an entity after fetching it, we should not use `AsNoTracking` unless we attach the entity manually.

### Final Interview Answer

> `AsNoTracking`() is used in EF Core for read-only queries. It tells EF not to track the returned entities, which improves performance and reduces memory usage. I use it in GET APIs, reports, search screens, and dropdown data where I do not plan to update the entity.


---


## 14. Difference between First, FirstOrDefault, Single, and SingleOrDefault?



### Question Summary

> Tests whether you understand LINQ result expectations and exception behavior.


### Crisp Answer

- First returns the first matching record and throws if no record exists.
- FirstOrDefault returns the first record or default/null if none exists.
- Single expects exactly one record and throws if none or more than one exists.
- SingleOrDefault allows zero or one record but throws if more than one exists.

### Detailed Explanation

- These methods should be chosen based on the business expectation.
- If multiple records are allowed and we only need the first one, use FirstOrDefault.
- If the business rule expects exactly one matching record, use Single or SingleOrDefault.
- Single is stricter and can reveal data quality issues when duplicates exist.
- Both Single and SingleOrDefault throw an exception if more than one record matches.

### Final Interview Answer

> I use FirstOrDefault when I need the first matching record and zero records are acceptable. I use Single when exactly one record must exist. I use SingleOrDefault when zero or one record is acceptable. If two records match, both Single and SingleOrDefault throw an exception because they expect uniqueness.


---


## 15. What is async/await and why is it used?



### Question Summary

> Tests whether you understand asynchronous programming and API scalability.


### Crisp Answer

- `async/await` is used for asynchronous programming in .NET.
- It prevents blocking threads while waiting for I/O operations like database calls, file access, or HTTP calls.
- It improves scalability because the server can handle more concurrent requests.

### Detailed Explanation

- In web applications, many operations are I/O-bound.
- If a thread blocks while waiting for a database or external API, scalability reduces.
- `async/await` allows the thread to be released while the operation is pending.
- When the operation completes, execution resumes.
- This does not necessarily make one request faster, but it improves overall throughput under load.

### Final Interview Answer

> `async/await` is used to write asynchronous code in a readable way. In Web APIs, I use it for database calls, external API calls, file operations, and queue operations. It prevents thread blocking and improves scalability because server threads can handle other requests while waiting for I/O to complete.


---


## 16. What is repository pattern?



### Question Summary

> Tests whether you understand abstraction of data access logic.


### Crisp Answer

- Repository pattern abstracts data access behind an interface.
- The service layer depends on repository interfaces instead of direct database code.
- It improves separation of concerns, testability, and maintainability.

### Detailed Explanation

- A repository encapsulates queries and persistence logic for an aggregate or entity.
- The service layer calls repository methods like GetByIdAsync, AddAsync, or DeleteAsync instead of directly writing EF queries everywhere.
- This centralizes data access and makes unit testing easier using mocks.
- However, with EF Core, overusing generic repositories can add unnecessary abstraction because `DbContext` already provides repository-like behavior.

### Final Interview Answer

> Repository pattern separates data access logic from business logic. The service layer talks to an interface like IEmployeeRepository instead of directly querying the database. This improves testability and maintainability. In EF Core projects, I use repositories carefully, mainly when I need clear domain boundaries or complex data access abstraction.


---


## 17. What is Clean Architecture in .NET Core?



### Question Summary

> Tests whether you understand maintainable enterprise application structure.


### Crisp Answer

- Clean Architecture separates the application into layers such as API, Application, Domain, and Infrastructure.
- The Domain layer contains business rules and should not depend on external frameworks.
- Dependencies point inward.
- This improves testability, maintainability, and technology independence.

### Detailed Explanation

- In Clean Architecture, the API layer handles HTTP concerns.
- The Application layer contains use cases, commands, queries, DTOs, and interfaces.
- The Domain layer contains core entities and business rules.
- The Infrastructure layer implements external concerns like database, email, storage, and third-party integrations.
- The key rule is dependency inversion: inner layers should not depend on outer layers.

### Final Interview Answer

> Clean Architecture organizes a .NET Core application into API, Application, Domain, and Infrastructure layers. Domain contains core business rules, Application contains use cases, Infrastructure contains database and external integrations, and API exposes endpoints. Dependencies point inward, which makes the system testable, maintainable, and loosely coupled.


---


## 18. What is Minimal API?



### Question Summary

> Tests whether you know lightweight API development in ASP.NET Core.


### Crisp Answer

- `Minimal API` allows building HTTP APIs with minimal ceremony without controllers.
- Endpoints are defined directly in `Program.cs` or endpoint extension methods.
- It is useful for small services, microservices, health endpoints, and lightweight APIs.

### Detailed Explanation

- Traditional Web API uses controllers and attributes.
- `Minimal API` allows defining endpoints using methods like MapGet, MapPost, MapPut, and MapDelete.
- It reduces boilerplate and is good for small services or microservices.
- For large enterprise APIs, controllers may still be preferred for structure, filters, versioning, and separation.

### Final Interview Answer

> `Minimal API` is a lightweight way to create APIs in ASP.NET Core without controllers. It uses endpoint mappings like app.MapGet and app.MapPost. I use it for small microservices, health checks, internal APIs, or lightweight endpoints. For larger enterprise APIs, I may still prefer controllers for better organization.


---


## 19. What is Swagger/OpenAPI?



### Question Summary

> Tests whether you understand API documentation and testing support.


### Crisp Answer

- Swagger/OpenAPI provides interactive documentation for APIs.
- It shows available endpoints, request/response models, status codes, and allows testing APIs from the browser.
- In .NET Core, it is commonly enabled using Swashbuckle.

### Detailed Explanation

- `Swagger` is very useful during API development because frontend developers, testers, and integration teams can understand and test APIs without reading code.
- It also helps generate API clients and `OpenAPI` contracts.
- In production, `Swagger` access may be restricted based on security requirements.

### Final Interview Answer

> Swagger/OpenAPI is used to document and test APIs. It provides a UI where developers can see endpoints, request parameters, response schemas, and test API calls. In .NET Core, I usually add `Swagger` during development and restrict or secure it in production environments.


---


## 20. What is CORS and how do you implement it?



### Question Summary

> Tests whether you understand browser cross-origin security.


### Crisp Answer

- `CORS` stands for Cross-Origin Resource Sharing.
- It controls whether a browser allows a frontend from one origin to call an API on another origin.
- In ASP.NET Core, we define a `CORS` policy with allowed origins, methods, and headers, then apply it in the middleware pipeline.

### Detailed Explanation

- `CORS` is enforced by browsers.
- For example, an Angular app running on localhost:4200 may call an API running on localhost:5001.
- Without proper `CORS` policy, the browser blocks the request.
- In production, we should allow only trusted origins and avoid AllowAnyOrigin for secured APIs.

### Final Interview Answer

> `CORS` is a browser security feature that controls cross-origin API calls. In ASP.NET Core, I configure a `CORS` policy with allowed origins, headers, and methods, then use app.`UseCors`(). For production, I allow only trusted frontend domains instead of using AllowAnyOrigin.


---


## 21. What is HttpClientFactory?



### Question Summary

> Tests whether you understand safe and scalable external HTTP calls.


### Crisp Answer

- `IHttpClientFactory` is used to create and manage HttpClient instances properly.
- It avoids socket exhaustion and supports named clients, typed clients, logging, resilience policies, and centralized configuration.

### Detailed Explanation

- Creating new HttpClient objects repeatedly can cause socket exhaustion.
- Keeping one static HttpClient can create DNS refresh issues.
- `IHttpClientFactory` solves these problems by managing underlying handlers and lifetimes.
- It also integrates well with Polly for retry, timeout, and circuit breaker policies.

### Final Interview Answer

> `HttpClientFactory` is the recommended way to call external HTTP services in .NET Core. It manages HttpClient lifecycle, avoids socket exhaustion, supports named and typed clients, and integrates with resilience policies like retry and circuit breaker. I use it for external API integrations.


---


## 22. What is caching in .NET Core?



### Question Summary

> Tests whether you understand performance optimization using cached data.


### Crisp Answer

- Caching stores frequently used data so the application can avoid repeated expensive operations. .NET Core supports in-memory cache, distributed cache, response caching, and external caches like Redis.
- Caching improves performance and reduces database/API load.

### Detailed Explanation

- In-memory cache stores data inside the application process and is suitable for single-instance applications or non-critical cache.
- Distributed cache stores cache outside the app, such as Redis, and works across multiple instances.
- Cache must be used carefully with expiration, invalidation, and consistency strategy.

### Final Interview Answer

> Caching is used to improve performance by storing frequently accessed data. In .NET Core, I can use IMemoryCache for single-instance scenarios and distributed cache like Redis for multi-instance applications. I use caching for lookup data, configuration, expensive queries, and frequently requested read-only data.


---


## 23. What is rate limiting?



### Question Summary

> Tests whether you understand API protection and traffic control.


### Crisp Answer

- Rate limiting controls how many requests a client can make within a time window.
- It protects APIs from abuse, accidental overload, brute force attempts, and cost spikes.
- It can be applied per IP, user, API key, route, or tenant.

### Detailed Explanation

- Rate limiting is important for public APIs and high-cost operations.
- For example, login APIs should limit repeated attempts, and AI APIs should limit calls to control cost.
- If the limit is exceeded, the API usually returns 429 Too Many Requests.
- Rate limiting can be implemented in ASP.NET Core, API Gateway, Azure API Management, or reverse proxies.

### Final Interview Answer

> Rate limiting protects APIs by controlling request volume. It prevents abuse, overload, and unnecessary cost. I usually apply it at API gateway level or application level based on IP, user, tenant, or API key. When the limit is exceeded, the client receives 429 Too Many Requests.


---


## 24. What is background service in .NET Core?



### Question Summary

> Tests whether you know how to run long-running or scheduled tasks.


### Crisp Answer

- A background service runs tasks outside the normal HTTP request pipeline.
- In .NET Core, it is implemented using `BackgroundService` or `IHostedService`.
- It is used for queue processing, scheduled jobs, polling, notifications, cleanup tasks, and background workflows.

### Detailed Explanation

- Web APIs should not perform long-running work inside the request if it can delay response or cause timeout.
- Instead, the API can enqueue work and a background service can process it.
- Background services run with the application host and should handle cancellation tokens, exceptions, retries, and graceful shutdown properly.

### Final Interview Answer

> `BackgroundService` is used to run long-running or recurring tasks in .NET Core. I use it for queue processing, scheduled cleanup, notification sending, or background integration jobs. It runs outside the HTTP request pipeline and should support cancellation, logging, retry handling, and graceful shutdown.


---


## 25. How do you secure a .NET Core API?



### Question Summary

> Tests whether you understand API security best practices.


### Crisp Answer

- Secure a .NET Core API using HTTPS, authentication, authorization, input validation, `CORS` restrictions, rate limiting, secure headers, secrets management, logging, dependency updates, parameterized queries, and proper error handling.
- Sensitive secrets should be stored in Key Vault or secure configuration.

### Detailed Explanation

- API security is layered.
- Transport must be secured using HTTPS.
- Authentication verifies user identity and authorization controls access.
- Input validation prevents invalid data and injection attacks.
- `CORS` should allow only trusted origins.
- Secrets should not be stored in code.
- Logs should avoid sensitive data.
- APIs should also use rate limiting, centralized exception handling, and monitoring for suspicious activity.

### Final Interview Answer

> I secure .NET Core APIs with HTTPS, JWT/OAuth authentication, policy-based authorization, input validation, `CORS` restrictions, rate limiting, secure secret storage, and global exception handling. I also avoid exposing stack traces, use parameterized queries, log security events, and monitor failed authentication or unusual traffic patterns.


---


## 26. How do you improve API performance?



### Question Summary

> Tests whether you can optimize .NET APIs beyond basic coding.


### Crisp Answer

- Improve API performance using `async/await`, efficient database queries, `AsNoTracking`, pagination, caching, proper indexes, response compression, DTO projection, avoiding SELECT *, reducing unnecessary joins, connection pooling, and monitoring slow endpoints.

### Detailed Explanation

- Performance bottlenecks usually come from database queries, external API calls, serialization, large payloads, inefficient loops, or blocking calls.
- First measure using logs, Application Insights, profiling, and execution plans.
- Then optimize queries, add indexes, reduce payload size, cache read-heavy data, and avoid blocking threads.
- Performance optimization should be evidence-based, not guesswork.

### Final Interview Answer

> I improve API performance by measuring first, then optimizing. Common actions include async I/O, `AsNoTracking` for read-only EF queries, projection to DTOs, pagination, caching, proper indexing, avoiding SELECT *, response compression, and optimizing external API calls with timeout and retry policies. I also monitor latency, throughput, errors, and database execution plans.


---


## 27. What is circuit breaker pattern?



### Question Summary

> Tests whether you understand resilience when dependencies fail.


### Crisp Answer

- Circuit breaker prevents repeated calls to a failing dependency.
- It has states like Closed, Open, and Half-Open.
- When failures cross a threshold, the circuit opens and calls fail fast.
- After a cooldown, it allows limited calls to check recovery.

### Detailed Explanation

- In distributed systems, repeated calls to a failing service can increase latency, consume resources, and worsen the outage.
- Circuit breaker protects the application by stopping calls temporarily.
- It is usually combined with timeout, retry, fallback, and monitoring.
- In .NET, Polly is commonly used to implement circuit breaker.

### Final Interview Answer

> Circuit breaker is a resilience pattern used when an external dependency is failing. Instead of repeatedly calling the failing service, the circuit opens and fails fast. After some time, it moves to half-open to test recovery. I use it with Polly for external APIs, payment gateways, notification services, and unstable dependencies.


---


## 28. What is idempotency in API?



### Question Summary

> Tests whether you understand safe retry behavior and duplicate prevention.


### Crisp Answer

- Idempotency means calling the same operation multiple times has the same effect as calling it once.
- GET, PUT, and DELETE are generally idempotent.
- POST is usually not idempotent, but it can be made idempotent using an idempotency key.

### Detailed Explanation

- Idempotency is important for payment, order creation, booking, and distributed systems where retries may happen due to timeouts.
- Without idempotency, a retry can create duplicate orders or duplicate payments.
- An idempotency key allows the server to recognize repeated requests and return the same result instead of creating a duplicate action.

### Final Interview Answer

> Idempotency means repeated calls produce the same result without duplicate side effects. It is critical in payment, order, and booking APIs. For POST operations, I use an idempotency key so retries do not create duplicate records or transactions. This makes APIs safer under network failures and retries.


---


## 29. What is correlation ID?



### Question Summary

> Tests whether you understand traceability in distributed systems.


### Crisp Answer

- Correlation ID is a unique identifier assigned to a request and passed across services.
- It helps trace one request end-to-end across APIs, services, logs, queues, and external dependencies.

### Detailed Explanation

- In microservices, one user request may pass through multiple services.
- Without correlation ID, it is difficult to debug failures.
- A correlation ID is added at the entry point and propagated in headers and logs.
- It allows teams to search logs and reconstruct the full journey of a request.

### Final Interview Answer

> Correlation ID is used to trace a request across multiple services. I generate or accept a correlation ID at the API boundary, pass it to downstream services, and include it in logs. This helps debugging, monitoring, and root cause analysis in distributed systems.


---


## 30. What is OpenTelemetry?



### Question Summary

> Tests whether you understand modern observability.


### Crisp Answer

- `OpenTelemetry` is an observability framework for collecting traces, metrics, and logs.
- It helps monitor distributed applications and export telemetry to tools like Application Insights, Jaeger, Zipkin, or Prometheus.

### Detailed Explanation

- Observability is important in cloud-native systems because issues may occur across multiple services.
- `OpenTelemetry` provides standard instrumentation and context propagation.
- It can capture request traces, dependency calls, latency, errors, and custom metrics.
- This helps teams troubleshoot performance and reliability issues.

### Final Interview Answer

> `OpenTelemetry` is a standard framework for collecting telemetry such as traces, metrics, and logs. In .NET applications, I use it to trace requests across services, capture dependency calls, monitor latency and errors, and export data to platforms like Azure Application Insights or Prometheus.


---


## 31. How do you deploy a .NET Core API?



### Question Summary

> Tests whether you understand practical hosting and deployment options.


### Crisp Answer

- .NET Core APIs can be deployed to IIS, Azure App Service, Azure Container Apps, AKS, Docker, Linux VM, Windows Service, or Kubernetes.
- The choice depends on scalability, operational maturity, cost, and deployment model.

### Detailed Explanation

- .NET Core is flexible because it can run cross-platform.
- For simple enterprise APIs, Azure App Service is easy to manage.
- For containerized microservices, Docker with AKS or Azure Container Apps may be suitable.
- Deployment should include environment-based configuration, secret management, health checks, logging, CI/CD pipeline, and rollback strategy.

### Final Interview Answer

> I can deploy .NET Core APIs to IIS, Azure App Service, Docker containers, AKS, Azure Container Apps, or VMs. For cloud-native applications, I prefer containerized deployment with CI/CD, health checks, centralized logging, environment configuration, and secret management through Key Vault or platform-managed secrets.


---


## Quick Revision Table

| Area | Must Remember |
|---|---|
| .NET Core | Cross-platform, modern, cloud-ready .NET platform |
| Middleware | Request pipeline component |
| Dependency Injection | Built-in dependency management and loose coupling |
| Service Lifetimes | `Singleton`, `Scoped`, `Transient` |
| Routing | Maps URL and HTTP verb to endpoint |
| Model Binding | Maps request data to C# object |
| Validation | Data annotations, `ModelState`, `FluentValidation` |
| JWT | Header, Payload, Signature |
| Authorization | Role, claims, policy, resource-based |
| EF Core | ORM with `DbContext`, `DbSet`, LINQ, migrations |
| AsNoTracking | Read-only query performance optimization |
| Async/Await | Non-blocking I/O for scalability |
| Clean Architecture | API, Application, Domain, Infrastructure |
| HttpClientFactory | Safe external HTTP call management |
| CORS | Browser cross-origin access control |
| Caching | Improve performance and reduce repeated work |
| Rate Limiting | Protect APIs from abuse and cost spike |
| Circuit Breaker | Avoid repeated calls to failing dependencies |
| Idempotency | Prevent duplicate side effects on retry |
| Correlation ID | End-to-end request tracing |
| OpenTelemetry | Standard traces, metrics, and logs |
