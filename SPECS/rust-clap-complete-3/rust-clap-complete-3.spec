# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global crate_name clap_complete
%global full_version 3.2.5
%global pkgname clap-complete-3

Name:           rust-clap-complete-3
Version:        3.2.5
Release:        %autorelease
Summary:        Rust crate "clap_complete"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:3f7a2e0a962c45ce25afce14220bc24f9dade0a1787f185cecf96bfba7847cd8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-3/std) >= 3.2.25
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clap_complete"

%package     -n %{name}+debug
Summary:        Generate shell completion scripts for your clap::Command - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-3/debug) >= 3.2.25
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap_complete crate.

%package     -n %{name}+unstable-dynamic
Summary:        Generate shell completion scripts for your clap::Command - feature "unstable-dynamic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-3/derive) >= 3.2.25
Requires:       crate(clap-lex-0.2/default) >= 0.2.2
Requires:       crate(is-executable-1/default) >= 1.0.1
Requires:       crate(os-str-bytes-6/default) >= 6.0
Requires:       crate(pathdiff-0.2/default) >= 0.2.1
Requires:       crate(shlex-1/default) >= 1.1.0
Requires:       crate(unicode-xid-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/unstable-dynamic) = %{version}

%description -n %{name}+unstable-dynamic
This metapackage enables feature "unstable-dynamic" for the Rust clap_complete crate.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
