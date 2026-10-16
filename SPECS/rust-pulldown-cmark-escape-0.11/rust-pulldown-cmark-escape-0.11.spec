# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pulldown-cmark-escape
%global full_version 0.11.0
%global pkgname pulldown-cmark-escape-0.11

Name:           rust-pulldown-cmark-escape-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "pulldown-cmark-escape"
License:        MIT
URL:            https://github.com/raphlinus/pulldown-cmark
#!RemoteAsset:  sha256:007d8adb5ddab6f8e3f491ac63566a7d5002cc7ed73901f72057943fa71ae1ae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}

%description
Source code for takopackized Rust crate "pulldown-cmark-escape"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
