# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tree-sitter-bash
%global full_version 0.25.1
%global pkgname tree-sitter-bash-0.25

Name:           rust-tree-sitter-bash-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "tree-sitter-bash"
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-bash
#!RemoteAsset:  sha256:9e5ec769279cc91b561d3df0d8a5deb26b0ad40d183127f409494d6d8fc53062
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.1.0
Requires:       crate(tree-sitter-language-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tree-sitter-bash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
