# AI Rule: Hash Consistency Tracking

**Date:** December 2024 (Adapted for Fantasy Project)  
**Status:** OPTIONAL/INFORMATIONAL RULE  
**Purpose:** Ensure dependency tracking and consistency when files are edited

**Note:** This rule is adapted from an alt-history project. The hash tracking scripts referenced below may not exist in this project. This document serves as a guideline for maintaining consistency, but manual tracking may be required.

---

## THE RULE

**When AI edits any markdown file that has dependency tracking, it SHOULD:**

1. **Note any dependency relationships** mentioned in the file
2. **Consider impact on dependent files** when making edits
3. **Update documentation** if dependencies change
4. **Maintain consistency** across related files

---

## DEPENDENCY TRACKING (If Implemented)

If dependency tracking is added to this project, the following would apply:

### After Editing Any File

After making edits to a markdown file:

1. **Check if the file has a "Document Dependencies" section**
2. **If it does, note that dependencies may need review**
3. **Check if other files reference the edited file**
4. **Update cross-references** if paths or content change

### Updating Dependent Files

If the edited file is referenced by other files:

1. **Find files that reference the edited file** (via cross-references or indexes)
2. **Review dependent files** for consistency
3. **Update references** if file paths or content changed
4. **Verify consistency** across related documents

---

## CURRENT PROJECT STRUCTURE

This project uses:
- Cross-references via markdown links
- Index files (README.md) in each directory
- Framework consistency process (`meta/CONSISTENCY_PROCESS.md`)

### Consistency Maintenance

For this fantasy project, consistency is maintained through:

1. **Framework Conformance** - See `meta/CONSISTENCY_PROCESS.md`
2. **Cross-References** - Markdown links between related files
3. **Index Files** - README.md files track related content
4. **Consistency Checks** - Manual review using `oververse/worlds/iolinus/CONSISTENCY_CHECK.md`

---

## HASH TRACKING (Future Enhancement)

If hash tracking scripts are added to this project, they would:

### Hash Calculation (Hypothetical)
```bash
# If implemented, would calculate hash for a file
python scripts/calculate-hash.py <file-path>

# Output: 8-character hash (e.g., "a1b2c3d4")
```

### Consistency Check (Hypothetical)
```bash
# If implemented, would check all files
python scripts/consistency-checker.py

# Or check specific file
python scripts/consistency-checker.py <file-path>
```

### Dependency Table Format (If Added)
```markdown
## Document Dependencies

| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Source Document | `../path/to/source.md` | `a1b2c3d4` | 2024-12-XX | ✅ Verified |

**This Document's Hash:** `98765432`  
**Last Updated:** 2024-12-XX
```

---

## WHEN TO UPDATE REFERENCES

### Always Update:
- ✅ After moving files to new locations
- ✅ After renaming files
- ✅ After changing file structure
- ✅ After major content changes that affect dependencies
- ✅ When framework changes affect world content

### Current Process:
1. Edit file
2. Check related files for cross-references
3. Update links in index files (README.md) if needed
4. Review framework conformance if applicable
5. Update `oververse/worlds/iolinus/CONSISTENCY_CHECK.md` if framework-related

---

## INTEGRATION WITH OTHER RULES

This rule works alongside:
- **Golden Rule (No Original Text):** Consistency tracking applies to all files
- **Framework Consistency:** See `meta/CONSISTENCY_PROCESS.md`
- **World Consistency:** See `oververse/worlds/iolinus/CONSISTENCY_CHECK.md`

---

## CURRENT APPROACH

Since hash tracking scripts may not exist:

1. **Use Cross-References** - Markdown links maintain relationships
2. **Update Index Files** - Keep README.md files current
3. **Framework Process** - Follow `meta/CONSISTENCY_PROCESS.md` for framework-related changes
4. **Manual Review** - Periodically review consistency across files

---

## QUICK CHECKLIST

When editing any file:
- [ ] Make edits
- [ ] Check for cross-references to this file in other documents
- [ ] Update links in index files (README.md) if file moved/renamed
- [ ] Review framework conformance if applicable
- [ ] Verify related files are still consistent
- [ ] Update `oververse/worlds/iolinus/CONSISTENCY_CHECK.md` if framework-related

---

## FUTURE ENHANCEMENTS

If hash tracking is desired:
- Consider adding Python scripts for hash calculation
- Consider adding dependency tracking sections to files
- Consider automating consistency checks
- Consider pre-commit hooks for hash updates

---

**Status:** ADAPTED RULE - Informational/Reference  
**Scripts:** May not exist - manual tracking recommended  
**Last Updated:** 2024-12-XX

---

**Remember:** The goal is consistency, not perfection. Focus on maintaining accurate cross-references and following the framework consistency process. Hash tracking is a tool for change detection, but careful editing and cross-reference maintenance serve the same purpose.
