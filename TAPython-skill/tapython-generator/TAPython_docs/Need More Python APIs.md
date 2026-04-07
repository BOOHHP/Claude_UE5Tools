## Need More Python APIs[¶](#need-more-python-apis)

This guide explains how to access additional Python APIs in Unreal Engine.

## Overview[¶](#overview)

If you need APIs not directly available in TAPython, there are several ways to access them.

## Using unreal Module[¶](#using-unreal-module)

The `unreal` module provides access to many UE C++ APIs:

```python
import unreal

# Access C++ classes
UClass = unreal.get_class(unreal.Actor)
```

## Using PythonBPLib[¶](#using-pythonbplib)

TAPython's PythonBPLib provides many editor functions:

```python
# Access editor functions
unreal.PythonBPLib.some_function()
```

## Accessing C++ APIs Directly[¶](#accessing-c-apis-directly)

Many C++ APIs can be called from Python:

```python
# Call C++ function
result = unreal.some_cpp_function(args)
```

## Contributing New APIs[¶](#contributing-new-apis)

If you need a specific API that isn't available:

1. Check if it's available in C++
2. Consider requesting it in the TAPython GitHub
3. Implement it yourself in C++ if needed

## Resources[¶](#resources)

- Unreal Engine Python API Documentation
- TAPython GitHub Issues

 [Previous](most_used_editor_apis.html) [Next](auto_complete_for_tapython.html)
