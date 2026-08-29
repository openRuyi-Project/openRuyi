# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anstyle-svg
%global full_version 1.1.1
%global pkgname anstyle-svg-1

Name:           rust-anstyle-svg-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "anstyle-svg"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/anstyle.git
#!RemoteAsset:  sha256:ab68e0b71ea68eb6b399ffe1957f26330aeed91f5e578d442a1c2f3df69f6ec1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.0
Requires:       crate(anstyle-lossy-1/default) >= 1.0.0
Requires:       crate(anstyle-parse-1/default) >= 1.0.0
Requires:       crate(html-escape-0.2/default) >= 0.2.13
Requires:       crate(unicode-width-0.2/default) >= 0.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "anstyle-svg"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
