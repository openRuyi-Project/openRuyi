# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name polib
%global full_version 0.3.0
%global pkgname polib-0.3

Name:           rust-polib-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "polib"
License:        MIT
URL:            https://github.com/brettdong/polib
#!RemoteAsset:  sha256:ee83e5a284d919e51b071969bbf2d12d6943857aab02d84c5cc449373c9f3b7b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(concat-string-1/default) >= 1.0.1
Requires:       crate(linereader-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "polib"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
