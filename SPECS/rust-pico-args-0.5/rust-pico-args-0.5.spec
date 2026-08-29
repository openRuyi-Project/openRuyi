# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pico-args
%global full_version 0.5.0
%global pkgname pico-args-0.5

Name:           rust-pico-args-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "pico-args"
License:        MIT
URL:            https://github.com/RazrFalcon/pico-args
#!RemoteAsset:  sha256:5be167a7af36ee22fe3115051bc51f6e6c7054c9348e28deb4f49bd6f705a315
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/combined-flags) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/eq-separator) = %{version}
Provides:       crate(%{pkgname}/short-space-opt) = %{version}

%description
Source code for takopackized Rust crate "pico-args"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
