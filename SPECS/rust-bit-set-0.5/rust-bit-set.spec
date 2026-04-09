# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bit-set
%global full_version 0.5.3
%global pkgname bit-set-0.5

Name:           rust-bit-set-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "bit-set"
License:        MIT/Apache-2.0
URL:            https://github.com/contain-rs/bit-set
#!RemoteAsset:  sha256:0700ddab506f33b20a03b13996eccd309a48e5ff77d0d95926aa0210fb4e95f1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-vec-0.6) >= 0.6.1
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "bit-set"

%package     -n %{name}+std
Summary:        Set of bits - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bit-vec-0.6/std) >= 0.6.1
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bit-set crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
