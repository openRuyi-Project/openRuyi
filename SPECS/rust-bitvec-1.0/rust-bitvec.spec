# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitvec
%global full_version 1.0.1
%global pkgname bitvec-1.0

Name:           rust-bitvec-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "bitvec"
License:        MIT
URL:            https://bitvecto-rs.github.io/bitvec
#!RemoteAsset:  sha256:1bc2832c24239b0141d5674bb9174f9d68a8b5b3f2753311927c172ca46f7e9c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(funty-2.0) >= 2.0.0
Requires:       crate(radium-0.7/default) >= 0.7.0
Requires:       crate(tap-1.0/default) >= 1.0.1
Requires:       crate(wyz-0.5) >= 0.5.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/atomic)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/testing)

%description
Source code for takopackized Rust crate "bitvec"

%package     -n %{name}+default
Summary:        Addresses memory by bits, for packed collections and bitfields - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/atomic)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bitvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Addresses memory by bits, for packed collections and bitfields - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bitvec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
