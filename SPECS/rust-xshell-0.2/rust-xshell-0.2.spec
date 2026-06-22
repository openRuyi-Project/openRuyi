# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xshell
%global full_version 0.2.7
%global pkgname xshell-0.2

Name:           rust-xshell-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "xshell"
License:        MIT OR Apache-2.0
URL:            https://github.com/matklad/xshell
#!RemoteAsset:  sha256:9e7290c623014758632efe00737145b6867b66292c42167f2ec381eb566a373d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(xshell-macros-0.2/default) >= 0.2.7
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "xshell"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
