# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-deque
%global full_version 0.7.4
%global pkgname crossbeam-deque-0.7

Name:           rust-crossbeam-deque-0.7
Version:        0.7.4
Release:        %autorelease
Summary:        Rust crate "crossbeam-deque"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque
#!RemoteAsset:  sha256:c20ff29ded3204c5106278a81a38f4b482636ed4fa1e6cfbeef193291beb29ed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-epoch-0.8/default) >= 0.8.0
Requires:       crate(crossbeam-utils-0.7/default) >= 0.7.0
Requires:       crate(maybe-uninit-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "crossbeam-deque"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
