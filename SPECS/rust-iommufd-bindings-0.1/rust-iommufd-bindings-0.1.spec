# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iommufd-bindings
%global full_version 0.1.0
%global pkgname iommufd-bindings-0.1

Name:           rust-iommufd-bindings-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "iommufd-bindings"
License:        Apache-2.0
URL:            https://github.com/cloud-hypervisor/iommufd
#!RemoteAsset:  sha256:fd7de3a04f6fd55f171a6682852f7aa360bb848a85e0c610513349e006b3c139
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "iommufd-bindings"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
