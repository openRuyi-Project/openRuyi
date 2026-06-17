# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde-pyobject
%global full_version 0.8.0
%global pkgname serde-pyobject-0.8

Name:           rust-serde-pyobject-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "serde-pyobject"
License:        MIT OR Apache-2.0
URL:            https://github.com/Jij-Inc/serde-pyobject
#!RemoteAsset:  sha256:5614e792b7c36d3feeb45b8287ea2dc615f063896e59258d11ef5015c18bdf6a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.28
Requires:       crate(pyo3-0.27/default) >= 0.27.0
Requires:       crate(serde-1/default) >= 1.0.228
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde-pyobject"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
