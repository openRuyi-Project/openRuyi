# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode_names2
%global full_version 1.3.0
%global pkgname unicode-names2-1.0

Name:           rust-unicode-names2-1.0
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "unicode_names2"
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://github.com/progval/unicode_names2
#!RemoteAsset:  sha256:d1673eca9782c84de5f81b82e4109dcfb3611c8ba0d52930ec4a9478f547b2dd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-0.11) >= 0.11.1
Requires:       crate(unicode-names2-generator-1.0/default) >= 1.3.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-std)
Provides:       crate(%{pkgname}/unstable)

%description
This goes to great lengths to be as efficient as possible in both time and space, with the full bidirectional tables weighing barely 500 KB but still offering O(1)* look-up in both directions. (*more precisely, O(length of name).)
Source code for takopackized Rust crate "unicode_names2"

%package     -n %{name}+generator-timing
Summary:        Map characters to and from their name given in the Unicode standard - feature "generator-timing"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-names2-generator-1.0/timing) >= 1.3.0
Provides:       crate(%{pkgname}/generator-timing)

%description -n %{name}+generator-timing
This goes to great lengths to be as efficient as possible in both time and space, with the full bidirectional tables weighing barely 500 KB but still offering O(1)* look-up in both directions. (*more precisely, O(length of name).)
This metapackage enables feature "generator-timing" for the Rust unicode_names2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
