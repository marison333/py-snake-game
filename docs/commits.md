**Conceptual commits** in Git are a practice where each commit represents a **single, coherent idea** or **logical change** in your codebase, rather than a random set of edits or changes made over time. This approach improves code readability, collaboration, and version control history.

# What Is a Conceptual Commit?

A **conceptual commit**:
• Implements **one distinct idea or change**.
• Answers the question: **“What is this commit about?”**
• Can be understood **without needing to read the code** in full.
• Is easy to review, revert, or build upon.

## Why Use Conceptual Commits?
1. **Clarity** – Other developers can quickly understand your change.
2. **Debugging** – Easier to use git bisect to isolate bugs.
3. **Code review** – Reviewers can focus on a single idea at a time.
4. **Reversibility** – One change = one commit = easy rollback if needed.
5. **History tracking** – Logs show clean, logical progression.

# How to Make Conceptual Commits
1. **Work on one idea at a time.**
	• Split refactoring, feature changes, and bug fixes.
2. **Stage selectively** with `git add -p (interactive)`.
	• Choose what to include in the commit.
3. **Write clear messages**, ideally in [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/) format:
	`<type>(optional scope): <description>`
4. **Squash or reorganize commits** with `git rebase -i` if needed.
5. **Avoid mixing unrelated changes.**

**Tip: Conceptual Commits in Practice**
Imagine you:
• Add a new form
• Fix a bug in another component
• Rename a variable

Split this into:
```
1. feat(form): add contact form component
2. fix(header): fix broken link to homepage
3. refactor: rename 'userName' to 'username' in UserProfile
```

Each is **reviewable and traceable** on its own.

## Branch Naming
- Use structured, descriptive names for branches (one topic per branch).
- Suggested patterns:
  - `feat/<short-description>` for new features
  - `fix/<short-description>` for bug fixes
  - `refactor/<short-description>` for refactoring work
  - `docs/<short-description>` for documentation updates
  - `chore/<short-description>` for maintenance tasks
- Keep names lowercase, words separated by hyphens, and avoid spaces.

Example:
- `feat/enhance-snake-ai`
- `fix/collision-boundary-error`
- `docs/add-naming-conventions`

## **Types**
there are more **types of conceptual commits** beyond the few listed in the examples (feat, fix, refactor, etc.). These are often based on the [**Conventional Commits**](https://www.conventionalcommits.org/en/v1.0.0/) standard, which provides a useful naming convention to describe the purpose of each commit.

### **Common Commit Types (Conventional Commits)**

| **Type** | **Purpose**                                                   |
| -------- | ------------------------------------------------------------- |
| feat     | A new feature                                                 |
| fix      | A bug fix                                                     |
| refactor | A code change that neither fixes a bug nor adds a feature     |
| chore    | Maintenance tasks (e.g., updating configs, build tools, deps) |
| docs     | Documentation-only changes                                    |
| style    | Code style changes (formatting, whitespace, semicolons)       |
| test     | Adding or modifying tests                                     |
| perf     | A code change that improves performance                       |
| build    | Changes affecting the build system or external dependencies   |
| ci       | Changes to CI/CD configuration                                |
| revert   | Revert a previous commit                                      |
| chore    |                                                               |

### **Examples of Each Type**
```
feat(ui): add dark mode toggle
fix(login): handle empty password input
refactor(auth): simplify token validation logic
chore(deps): update eslint to v9.1.0
docs(readme): update installation instructions
style(button): remove extra margin
test(api): add test for getUser endpoint
perf: cache user profile data
build: switch to Vite for faster builds
ci(github): add Node.js v20 to test matrix
revert: revert "feat(api): add rate limiting"
```