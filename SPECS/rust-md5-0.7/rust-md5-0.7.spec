# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name md5
%global full_version 0.7.0
%global pkgname md5-0.7

Name:           rust-md5-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "md5"
License:        Apache-2.0 OR MIT
URL:            https://github.com/stainless-steel/md5
#!RemoteAsset:  sha256:490cc448043f947bae3cbee9c203358d62dbee0db12107a74be5c30ccfd09771
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "md5"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
