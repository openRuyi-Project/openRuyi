# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name      path-clean
%global full_version    1.0.1
%global pkgname         path-clean-1

Name:           rust-path-clean-1
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "path-clean"
License:        MIT OR Apache-2.0
URL:            https://github.com/danreeves/path-clean
#!RemoteAsset:  sha256:17359afc20d7ab31fdb42bb844c8b3bb1dabd7dcf7e68428492da7f16966fcef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "path-clean"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
