# Risks and Issues in AI-Agent-Assisted Research Coding

This document collects issues that may arise when using AI coding agents in computational communication research and related data-intensive research workflows. It is intended as a working risk taxonomy for discussion, guideline development, checklist design, and reviewer-facing transparency.

The list below is deliberately condensed: each bullet names a general risk, with examples included where they clarify the issue.

## Data Privacy, Confidentiality, and Data Governance

- Sensitive data may be transmitted to unauthorized third parties when an agent can see prompts, files, terminal output, stack traces, screenshots, notebook outputs, autocomplete context, generated code snippets, or logs.
- Scraped communication data should be treated as potentially sensitive unless shown otherwise. Public availability does not automatically make bulk processing or third-party sharing ethically safe.
- Sensitive information can leak directly through raw data and indirectly through usernames, profile URLs, comments, images, video metadata, timestamps, location traces, IDs, URLs, schema descriptions, filenames, folder names, variable names, or small "example" rows.
- Provider-side policies may be hard to interpret. "No training on your data" does not necessarily mean no external processing, logging, retention, abuse monitoring, telemetry, human review, or model-improvement use.
- Researchers may be unable to verify exactly what an agent saw, indexed, cached, retained, transmitted, or exposed to plugins and cloud tooling.
- Secrets and restricted assets can leak through agent-accessible contexts, including API keys, access tokens, cookies, credentials, database URLs, private repository contents, embargoed datasets, and non-public data.
- Re-identification risk can arise when agents see metadata, partial records, schema information, or combinations of details that seem low-risk in isolation.
- Consent agreements, platform terms of service, IRB or ethics approvals, data use agreements, journal policies, and institutional rules may prohibit or restrict third-party processing.

## Separation Between Agent-Safe and Protected Data

- Agent-assisted development and protected real-data analysis may not be separated clearly enough, allowing the agent to see real data during debugging, testing, visualization, or error handling.
- The boundary between "agent-safe development" and "protected analysis" can erode over time, especially when researchers paste real examples, outputs, error traces, tables, or plots back into the agent environment.
- Mock data can create two different risks: it may be too simple to capture quirks of the real data, or too realistic and therefore identifiable.
- Mock data may accidentally contain real examples, copied rows, reconstructed cases, or sensitive patterns.
- Code developed on mock data may silently fail on messy, multilingual, large-scale, platform-specific, or otherwise non-toy real data.
- Real data can leak through secondary artifacts such as cached notebooks, `.ipynb_checkpoints`, logs, temporary files, generated plots, saved console output, intermediate artifacts, hidden files, and repository commits.
- Synthetic, placeholder, or generated data may later be confused with real data if not clearly labeled and isolated.
- Folder structures, file names, ignored files, and environment boundaries may not make it obvious which spaces are agent-safe and which are protected.
- Local tools, workspace search, embeddings, memory, plugins, and recursive folder inspection may expose protected files even when researchers intended to share only code.
- Mock and real environments may drift apart over time, reducing confidence that agent-developed code behaves correctly in the protected analysis environment.

## Agent Access Control, Containment, and Security

- Coding agents often have powerful tool access: reading and writing files, running shell commands, using Git, installing packages, browsing the web, inspecting workspaces, taking screenshots, or automating browsers.
- Permission boundaries may be unclear, inconsistent across tools, or too broad by default.
- Agents may read beyond the intended scope, including protected directories, symlinked folders, `.env`, `.ssh`, `.gitconfig`, credential stores, shell history, or files outside the project root.
- Agents may modify, delete, overwrite, rename, restructure, or generate files without the researcher fully noticing.
- Agents may change configuration files, environment variables, credentials, project settings, dependency files, access permissions, or paths in ways that affect later analyses.
- Agents may write outputs into directories later used for real-data analysis.
- Agents may execute unsafe shell commands, use internet access when offline analysis was intended, download external files without verification, send data to external services, or run code copied from unknown sources.
- Agent-generated code may introduce dependency confusion, malicious packages, supply-chain vulnerabilities, injection vulnerabilities, weak file permissions, or unsafe practices on shared servers and HPC systems.
- Prompt injection can occur through web pages, README files, issue text, code comments, data files, or malicious text inside research data if the agent treats untrusted content as instructions.
- Secrets may be mishandled in notebooks, logs, config files, commits, Git history, GitHub repositories, or shared folders.
- Researchers may lack audit logs showing what files, commands, URLs, tools, and external services the agent accessed or changed.

