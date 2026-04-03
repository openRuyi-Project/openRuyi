# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name implib
%global full_version 0.4.0
%global pkgname implib-0.4

Name:           rust-implib-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "implib"
License:        MIT
URL:            https://github.com/messense/implib-rs
#!RemoteAsset:  sha256:7923c255262a0e44362e221f8b74b931fe21484b83f27386aa45f021a379caf6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memoffset-0.9/default) >= 0.9.0
Requires:       crate(object-0.37/pe) >= 0.37.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/msvc)

%description
Source code for takopackized Rust crate "implib"

%package     -n %{name}+default
Summary:        Generate Windows import library from module definition file - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnu)
Requires:       crate(%{pkgname}/msvc)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust implib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnu
Summary:        Generate Windows import library from module definition file - feature "gnu"
Requires:       crate(%{pkgname})
Requires:       crate(object-0.37/pe) >= 0.37.1
Requires:       crate(object-0.37/write-std) >= 0.37.1
Provides:       crate(%{pkgname}/gnu)

%description -n %{name}+gnu
This metapackage enables feature "gnu" for the Rust implib crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
