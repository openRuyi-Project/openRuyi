# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name generator
%global full_version 0.8.9
%global pkgname generator-0.8

Name:           rust-generator-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "generator"
License:        MIT OR Apache-2.0
URL:            https://github.com/Xudong-Huang/generator-rs.git
#!RemoteAsset:  sha256:b3b854b0e584ead1a33f18b2fcad7cf7be18b3875c78816b753639aa501513ae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.100
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(rustversion-1) >= 1.0.0
Requires:       crate(windows-link-0.1/default) >= 0.1.0
Requires:       crate(windows-result-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "generator"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
