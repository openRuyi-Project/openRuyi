# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name diffy
%global full_version 0.4.2
%global pkgname diffy-0.4

Name:           rust-diffy-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "diffy"
License:        MIT OR Apache-2.0
URL:            https://github.com/bmwill/diffy
#!RemoteAsset:  sha256:b545b8c50194bdd008283985ab0b31dba153cfd5b3066a92770634fbc0d7d291
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nu-ansi-term-0.50/default) >= 0.50.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "diffy"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
