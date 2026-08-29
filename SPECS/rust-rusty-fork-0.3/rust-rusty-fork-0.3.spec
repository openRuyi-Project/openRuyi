# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rusty-fork
%global full_version 0.3.0
%global pkgname rusty-fork-0.3

Name:           rust-rusty-fork-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "rusty-fork"
License:        MIT OR Apache-2.0
URL:            https://github.com/altsysrq/rusty-fork
#!RemoteAsset:  sha256:cb3dcc6e454c328bb824492db107ab7c0ae8fcffe4ad210136ef014458c1bc4f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.0
Requires:       crate(quick-error-1/default) >= 1.2.0
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rusty-fork"

%package     -n %{name}+wait-timeout
Summary:        Cross-platform library for running Rust tests in sub-processes using a fork-like interface - feature "wait-timeout" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wait-timeout-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/timeout) = %{version}
Provides:       crate(%{pkgname}/wait-timeout) = %{version}

%description -n %{name}+wait-timeout
This metapackage enables feature "wait-timeout" for the Rust rusty-fork crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "timeout" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
