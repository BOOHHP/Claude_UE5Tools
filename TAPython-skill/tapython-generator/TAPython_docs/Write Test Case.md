## Write Test Case[¶](#write-test-case)

This guide explains how to write test cases for TAPython tools.

## PythonTestLib[¶](#pythontestlib)

PythonTestLib provides functionality for unit testing TAPython's editor extension APIs.

## Logs[¶](#logs)

### Getting Logs from Output[¶](#getting-logs-from-output)

```python
logs = unreal.PythonTestLib.get_logs()
```

Note:
Log and Output Log are different. Clearing Output Log does not affect PythonTestLib.get_log().

### Clearing Log Buffer[¶](#clearing-log-buffer)

```python
unreal.PythonTestLib.clear_log_buffer()
```

Default log buffer size is 10240 logs, configurable via Config.ini.

## Delayed Command Invocation[¶](#delayed-command-invocation)

### delay_call[¶](#delaycall)

Designed to simulate user operations:

- Main thread execution
- "Delay Time" equals "Available Time in Editor"

### push_call[¶](#push_call)

Wrapper for delay_call that calculates accumulated delay time:

```python
def test_category_level_actor(self, id):
    self.test_being(id=id)
    level_path = '/Game/StarterContent/Maps/StarterMap'
    self.push_call(py_task(unreal.EditorLevelLibrary.load_level, level_path), delay_seconds=0.1)
    self.push_call(py_task(self._testcase_get_all_worlds), delay_seconds=0.5)
```

## Verifying Data[¶](#verifying-data)

### Capturing Editor Window[¶](#capturing-editor-window)

```python
def editor_snapshot(window_name):
    unreal.PythonBPLib.execute_console_command(f'EditorShot Name="{window_name}"')
```

### Capturing Chameleon Window[¶](#capturing-chameleon-window)

```python
saved_file_path = unreal.ChameleonData.snapshot_chameleon_window(json_path, override_size)
```

### OCR[¶](#ocr)

Using easyocr:

```python
ocr_result = easyocr.Reader(['en'], gpu=False, verbose=False).readtext(image_file_path)
```

## Resources[¶](#resources)

Example test cases: [UE_TAPython_Plugin_TestCases@github](https://github.com/cgerchenhp/UE_TAPython_Plugin_TestCases)

 [Previous](take_ui_snapshot.html) [Next](on_close_callback.html)
