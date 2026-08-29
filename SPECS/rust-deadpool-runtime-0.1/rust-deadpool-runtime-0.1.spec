# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deadpool-runtime
%global full_version 0.1.4
%global pkgname deadpool-runtime-0.1

Name:           rust-deadpool-runtime-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "deadpool-runtime"
License:        MIT OR Apache-2.0
URL:            https://github.com/bikeshedder/deadpool
#!RemoteAsset:  sha256:092966b41edc516079bdf31ec78a2e0588d1d0c08f78b91d8307215928642b2b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "deadpool-runtime"

%package     -n %{name}+async-std-1
Summary:        Dead simple async pool utitities for sync managers - feature "async-std_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.0.0
Requires:       crate(async-std-1/unstable) >= 1.0.0
Provides:       crate(%{pkgname}/async-std-1) = %{version}

%description -n %{name}+async-std-1
This metapackage enables feature "async-std_1" for the Rust deadpool-runtime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-1
Summary:        Dead simple async pool utitities for sync managers - feature "tokio_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/tokio-1) = %{version}

%description -n %{name}+tokio-1
This metapackage enables feature "tokio_1" for the Rust deadpool-runtime crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
