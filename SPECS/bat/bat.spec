# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bat
Version:        0.26.1
Release:        %autorelease
Summary:        A cat(1) clone with wings
License:        MIT OR Apache-2.0
URL:            https://github.com/sharkdp/bat
#!RemoteAsset:  sha256:cf66d0164db6827afe1694b8d4939f36a5507b7186f8d3cc529c66baf03b0d09
Source0:        https://static.crates.io/crates/bat/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust >= 1.87.0
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(ansi-colours-1/default) >= 1.2.0
BuildRequires:  crate(anyhow-1) >= 1.0.97
BuildRequires:  crate(assert-cmd-2/default) >= 2.0.12
BuildRequires:  crate(bincode-1/default) >= 1.0.0
BuildRequires:  crate(bugreport-0.5/default) >= 0.5.0
BuildRequires:  crate(bytesize-1/default) >= 1.3.0
BuildRequires:  crate(clap-4/cargo) >= 4.5.46
BuildRequires:  crate(clap-4/default) >= 4.5.46
BuildRequires:  crate(clap-4/wrap-help) >= 4.5.46
BuildRequires:  crate(clircle-0.6) >= 0.6.1
BuildRequires:  crate(console-0.16/default) >= 0.16.0
BuildRequires:  crate(content-inspector-0.2/default) >= 0.2.4
BuildRequires:  crate(core-foundation-sys-0.8/default) >= 0.8.0
BuildRequires:  crate(crossterm-winapi-0.9/default) >= 0.9.0
BuildRequires:  crate(encoding-rs-0.8/default) >= 0.8.35
BuildRequires:  crate(execute-0.2/default) >= 0.2.13
BuildRequires:  crate(etcetera-0.11/default) >= 0.11.0
BuildRequires:  crate(expect-test-1/default) >= 1.5.0
BuildRequires:  crate(fancy-regex-0.16/default) >= 0.16.2
BuildRequires:  crate(flate2-1/default) >= 1.1.0
BuildRequires:  crate(git2-0.20) >= 0.20.0
BuildRequires:  crate(globset-0.4/default) >= 0.4.0
BuildRequires:  crate(grep-cli-0.1/default) >= 0.1.11
BuildRequires:  crate(indexmap-2) >= 2.8.0
BuildRequires:  crate(indexmap-2/serde) >= 2.8.0
BuildRequires:  crate(itertools-0.14) >= 0.14.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(minus-5/default) >= 5.6.0
BuildRequires:  crate(minus-5/dynamic-output) >= 5.6.0
BuildRequires:  crate(minus-5/search) >= 5.6.0
BuildRequires:  crate(nix-0.30) >= 0.30.0
BuildRequires:  crate(nix-0.30/term) >= 0.30.0
BuildRequires:  crate(ntapi-0.4/default) >= 0.4.0
BuildRequires:  crate(nu-ansi-term-0.50/default) >= 0.50.0
BuildRequires:  crate(once-cell-1) >= 1.20.0
BuildRequires:  crate(once-cell-1/default) >= 1.20.0
BuildRequires:  crate(path-abs-0.5) >= 0.5.0
BuildRequires:  crate(plist-1/default) >= 1.7.0
BuildRequires:  crate(predicates-3/default) >= 3.1.3
BuildRequires:  crate(prettyplease-0.2) >= 0.2.37
BuildRequires:  crate(proc-macro2-1) >= 1.0.95
BuildRequires:  crate(quote-1) >= 1.0.40
BuildRequires:  crate(regex-1) >= 1.12.2
BuildRequires:  crate(semver-1/default) >= 1.0.0
BuildRequires:  crate(serde-1) >= 1.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-derive-1) >= 1.0.0
BuildRequires:  crate(serde-derive-1/default) >= 1.0.0
BuildRequires:  crate(serde-with-3) >= 3.15.1
BuildRequires:  crate(serde-with-3/macros) >= 3.15.1
BuildRequires:  crate(serde-yaml-0.9/default) >= 0.9.28
BuildRequires:  crate(serial-test-2) >= 2.0.0
BuildRequires:  crate(shell-words-1/default) >= 1.1.0
BuildRequires:  crate(syn-2) >= 2.0.104
BuildRequires:  crate(syn-2/full) >= 2.0.104
BuildRequires:  crate(syntect-5/parsing) >= 5.3.0
BuildRequires:  crate(syntect-5/plist-load) >= 5.3.0
BuildRequires:  crate(syntect-5/regex-onig) >= 5.3.0
BuildRequires:  crate(syntect-5/yaml-load) >= 5.3.0
BuildRequires:  crate(tempfile-3/default) >= 3.16.0
BuildRequires:  crate(terminal-colorsaurus-1/default) >= 1.0.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(toml-0.9) >= 0.9.1
BuildRequires:  crate(toml-0.9/preserve-order) >= 0.9.1
BuildRequires:  crate(unicode-segmentation-1/default) >= 1.12.0
BuildRequires:  crate(unicode-width-0.2/default) >= 0.2.1
BuildRequires:  crate(wait-timeout-0.2/default) >= 0.2.1
BuildRequires:  crate(walkdir-2) >= 2.5.0
BuildRequires:  crate(walkdir-2/default) >= 2.5.0
BuildRequires:  crate(wild-2/default) >= 2.2.0
BuildRequires:  crate(winnow-0.7/default) >= 0.7.13