## Code Correctness, Reliability, and Validation

- Agents can produce plausible code that runs but is wrong.
- Agents may misunderstand APIs, statistics, causal claims, sampling logic, model evaluation, or platform-specific data structures.
- Agents may hallucinate functions, packages, citations, code behavior, or best practices.
- Agent-generated code may contain subtle bugs in joins, merge keys, row counts, deduplication, missing-data handling, filtering, weighting, aggregation, date parsing, time zones, type conversion, text normalization, regular expressions, or platform metadata extraction.
- Agent-generated analyses may use incorrect statistical formulas, model specifications, train/test splits, sampling weights, denominators, p-values, confidence intervals, effect sizes, aggregation levels, or causal interpretations.
- Agent-generated pipelines may leak information between training and test sets, duplicate or drop rows, mishandle deleted posts or quote tweets, or confuse post-level, user-level, and comment-level units.
- Agent-written code may scale poorly, silently time out, truncate large datasets, sample incorrectly, or work only on toy examples.
- Agent-generated visualizations and tables may mislead through scaling, aggregation, omitted uncertainty, unclear denominators, stale data, or mismatches with the underlying code.
- Tests may be too shallow, too tailored to the current implementation, or disconnected from the substantive research question.
- Researchers may validate only whether code runs, not whether it is correct.
- Validation may omit unit tests for data transformations, row-count checks, missingness checks, distribution checks, edge-case checks, mock-versus-real behavior checks, manual inspection of classification outputs, robustness checks, and audit trails for changed results.
- The same agent that generated code may also generate validation code, explanations, and tests, reproducing the same flawed assumptions.
- Agent-generated comments and explanations may create false confidence about code the researcher has not fully understood.

## Methodological Validity and Epistemic Authority

- Agents can silently introduce analytic choices the researcher did not intend.
- Agents may implement the analysis the user seems to want rather than the analysis specified by the research design.
- Agents may "fix" problems by changing preprocessing, cleaning, filtering, exclusion criteria, or model specifications rather than preserving the intended analysis.
- Agents may optimize for satisfying the user, producing expected-looking results, or making code run rather than preserving methodological rigor.
- Agentic workflows can accelerate researcher degrees of freedom, p-hacking, garden-of-forking-paths behavior, specification search, and post hoc rationalization.
- Agents may misinterpret theoretical constructs, collapse distinct concepts, choose convenient proxies, or select metrics because they are easy to compute rather than theoretically meaningful.
- Agents may recommend generic or technically elegant methods without understanding communication theory, platform affordances, sampling bias, representativeness, or field-specific assumptions.
- Agents may suggest inappropriate models, classifiers, embeddings, topic models, regressions, causal designs, validation strategies, codebooks, classification prompts, or annotation schemes.
- Agents may suggest automated validation where human validation or expert interpretation is needed.
- Researchers may mistake working code for valid research, defer to fluent explanations, lose understanding of their own pipeline, or outsource analytic judgment without noticing.
- The review burden can shift from writing code to auditing code, which may be harder and more specialized.
- Junior researchers may be especially vulnerable to over-trusting agent authority or being pressured to use agents without adequate training and safeguards.
- The agent may become an unacknowledged methodological collaborator even though epistemic responsibility remains with the human researchers.

## Data Contamination, Fabrication, and Output Integrity

- Agents may generate placeholder data, simulated rows, labels, variables, model results, file contents, tables, figures, or summaries that accidentally enter the real research pipeline.
- Agents may invent data rows when expected files are missing, silently replace failed analyses with toy examples, or generate "expected" results instead of preserving failed, null, or surprising results.
- Agents may overwrite, append to, "repair", impute, clean, filter, normalize, or remove data in ways that change substantive meaning without transparent justification.
- Agents may treat generated labels or annotations as observed or human-coded data.
- Agents may hallucinate variable names, column meanings, model results, data semantics, robustness checks, or analysis steps.
- Agent-written code may route analyses to test data, stale data, wrong subsets, generated data, or outdated intermediate files.
- Manuscript text may describe analyses, validation steps, results, or robustness checks that were suggested but not actually conducted.
- Generated tables, plots, and manuscript claims may not match the underlying code, data, or model output.
- The central epistemic risk is that the agent may become an invisible co-producer of evidence.

