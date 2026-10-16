# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name culpa-macros
%global full_version 1.0.2
%global pkgname culpa-macros-1

Name:           rust-culpa-macros-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "culpa-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/Nullus157/culpa
#!RemoteAsset:  sha256:1234e1717066d3c71dcf89b75e7b586299e41204d361db56ec51e6ded5014279
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.63
Requires:       crate(quote-1/default) >= 1.0.29
Requires:       crate(syn-2/default) >= 2.0.22
Requires:       crate(syn-2/fold) >= 2.0.22
Requires:       crate(syn-2/full) >= 2.0.22
Requires:       crate(syn-2/parsing) >= 2.0.22

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "culpa-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
