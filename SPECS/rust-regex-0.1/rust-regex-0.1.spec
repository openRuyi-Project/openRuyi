# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex
%global full_version 0.1.80
%global pkgname regex-0.1

Name:           rust-regex-0.1
Version:        0.1.80
Release:        %autorelease
Summary:        Rust crate "regex"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex
#!RemoteAsset:  sha256:4fd4ace6a8cf7860714a2c2280d6c1f7e6a413486c13298bbc86fd3da019402f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aho-corasick-0.5/default) >= 0.5.3
Requires:       crate(memchr-0.1/default) >= 0.1.9
Requires:       crate(regex-syntax-0.3/default) >= 0.3.8
Requires:       crate(thread-local-0.2/default) >= 0.2.4
Requires:       crate(utf8-ranges-0.1/default) >= 0.1.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/pattern) = %{version}

%description
This implementation uses finite automata and guarantees linear time matching on all inputs.
Source code for takopackized Rust crate "regex"

%package     -n %{name}+simd
Summary:        Regular expressions for Rust - feature "simd" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simd-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/simd-accel) = %{version}

%description -n %{name}+simd
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "simd" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simd-accel" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