## Reproducibility and Provenance

- Agent interactions are often poorly logged, hard to reconstruct, or missing from the research record.
- Prompts, instructions, model versions, agent settings, tool permissions, accepted suggestions, rejected suggestions, and human edits may not be archived.
- It may be unclear which code was human-written, agent-written, jointly edited, or merely refactored by an agent.
- The same prompt may produce different code across time, models, providers, settings, and tool contexts.
- Agents may modify multiple files at once, making individual analytic changes hard to trace.
- Version history may not clearly identify agent-generated changes or distinguish researcher intent from agent suggestion.
- Agents may install dependencies, change versions, edit configuration files, or rely on unavailable packages, hidden local state, absolute paths, environment variables, or provider-specific tools.
- Notebooks can obscure execution order, hidden state, cached outputs, and interactive debugging sessions.
- Random seeds, train/test split definitions, nondeterministic steps, and hardware-dependent behavior may not be fixed or recorded.
- There may be no clear traceability from raw data to final table, figure, or manuscript claim.
- Lack of versioned mock data, fixtures, validation cases, and environment specifications can make agent-assisted development hard to assess.
- Reviewers may be unable to tell whether real data was ever exposed to the agent.

## Bias, Measurement, and Representation

- Agents may reproduce dominant-language, Western, platform-specific, majority-culture, or computer-science-centric assumptions.
- Agents may misclassify slang, irony, dialect, code-switching, memes, non-Latin scripts, visual culture, or context-dependent speech.
- Agents may recommend off-the-shelf classifiers, labels, prompts, or metrics that are inappropriate for the population, platform, language, or cultural context.
- Agent-generated categories may encode political, cultural, racialized, gendered, ideological, or class-based biases.
- Agents may flatten theoretically rich communication phenomena into convenient computational categories.
- Harmful categories may be normalized because they are technically convenient.
- Sensitive or marginalized populations may face greater privacy, classification, and representational risks.
- Moderation, toxicity, sentiment, stance, ideology, and similar measures may be especially fragile and require explicit uncertainty reporting.
- Agent-assisted analysis may obscure whose voices are misrepresented and whose assumptions are embedded in measurement choices.

## Transparency, Peer Review, Authorship, and Accountability

- There is no stable norm for how to disclose agent-assisted coding in manuscripts, appendices, acknowledgements, repositories, or AI-use statements.
- Disclosure may need to distinguish different forms of assistance: coding, debugging, refactoring, statistical modeling, visualization, validation, interpretation, and writing.
- Researchers and reviewers may need to know whether prompts were archived, agent-generated code was marked, agents had access to real data, and safeguards were used to protect data.
- Disclosure can become too vague to be useful, but too much detail may expose sensitive information.
- Non-disclosure makes it difficult to evaluate provenance, reproducibility, methodological control, and responsibility.
- Researchers may fear that disclosure will unfairly undermine trust in otherwise valid work.
- Reviewers may lack time, expertise, documentation, or tooling to audit full agent-assisted pipelines.
- Code may be transparent while the process that produced it remains opaque.
- Agents cannot take responsibility for research claims, errors, misconduct, privacy breaches, or ethical failures.
- Human authors remain accountable even when they do not fully understand agent-generated code.
- Teams may disagree about acceptable levels of agent involvement, disclosure, and responsibility for validation.
- Agent use may shift credit away from human research labor, including data cleaning, annotation, infrastructure, and methodological judgment.
- Generated code may contain unrecognized intellectual contributions, licensing traces, or copied patterns from training data.
- Hidden labor behind model development, data labeling, content moderation, and infrastructure is rarely acknowledged.

## Legal, Contractual, and Institutional Compliance

