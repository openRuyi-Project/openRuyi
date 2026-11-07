# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name version_check
%global full_version 0.1.5
%global pkgname version-check-0.1

Name:           rust-version-check-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "version_check"
License:        MIT OR Apache-2.0
URL:            https://github.com/SergioBenitez/version_check
#!RemoteAsset:  sha256:914b1a6776c4c929a602fafd8bc742e06365d4bcbe48c30f9cca5824f70dc9dd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "version_check"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
