# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minisign
%global full_version 0.7.9
%global pkgname minisign-0.7

Name:           rust-minisign-0.7
Version:        0.7.9
Release:        %autorelease
Summary:        Rust crate "minisign"
License:        MIT
URL:            https://github.com/jedisct1/rust-minisign
#!RemoteAsset:  sha256:26541387415a1e829df5d532aad019fb11bc723e2b5bc99edefa4cf5bfad0de7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ct-codecs-1/default) >= 1.1.3
Requires:       crate(getrandom-0.2) >= 0.2.0
Requires:       crate(getrandom-0.2/js) >= 0.2.0
Requires:       crate(rpassword-7/default) >= 7.3.1
Requires:       crate(scrypt-0.11) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "minisign"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
