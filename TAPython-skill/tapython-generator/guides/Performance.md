# 性能优化指南 / Performance Guide

Best practices for building performant TAPython tools that don't freeze or slow down the Unreal Editor.

---

## 批量资产操作 / Batch Asset Operations

### Process in Chunks
Never process thousands of assets in a single loop without yielding. Use `unreal.ScopedSlowTask` to provide progress feedback and keep the editor responsive:

```python
def batch_process(self):
    try:
        assets = unreal.EditorAssetLibrary.list_assets("/Game/", recursive=True)
        if not assets:
            self.data.set_text("status_label", "No assets found")
            return

        total = len(assets)
        with unreal.ScopedSlowTask(total, "Processing assets...") as slow_task:
            slow_task.make_dialog(True)  # Show cancel button
            for i, asset_path in enumerate(assets):
                if slow_task.should_cancel():
                    self.data.set_text("status_label", f"Cancelled at {i}/{total}")
                    return
                slow_task.enter_progress_frame(1, f"Processing {i+1}/{total}")

                try:
                    # Process single asset
                    asset = unreal.EditorAssetLibrary.load_asset(asset_path)
                    # ... your logic ...
                except Exception as e:
                    unreal.log_error(f"Failed on {asset_path}: {str(e)}")
                    continue

        self.data.set_text("status_label", f"✓ Processed {total} assets")

    except Exception as e:
        unreal.log_error(f"Batch process failed: {str(e)}")
        self.data.set_text("status_label", f"Error: {str(e)}")
```

### Key Principles
- **Always show progress** — users need to know the tool isn't frozen
- **Support cancellation** — `slow_task.should_cancel()` lets users abort long operations
- **Continue on failure** — one bad asset shouldn't stop the entire batch
- **Report results** — show processed/failed counts via `set_text` on a status label

---

## UI 响应性 / UI Responsiveness

### Minimize Widget Count
Each widget in the UI tree adds rendering overhead. For large data sets, prefer `SListView` over creating many individual `STextBlock` widgets:

```json
// ❌ Avoid: 500 individual text blocks
"Slots": [
    {"STextBlock": {"Text": "Item 1"}},
    {"STextBlock": {"Text": "Item 2"}},
    // ... hundreds more
]

// ✅ Better: SListView with virtual scrolling
{"SListView": {"Aka": "results_list", "ItemHeight": 20}}
```

### Avoid Frequent set_text in Tight Loops
Calling `self.data.set_text()` triggers a UI update. In a loop processing 1000 items, update the status every N items instead of every iteration:

```python
for i, asset in enumerate(assets):
    # Process asset...

    # Update UI every 50 items, not every item
    if i % 50 == 0 or i == len(assets) - 1:
        self.data.set_text("status_label", f"Processing {i+1}/{len(assets)}")
```

### Use SScrollBox for Long Content
Wrap dynamic content in `SScrollBox` to enable scrolling instead of clipping. This is both a usability and performance pattern — the editor only renders visible widgets in a scroll view. See [Pitfall 6](../pitfalls/CommonPitfalls.md#pitfall-6-ui-overflow--no-scrolling).

---

## 内存管理 / Memory Management

### Clean Up in OnClosePyCmd
Always release resources when the tool closes. Large data structures held by the singleton persist until explicitly cleared:

```python
def cleanup(self):
    """Release resources on tool close."""
    try:
        self.cached_assets = None
        self.search_results = None
        self.large_data = None
    except Exception as e:
        unreal.log_error(f"Cleanup failed: {str(e)}")
```

```json
"OnClosePyCmd": "MyTool.instance.cleanup(); MyTool.instance = None"
```

### Avoid Storing Large Data in the Singleton
The singleton lives for the entire editor session. Store only what you need:

```python
# ❌ Avoid: caching thousands of loaded assets
self.all_assets = [unreal.EditorAssetLibrary.load_asset(p) for p in all_paths]

# ✅ Better: store paths, load on demand
self.asset_paths = all_paths
# Load individually when needed:
asset = unreal.EditorAssetLibrary.load_asset(self.asset_paths[index])
```

### Use Weak References for UE Objects
Unreal objects can be garbage collected by the engine. Holding strong Python references can prevent GC or cause stale references:

```python
import weakref

# Store a weak reference instead of a strong one
self.actor_ref = weakref.ref(actor)

# Access later — returns None if GC'd
actor = self.actor_ref()
if actor is not None:
    # Safe to use
    pass
```

---

## 异步操作 / Async Operations

### ScopedSlowTask for Long Operations
As shown above, `unreal.ScopedSlowTask` is the primary mechanism for long operations. It shows a progress bar and keeps the editor from appearing frozen.

### Timer-Based Periodic Updates
For operations that need periodic execution (e.g., monitoring, auto-refresh), use Unreal's timer system instead of busy loops:

```python
def start_monitoring(self):
    """Start a periodic check using a timer."""
    try:
        # Register a timer that calls update_status every 2 seconds
        self.timer_handle = unreal.PythonBPLib.set_timer(
            self.update_status, 2.0, True  # repeat=True
        )
    except Exception as e:
        unreal.log_error(f"Timer setup failed: {str(e)}")

def stop_monitoring(self):
    """Stop the periodic timer."""
    try:
        if hasattr(self, 'timer_handle') and self.timer_handle:
            unreal.PythonBPLib.clear_timer(self.timer_handle)
            self.timer_handle = None
    except Exception as e:
        unreal.log_error(f"Timer cleanup failed: {str(e)}")
```

> **Important**: Always clear timers in your `cleanup()` method called from `OnClosePyCmd`.

### Progress Reporting Patterns
Combine `ScopedSlowTask` with UI status updates for the best user experience:

```python
def process_with_progress(self, items):
    total = len(items)
    processed = 0
    with unreal.ScopedSlowTask(total, "Working...") as slow_task:
        slow_task.make_dialog(True)
        for item in items:
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1)
            # ... process item ...
            processed += 1

    self.data.set_text("status_label", f"Done: {processed}/{total}")
```

---

## 最佳实践总结 / Best Practices Summary

| Area | Do | Don't |
|------|----|-------|
| **Batch operations** | Use `ScopedSlowTask` with cancel support | Process all items in a blocking loop |
| **Progress** | Update UI every N items | Call `set_text` on every iteration |
| **Lists** | Use `SListView` for large data sets | Create hundreds of individual widgets |
| **Memory** | Clear data in `cleanup()` / `OnClosePyCmd` | Cache large asset lists in the singleton |
| **UE objects** | Use `weakref` for actor/asset references | Hold strong references to transient objects |
| **Timers** | Clear in `cleanup()`; use Unreal timer APIs | Use `while True` loops or `time.sleep()` |
| **Root widget** | Wrap in `SScrollBox` for dynamic content | Use bare `SVerticalBox` for long forms |
| **Error handling** | Wrap each item in try-except, continue | Let one failure abort the entire batch |

---

## 参考链接 / References

- [Common Patterns](../patterns/CommonPatterns.md) — implementation templates with error handling
- [Common Pitfalls](../pitfalls/CommonPitfalls.md) — architectural mistakes to avoid
- [Troubleshooting Guide](./Troubleshooting.md) — diagnosing runtime issues
- [Most Used Editor APIs](../TAPython_docs/Most%20Used%20Editor%20APIs.md) — common Unreal Python operations
- [ChameleonData API](../TAPython_docs/TA%20Python%20ChameleonData%20API.md) — data bridge reference
