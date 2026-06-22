# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-build-config
%global full_version 0.29.0
%global pkgname pyo3-build-config-0.29

Name:           rust-pyo3-build-config-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "pyo3-build-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:c5e2a7d2f0d013342f295c048ad19237add5154a55b1c5a254c0ec93d4109078
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(target-lexicon-0.13) >= 0.13.3
Requires:       crate(target-lexicon-0.13/default) >= 0.13.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extension-module) = %{version}
Provides:       crate(%{pkgname}/generate-import-lib) = %{version}
Provides:       crate(%{pkgname}/resolve-config) = %{version}

%description
Source code for takopackized Rust crate "pyo3-build-config"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
