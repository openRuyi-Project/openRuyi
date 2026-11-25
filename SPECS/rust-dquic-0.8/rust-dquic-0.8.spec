# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dquic
%global full_version 0.8.1
%global pkgname dquic-0.8

Name:           rust-dquic-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "dquic"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:aa8a16cef8ba5271d77cc58e5381e03d99512d12283afbd754fc5adec7718ffe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(qconnection-0.9/default) >= 0.9.0
Requires:       crate(qprotocol-0.7/default) >= 0.7.0
Requires:       crate(qresolve-0.9/default) >= 0.9.0
Requires:       crate(qtls-0.1/default) >= 0.1.0
Requires:       crate(qtransport-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dquic"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
