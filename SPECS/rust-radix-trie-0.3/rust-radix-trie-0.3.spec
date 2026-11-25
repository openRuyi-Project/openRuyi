# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name radix_trie
%global full_version 0.3.0
%global pkgname radix-trie-0.3

Name:           rust-radix-trie-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "radix_trie"
License:        MIT
URL:            https://github.com/michaelsproul/rust_radix_trie
#!RemoteAsset:  sha256:3b4431027dcd37fc2a73ef740b5f233aa805897935b8bce0195e41bbf9a3289a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(endian-type-0.2/default) >= 0.2.0
Requires:       crate(nibble-vec-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "radix_trie"

%package     -n %{name}+serde
Summary:        Generic radix trie data-structure - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust radix_trie crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
