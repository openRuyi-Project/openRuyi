# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fastrand-2/default) >= 2.0.0
Requires:       crate(unicode-normalization-0.1) >= 0.1.19
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-utils"

%package     -n %{name}+bstr
Summary:        Crate with `gitoxide` utilities that don't need feature toggles - feature "bstr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/std) >= 1.12.0
Provides:       crate(%{pkgname}/bstr) = %{version}

%description -n %{name}+bstr
This metapackage enables feature "bstr" for the Rust gix-utils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
