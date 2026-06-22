# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linktime-proc-macro
%global full_version 0.2.0
%global pkgname linktime-proc-macro-0.2

Name:           rust-linktime-proc-macro-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "linktime-proc-macro"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/linktime
#!RemoteAsset:  sha256:8c7b0a3383c2a1002d11349c92c85a666a5fb679e96c79d782cf0dbe557fd6ee
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ctor) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dtor) = %{version}
Provides:       crate(%{pkgname}/link-section) = %{version}
Provides:       crate(%{pkgname}/scattered-collect) = %{version}

%description
Source code for takopackized Rust crate "linktime-proc-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
