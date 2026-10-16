# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name doc-comment
%global full_version 0.3.4
%global pkgname doc-comment-0.3

Name:           rust-doc-comment-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "doc-comment"
License:        MIT
URL:            https://github.com/GuillaumeGomez/doc-comment
#!RemoteAsset:  sha256:780955b8b195a21ab8e4ac6b60dd1dbdcec1dc6c51c0617964b08c81785e12c9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-core) = %{version}
Provides:       crate(%{pkgname}/old-macros) = %{version}

%description
Source code for takopackized Rust crate "doc-comment"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
