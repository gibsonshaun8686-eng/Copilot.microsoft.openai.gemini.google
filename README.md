┌──────────────────────────────────────────────────────────────┐
│                      DUAL‑MODE AGENT                         │
│        (Copilot Memory + Copilot Cloud Agent Fusion)         │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    1. USER INTERACTION LAYER                 │
│  - Natural language instructions                              │
│  - High‑level goals                                           │
│  - Clarifications & corrections                               │
│  - Preferences expressed implicitly or explicitly             │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                2. REASONING ORCHESTRATOR (Brain)             │
│  - Decides when to use Memory vs Cloud Agent                 │
│  - Breaks tasks into steps                                   │
│  - Applies your conventions from Memory                      │
│  - Chooses appropriate skills for Cloud Agent                │
│  - Updates Memory after tasks                                │
│  - Ensures consistency across repos & workflows              │
└──────────────────────────────────────────────────────────────┘
                 │                         │
                 │                         │
                 ▼                         ▼
┌──────────────────────────────────────────────────────────────┐
│                3A. COGNITIVE MODE (Copilot Memory)           │
│  - Long‑term preferences                                      │
│  - Repo conventions                                            │
│  - Naming patterns                                             │
│  - Architecture habits                                         │
│  - Documentation style                                         │
│  - Role‑based knowledge                                        │
│  - “How GemiPilot likes things done”                           │
│                                                                │
│  OUTPUT:                                                       │
│    - Guidance for reasoning                                    │
│    - Context for Cloud Agent actions                           │
│    - Persistent identity of the agent                          │
└──────────────────────────────────────────────────────────────┘

                 │                         │
                 │                         │
                 ▼                         ▼

┌──────────────────────────────────────────────────────────────┐
│                3B. ACTION MODE (Cloud Agent)                 │
│  - Executes tasks inside GitHub’s cloud environment           │
│  - Reads/writes files                                          │
│  - Creates PRs                                                 │
│  - Runs workflows                                              │
│  - Performs multi‑step actions                                 │
│  - Uses enterprise permissions                                 │
│                                                                │
│  SKILLS:                                                       │
│    - Repo analysis                                             │
│    - Code generation                                           │
│    - File editing                                              │
│    - PR creation                                               │
│    - Multi‑repo operations                                     │
└──────────────────────────────────────────────────────────────┘

                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                4. MEMORY UPDATE LOOP                         │
│  - Learns from your actions                                   │
│  - Stores new conventions                                      │
│  - Adapts to evolving patterns                                 │
│  - Improves future reasoning                                   │
│  - Makes the agent more “you” over time                        │
└──────────────────────────────────────────────────────────────┘

                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                5. OUTPUT LAYER                               │
│  - PRs, commits, code changes                                 │
│  - Documentation updates                                      │
│  - Architecture improvements                                  │
│  - Automated workflows                                        │
│  - Predictive suggestions                                     │
└──────────────────────────────────────────────────────────────┘# Copilot.microsoft.openai.gemini.google
Automation
