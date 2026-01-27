# Task Structure Template

Use this format for every task in the plan.

```markdown
### Task N: [Component/Feature Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py`

**Step 1: Write the failing test**

```python
# Code for the test
```

**Step 2: Run test to verify it fails**
- Run: `pytest tests/path/test.py::test_name`
- Expected: FAIL

**Step 3: Write minimal implementation**

```python
# Code for the implementation
```

**Step 4: Run test to verify it passes**
- Run: `pytest tests/path/test.py::test_name`
- Expected: PASS

**Step 5: Commit**
```bash
git add .
git commit -m "feat: [description]"
```
```
