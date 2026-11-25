# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequence_trie
%global full_version 0.3.6
%global pkgname sequence-trie-0.3

Name:           rust-sequence-trie-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "sequence_trie"
License:        MIT OR Apache-2.0
URL:            https://github.com/michaelsproul/rust_sequence_trie
#!RemoteAsset:  sha256:1ee22067b7ccd072eeb64454b9c6e1b33b61cd0d49e895fd48676a184580e0c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/btreemap) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequence_trie"

%package     -n %{name}+serde
Summary:        Trie-like data-structure for storing sequences of values - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sequence_trie crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
