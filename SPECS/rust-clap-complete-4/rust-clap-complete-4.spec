# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_complete
%global full_version 4.6.3
%global pkgname clap-complete-4

Name:           rust-clap-complete-4
Version:        4.6.3
Release:        %autorelease
Summary:        Rust crate "clap_complete"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:660c0520455b1013b9bcb0393d5f643d7e4454fb69c915b8d6d2aa0e9a45acc3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/std) >= 4.5.20
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clap_complete"

%package     -n %{name}+debug
Summary:        Generate shell completion scripts for your clap::Command - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/debug) >= 4.5.20
Requires:       crate(clap-4/std) >= 4.5.20
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-dynamic
Summary:        Generate shell completion scripts for your clap::Command - feature "unstable-dynamic" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/std) >= 4.5.20
Requires:       crate(clap-4/unstable-ext) >= 4.5.20
Requires:       crate(clap-lex-1/default) >= 1.0.0
Requires:       crate(is-executable-1/default) >= 1.0.5
Requires:       crate(shlex-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/unstable-doc) = %{version}
Provides:       crate(%{pkgname}/unstable-dynamic) = %{version}

%description -n %{name}+unstable-dynamic
This metapackage enables feature "unstable-dynamic" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-doc" feature.

%package     -n %{name}+unstable-shell-tests
Summary:        Generate shell completion scripts for your clap::Command - feature "unstable-shell-tests"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(completest-1/default) >= 1.1.0
Requires:       crate(completest-pty-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/unstable-shell-tests) = %{version}

%description -n %{name}+unstable-shell-tests
This metapackage enables feature "unstable-shell-tests" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
