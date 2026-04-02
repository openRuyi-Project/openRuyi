# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashlink
%global full_version 0.10.0
%global pkgname hashlink-0.10

Name:           rust-hashlink-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "hashlink"
License:        MIT OR Apache-2.0
URL:            https://github.com/kyren/hashlink
#!RemoteAsset:  sha256:7382cf6263419f2d8df38c55d7da83da5c18aef87fc7a7fc1fb1e344edfe14c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.5
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "hashlink"

%package     -n %{name}+serde
Summary:        HashMap-like containers that hold their key-value pairs in a user controllable order - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serde-impl)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hashlink crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde_impl" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