- External processing by agents or model providers may violate data protection laws, cross-border transfer rules, or institutional data policies.
- GDPR, HIPAA, FERPA, POPIA, and other local privacy regimes may apply depending on the data, location, and population.
- Data processing agreements with AI providers may be absent, unclear, or insufficient.
- Platform terms of service, data use agreements, consent language, IRB or ethics approvals, journal rules, and institutional procurement rules may not anticipate AI coding tools.
- Public communication data may still involve contextual privacy expectations, especially under bulk collection and analysis.
- Data involving minors, sensitive political communication, health-related communication, or vulnerable populations may require additional safeguards.
- Copyright, database rights, and licensing restrictions may apply to scraped text, images, videos, code, and generated code.
- Proprietary APIs may be used in ways not approved by the institution.
- Researchers may be unable to explain agent-related data flows, retention, deletion, accessibility, and audit procedures in a data management plan.

## Infrastructure and Workflow Engineering

- Package versions, environments, paths, and configurations may drift between agent-assisted development and protected analysis.
- Agents may change dependencies, lockfiles, configuration files, or environment descriptions to resolve errors, affecting downstream results.
- Docker, Conda, renv, virtualenv, and similar environment specifications may be incomplete or misleading.
- File paths may differ across local, cloud, and HPC environments; hard-coded paths may reveal identities, institutions, usernames, or sensitive project structures.
- Generated code may not be portable across systems, operating systems, hardware, GPUs, or random-seed settings.
- Analysis environments may accidentally include agent tooling, telemetry, cloud IDE extensions, or local IDE agents with different data policies.
- Agents may introduce excessive complexity, unnecessary abstraction, overengineering, fragile project structure, poor documentation, or unreadable notebooks.
- Hidden notebook execution-order problems can make results depend on stale state.
- Final results may be produced from outdated intermediate files.

## Writing and Manuscript Interpretation

- Agent-assisted writing may overstate claims, soften limitations, smooth over uncertainty, or make unresolved problems appear settled.
- Agents may introduce citations that do not exist or do not support the claim.
- Agents may reshape arguments toward generic framings and away from field-specific contributions.
- Agent-assisted writing can blur the line between language support, conceptual contribution, and rhetorical spin.
- Methods sections may omit agent involvement or describe idealized workflows rather than the workflows actually used.
- Manuscript text may claim robustness checks, validation steps, analyses, or interpretations that were suggested but not performed.
- Polished prose may obscure authorial responsibility, uncertainty, and the connection between the manuscript and the actual analysis pipeline.

## Environmental, Labor, Equity, and Field-Level Risks

- LLM use has environmental costs through compute, energy, water use, hardware, and infrastructure.
- Large-scale agentic workflows may increase carbon footprints and normalize high-compute research practices.
- Model development may involve labor conditions, content moderation work, data-labeling work, infrastructure labor, and extractive data practices that conflict with research ethics commitments.
- Researchers may need to acknowledge these costs without reducing them to ritual boilerplate.
- Unequal access to high-quality agents, paid tools, cloud infrastructure, and institutional support may widen research inequalities.
- Commercial dependence on a small number of AI providers may reduce academic autonomy.
- Agent-assisted productivity may reshape expectations for graduate students, researchers, reviewers, journals, supervisors, funders, and collaborators.
- Speed and technical polish may become valued over understanding, theoretical grounding, and cautious validation.
- Responsible researchers may be disadvantaged compared with less cautious researchers if the field lacks shared norms.

## Governance and Workflow Design

- Labs and project teams may lack shared policies for where, when, and how agents can be used.
- Teams may need role-based access rules specifying who can use agents, on what data, in which environments, and for which tasks.
- Different collaborators may use different agents, settings, prompts, model versions, coding styles, dependencies, and disclosure practices.
- One collaborator may expose data against team policy or institutional rules.
- Responsibility for validating agent-generated code may be unclear in collaborative projects.
- Large automatic edits may create merge conflicts or obscure the source of analytic changes.
- Best practices may differ across public data, restricted data, commercial platform data, interviews, ethnographic materials, donated digital trace data, and administrative data.
- Overly strict rules may push agent use underground; overly loose rules may normalize unsafe practice.
- Responsible workflows may require templates, standard operating procedures, repository audits, ignored-file audits, environment permission checks, incident-response plans, and explicit rules for what the agent may read.
- The field needs shared language for communicating boundaries, safeguards, residual risks, acceptable uses, questionable uses, and prohibited uses.

## Framing Sentence

The core issue is not simply that coding agents can make mistakes. It is that they can make plausible, productive, hard-to-notice mistakes inside workflows where validity, privacy, and trust matter enormously.
