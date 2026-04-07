## How to Debug Python in UE[¶](#how-to-debug-python-in-ue)

This guide explains how to debug Python code in Unreal Engine.

## Overview[¶](#overview)

Debugging Python in Unreal Engine requires special techniques due to the embedded Python environment.

## Using Print Statements[¶](#using-print-statements)

The simplest debugging method:

```python
print("Debug: Reached here")
print(f"Variable value: {variable}")
```

Output appears in the Output Log.

## Using the Python Console[¶](#using-the-python-console)

Test code in the Python Console before adding to your tool:

1. Open **TA Python > Python Console**
2. Type and execute Python code
3. See results immediately

## Using VS Code Debugger[¶](#using-vs-code-debugger)

### Setup[¶](#setup)

1. Install the debugpy package:
   ```
   pip install debugpy
   ```

2. Add this to your code:
   ```python
   import debugpy
   debugpy.listen(("localhost", 5678))
   ```

3. Attach VS Code debugger to localhost:5678

## Using PyCharm[¶](#using-pycharm)

PyCharm Professional supports remote debugging:

1. Configure Python remote debug
2. Set breakpoint in your code
3. Attach to the running Python in UE

## Best Practices[¶](#best-practices)

- Use try/except blocks for error handling
- Log important events
- Use the Output Log for debugging

## Common Issues[¶](#common-issues)

- Variable values not showing
- Breakpoints not hitting
- Connection failures

 [Previous](extend_an_assets_editor.html) [Next](most_used_editor_apis.html)
