# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-core
%global full_version 0.56.0
%global pkgname windows-core-0.56

Name:           rust-windows-core-0.56
Version:        0.56.0
Release:        %autorelease
Summary:        Rust crate "windows-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:4698e52ed2d08f8658ab0c39512a7c00ee5fe2688c65f8c0a4f06750d729f2a6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-implement-0.56/default) >= 0.56.0
Requires:       crate(windows-interface-0.56/default) >= 0.56.0
Requires:       crate(windows-result-0.1/default) >= 0.1.1
Requires:       crate(windows-targets-0.52/default) >= 0.52.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
