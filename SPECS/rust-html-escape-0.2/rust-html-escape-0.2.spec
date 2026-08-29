# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name html-escape
%global full_version 0.2.14
%global pkgname html-escape-0.2

Name:           rust-html-escape-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "html-escape"
License:        MIT
URL:            https://magiclen.org/html-escape
#!RemoteAsset:  sha256:46c1ff2d1cbf39efe5af0900ced8a069b5e61557a17544eb0c4a50239937389e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "html-escape"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
