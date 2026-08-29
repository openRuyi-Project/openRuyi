# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name python3-dll-a
%global full_version 0.2.14
%global pkgname python3-dll-a-0.2

Name:           rust-python3-dll-a-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "python3-dll-a"
License:        MIT
URL:            https://github.com/PyO3/python3-dll-a
#!RemoteAsset:  sha256:d381ef313ae70b4da5f95f8a4de773c6aa5cd28f73adec4b4a31df70b66780d8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1/default) >= 1.0.73
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "python3-dll-a"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
