# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-traits
%global full_version 0.2.19
%global pkgname num-traits-0.2

Name:           rust-num-traits-0.2
Version:        0.2.19
Release:        %autorelease
Summary:        Rust crate "num-traits"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-traits
#!RemoteAsset:  sha256:071dfc062690e90b734c0b2273ce72ad0ffa95f0c74596bc250dcfd960262841
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1.0/default) >= 1.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/i128)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "num-traits"

%package     -n %{name}+libm
Summary:        Numeric traits for generic mathematics - feature "libm"
Requires:       crate(%{pkgname})
Requires:       crate(libm-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libm)

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust num-traits crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