%description
bat is a cat(1) clone with syntax highlighting, Git integration, and
support for a wide range of programming and markup languages.

%install
# Install the application and assets generated from the upstream templates.
install -Dpm0755 target/release/bat %{buildroot}%{_bindir}/bat
install -d %{buildroot}%{_mandir}/man1
sed -e 's/{{PROJECT_NAME}}/bat/g' -e 's/{{PROJECT_EXECUTABLE}}/bat/g' -e 's/{{PROJECT_EXECUTABLE_UPPERCASE}}/BAT/g' -e 's/{{PROJECT_VERSION}}/%{version}/g' assets/manual/bat.1.in > %{buildroot}%{_mandir}/man1/bat.1
install -d %{buildroot}%{_datadir}/bash-completion/completions %{buildroot}%{_datadir}/fish/vendor_completions.d %{buildroot}%{_datadir}/zsh/site-functions
sed -e 's/{{PROJECT_NAME}}/bat/g' -e 's/{{PROJECT_EXECUTABLE}}/bat/g' -e 's/{{PROJECT_EXECUTABLE_UPPERCASE}}/BAT/g' -e 's/{{PROJECT_VERSION}}/%{version}/g' assets/completions/bat.bash.in > %{buildroot}%{_datadir}/bash-completion/completions/bat
sed -e 's/{{PROJECT_NAME}}/bat/g' -e 's/{{PROJECT_EXECUTABLE}}/bat/g' -e 's/{{PROJECT_EXECUTABLE_UPPERCASE}}/BAT/g' -e 's/{{PROJECT_VERSION}}/%{version}/g' assets/completions/bat.fish.in > %{buildroot}%{_datadir}/fish/vendor_completions.d/bat.fish
sed -e 's/{{PROJECT_NAME}}/bat/g' -e 's/{{PROJECT_EXECUTABLE}}/bat/g' -e 's/{{PROJECT_EXECUTABLE_UPPERCASE}}/BAT/g' -e 's/{{PROJECT_VERSION}}/%{version}/g' assets/completions/bat.zsh.in > %{buildroot}%{_datadir}/zsh/site-functions/_bat

%files
%doc CHANGELOG.md README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/bat
%{_mandir}/man1/bat.1*
%{_datadir}/bash-completion/completions/bat
%{_datadir}/fish/vendor_completions.d/bat.fish
%{_datadir}/zsh/site-functions/_bat

%changelog
%autochangelog
