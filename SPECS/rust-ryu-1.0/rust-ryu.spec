# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ryu
%global full_version 1.0.23
%global pkgname ryu-1.0

Name:           rust-ryu-1.0
Version:        1.0.23
Release:        %autorelease
Summary:        Rust crate "ryu"
License:        Apache-2.0 OR BSL-1.0
URL:            https://github.com/dtolnay/ryu
#!RemoteAsset:  sha256:9774ba4a74de5f7b1c1451ed6cd5285a32eddb5cccb8cc655a4e50009e06477f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/small)

%description
Source code for takopackized Rust crate "ryu"

%package     -n %{name}+no-panic
Summary:        Fast floating point to string conversion - feature "no-panic"
Requires:       crate(%{pkgname})
Requires:       crate(no-panic-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/no-panic)

%description -n %{name}+no-panic
This metapackage enables feature "no-panic" for the Rust ryu crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
