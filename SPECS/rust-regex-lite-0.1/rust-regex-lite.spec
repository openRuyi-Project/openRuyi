# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex-lite
%global full_version 0.1.7
%global pkgname regex-lite-0.1

Name:           rust-regex-lite-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "regex-lite"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex/tree/master/regex-lite
#!RemoteAsset:  sha256:943f41321c63ef1c92fd763bfe054d2668f7f225a5c29f0105903dc2fc04ba30
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/string)

%description
Source code for takopackized Rust crate "regex-lite"

%package     -n %{name}+default
Summary:        Lightweight regex engine that optimizes for binary size and compilation time - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/string)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust regex-lite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
