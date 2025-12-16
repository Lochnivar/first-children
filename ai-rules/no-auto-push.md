# AI Rule: No Auto-Push to GitHub

**Status:** Active Rule  
**Priority:** High  
**Category:** Git Workflow

## Rule

**AI assistants MUST NOT push commits to GitHub without explicit user request.**

## Details

- **Commits:** AI may create commits locally as part of organizing work
- **Push:** AI must NOT execute `git push` unless the user explicitly requests it
- **User Control:** The user maintains full control over when changes are pushed to remote repositories

## Rationale

- Allows user to review commits before pushing
- Gives user control over when changes become visible to collaborators
- Prevents accidental pushes of incomplete or experimental work
- Respects user's workflow preferences

## Exceptions

None. This rule applies in all circumstances unless the user explicitly requests a push.

## Related Rules

- See [README.md](README.md) for other AI rules
- This rule complements other workflow rules but takes precedence for git push operations

---

*Last updated: December 2024*

