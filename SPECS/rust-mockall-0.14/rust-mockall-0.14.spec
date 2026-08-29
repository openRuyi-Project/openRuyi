# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mockall
%global full_version 0.14.0
%global pkgname mockall-0.14

Name:           rust-mockall-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "mockall"
License:        MIT OR Apache-2.0
URL:            https://github.com/asomers/mockall
#!RemoteAsset:  sha256:f58d964098a5f9c6b63d0798e5372fd04708193510a7af313c22e9f29b7b620b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(downcast-0.11/default) >= 0.11.0
Requires:       crate(fragile-2/default) >= 2.0.0
Requires:       crate(mockall-derive-0.14/default) >= 0.14.0
Requires:       crate(predicates-3) >= 3.0.0
Requires:       crate(predicates-tree-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mockall"

%package     -n %{name}+nightly
Summary:        Powerful mock object library for Rust - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(downcast-0.11/nightly) >= 0.11.0
Requires:       crate(mockall-derive-0.14/nightly-derive) >= 0.14.0
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust mockall crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
