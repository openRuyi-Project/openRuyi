# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prefix-trie
%global full_version 0.7.0
%global pkgname prefix-trie-0.7

Name:           rust-prefix-trie-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "prefix-trie"
License:        MIT OR Apache-2.0
URL:            https://github.com/tiborschneider/prefix-trie
#!RemoteAsset:  sha256:85cf4c7c25f1dd66c76b451e9041a8cfce26e4ca754934fa7aed8d5a59a01d20
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "prefix-trie"

%package     -n %{name}+cidr
Summary:        Prefix trie (tree) datastructure (both a set and a map) that provides exact and longest-prefix matches - feature "cidr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cidr-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/cidr) = %{version}

%description -n %{name}+cidr
This metapackage enables feature "cidr" for the Rust prefix-trie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnet
Summary:        Prefix trie (tree) datastructure (both a set and a map) that provides exact and longest-prefix matches - feature "ipnet" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnet-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/ipnet) = %{version}

%description -n %{name}+ipnet
This metapackage enables feature "ipnet" for the Rust prefix-trie crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+ipnetwork
Summary:        Prefix trie (tree) datastructure (both a set and a map) that provides exact and longest-prefix matches - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnetwork-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
This metapackage enables feature "ipnetwork" for the Rust prefix-trie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Prefix trie (tree) datastructure (both a set and a map) that provides exact and longest-prefix matches - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust prefix-trie crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
