# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name beef
%global full_version 0.5.2
%global pkgname beef-0.5

Name:           rust-beef-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "beef"
License:        MIT OR Apache-2.0
URL:            https://github.com/maciejhirsz/beef
#!RemoteAsset:  sha256:3a8241f3ebb85c056b509d4327ad0358fbbba6ffb340bf388f26350aeda225b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-fn) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "beef"

%package     -n %{name}+serde
Summary:        More compact Cow - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.105
Provides:       crate(%{pkgname}/impl-serde) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust beef crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "impl_serde" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
