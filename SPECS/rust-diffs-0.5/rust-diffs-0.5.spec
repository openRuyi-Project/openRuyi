# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name diffs
%global full_version 0.5.1
%global pkgname diffs-0.5

Name:           rust-diffs-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "diffs"
License:        MIT OR Apache-2.0
URL:            https://nest.pijul.com/pijul/diffs
#!RemoteAsset:  sha256:ff116c9781d74b71b9b8958281309dd2faaeabad2f0a3df27e50bd79ce5dc805
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "diffs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
