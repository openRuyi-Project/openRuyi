# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-utils
%global full_version 0.3.1
%global pkgname gix-utils-0.3

Name:           rust-gix-utils-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "gix-utils"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:befcdbdfb1238d2854591f760a48711bed85e72d80a10e8f2f93f656746ef7c5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fastrand-2.0/default) >= 2.3.0
Requires:       crate(unicode-normalization-0.1) >= 0.1.25
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-utils"

%package     -n %{name}+bstr
Summary:        Crate with `gitoxide` utilities that don't need feature toggles - feature "bstr"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/std) >= 1.12.1
Provides:       crate(%{pkgname}/bstr)

%description -n %{name}+bstr
This metapackage enables feature "bstr" for the Rust gix-utils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
