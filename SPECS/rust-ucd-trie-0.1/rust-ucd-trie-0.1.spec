# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ucd-trie
%global full_version 0.1.7
%global pkgname ucd-trie-0.1

Name:           rust-ucd-trie-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "ucd-trie"
License:        MIT OR Apache-2.0
URL:            https://github.com/BurntSushi/ucd-generate
#!RemoteAsset:  sha256:2896d95c02a80c6d6a5d6e953d479f5ddf2dfdb6a244441010e373ac0fb88971
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ucd-trie"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
