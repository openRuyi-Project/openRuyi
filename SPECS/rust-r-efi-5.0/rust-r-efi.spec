# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name r-efi
%global full_version 5.3.0
%global pkgname r-efi-5.0

Name:           rust-r-efi-5.0
Version:        5.3.0
Release:        %autorelease
Summary:        Rust crate "r-efi"
License:        MIT OR Apache-2.0 OR LGPL-2.1-or-later
URL:            https://github.com/r-efi/r-efi/wiki
#!RemoteAsset:  sha256:69cdb34c158ceb288df11e18b4bd39de994f6657d83847bdffdbd7f346754b0f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/efiapi)
Provides:       crate(%{pkgname}/examples)
Provides:       crate(%{pkgname}/native)

%description
Source code for takopackized Rust crate "r-efi"

%package     -n %{name}+core
Summary:        UEFI Reference Specification Protocol Constants and Definitions - feature "core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust r-efi crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustc-dep-of-std" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
