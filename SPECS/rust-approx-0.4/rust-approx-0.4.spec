# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name approx
%global full_version 0.4.0
%global pkgname approx-0.4

Name:           rust-approx-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "approx"
License:        Apache-2.0
URL:            https://github.com/brendanzab/approx
#!RemoteAsset:  sha256:3f2a05fd1bd10b2527e20a2cd32d8873d115b8b39fe219ee25f42a8aca6ba278
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "approx"

%package     -n %{name}+num-complex
Summary:        Approximate floating point equality comparisons and assertions - feature "num-complex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-complex-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/num-complex) = %{version}

%description -n %{name}+num-complex
This metapackage enables feature "num-complex" for the Rust approx crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
