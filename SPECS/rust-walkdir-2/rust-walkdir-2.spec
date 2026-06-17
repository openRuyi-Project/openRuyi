# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name walkdir
%global full_version 2.5.0
%global pkgname walkdir-2

Name:           rust-walkdir-2
Version:        2.5.0
Release:        %autorelease
Summary:        Rust crate "walkdir"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/walkdir
#!RemoteAsset:  sha256:29790946404f91d9c5d06f9874efddea1dc06c5efe94541a7d6863108e3a5e4b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(same-file-1/default) >= 1.0.1
Requires:       crate(winapi-util-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "walkdir"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
