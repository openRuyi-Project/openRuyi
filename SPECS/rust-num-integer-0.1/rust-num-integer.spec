# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-integer
%global full_version 0.1.46
%global pkgname num-integer-0.1

Name:           rust-num-integer-0.1
Version:        0.1.46
Release:        %autorelease
Summary:        Rust crate "num-integer"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-integer
#!RemoteAsset:  sha256:7969661fd2958a5cb096e56c8e1ad0444ac2bbcd0061bd28660485a44879858f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/i128)

%description
Source code for takopackized Rust crate "num-integer"

%package     -n %{name}+std
Summary:        Integer traits and functions - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-integer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
