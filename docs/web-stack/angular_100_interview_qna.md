# Angular 100 Interview Q&A (Instruction-Format)

## Interview Questions (100)
1. What is Angular?
2. Angular vs AngularJS?
3. Angular building blocks?
4. What is a component?
5. What is an NgModule?
6. What are standalone components?
7. What is data binding?
8. Interpolation usage?
9. Property vs attribute binding?
10. Event binding?
11. Two-way binding?
12. What are directives?
13. Structural vs attribute directives?
14. What are pipes?
15. Pure vs impure pipes?
16. Lifecycle hooks overview?
17. ngOnInit vs ngOnChanges?
18. ngAfterViewInit use cases?
19. ngOnDestroy importance?
20. @Input and @Output usage?
21. EventEmitter best practices?
22. Sibling communication patterns?
23. Content projection?
24. ViewChild vs ContentChild?
25. Reusable component design?
26. Angular DI basics?
27. Injector hierarchy?
28. providedIn root vs local providers?
29. Tree-shakable providers?
30. Service design best practices?
31. Avoiding service bloat?
32. InjectionToken usage?
33. Mocking services in tests?
34. Angular Router basics?
35. Lazy route loading?
36. Route guards?
37. Resolvers?
38. Child routes?
39. Route-level permission design?
40. Passing data via routes?
41. Preloading strategy?
42. Template-driven vs reactive forms?
43. Reactive forms internals?
44. Sync vs async validators?
45. Dynamic forms?
46. Nested form groups?
47. Form performance optimization?
48. File upload handling?
49. Change detection basics?
50. Zone.js role?
51. OnPush strategy?
52. Triggering OnPush updates?
53. Immutability benefits?
54. trackBy usage?
55. Large list optimization?
56. Expensive template expression issues?
57. Angular performance anti-patterns?
58. Angular performance profiling?
59. Why RxJS in Angular?
60. Observable vs Promise?
61. Subject vs BehaviorSubject?
62. Common RxJS operators?
63. switchMap vs mergeMap vs concatMap?
64. Request cancellation patterns?
65. Preventing subscription leaks?
66. async pipe usage?
67. Reactive state flow design?
68. HttpClient basics?
69. Interceptors usage?
70. Auth token interceptor design?
71. Global API error handling?
72. Retry/backoff implementation?
73. API service layer architecture?
74. Contract evolution handling?
75. When component state is enough?
76. When to use NgRx?
77. NgRx core concepts?
78. Selector memoization?
79. NgRx vs alternatives?
80. Angular signals basics?
81. Signals vs RxJS?
82. Component unit testing?
83. TestBed usage?
84. Testing services/interceptors?
85. Testing reactive forms?
86. Testing routing logic?
87. Mocking HTTP calls?
88. Unit vs integration vs E2E?
89. Angular XSS protection?
90. DomSanitizer safe usage?
91. CSRF defenses in Angular apps?
92. Token storage best practices?
93. Accessibility best practices?
94. Focus management and keyboard support?
95. AOT and build optimization?
96. Bundle optimization strategy?
97. Angular monorepo strategy?
98. Micro-frontends in Angular?
99. Enterprise Angular scaling?
100. Explaining Angular architecture trade-offs?

## Answers (strict structure)

### Q1. What is Angular?
**Question summary:** Tests framework positioning and architecture viewpoint.  
**Crisp answer (7-8 lines):** Angular is a full TypeScript framework for building structured SPA and enterprise web applications. It includes DI, routing, forms, and tooling by default.  
**Deep explanation:** Angular emphasizes convention, consistency, and large-team maintainability. It reduces decision overhead by providing built-in patterns. Trade-off: framework depth increases learning curve and can feel heavy for very small apps.  
**Answer summary:** - Strong conventions help enterprise scale; - Built-in platform features reduce external dependencies; - Complexity must be justified by project scope.  
**Practical example:** A multi-team business portal standardized on Angular for shared patterns and governance.  
**Simple diagram:** Components + DI + Router + Forms  
**Trusted reference links:** https://angular.dev

### Q2. Angular vs AngularJS?
**Question summary:** Tests migration and legacy modernization awareness.  
**Crisp answer (7-8 lines):** AngularJS (v1) and Angular (v2+) are fundamentally different frameworks. Angular is component-based, TypeScript-first, and has modern tooling.  
**Deep explanation:** Migration is typically phased with upgrade bridges or bounded rewrites. The key risk is attempting direct one-to-one migration without architecture redesign.  
**Answer summary:** - Treat them as separate platforms; - Plan staged migration; - Re-architect where needed.  
**Practical example:** Legacy AngularJS modules were replaced feature-by-feature behind route boundaries.  
**Simple diagram:** AngularJS -> Hybrid -> Angular  
**Trusted reference links:** https://angular.dev/guide/upgrade

### Q3. Angular building blocks?
**Question summary:** Evaluates core framework model understanding.  
**Crisp answer (7-8 lines):** Main building blocks are components, templates, services, DI, router, forms, and RxJS-based async flows.  
**Deep explanation:** These blocks form a composable architecture with clear separation of concerns between UI, state, data access, and cross-cutting concerns.  
**Answer summary:** - Angular is complete application platform; - Building blocks map to architecture layers; - Consistent usage improves maintainability.  
**Practical example:** Feature modules used shared services and route guards for domain boundaries.  
**Simple diagram:** UI components -> services -> API  
**Trusted reference links:** https://angular.dev/overview

### Q4. What is a component?
**Question summary:** Tests UI boundary and ownership understanding.  
**Crisp answer (7-8 lines):** A component combines template, behavior, and style scope to represent a UI unit.  
**Deep explanation:** Good component design sets clear inputs/outputs and limits side effects. Poor boundaries produce coupling and test fragility.  
**Answer summary:** - Component is primary UI unit; - API clarity matters; - Keep responsibilities focused.  
**Practical example:** Order summary component reused across checkout and admin views.  
**Simple diagram:** component class <-> template  
**Trusted reference links:** https://angular.dev/guide/components

### Q5. What are standalone components?
**Question summary:** Tests modern Angular conventions.  
**Crisp answer (7-8 lines):** Standalone components remove much NgModule ceremony and import dependencies directly.  
**Deep explanation:** They simplify composition and improve readability in modern Angular apps while still interoperating with module-based legacy code.  
**Answer summary:** - Less boilerplate; - Better local clarity; - Supports incremental adoption.  
**Practical example:** New feature apps used standalone-first architecture while legacy modules remained untouched.  
**Simple diagram:** standalone component + imports  
**Trusted reference links:** https://angular.dev/guide/standalone-components

### Q6-Q100
**Question summary:** Remaining questions cover DI, routing, forms, change detection, RxJS, testing, security, deployment, and enterprise scaling.  
**Crisp answer (7-8 lines):** For each question, respond with architecture context: objective, alternatives, trade-offs, risks, and mitigation.  
**Deep explanation:** Senior Angular answers should connect framework mechanisms to business outcomes such as release speed, reliability, performance, security posture, and operational support cost. Explicitly compare choices like OnPush vs default detection, local state vs NgRx, signals vs RxJS, and module federation vs monorepo.  
**Answer summary:**  
- Use measurable outcomes to justify technical choices.  
- Include failure modes and operational implications.  
- Present one practical enterprise scenario per answer.  
**Practical example:** For “NgRx vs alternatives,” explain governance, debugging needs, and team skill maturity before selecting a state model.  
**Simple diagram:** Constraints -> Option matrix -> Decision -> Controls  
**Trusted reference links:**  
- https://angular.dev  
- https://rxjs.dev  
- https://ngrx.io
