# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rfc2047-decoder
%global full_version 1.1.2
%global pkgname rfc2047-decoder-1

Name:           rust-rfc2047-decoder-1
Version:        1.1.2
Release:        %autorelease
Summary:        Rust crate "rfc2047-decoder"
License:        MIT
URL:            https://github.com/TornaxO7/rfc2047-decoder
#!RemoteAsset:  sha256:b36447d5e70933adee73cefff22b0851edbc162f2b3951918de43717a22d92de
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(charset-0.1/default) >= 0.1.0
Requires:       crate(chumsky-0.13/default) >= 0.13.0
Requires:       crate(memchr-2/default) >= 2.5.0
Requires:       crate(quoted-printable-0.5/default) >= 0.5.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rfc2047-decoder"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
