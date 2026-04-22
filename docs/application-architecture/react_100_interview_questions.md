# React Interview Questions (100)

## Core React Fundamentals
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

## Hooks
16. What problem do Hooks solve in React?
17. How does `useState` work internally at a high level?
18. What are functional updates in `useState`?
19. How does `useEffect` lifecycle map to class lifecycles?
20. What is the dependency array in `useEffect`?
21. What causes infinite loops in `useEffect`?
22. How do you clean up side effects in `useEffect`?
23. What is `useLayoutEffect`, and when should it be used?
24. What is `useRef`, and when do you use it?
25. What is `useMemo`, and when is it useful?
26. What is `useCallback`, and how is it different from `useMemo`?
27. What is `useContext`, and how does it work?
28. What is `useReducer`, and when is it better than `useState`?
29. How do custom hooks improve code reuse?
30. What are the Rules of Hooks and why do they exist?

## Rendering and Performance
31. What triggers a re-render in React?
32. What is React.memo, and when should it be used?
33. How do you avoid unnecessary re-renders?
34. What is referential equality and why does it matter in React?
35. How do keys affect rendering performance?
36. What is lazy loading with `React.lazy` and `Suspense`?
37. What is code splitting in React?
38. What is concurrent rendering in React 18?
39. What is automatic batching in React 18?
40. How do transitions (`startTransition`) improve UX?
41. What are common React performance anti-patterns?
42. How do you profile React app performance?
43. What is hydration, and how does it work?
44. What can cause hydration mismatch errors?
45. What are best practices for large list rendering?

## State Management
46. When is Context enough, and when do you need Redux?
47. What are the core principles of Redux?
48. What is Redux Toolkit, and why is it preferred now?
49. What are selectors, and why are memoized selectors useful?
50. How does Zustand compare to Redux?
51. What is Recoil/Jotai style atom-based state management?
52. What is server state vs client state?
53. Why use TanStack Query (React Query)?
54. How do you handle optimistic updates in React apps?
55. How do you design predictable state transitions?

## Routing and App Architecture
56. What is React Router, and how does route matching work?
57. What is nested routing in React Router?
58. What are route guards and auth-protected routes?
59. How do loaders/actions work in modern React Router?
60. What is file-based routing in frameworks like Next.js?
61. How do you structure a scalable React project?
62. How do you separate presentational and container logic?
63. What is feature-based folder structure?
64. How do you manage shared UI component libraries?
65. What are micro-frontend considerations with React?

## Forms and Validation
66. Why are forms complex in React?
67. What is React Hook Form, and why is it popular?
68. How do you validate forms with Zod/Yup?
69. How do you handle dynamic forms?
70. How do you handle file uploads in React forms?

## API and Async Patterns
71. What is the best place to call APIs in React?
72. How do you cancel in-flight requests in React?
73. How do you handle race conditions in async data fetching?
74. How do you handle retries and error boundaries for API failures?
75. What is SWR, and how is it different from React Query?

## Testing
76. What is the React Testing Library philosophy?
77. How do you test React components effectively?
78. What should be unit-tested vs integration-tested?
79. How do you mock API calls in component tests?
80. How do you test hooks?
81. What are end-to-end testing options for React apps?
82. How do you write resilient selectors in UI tests?

## Security and Accessibility
83. What are common React security risks?
84. What is XSS, and how does React help prevent it?
85. When is `dangerouslySetInnerHTML` safe to use?
86. How do you secure tokens in a React app?
87. What are React accessibility best practices?
88. How do you support keyboard navigation and focus management?
89. How do you ensure semantic HTML in component libraries?

## SSR, Frameworks, and Ecosystem
90. What is SSR vs CSR vs SSG in React ecosystems?
91. What are ISR and edge rendering concepts in Next.js?
92. How do client and server components differ in modern React frameworks?
93. What are hydration and streaming SSR trade-offs?
94. How do you choose between Next.js, Remix, and Vite-based SPA?

## Advanced and Architecture Discussion
95. How do you handle i18n in large React apps?
96. How do you manage theme systems (light/dark/design tokens)?
97. How do you design error boundaries and fallback UX?
98. What are strategies for React app observability?
99. How do you prepare React apps for enterprise scale?
100. How would you explain React architecture choices in a senior interview?
