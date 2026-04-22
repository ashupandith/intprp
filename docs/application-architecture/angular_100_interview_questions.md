# Angular Interview Questions (100)

## Angular Fundamentals
1. What is Angular, and how is it different from AngularJS?
2. What are the main building blocks of Angular?
3. What is a component in Angular?
4. What is a module (`NgModule`)?
5. What is standalone component architecture in modern Angular?
6. What are templates in Angular?
7. What is data binding in Angular?
8. What is interpolation in Angular templates?
9. What is property binding vs attribute binding?
10. What is event binding?
11. What is two-way binding and how does `ngModel` work?
12. What are directives in Angular?
13. What is the difference between structural and attribute directives?
14. What are pipes in Angular?
15. How do pure and impure pipes differ?

## Components and Lifecycle
16. What are Angular component lifecycle hooks?
17. When do `ngOnInit` and `ngOnChanges` run?
18. What is `ngAfterViewInit`, and when is it needed?
19. How does `ngOnDestroy` help prevent leaks?
20. How do `@Input` and `@Output` work?
21. What are `EventEmitter` best practices?
22. How do you communicate between sibling components?
23. What are content projection (`ng-content`) use cases?
24. What are view queries (`ViewChild`) and content queries (`ContentChild`)?
25. How do you design reusable Angular components at scale?

## Dependency Injection and Services
26. How does Angular dependency injection work?
27. What are providers and injector hierarchies?
28. `providedIn: 'root'` vs module/component providers: differences?
29. What is tree-shakable provider design?
30. How do services improve architecture in Angular apps?
31. How do you avoid service bloat?
32. How do injection tokens work?
33. How do you mock services for testing?

## Routing
34. How does Angular Router work?
35. What is lazy loading in Angular routes?
36. How do route guards (`CanActivate`, etc.) work?
37. What are resolvers and when should they be used?
38. How do child routes and nested outlets work?
39. How do you handle route-level permissions?
40. How do you pass data between routes?
41. How do you optimize route preloading strategy?

## Forms
42. Template-driven vs reactive forms: when to use each?
43. How do reactive forms work internally?
44. How do synchronous and asynchronous validators differ?
45. How do you build dynamic forms in Angular?
46. How do you manage complex form state and nested controls?
47. How do you handle form performance at scale?
48. How do you handle file upload in Angular forms?

## Change Detection and Performance
49. How does Angular change detection work?
50. What is Zone.js and how does it relate to Angular?
51. What is `ChangeDetectionStrategy.OnPush`?
52. How do you trigger view updates with OnPush correctly?
53. How does immutability improve Angular performance?
54. What is `trackBy`, and why is it important in `*ngFor`?
55. How do you optimize large list rendering in Angular?
56. How do you avoid expensive template expressions?
57. What are common Angular performance anti-patterns?
58. How do you profile Angular app performance?

## RxJS and Async Patterns
59. Why is RxJS central in Angular?
60. Observable vs Promise in Angular: when to use which?
61. What are Subjects and BehaviorSubjects?
62. What are common RxJS operators in Angular apps?
63. How do `switchMap`, `mergeMap`, and `concatMap` differ?
64. How do you handle cancellation in HTTP streams?
65. How do you prevent subscription memory leaks?
66. What does `async` pipe do and why is it recommended?
67. How do you design reactive state flows with RxJS?

## HTTP and API Integration
68. How does `HttpClient` work in Angular?
69. How do HTTP interceptors work?
70. How do you add auth tokens with interceptors safely?
71. How do you handle global error handling for API calls?
72. How do you implement retries/backoff in Angular clients?
73. How do you design API service layers in Angular projects?
74. How do you handle API contract evolution in frontend apps?

## State Management
75. When is component state enough in Angular?
76. When do you need NgRx?
77. What are NgRx Store, Actions, Reducers, and Effects?
78. What are selectors and memoization in NgRx?
79. NgRx vs Akita vs signals-based state: how do you choose?
80. How do Angular signals work in modern Angular?
81. How do signals compare with RxJS for state scenarios?

## Testing
82. How do you unit test Angular components?
83. What is TestBed and when should you use it?
84. How do you test services and interceptors?
85. How do you test reactive forms?
86. How do you test routing behavior?
87. How do you mock HTTP calls in Angular tests?
88. What belongs in unit vs integration vs E2E tests for Angular?

## Security and Accessibility
89. How does Angular prevent XSS by default?
90. When do you use `DomSanitizer`, and what are risks?
91. How do you protect against CSRF in Angular apps?
92. How do you handle secure token storage in SPA contexts?
93. What are Angular accessibility best practices?
94. How do you manage focus and keyboard accessibility in Angular apps?

## Build, Deployment, and Architecture
95. How does Angular build optimization (AOT, tree shaking) work?
96. What is differential loading and modern bundle targeting?
97. How do you structure Angular monorepos (Nx/workspaces)?
98. How do you do micro-frontend architecture with Angular?
99. How do you prepare Angular apps for enterprise scale?
100. How do you explain Angular architectural trade-offs in a senior interview?
