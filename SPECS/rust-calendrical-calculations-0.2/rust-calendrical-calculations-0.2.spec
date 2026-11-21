# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name calendrical_calculations
%global full_version 0.2.4
%global pkgname calendrical-calculations-0.2

Name:           rust-calendrical-calculations-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "calendrical_calculations"
License:        Apache-2.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:5abbd6eeda6885048d357edc66748eea6e0268e3dd11f326fff5bd248d779c26
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(core-maths-0.1) >= 0.1.0
Requires:       crate(displaydoc-0.2) >= 0.2.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "calendrical_calculations"

%package     -n %{name}+logging
Summary:        Calendrical calculations in Rust - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.17
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust calendrical_calculations crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
