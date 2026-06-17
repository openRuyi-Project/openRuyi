# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crunchy
%global full_version 0.2.4
%global pkgname crunchy-0.2

Name:           rust-crunchy-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "crunchy"
License:        MIT
URL:            https://github.com/eira-fransham/crunchy
#!RemoteAsset:  sha256:460fbee9c2c2f33933d720630a6a0bac33ba7053db5344fac858d4b8952d77d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/limit-1024) = %{version}
Provides:       crate(%{pkgname}/limit-128) = %{version}
Provides:       crate(%{pkgname}/limit-2048) = %{version}
Provides:       crate(%{pkgname}/limit-256) = %{version}
Provides:       crate(%{pkgname}/limit-512) = %{version}
Provides:       crate(%{pkgname}/limit-64) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "crunchy"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
