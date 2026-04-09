# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name csv-core
%global full_version 0.1.13
%global pkgname csv-core-0.1

Name:           rust-csv-core-0.1
Version:        0.1.13
Release:        %autorelease
Summary:        Rust crate "csv-core"
License:        Unlicense/MIT
URL:            https://github.com/BurntSushi/rust-csv
#!RemoteAsset:  sha256:704a3c26996a80471189265814dbc2c257598b96b8a7feae2d31ace646bb9782
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0) >= 2.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "csv-core"

%package     -n %{name}+libc
Summary:        Bare bones CSV parsing with no_std support - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/libc) >= 2.0.0
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust csv-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
