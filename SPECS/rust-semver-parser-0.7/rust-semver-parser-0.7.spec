# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name semver-parser
%global full_version 0.7.0
%global pkgname semver-parser-0.7

Name:           rust-semver-parser-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "semver-parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/steveklabnik/semver-parser
#!RemoteAsset:  sha256:388a1df253eca08550bef6c72392cfe7c30914bf41df5269b68cbd6ff8f570a3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "semver-parser"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
