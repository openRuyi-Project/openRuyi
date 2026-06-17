# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sync_wrapper
%global full_version 1.0.2
%global pkgname sync-wrapper-1

Name:           rust-sync-wrapper-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "sync_wrapper"
License:        Apache-2.0
URL:            https://docs.rs/sync_wrapper
#!RemoteAsset:  sha256:0bf256ce5efdfa370213c1dabab5935a12e49f2c58d15e9eac2870d3b4f27263
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sync_wrapper"

%package     -n %{name}+futures-core
Summary:        Enlisting the compiler's help in proving the absence of concurrency - feature "futures-core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures) = %{version}
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust sync_wrapper crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "futures" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
