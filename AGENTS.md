<!--
  SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
  SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
  SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>

  SPDX-License-Identifier: MulanPSL-2.0
-->

# openRuyi Agent Instructions

Obey the [AI-Assisted Contribution Policy](https://openruyi.cn/community/policy/ai-contribution-policy) whenever you work on or interact with openRuyi projects.
Use normative keywords according to [RFC 2119](https://openruyi.cn/docs/guide/normative-keywords-reference) in project text.

## Do not

- Agents **MUST NOT** include unrelated changes in the diff.
- Agents **MUST NOT** include task conversations, task prompts, or agent iteration history in maintainer-facing text.
- Agents **MUST NOT** list AI models or services as authors or contributors in commits, `SPEC` files, or patch headers.
  This includes author names, email addresses, `Co-Developed-By`, `Co-Authored-By`, and similar attribution.
- Agents **MUST NOT** write replies to review comments, issues, or discussions in the openRuyi main repository.
- Agents **MUST NOT** push changes to the [openRuyi repository](https://github.com/openRuyi-Project/openRuyi) or create PRs, issues, or discussions there.
- Agents **MUST NOT** change PR templates, issue templates, or their configuration files.

## Contributor responsibilities

- The human contributor **MUST** personally add the [DCO](https://developercertificate.org/) `Signed-off-by` trailer.
- The human contributor **MUST** disclose AI use when the AI-Assisted Contribution Policy requires disclosure.

## Repository layout

```text
_manifest                     Package directory manifest for the build service
AGENTS.md                     Agent instructions
LICENSE                       Repository license
LICENSES/                     License texts
SPECS/                        Package recipes, patches, and local sources
  <pkgname>/                  Directory name = SPEC filename without .spec = Name value after RPM macro expansion
README.md                     Project overview
REUSE.toml                    Copyright and license annotations
scripts/
  pre-commit-hooks/           Repository checks
  remoteassetify.py           Remote downloads and checksum correction patches
  update-package              Git-to-OBS package synchronization, with remote writes
```

## Guides

Follow the applicable guides for these tasks:

- [Packaging](https://openruyi.cn/docs/guide/packaging-guidelines): Write `SPEC` files. Give source checksums.
- [Patches](https://openruyi.cn/docs/guide/packaging-guidelines/Patch/): Give each patch an upstream reference and status.
  Base downstream patches on applicable upstream fixes when available.
- [Containers](https://openruyi.cn/docs/guide/how-to-install/container/): Prepare local test environments with `Docker` or `Podman`.
- [New contributors](https://openruyi.cn/docs/guide/new-contributor-guide): Prepare the repository. Follow the contribution workflow.
- [Build systems](https://openruyi.cn/docs/guide/buildsystem-authoring-guidelines): Write build steps with the applicable macros.
- [Documentation](https://openruyi.cn/docs/guide/documentation-contribution-guide): Change documentation according to this guide.
- [Style](https://openruyi.cn/docs/guide/styleguide): Use the project writing style.
- [RemoteAsset](https://openruyi.cn/docs/guide/remoteassetify-usage-guide): Use `remoteassetify.py` for remote downloads and checksum correction patches.
   - If a source checksum changes unexpectedly at the same URL, verify the cause before updating the checksum. Agents **MUST NOT** replace a checksum merely to pass checks.
- [Package review](https://openruyi.cn/docs/guide/review/ReviewGuidelines/): Do the required `riscv64` builds and `RPM` checks.

When general and subject-specific packaging guidelines conflict, use the subject-specific guidelines.
The maintainer decides unresolved rule conflicts and requests for exceptions. Give the applicable rules and reasons in the request.

## Licensing and provenance

- Use [SPDX license expressions](https://spdx.github.io/spdx-spec/v3.0.1/annexes/spdx-license-expressions/) that agree with the upstream license texts.
- Keep the original patch authorship.

## Changes

### Commits

- Use existing coding conventions.
- Related changes **MAY** share one PR, within or across packages.
- Divide commits by purpose and impact. Keep related changes for one clear objective in each commit.

### PR comments: review context

The human contributor **SHOULD** provide review context in PR comments when the diff alone is insufficient.
Include applicable items:

- The problem and expected behavior, with a related issue link if available.
- For a new package, its use cases and value to the RISC-V ecosystem.
- For changes to package behavior: functional and compatibility test results for affected packages, and reasons for relevant tests not run.
- The technical reason for each disabled test.
- The corresponding build link on the openRuyi build service, if available.

PR descriptions **SHOULD** keep the template structure. Fill in only the relevant sections.

## Core components

- The destination for `linux` source changes is [openRuyi-Project/linux](https://github.com/openRuyi-Project/linux).

Fixes to `linux`, `glibc`, `GCC`, or `binutils` **SHOULD** be human-led. When using AI assistance, include these items in the change description:

- A minimal reproducer of the defect.
- Technical references for the fix.
- The build environment and build results.
- Regression test results for affected functions.

For all platform-dependent changes:

- You **SHOULD** do tests on affected target architectures.
- Platform test reports **SHOULD** identify the hardware model or emulator version, plus the kernel and firmware versions.

## Before a push

Changes within the configured scope **MUST** pass the applicable [pre-commit checks](https://openruyi.cn/docs/guide/pre-commit-usage-guide).
Check the final version, including automatic corrections.
The repository's `.pre-commit-config.yaml` defines the scope.

## Rule violations

For violations, add `BARNACLE: <SPECIFIC VIOLATION>` to related text you may still edit. Use a short description in uppercase English.
