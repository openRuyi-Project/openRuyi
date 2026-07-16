# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minisign
%global full_version 0.9.1
%global pkgname minisign-0.9

Name:           rust-minisign-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "minisign"
License:        MIT
URL:            https://github.com/jedisct1/rust-minisign
#!RemoteAsset:  sha256:aefd422a7a8b5efced01cd7cdf3771e62ebecbc90e3d27695002d3af6af94586
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ct-codecs-1/default) >= 1.1.6
Requires:       crate(getrandom-0.4) >= 0.4.0
Requires:       crate(rpassword-7/default) >= 7.4.0
Requires:       crate(scrypt-0.11) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "minisign"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
