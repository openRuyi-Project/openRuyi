# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-deque
%global full_version 0.8.6
%global pkgname crossbeam-deque-0.8

Name:           rust-crossbeam-deque-0.8
Version:        0.8.6
Release:        %autorelease
Summary:        Rust crate "crossbeam-deque"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque
#!RemoteAsset:  sha256:9dd111b7b7f7d55b72c0a6ae361660ee5853c9af73f70c3c2ef6858b950e2e51
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-epoch-0.9) >= 0.9.18
Requires:       crate(crossbeam-utils-0.8) >= 0.8.21
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "crossbeam-deque"

%package     -n %{name}+std
Summary:        Concurrent work-stealing deque - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(crossbeam-epoch-0.9/std) >= 0.9.18
Requires:       crate(crossbeam-utils-0.8/std) >= 0.8.21
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam-deque crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
