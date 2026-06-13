# Supply-Chain-Threat-Hunting-Toolbox

A collection of lightweight, custom Python utilities and automated engines designed to analyze open-source packages (npm, PyPI) and detect software supply-chain threat vectors before installation. 

This repository serves as an active security research lab focusing on malicious code behavior, code-level heuristics, and automated threat triage.

## Active Modules & Architecture

### 1. Registry Typosquatting Evaluator (`typosquat_sentinel.py`) - *In Development*
* **Objective:** Mitigate brandjacking and typosquatting vectors.
* **Mechanics:** Utilizes string-similarity metrics (including Levenshtein Distance algorithms) to programmatically cross-reference a manifest of approved internal dependencies against untrusted public registry inputs, isolating deceptively similar package names.

### 2. Malicious Installation Hook Sentinel (`hook_sentinel.py`) - *In Development*
* **Objective:** Detect pre-execution or installation-stage compromises.
* **Mechanics:** An automated metadata parser that securely ingests package configuration layouts (such as Node.js `package.json` manifests or Python `setup.py` scripts) to flag unauthorized lifecycle hooks (`preinstall`, `postinstall`) mapping to outbound connections or hidden shell executions.

### 3. AST-Driven Sources & Sinks Engine (`ast_engine.py`) - *In Development*
* **Objective:** Uncover complex code anomalies and highly obfuscated payloads where simple regex searches (`grep`) fail.
* **Mechanics:** Leverages Python's native `ast` (Abstract Syntax Tree) module to convert source files into structural logical trees. The engine walks the nodes to flag dangerous system code execution sinks (e.g., `os.system`, `subprocess`) feeding off dynamically resolved variables or obfuscated strings.

## Research & Upskilling Goals
This toolkit is part of a dedicated deep-dive into automated code analysis, software bill-of-materials (SBOM) verification, and software supply chain defense mechanisms. 

## License
This project is licensed under the MIT License - see the LICENSE file for details. For educational and authorized defensive security research purposes only.
