# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fsevent-sys
%global full_version 4.1.0
%global pkgname fsevent-sys-4.0

Name:           rust-fsevent-sys-4.0
Version:        4.1.0
Release:        %autorelease
Summary:        Rust crate "fsevent-sys"
License:        MIT
URL:            https://github.com/octplane/fsevent-rust/tree/master/fsevent-sys
#!RemoteAsset:  sha256:76ee7a02da4d231650c7cea31349b889be2f45ddb3ef3032d2ec8185f6313fd2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.169
Provides:       crate(fsevent-sys) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "fsevent-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
