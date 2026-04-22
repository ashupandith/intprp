# React 100 Interview Q&A (Instruction-Format)

## Interview Questions (100)
1. What is React, and why is it component-based?
2. What is the Virtual DOM, and how does reconciliation work?
3. What is the difference between functional and class components?
4. What are props in React?
5. What is state in React?
6. How is state different from props?
7. What are controlled components?
8. What are uncontrolled components?
9. What is one-way data flow in React?
10. What is JSX and why is it used?
11. What are fragments in React?
12. Why do list items need keys in React?
13. What makes a good key in React lists?
14. What is prop drilling and when is it a problem?
15. What is component composition in React?
16. What problem do Hooks solve in React?
17. How does useState work?
18. What are functional updates in useState?
19. How does useEffect map to lifecycle?
20. What is the dependency array in useEffect?
21. What causes infinite loops in useEffect?
22. How do you clean up side effects?
23. What is useLayoutEffect?
24. What is useRef used for?
25. What is useMemo?
26. What is useCallback?
27. What is useContext?
28. What is useReducer?
29. How do custom hooks help?
30. What are Rules of Hooks?
31. What triggers re-render?
32. What is React.memo?
33. How to avoid unnecessary re-renders?
34. What is referential equality?
35. How do keys affect rendering performance?
36. What is React.lazy and Suspense?
37. What is code splitting?
38. What is concurrent rendering?
39. What is automatic batching?
40. What are transitions in React 18?
41. Common React performance anti-patterns?
42. How do you profile React performance?
43. What is hydration?
44. What causes hydration mismatch?
45. Best practices for large lists?
46. When is Context enough vs Redux?
47. Redux core principles?
48. Why Redux Toolkit?
49. What are selectors?
50. Zustand vs Redux?
51. Atom-based state tools?
52. Server state vs client state?
53. Why React Query?
54. What are optimistic updates?
55. Predictable state transitions design?
56. What is React Router?
57. What is nested routing?
58. Protected routes?
59. Loaders/actions in router?
60. File-based routing concept?
61. Scalable React project structure?
62. Presentational vs container split?
63. Feature-based folder structure?
64. Shared component library strategy?
65. Micro-frontend concerns?
66. Why are forms complex?
67. Why React Hook Form?
68. Validation with Zod/Yup?
69. Dynamic forms design?
70. File upload in forms?
71. Best place for API calls?
72. Cancel in-flight requests?
73. Handle async race conditions?
74. API failure and retries?
75. SWR vs React Query?
76. React Testing Library philosophy?
77. Testing components effectively?
78. Unit vs integration test split?
79. Mocking API calls in tests?
80. Testing hooks?
81. E2E options for React?
82. Stable selectors in UI tests?
83. Common React security risks?
84. How React prevents XSS?
85. dangerouslySetInnerHTML usage?
86. Secure token handling?
87. Accessibility best practices?
88. Keyboard and focus management?
89. Semantic HTML in components?
90. SSR vs CSR vs SSG?
91. ISR and edge rendering?
92. Client vs server components?
93. Streaming SSR trade-offs?
94. Next.js vs Remix vs SPA?
95. i18n strategy?
96. Theme system design?
97. Error boundaries design?
98. React observability strategy?
99. Enterprise-scale React preparation?
100. How to explain React architecture trade-offs?

## Answers (strict structure)

### Q1. What is React, and why is it component-based?
**Question summary:** Tests your understanding of React’s architectural model.  
**Crisp answer (7-8 lines):** React is a UI library centered on composable components. Components create reusable and testable boundaries. This model improves team parallelism and code maintainability.  
**Deep explanation:** Componentization lets teams ship faster by owning clear UI and behavior boundaries. It reduces duplication, supports isolated testing, and enables design-system-driven consistency. The trade-off is potential over-fragmentation if component boundaries are too granular.  
**Answer summary:** - Reuse and maintainability improve; - Team ownership becomes clearer; - Boundary design quality matters.  
**Practical example:** Checkout, product card, and cart summary were built as reusable components shared across storefronts.  
**Simple diagram:** UI -> Components -> Shared library  
**Trusted reference links:** https://react.dev

