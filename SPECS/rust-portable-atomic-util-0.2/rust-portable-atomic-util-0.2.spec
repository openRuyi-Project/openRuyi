# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name portable-atomic-util
%global full_version 0.2.7
%global pkgname portable-atomic-util-0.2

Name:           rust-portable-atomic-util-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "portable-atomic-util"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/portable-atomic-util
#!RemoteAsset:  sha256:c2a106d1259c23fac8e543272398ae0e3c0b8d33c88ed73d0cc71b0f1d902618
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(portable-atomic-1/require-cas) >= 1.5.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "portable-atomic-util"

%package     -n %{name}+serde
Summary:        Synchronization primitives built with portable-atomic - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.60
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust portable-atomic-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
