# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strict-num
%global full_version 0.1.1
%global pkgname strict-num-0.1

Name:           rust-strict-num-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "strict-num"
License:        MIT
URL:            https://github.com/RazrFalcon/strict-num
#!RemoteAsset:  sha256:6637bab7722d379c8b41ba849228d680cc12d0a45ba1fa2b48f2a30577a06731
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "strict-num"

%package     -n %{name}+float-cmp
Summary:        Collection of bounded numeric types - feature "float-cmp" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(float-cmp-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/approx-eq) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/float-cmp) = %{version}

%description -n %{name}+float-cmp
This metapackage enables feature "float-cmp" for the Rust strict-num crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "approx-eq", and "default" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
