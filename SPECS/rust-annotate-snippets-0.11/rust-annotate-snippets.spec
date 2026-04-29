# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name annotate-snippets
%global full_version 0.11.5
%global pkgname annotate-snippets-0.11

Name:           rust-annotate-snippets-0.11
Version:        0.11.5
Release:        %autorelease
Summary:        Rust crate "annotate-snippets"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/annotate-snippets-rs
#!RemoteAsset:  sha256:710e8eae58854cdc1790fcb56cca04d712a17be849eeb81da2a724bf4bae2bc4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/testing-colors)

%description
Source code for takopackized Rust crate "annotate-snippets"

%package     -n %{name}+memchr
Summary:        Building code annotations - feature "memchr" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/default) >= 2.7.4
Provides:       crate(%{pkgname}/memchr)
Provides:       crate(%{pkgname}/simd)

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust annotate-snippets crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simd" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
