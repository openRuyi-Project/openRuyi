# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           eza
Version:        0.23.5
Release:        %autorelease
Summary:        Modern replacement for ls
License:        EUPL-1.2
URL:            https://github.com/eza-community/eza
#!RemoteAsset:  sha256:334199a8059861f81a2d3d888a45f44fa55f82dade2412e752144a404d7ae9af
Source0:        https://static.crates.io/crates/eza/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# Remove the unused criterion dev dependency and its unavailable plotting closure.
Patch2000:      2000-disable-criterion-dev-dependency.patch
# Allow the palette 0.7.6 release shipped by openRuyi instead of the 0.7.5 pin.
Patch2001:      2001-use-palette-0.7.6.patch
# Remove the Windows-only windows-sys dependency; it is not used on Linux.
Patch2002:      2002-remove-windows-sys-dependency.patch

BuildRequires:  rust >= 1.90.0
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
# TakoPack-generated dependencies.
BuildRequires:  crate(ansi-width-0.1/default) >= 0.1.0
BuildRequires:  crate(backtrace-0.3/default) >= 0.3.0
BuildRequires:  crate(chrono-0.4) >= 0.4.40
BuildRequires:  crate(chrono-0.4/clock) >= 0.4.40
BuildRequires:  crate(clap-4/cargo) >= 4.5.38
BuildRequires:  crate(clap-4/default) >= 4.5.38
BuildRequires:  crate(clap-4/derive) >= 4.5.38
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(git2-0.21) >= 0.21.0
BuildRequires:  crate(glob-0.3/default) >= 0.3.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(locale-0.2/default) >= 0.2.0
BuildRequires:  crate(log-0.4/default) >= 0.4.0
BuildRequires:  crate(natord-plus-plus-2/default) >= 2.0.0
BuildRequires:  crate(nu-ansi-term-0.50/default) >= 0.50.1
BuildRequires:  crate(nu-ansi-term-0.50/derive-serde-style) >= 0.50.1
BuildRequires:  crate(nu-ansi-term-0.50/serde) >= 0.50.1
BuildRequires:  crate(palette-0.7/std) >= 0.7.6
BuildRequires:  crate(path-clean-1/default) >= 1.0.1
BuildRequires:  crate(percent-encoding-2/default) >= 2.3.1
BuildRequires:  crate(phf-0.13/default) >= 0.13.1
BuildRequires:  crate(phf-0.13/macros) >= 0.13.1
BuildRequires:  crate(plist-1) >= 1.7.0
BuildRequires:  crate(proc-mounts-0.3/default) >= 0.3.0
BuildRequires:  crate(rayon-1/default) >= 1.10.0
BuildRequires:  crate(serde-1/default) >= 1.0.219
BuildRequires:  crate(serde-1/derive) >= 1.0.219
BuildRequires:  crate(serde-norway-0.9/default) >= 0.9.0
BuildRequires:  crate(terminal-size-0.4/default) >= 0.4.2
BuildRequires:  crate(timeago-0.6) >= 0.6.0
BuildRequires:  crate(unicode-width-0.2/default) >= 0.2.0
BuildRequires:  crate(unit-prefix-0.5/default) >= 0.5.2
BuildRequires:  crate(uutils-term-grid-0.7/default) >= 0.7.0
BuildRequires:  crate(uzers-0.12/default) >= 0.12.1
# Additional dependencies required by OBS builds.
BuildRequires:  crate(approx-0.5/default) >= 0.5.0
BuildRequires:  crate(openssl-src-300/default) >= 300.2.0
BuildRequires:  crate(openssl-sys-0.9/default) >= 0.9.45
BuildRequires:  crate(trycmd-1/default) >= 1.0.2

%description
eza is a modern, maintained replacement for ls with rich colors,
icons, Git integration, and configurable output formats.

%prep -a
# Regenerate the lockfile from the patched manifest and available registry.
rm -f Cargo.lock

%install
# Install the binary and the shell integration files shipped by upstream.
install -Dpm0755 target/release/eza %{buildroot}%{_bindir}/eza
install -Dpm0644 completions/bash/eza %{buildroot}%{_datadir}/bash-completion/completions/eza
install -Dpm0644 completions/fish/eza.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/eza.fish
install -Dpm0644 completions/zsh/_eza %{buildroot}%{_datadir}/zsh/site-functions/_eza
install -Dpm0644 completions/nush/eza.nu %{buildroot}%{_datadir}/nushell/completions/eza.nu
install -Dpm0644 completions/pwsh/_eza.ps1 %{buildroot}%{_datadir}/powershell/Completions/_eza.ps1

%files
%doc README.md man/*.md
%license LICENSE.txt LICENSES/*.txt
%{_bindir}/eza
%{_datadir}/bash-completion/completions/eza
%{_datadir}/fish/vendor_completions.d/eza.fish
%{_datadir}/nushell/completions/eza.nu
%{_datadir}/powershell/Completions/_eza.ps1
%{_datadir}/zsh/site-functions/_eza

%changelog
%autochangelog
