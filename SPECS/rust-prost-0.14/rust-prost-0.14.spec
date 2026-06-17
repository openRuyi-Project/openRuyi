# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost
%global full_version 0.14.1
%global pkgname prost-0.14

Name:           rust-prost-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "prost"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:7231bd9b3d3d33c86b58adbac74b5ec0ad9f496b19d22801d773636feaa95f3d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/no-recursion-limit) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "prost"

%package     -n %{name}+default
Summary:        Protocol Buffers implementation for the Rust Language - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust prost crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Protocol Buffers implementation for the Rust Language - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-derive-0.14/default) >= 0.14.1
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust prost crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
