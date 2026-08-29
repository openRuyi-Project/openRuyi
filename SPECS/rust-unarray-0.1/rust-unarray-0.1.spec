# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unarray
%global full_version 0.1.4
%global pkgname unarray-0.1

Name:           rust-unarray-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "unarray"
License:        MIT OR Apache-2.0
URL:            https://github.com/cameron1024/unarray
#!RemoteAsset:  sha256:eaea85b334db583fe3274d12b4cd1880032beab409c0d774be044d4480ab9a94
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unarray"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
