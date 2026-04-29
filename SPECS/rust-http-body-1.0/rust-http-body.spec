# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name http-body
%global full_version 1.0.1
%global pkgname http-body-1.0

Name:           rust-http-body-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "http-body"
License:        MIT
URL:            https://github.com/hyperium/http-body
#!RemoteAsset:  sha256:1efedce1fb8e6913f23e0c92de8e62cd5b772a67e7b3946df930a62566c93184
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(http-1.0/default) >= 1.4.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "http-body"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
