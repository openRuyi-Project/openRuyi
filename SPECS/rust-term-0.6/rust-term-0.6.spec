# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name term
%global full_version 0.6.1
%global pkgname term-0.6

Name:           rust-term-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "term"
License:        MIT OR Apache-2.0
URL:            https://github.com/Stebalien/term
#!RemoteAsset:  sha256:c0863a3345e70f61d613eab32ee046ccd1bcc5f9105fe402c61fcd0c13eeb8b5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-2/default) >= 2.0.1
Requires:       crate(winapi-0.3/consoleapi) >= 0.3.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/fileapi) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/wincon) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "term"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
