# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_mangen
%global full_version 0.2.27
%global pkgname clap-mangen-0.2

Name:           rust-clap-mangen-0.2
Version:        0.2.27
Release:        %autorelease
Summary:        Rust crate "clap_mangen"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:fc33c849748320656a90832f54a5eeecaa598e92557fb5dedebc3355746d31e4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/env) >= 4.0.0
Requires:       crate(clap-4/std) >= 4.0.0
Requires:       crate(roff-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clap_mangen"

%package     -n %{name}+debug
Summary:        Manpage generator for clap - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/debug) >= 4.0.0
Requires:       crate(clap-4/env) >= 4.0.0
Requires:       crate(clap-4/std) >= 4.0.0
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap_mangen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
