# Project: Batch Script Automation

This project consists of two batch files (`mainscript.bat` and `start.bat`) designed for automating tasks such as folder creation, opening URLs, and running other scripts.

---

## Files Overview

### 1. **mainscript.bat**
This is the main automation script. It performs the following tasks:
- Disables command echoing for cleaner output.
- Opens multiple GitHub release URLs in the default browser.
- Waits for 5 seconds using a timeout.
- Executes other batch files (`start.bat`, `start (1).bat`, `start (2).bat`) located in the `Downloads` directory.

### 2. **start.bat**
This is a simple loop script that repeatedly calls the `start` command.
- The `:start` label defines the loop entry point.
- Executes the `start` command.
- Redirects execution back to `:start`, creating an infinite loop.

---

## Usage
1. Place both files (`mainscript.bat` and `start.bat`) in the same directory.
2. Run `mainscript.bat` to execute the automation sequence.
3. Ensure that the paths in the script (e.g., Desktop, Downloads) exist and match your system’s directory structure.

---

## Notes
- Running `start.bat` directly will cause an **infinite loop** of opening new command windows. It is recommended to only run it through `mainscript.bat`.
- Modify the GitHub release URLs in `mainscript.bat` as per your project requirements.
- Administrator privileges may be required if creating folders in restricted directories.

---

## Example Workflow
1. Run `mainscript.bat`.
2. A new folder is created on the Desktop with subfolders.
3. GitHub release pages open automatically.
4. After 5 seconds, additional batch files (`start.bat`, `start (1).bat`, and `start (2).bat`) are executed.

---

## Warning ⚠️
- `start.bat` creates an infinite loop of command prompts. Use with caution.
- Make sure to edit file paths to match your environment to avoid errors.

