# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iptables
%global full_version 0.6.0
%global pkgname iptables-0.6

Name:           rust-iptables-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "iptables"
License:        MIT
URL:            https://github.com/yaa110/rust-iptables
#!RemoteAsset:  sha256:f30c9a636a0a728c67d1d420471c99b215708a17c222bb9afb16d0821e2d80d8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(regex-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "iptables"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
