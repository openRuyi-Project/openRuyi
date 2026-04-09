# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name portable-atomic
%global full_version 1.0.1
%global pkgname portable-atomic-1.0

Name:           rust-portable-atomic-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "portable-atomic"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/portable-atomic
#!RemoteAsset:  sha256:39c00c8683a03bd4fe7db7dd64ab4abee6b42166bc81231da983486ce96be51a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fallback)
Provides:       crate(%{pkgname}/float)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "portable-atomic"

%package     -n %{name}+critical-section
Summary:        Portable atomic types including support for 128-bit atomics, atomic float, etc - feature "critical-section"
Requires:       crate(%{pkgname})
Requires:       crate(critical-section-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/critical-section)

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust portable-atomic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Portable atomic types including support for 128-bit atomics, atomic float, etc - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.103
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust portable-atomic crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
