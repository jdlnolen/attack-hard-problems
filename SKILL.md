---
name: attack-hard-problems
description: Structure and pursue difficult, high-uncertainty problems through outcome branching, proxy problems, diverse hypotheses, adaptive research rounds, synthesis, and independent verification. Use for open-ended scientific, technical, analytical, diagnostic, design, or strategy problems where the answer or path is genuinely unknown; not for routine tasks with an established procedure.
---

# Attack Hard Problems

Turn the problem into an adaptive research program, then pursue it until there is a supported answer, a decisive falsification, or a precise account of what remains unresolved.

The goal is not maximum parallelism. The goal is useful diversity, rapid learning, and progressively stronger verification.

## Choose the operating depth

- If the user asks for a plan, framing, or strategy, produce the attack map and stop before execution.
- If the user asks to solve, investigate, diagnose, or make progress, build the attack map and execute the highest-value safe research rounds.
- If the user supplies a proposed answer, treat it as one hypothesis rather than the default conclusion.
- If the task becomes routine after inspection, leave this workflow and complete it directly.

## 1. Define the decision surface

State the problem in a form that can fail. Capture:

- the exact claim, decision, or target;
- constraints and invariants that cannot be traded away;
- observable success criteria;
- observable failure or disproof criteria;
- what is known, assumed, and unknown;
- the smallest result that would materially change the next decision.

Enumerate the mutually exclusive resolution branches. Include both constructive and falsifying paths whenever the problem permits them. Do not quietly assume that the user's preferred conclusion is true.

For high-stakes, shared, external, or difficult-to-reverse consequences, also identify who can authorize action, the stop or rollback condition, and what requires experienced human review. Research and recommendation do not imply permission to act.

## 2. Build a mechanism-preserving proxy ladder

Look for smaller or adjacent problems that preserve the suspected hard mechanism while removing other complexity. Useful reductions may:

- remove one interaction, constraint, scale, or dependency;
- use a smaller dataset, subsystem, synthetic case, or limiting regime;
- replace a global claim with a local lemma or diagnostic prediction;
- construct a counterexample to a weakened or strengthened version;
- reproduce a known special case before attempting the general case.

For every proxy, state what finding would transfer to the original problem and what would not. A proxy result is evidence, not a solution, until the transfer argument is checked.

## 3. Create a hypothesis portfolio

Decompose by competing explanations or solution mechanisms, not merely by document section or task size. Select the smallest set of branches that provides meaningful diversity. Include, where useful:

- a direct construction or proof path;
- a counterexample or falsification path;
- a proxy or limiting-case path;
- an empirical or computational path;
- a literature or precedent path;
- an adversarial path aimed at breaking the leading idea.

Give each branch an evidence contract: the question it owns, its permitted assumptions, expected artifact, disconfirming evidence, and stop condition. Avoid launching several branches that differ only in wording.

When subagent delegation is available and these branches can run independently, read [references/agent-topology.md](references/agent-topology.md) before dispatching. Do not delegate merely to inflate agent count.

## 4. Run bounded research rounds

Begin with enough isolation to preserve independent reasoning. Each branch should return:

- its strongest supported claim;
- the evidence or derivation behind it;
- assumptions and unresolved gaps;
- failed approaches and why they failed;
- a confidence level calibrated to the evidence;
- the next experiment or check with the highest information value.

Prefer experiments that distinguish hypotheses over work that merely elaborates one. Use tools, code, literature, simulations, or formal methods when they produce relevant evidence. Keep source provenance and separate observations from interpretation.

## 5. Harvest and cross-pollinate

At a synthesis gate, compare branch outputs and extract only reusable material:

- verified lemmas, mechanisms, or measurements;
- contradictions and boundary cases;
- assumptions that failed;
- methods that transferred across branches;
- decisive missing evidence.

Compress those findings into a shared synthesis without erasing disagreement. Feed useful results into the next round as explicit context. Preserve the original evidence links so compression does not turn conjecture into fact.

## 6. Reallocate adaptively

Update the portfolio after each synthesis gate:

- expand branches whose predictions survived meaningful tests;
- merge branches that have converged on the same mechanism;
- pause branches whose key assumption was disproved;
- open a new branch when evidence reveals a genuinely different hypothesis;
- move effort from broad exploration to focused exploitation only after evidence warrants it.

Name why allocation changed. Raw effort, token count, or agent count is not evidence of progress.

Stop when one of these conditions holds:

- the success criteria are met with adequate verification;
- the target claim is decisively falsified;
- every live branch depends on the same missing information or authority;
- the next check costs more or carries more risk than its expected information value;
- the user-defined budget or stop condition is reached.

## 7. Separate discovery from verification

Do not let the mechanism that generated a candidate answer be its only validator. Choose checks appropriate to the domain:

- reproduce the result from raw inputs;
- test adversarial, boundary, and negative cases;
- compare with an independent method, source, implementation, or derivation;
- verify that a proxy result transfers to the original problem;
- use static analysis, formal proof, simulation, experiment, or expert review where appropriate;
- audit permissions, data exposure, destructive failure modes, confused-user behavior, dependency failures, maintenance, and rollback before external or production use.

State exactly what has and has not been verified. Passing tests raises confidence only for the properties those tests exercise.

## 8. Report the result as an evidence map

Lead with the current answer or decision. Then give:

1. the framing and resolution branches;
2. the mechanism or strongest surviving hypothesis;
3. decisive evidence and falsification attempts;
4. what proxy work transferred and why;
5. discarded paths and what they taught;
6. remaining uncertainty and the next highest-value check;
7. one recommendation: continue exploring privately, hold for verification, or escalate for experienced review when consequential action is contemplated.

Distinguish reported facts, direct observations, derived conclusions, and speculation. If the problem remains unsolved, deliver a narrower problem with sharper constraints and a ranked evidence gap rather than manufacturing closure.
