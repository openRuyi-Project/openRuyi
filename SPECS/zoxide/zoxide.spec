# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zoxide
Version:        0.10.0
Release:        %autorelease
Summary:        A smarter cd command for your terminal
License:        MIT
URL:            https://github.com/ajeetdsouza/zoxide
#!RemoteAsset:  sha256:4fcd4272b013a10b637dbcc299c58a9924b94470a9042677ca1a204cc2e9150e
Source0:        https://github.com/ajeetdsouza/zoxide/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# Remove the Windows-only dependency from the Linux Cargo resolution closure.
Patch2000:      2000-remove-windows-only-dependency.patch

BuildRequires:  rust >= 1.88.0
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/default) >= 1.0.32
BuildRequires:  crate(assert-cmd-2/default) >= 2.0.0
BuildRequires:  crate(askama-0.16/derive) >= 0.16.0
BuildRequires:  crate(askama-0.16/std) >= 0.16.0
BuildRequires:  crate(bincode-1/default) >= 1.3.1
BuildRequires:  crate(clap-4) >= 4.3.0
BuildRequires:  crate(clap-4/default) >= 4.3.0
BuildRequires:  crate(clap-4/derive) >= 4.3.0
BuildRequires:  crate(clap-complete-4) >= 4.5.50
BuildRequires:  crate(clap-complete-fig-4) >= 4.5.2
BuildRequires:  crate(clap-complete-nushell-4) >= 4.5.5
BuildRequires:  crate(color-print-0.3) >= 0.3.4
BuildRequires:  crate(color-print-0.3/default) >= 0.3.4
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(dunce-1/default) >= 1.0.1
BuildRequires:  crate(fastrand-2/default) >= 2.0.0
BuildRequires:  crate(glob-0.3/default) >= 0.3.0
BuildRequires:  crate(ouroboros-0.18/default) >= 0.18.3
BuildRequires:  crate(rstest-0.26/default) >= 0.26.0
BuildRequires:  crate(rstest-reuse-0.7/default) >= 0.7.0
BuildRequires:  crate(serde-1/default) >= 1.0.116
BuildRequires:  crate(serde-1/derive) >= 1.0.116
BuildRequires:  crate(tempfile-3/default) >= 3.15.0
BuildRequires:  crate(time-0.3/macros) >= 0.3.47
BuildRequires:  crate(time-0.3/parsing) >= 0.3.47
BuildRequires:  crate(time-0.3/std) >= 0.3.47

%description
zoxide is a smarter cd command inspired by z and autojump. It remembers which
directories you use most frequently, allowing you to jump to them with a few
keystrokes.

# BuildSystem: rust has no default install action. Install the binary and shell integrations.
%install
install -Dpm0755 target/release/zoxide %{buildroot}%{_bindir}/zoxide
install -Dpm0644 contrib/completions/zoxide.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/zoxide
install -Dpm0644 contrib/completions/zoxide.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/zoxide.fish
install -Dpm0644 contrib/completions/_zoxide \
    %{buildroot}%{_datadir}/zsh/site-functions/_zoxide
install -d %{buildroot}%{_mandir}/man1
install -pm0644 man/man1/*.1 %{buildroot}%{_mandir}/man1/

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/zoxide
%{_datadir}/bash-completion/completions/zoxide
%{_datadir}/fish/vendor_completions.d/zoxide.fish
%{_datadir}/zsh/site-functions/_zoxide
%{_mandir}/man1/zoxide*.1*

%changelog
%autochangelog
