# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zoneinfo64
%global full_version 0.3.0
%global pkgname zoneinfo64-0.3

Name:           rust-zoneinfo64-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "zoneinfo64"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:ed6eb2607e906160c457fd573e9297e65029669906b9ac8fb1b5cd5e055f0705
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(calendrical-calculations-0.2) >= 0.2.4
Requires:       crate(icu-locale-core-2) >= 2.2.0
Requires:       crate(potential-utf-0.1) >= 0.1.3
Requires:       crate(resb-0.1) >= 0.1.2
Requires:       crate(serde-1/derive) >= 1.0.220

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zoneinfo64"

%package     -n %{name}+chrono
Summary:        Working with ICU zoneinfo64.res timezone data bundles - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust zoneinfo64 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
