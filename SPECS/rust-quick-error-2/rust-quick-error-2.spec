# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quick-error
%global full_version 2.0.1
%global pkgname quick-error-2

Name:           rust-quick-error-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "quick-error"
License:        MIT OR Apache-2.0
URL:            http://github.com/tailhook/quick-error
#!RemoteAsset:  sha256:a993555f31e5a609f617c12db6250dedcac1b0a85076912c436e6fc9b2c8e6a3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quick-error"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
