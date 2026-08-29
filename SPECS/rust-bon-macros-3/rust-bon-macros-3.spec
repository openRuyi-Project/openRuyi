# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bon-macros
%global full_version 3.9.0
%global pkgname bon-macros-3

Name:           rust-bon-macros-3
Version:        3.9.0
Release:        %autorelease
Summary:        Rust crate "bon-macros"
License:        MIT OR Apache-2.0
URL:            https://bon-rs.com/
#!RemoteAsset:  sha256:d314cc62af2b6b0c65780555abb4d02a03dd3b799cd42419044f0c38d99738c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.20/default) >= 0.20.0
Requires:       crate(ident-case-1/default) >= 1.0.0
Requires:       crate(prettyplease-0.2/default) >= 0.2.0
Requires:       crate(proc-macro2-1/default) >= 1.0.88
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(rustversion-1/default) >= 1.0.18
Requires:       crate(syn-2/default) >= 2.0.56
Requires:       crate(syn-2/full) >= 2.0.56
Requires:       crate(syn-2/visit) >= 2.0.56
Requires:       crate(syn-2/visit-mut) >= 2.0.56

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/experimental-generics-setters) = %{version}
Provides:       crate(%{pkgname}/experimental-overwritable) = %{version}
Provides:       crate(%{pkgname}/implied-bounds) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bon-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
