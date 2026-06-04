# Validation Checklist

Use this checklist before interpreting real-data outputs.

## Data Structure

- [ ] Required columns are present.
- [ ] Column types are correct.
- [ ] Row counts are checked before and after transformations.
- [ ] Duplicate IDs are checked.
- [ ] Missingness patterns are checked.
- [ ] Timestamps and time zones are checked.
- [ ] Text encoding and language fields are checked.

## Transformations

- [ ] Filtering rules match the research design.
- [ ] Exclusion criteria are documented.
- [ ] Joins preserve the intended unit of analysis.
- [ ] Row losses after joins are explained.
- [ ] Aggregations use the correct denominator.
- [ ] Sampling design and weights are preserved where relevant.

## Modeling or Classification

- [ ] Train/test separation is verified.
- [ ] No information leaks between training and test data.
- [ ] Labels are inspected manually.
- [ ] Unexpected labels are investigated.
- [ ] Model inputs and outputs have expected dimensions.
- [ ] Uncertainty is reported where relevant.

## Outputs

- [ ] Tables match source outputs.
- [ ] Figures match source outputs.
- [ ] Plots use appropriate scales and denominators.
- [ ] Final claims match validated results.
- [ ] Protected outputs remain in the clean environment.

## Agent Review

- [ ] Agent-generated tests were reviewed by a human.
- [ ] Agent-generated explanations were checked against code.
- [ ] Core transformations were reviewed without relying only on the agent.
- [ ] Any agent-assisted changes are documented.
