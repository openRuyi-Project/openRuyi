# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashlink
%global full_version 0.11.1
%global pkgname hashlink-0.11

Name:           rust-hashlink-0.11
Version:        0.11.1
Release:        %autorelease
Summary:        Rust crate "hashlink"
License:        MIT OR Apache-2.0
URL:            https://github.com/djc/hashlink
#!RemoteAsset:  sha256:824e001ac4f3012dd16a264bec811403a67ca9deb6c102fc5049b32c4574b35f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.16/default-hasher) >= 0.16.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hashlink"

%package     -n %{name}+serde
Summary:        HashMap-like containers that hold their key-value pairs in a user controllable order - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-impl) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hashlink crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde_impl" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
