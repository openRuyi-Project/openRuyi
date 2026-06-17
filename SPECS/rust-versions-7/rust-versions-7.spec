# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name versions
%global full_version 7.0.0
%global pkgname versions-7

Name:           rust-versions-7
Version:        7.0.0
Release:        %autorelease
Summary:        Rust crate "versions"
License:        MIT
URL:            https://github.com/fosskers/rs-versions
#!RemoteAsset:  sha256:80a7e511ce1795821207a837b7b1c8d8aca0c648810966ad200446ae58f6667f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(nom-8/default) >= 8.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "versions"

%package     -n %{name}+serde
Summary:        Parsing and comparing software version numbers - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust versions crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
