# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: LI GUAN <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fd
Version:        10.5.0
Release:        %autorelease
Summary:        Simple, fast and user-friendly alternative to find
License:        MIT OR Apache-2.0
URL:            https://github.com/sharkdp/fd
#!RemoteAsset:  sha256:e6d9e90730bf316101691e49d59cc02565278dc3779d33a77423801569484851
Source:         https://github.com/sharkdp/fd/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    rust

# Use the default system allocator and let RPM generate debug information.
Patch2000:      2000-use-system-allocator-and-rpm-debuginfo.patch

BuildRequires:  rust >= 1.90.0
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(aho-corasick-1/default) >= 1.1
BuildRequires:  crate(anyhow-1/default) >= 1.0
BuildRequires:  crate(argmax-0.4/default) >= 0.4.0
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/cargo) >= 4.6.1
BuildRequires:  crate(clap-4/color) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(clap-4/suggestions) >= 4.6.1
BuildRequires:  crate(clap-4/wrap-help) >= 4.6.1
BuildRequires:  crate(clap-complete-4/default) >= 4.6.5
BuildRequires:  crate(crossbeam-channel-0.5/default) >= 0.5.15
BuildRequires:  crate(ctrlc-3/default) >= 3.5
BuildRequires:  crate(diff-0.1/default) >= 0.1
BuildRequires:  crate(etcetera-0.11/default) >= 0.11
BuildRequires:  crate(faccess-0.2/default) >= 0.2.4
BuildRequires:  crate(filetime-0.2/default) >= 0.2
BuildRequires:  crate(globset-0.4/default) >= 0.4
BuildRequires:  crate(ignore-0.4/default) >= 0.4.25
BuildRequires:  crate(jiff-0.2/default) >= 0.2.27
BuildRequires:  crate(libc-0.2/default) >= 0.2
BuildRequires:  crate(lscolors-0.21/nu-ansi-term) >= 0.21
BuildRequires:  crate(nix-0.31/hostname) >= 0.31.1
BuildRequires:  crate(nix-0.31/signal) >= 0.31.1
BuildRequires:  crate(nix-0.31/user) >= 0.31.1
BuildRequires:  crate(normpath-1/default) >= 1.5.1
BuildRequires:  crate(nu-ansi-term-0.50/default) >= 0.50
BuildRequires:  crate(regex-1/default) >= 1.12.2
BuildRequires:  crate(regex-syntax-0.8/default) >= 0.8
BuildRequires:  crate(tempfile-3/default) >= 3.27
BuildRequires:  crate(test-case-3/default) >= 3.3

%description
fd is a simple, fast and user-friendly alternative to find. It supports
regular expressions, parallel directory traversal, colorized output and
command execution, and respects ignore files by default.

%install
install -Dpm0755 target/release/fd %{buildroot}%{_bindir}/fd
install -Dpm0644 doc/fd.1 %{buildroot}%{_mandir}/man1/fd.1
install -Dpm0644 contrib/completion/_fd %{buildroot}%{_datadir}/zsh/site-functions/_fd
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
target/release/fd --gen-completions bash > %{buildroot}%{_datadir}/bash-completion/completions/fd
target/release/fd --gen-completions fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/fd.fish

%files
%doc README.md CHANGELOG.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/fd
%{_mandir}/man1/fd.1*
%{_datadir}/bash-completion/completions/fd
%{_datadir}/fish/vendor_completions.d/fd.fish
%{_datadir}/zsh/site-functions/_fd

%changelog
%autochangelog
