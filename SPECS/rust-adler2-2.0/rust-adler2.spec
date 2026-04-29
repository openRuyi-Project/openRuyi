# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name adler2
%global full_version 2.0.1
%global pkgname adler2-2.0

Name:           rust-adler2-2.0
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "adler2"
License:        0BSD OR MIT OR Apache-2.0
URL:            https://github.com/oyvindln/adler2
#!RemoteAsset:  sha256:320119579fcad9c21884f5c4861d16174d0e06250625266f50fe6898340abefa
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "adler2"

%package     -n %{name}+core
Summary:        Simple clean-room implementation of the Adler-32 checksum - feature "core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust adler2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustc-dep-of-std" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
