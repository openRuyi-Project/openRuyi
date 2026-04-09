# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros-backend
%global full_version 0.23.5
%global pkgname pyo3-macros-backend-0.23

Name:           rust-pyo3-macros-backend-0.23
Version:        0.23.5
Release:        %autorelease
Summary:        Rust crate "pyo3-macros-backend"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:fca6726ad0f3da9c9de093d6f116a93c1a38e417ed73bf138472cf4064f72028
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1.0) >= 1.0.60
Requires:       crate(pyo3-build-config-0.23/default) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(quote-1.0) >= 1.0.0
Requires:       crate(syn-2.0/clone-impls) >= 2.0.59
Requires:       crate(syn-2.0/derive) >= 2.0.59
Requires:       crate(syn-2.0/extra-traits) >= 2.0.59
Requires:       crate(syn-2.0/full) >= 2.0.59
Requires:       crate(syn-2.0/parsing) >= 2.0.59
Requires:       crate(syn-2.0/printing) >= 2.0.59
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-async)

%description
Source code for takopackized Rust crate "pyo3-macros-backend"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
