# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-registry
%global full_version 0.6.1
%global pkgname windows-registry-0.6

Name:           rust-windows-registry-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "windows-registry"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:02752bf7fbdcce7f2a27a742f798510f3e5ad88dbe84871e5168e2120c3d5720
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-link-0.2) >= 0.2.1
Requires:       crate(windows-result-0.4) >= 0.4.1
Requires:       crate(windows-strings-0.5) >= 0.5.1
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "windows-registry"

%package     -n %{name}+std
Summary:        Windows registry - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(windows-result-0.4/std) >= 0.4.1
Requires:       crate(windows-strings-0.5/std) >= 0.5.1
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust windows-registry crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
