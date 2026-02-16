# Simple Flet Login App (Android)

This project is a mobile application built with the **Flet** framework (Python), configured to be automatically built into an **APK** file using **GitHub Actions**.

## 🛠️ Enhancements & Fixes

### 1. CI/CD Workflow (GitHub Actions)
The `.github/workflows/bulid.yml` has been optimized for reliability:
* **Fixed EOFError:** Integrated the `yes |` command to bypass interactive prompts during the build process on headless servers.
* **Version Management:** Configured Flutter SDK to use the `stable` channel for maximum compatibility with Flet.
* **Dependency Automation:** Added a script to auto-detect and install dependencies from `requirements.txt`.
* **Artifact Pathing:** Fixed the APK output path to ensure successful uploads of the generated binaries.

### 2. Python App (Flet UI)
The `main.py` was refactored specifically for mobile devices:
* **SafeArea Integration:** Used `ft.SafeArea` to prevent UI elements from being hidden under notches or status bars.
* **Fixed "White Screen" Issue:** Removed forced `expand=True` properties that caused layout collapses on mobile, replaced with proper alignments.
* **Adaptive Scrolling:** Enabled `page.scroll = "adaptive"` to handle small screens and keyboard visibility gracefully.
* **Standardized Entry Point:** Added the `if __name__ == "__main__":` block to ensure the build CLI detects the app correctly.
