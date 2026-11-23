# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_mangen
%global full_version 0.3.4
%global pkgname clap-mangen-0.3

Name:           rust-clap-mangen-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "clap_mangen"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:a3b6a8907b1723f211693e27b9af5899b86a9512ef5b08bd4a15b6bceb30da6d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/std) >= 4.6.6
Requires:       crate(roff-1/default) >= 1.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clap_mangen"

%package     -n %{name}+debug
Summary:        Manpage generator for clap - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/debug) >= 4.6.6
Requires:       crate(clap-4/std) >= 4.6.6
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap_mangen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env
Summary:        Manpage generator for clap - feature "env"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/env) >= 4.6.6
Requires:       crate(clap-4/std) >= 4.6.6
Provides:       crate(%{pkgname}/env) = %{version}

%description -n %{name}+env
This metapackage enables feature "env" for the Rust clap_mangen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
