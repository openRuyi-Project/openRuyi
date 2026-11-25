# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tree-sitter-language
%global full_version 0.1.7
%global pkgname tree-sitter-language-0.1

Name:           rust-tree-sitter-language-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "tree-sitter-language"
License:        MIT
URL:            https://tree-sitter.github.io/tree-sitter
#!RemoteAsset:  sha256:009994f150cc0cd50ff54917d5bc8bffe8cad10ca10d81c34da2ec421ae61782
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tree-sitter-language"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
