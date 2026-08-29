# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pulldown-cmark-to-cmark
%global full_version 21.0.0
%global pkgname pulldown-cmark-to-cmark-21

Name:           rust-pulldown-cmark-to-cmark-21
Version:        21.0.0
Release:        %autorelease
Summary:        Rust crate "pulldown-cmark-to-cmark"
License:        Apache-2.0
URL:            https://github.com/Byron/pulldown-cmark-to-cmark
#!RemoteAsset:  sha256:e5b6a0769a491a08b31ea5c62494a8f144ee0987d86d670a8af4df1e1b7cde75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pulldown-cmark-0.13) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pulldown-cmark-to-cmark"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
