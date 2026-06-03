# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha1_smol
%global full_version 1.0.1
%global pkgname sha1-smol-1.0

Name:           rust-sha1-smol-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "sha1_smol"
License:        BSD-3-Clause
URL:            https://github.com/mitsuhiko/sha1-smol
#!RemoteAsset:  sha256:bbfa15b3dddfee50a0fff136974b3e1bde555604ba463834a7eb7deb6417705d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "sha1_smol"

%package     -n %{name}+serde
Summary:        Minimal dependency-free implementation of SHA1 for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sha1_smol crate.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
