# Multi-agent topology for hard problems

Read this only when multiple independent branches can run concurrently and subagent delegation is available.

## Dispatch test

Use multiple agents when all are true:

- there are at least two meaningfully different hypotheses, mechanisms, or evidence sources;
- branches can make progress without sharing rapidly changing state;
- results can be compared against a common evidence contract;
- synthesis value exceeds coordination overhead.

Otherwise work serially. More agents are not a substitute for a well-posed problem.

## Default topology

Keep the coordinating agent responsible for the problem statement, branch diversity, evidence ledger, synthesis, and final verification. Assign agents to hypotheses or methods rather than arbitrary slices.

Use the smallest topology the task needs:

- **Scout:** finds literature, precedents, datasets, or tractable proxies.
- **Solver:** develops one mechanism, construction, derivation, or diagnosis.
- **Breaker:** searches for counterexamples, hidden assumptions, and failure cases.
- **Verifier:** independently reproduces the surviving result from primary evidence.

One agent may fill more than one role in separate rounds, but the final verification should not merely restate the solver's reasoning. When capacity is limited, prioritize one independent solver and one breaker; the coordinator can synthesize.

## Branch prompt contract

Every dispatch should include:

- the shared problem statement and invariants;
- the single branch or hypothesis owned by that agent;
- what evidence would support or disprove it;
- permitted tools, sources, time, and side effects;
- the requested artifact or return format;
- an instruction to report failed attempts and uncertainty;
- a stop condition.

Do not give a breaker the intended answer unless testing that exact answer is its job. Do not ask several agents the same broad question and call the outputs diverse.

## Communication pattern

Start branches independently when premature consensus is a risk. At a synthesis gate, circulate a compact evidence packet containing:

- supported claims with provenance;
- contradictions;
- newly discovered constraints;
- reusable mechanisms;
- open proof or evidence obligations.

Then launch targeted follow-ups that explicitly name which imported result they should test or extend. Keep raw artifacts accessible; summaries are lossy.

## Resource allocation

Begin broad enough to test the main branches, then reallocate based on discriminating evidence. Expand a branch because it survived a hard test or produced a transferable mechanism—not because it generated more prose.

Terminate duplicated, stalled, or falsified branches. Open a new one only when it represents a distinct hypothesis or a necessary independent verification path.

## Verification firewall

The coordinator must compare the candidate answer against the original success criteria, not the proxy's criteria. Commission an independent verification pass when the result is consequential, surprising, or difficult to inspect.

Before shared, external, production, financial, legal, medical, privacy, permission, or security-sensitive action:

- identify what was verified and what was not;
- ask the user for unexplained context and rollback conditions;
- convert each material concern into a small check with an owner and disconfirming evidence;
- require appropriate human review.
