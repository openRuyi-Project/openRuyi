# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quickcheck_macros
%global full_version 1.2.0
%global pkgname quickcheck-macros-1.0

Name:           rust-quickcheck-macros-1.0
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "quickcheck_macros"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/quickcheck
#!RemoteAsset:  sha256:a9a28b8493dd664c8b171dd944da82d933f7d456b829bfb236738e1fe06c5ba4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "quickcheck_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