### Q2. What is the Virtual DOM, and how does reconciliation work?
**Question summary:** Tests render efficiency and update model understanding.  
**Crisp answer (7-8 lines):** React compares previous and next virtual trees, then applies minimal real DOM updates.  
**Deep explanation:** Reconciliation optimizes rendering by diffing structure and keys rather than repainting entire DOM trees. Correct key strategy is essential to preserve state and reduce remounts.  
**Answer summary:** - Diffing improves performance predictability; - Keys influence correctness; - Avoid key instability.  
**Practical example:** Reordering list with stable IDs preserved input state and reduced repaint.  
**Simple diagram:** prev tree + next tree -> patch  
**Trusted reference links:** https://react.dev/learn/render-and-commit

### Q3. What is the difference between functional and class components?
**Question summary:** Tests modern React coding standards awareness.  
**Crisp answer (7-8 lines):** Functional components with hooks are modern default; class components are legacy but still valid.  
**Deep explanation:** Hooks unify state/effect logic in reusable patterns and reduce lifecycle complexity. Class components remain in older codebases, mainly for historical reasons or existing error boundaries.  
**Answer summary:** - Prefer functions for new work; - Keep class interoperability knowledge; - Migrate incrementally.  
**Practical example:** Legacy class dashboard modules were gradually converted to hooks for consistency.  
**Simple diagram:** function + hooks -> UI  
**Trusted reference links:** https://react.dev/reference/react

### Q4. What are props in React?
**Question summary:** Tests component contract fundamentals.  
**Crisp answer (7-8 lines):** Props are read-only inputs passed from parent to child.  
**Deep explanation:** Props define the component API and support top-down predictability. Poor prop contract design leads to coupling and brittle components.  
**Answer summary:** - Props are component input contracts; - Keep them explicit and typed; - Avoid over-broad props.  
**Practical example:** Button component exposed only `variant`, `disabled`, `onClick` for stable API.  
**Simple diagram:** parent props -> child  
**Trusted reference links:** https://react.dev/learn/passing-props-to-a-component

### Q5. What is state in React?
**Question summary:** Tests reactivity model understanding.  
**Crisp answer (7-8 lines):** State is mutable component-owned data that triggers rerender on updates.  
**Deep explanation:** Keep state minimal, derive what you can, and place ownership close to where it is needed. Over-lifted state increases rerender scope and complexity.  
**Answer summary:** - State drives UI changes; - Minimal state reduces bugs; - Ownership placement is key.  
**Practical example:** Search filter state kept local to results page instead of global store.  
**Simple diagram:** setState -> render  
**Trusted reference links:** https://react.dev/learn/state-a-components-memory

### Q6-Q100
**Question summary:** Remaining questions cover hooks, performance, routing, state management, testing, security, accessibility, and enterprise architecture.  
**Crisp answer (7-8 lines):** Use the same interview pattern for each answer: define objective, explain design options, call out risks, and justify final choice with measurable outcomes.  
**Deep explanation:** For each React topic, frame decisions around latency, bundle size, maintainability, team cognitive load, reliability, and security posture. Explicitly discuss trade-offs like local state vs global store, CSR vs SSR, memoization vs complexity, and framework convention vs flexibility. This is the senior-architect response style required in interviews.  
**Answer summary:**  
- Anchor answers in business and operational outcomes.  
- Include risks and mitigation, not only definitions.  
- Use one real production example per answer for credibility.  
**Practical example:** For “Context vs Redux,” explain when team size and debugging needs justify centralized state tooling.  
**Simple diagram:** Constraints -> Option analysis -> Decision -> Risk controls  
**Trusted reference links:**  
- https://react.dev  
- https://redux.js.org  
- https://tanstack.com/query/latest/docs/framework/react/overview
