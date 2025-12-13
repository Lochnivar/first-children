# Consistency Process

## Source of Truth

**The framework in `../FRAMEWORK.md` is the PRIMARY source of truth.**

The framework contains the **general/universal** rules that apply across the entire over-universe. All stories in `../worlds/` are SUBORDINATE and must conform to framework rules, but they can:
- **Expand** framework rules with world-specific details
- **Provide exceptions** that work within or modify general rules

World details are either expansions or exceptions to the general framework rules.

## When Framework Changes

1. Update `../FRAMEWORK.md`
2. Check all worlds in `../worlds/` for contradictions
3. Update any world that contradicts
4. Document in `CHANGE_LOG.md`:
   - What changed in framework
   - Which worlds were affected
   - How worlds were updated

## When Story Contradicts Framework

1. Identify the contradiction
2. Decide: Intentional expansion or mistake?
   
   **If Intentional Expansion:**
   - Update framework first to accommodate
   - Then update story
   - Document as framework evolution
   
   **If Mistake:**
   - Change story to conform
   - Document why change was needed
   - Update story's CONSISTENCY_CHECK.md

3. Document decision in story's CONSISTENCY_CHECK.md

## Framework Expansion vs. Contradiction

**Framework Expansion (World Expands General Rules):** Story introduces new element that adds specific details **within** the framework rules
- Example: Framework says "mortals may have fragmented quantum abilities" → World expands with specific abilities and rules
- Example: Framework establishes liberation patterns → World expands with specific characters and conflicts
- Example: New First Child with different personality (expands general First Children concept)
- Process: World expands framework rules with specific details (this is expected and encouraged)

**Framework Exception (World Provides Variation):** Story introduces world-specific variation that works **within or modifies** general rules
- Example: Framework provides universal principles → World has unique cultural interpretation
- Example: Framework establishes patterns → World demonstrates a variation of those patterns
- Process: World provides exception/variation that respects framework constants

**Contradiction (Violates Framework Rule):** Story violates established framework constant
- Example: Story says "First Children can't create worlds" but framework says they can
- Example: Story violates established cosmological constant (Big 'G' God, quantum foundation, etc.)
- Example: Story violates fundamental prohibition that cannot be changed
- Process: Story must change OR framework constant was incorrectly stated and needs correction (rare)

## Review Process

- Before major story changes, check framework
- Before framework changes, check all stories
- Regular consistency audits (quarterly?)
- Document all changes

## Decision Tree for Contradictions

1. **Is it a contradiction or an expansion?**
   - Contradiction = violates established rule
   - Expansion = adds new example/variation within rules

2. **If contradiction:**
   - Is the framework rule correct?
     - If YES: Story must change
     - If NO: Framework rule needs correction, then update framework first

3. **If expansion:**
   - Does it fit within existing framework rules?
     - If YES: Add to story, optionally add to framework as example
     - If NO: Re-evaluate as potential contradiction

4. **Always document:**
   - Decision made
   - Reason for decision
   - Changes made
   - Impact on other worlds (if any)

## Change Log

All framework changes and story updates should be documented in `CHANGE_LOG.md`.

---

*This process ensures consistency across all worlds while allowing for creative expansion within the framework rules.*

