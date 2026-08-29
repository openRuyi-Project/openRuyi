# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name shell-words
%global full_version 1.1.1
%global pkgname shell-words-1

Name:           rust-shell-words-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "shell-words"
License:        MIT OR Apache-2.0
URL:            https://github.com/tmiasko/shell-words
#!RemoteAsset:  sha256:dc6fe69c597f9c37bfeeeeeb33da3530379845f10be461a66d16d03eca2ded77
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "shell-words"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
