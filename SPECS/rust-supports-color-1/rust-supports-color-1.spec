# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name supports-color
%global full_version 1.3.1
%global pkgname supports-color-1

Name:           rust-supports-color-1
Version:        1.3.1
Release:        %autorelease
Summary:        Rust crate "supports-color"
License:        Apache-2.0
URL:            https://github.com/zkat/supports-color
#!RemoteAsset:  sha256:8ba6faf2ca7ee42fdd458f4347ae0a9bd6bcc445ad7cb57ad82b383f18870d6f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atty-0.2/default) >= 0.2.14
Requires:       crate(is-ci-1/default) >= 1.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "supports-color"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
