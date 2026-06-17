# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name concat-idents
%global full_version 1.1.5
%global pkgname concat-idents-1

Name:           rust-concat-idents-1
Version:        1.1.5
Release:        %autorelease
Summary:        Rust crate "concat-idents"
License:        MIT OR Apache-2.0
URL:            https://github.com/DzenanJupic/concat-idents
#!RemoteAsset:  sha256:f76990911f2267d837d9d0ad060aa63aaad170af40904b29461734c339030d4d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.21
Requires:       crate(syn-2/default) >= 2.0.16
Requires:       crate(syn-2/full) >= 2.0.16
Requires:       crate(syn-2/visit-mut) >= 2.0.16
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "concat-idents"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
