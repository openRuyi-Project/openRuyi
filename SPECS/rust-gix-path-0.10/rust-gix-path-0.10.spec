# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-path
%global full_version 0.10.22
%global pkgname gix-path-0.10

Name:           rust-gix-path-0.10
Version:        0.10.22
Release:        %autorelease
Summary:        Rust crate "gix-path"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:7cb06c3e4f8eed6e24fd915fa93145e28a511f4ea0e768bae16673e05ed3f366
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.14
Requires:       crate(gix-validate-0.10/default) >= 0.10.1
Requires:       crate(thiserror-2/default) >= 2.0.17
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-path"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
