# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iommufd-ioctls
%global full_version 0.1.0
%global pkgname iommufd-ioctls-0.1

Name:           rust-iommufd-ioctls-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "iommufd-ioctls"
License:        Apache-2.0
URL:            https://github.com/cloud-hypervisor/iommufd
#!RemoteAsset:  sha256:4eabd3414d9c4e716c9a198fbfac484625f088c075605372daf037edfe336e18
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(iommufd-bindings-0.1/default) >= 0.1.0
Requires:       crate(thiserror-2/default) >= 2.0.17
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "iommufd-ioctls"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
