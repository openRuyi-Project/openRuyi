# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anstyle-query
%global full_version 1.1.5
%global pkgname anstyle-query-1

Name:           rust-anstyle-query-1
Version:        1.1.5
Release:        %autorelease
Summary:        Rust crate "anstyle-query"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/anstyle.git
#!RemoteAsset:  sha256:40c48f72fd53cd289104fc64099abca73db4166ad86ea0b4341abe65af83dadc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.60/default) >= 0.60.2
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.2
Requires:       crate(windows-sys-0.60/win32-system-console) >= 0.60.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "anstyle-query"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
