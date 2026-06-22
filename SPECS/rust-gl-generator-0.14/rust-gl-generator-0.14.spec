# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gl_generator
%global full_version 0.14.0
%global pkgname gl-generator-0.14

Name:           rust-gl-generator-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "gl_generator"
License:        Apache-2.0
URL:            https://github.com/brendanzab/gl-rs/
#!RemoteAsset:  sha256:1a95dfc23a2b4a9a2f5ab41d194f8bfda3cabec42af4e39f08c339eb2a0c124d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(khronos-api-3/default) >= 3.1.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(xml-rs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable-generator-utils) = %{version}

%description
Source code for takopackized Rust crate "gl_generator"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
