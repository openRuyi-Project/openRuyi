# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name subplot-build
%global full_version 0.12.0
%global pkgname subplot-build-0.12

Name:           rust-subplot-build-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "subplot-build"
License:        MIT-0
URL:            https://subplot.tech/
#!RemoteAsset:  sha256:008b31a93442526100369310bf717117df546b8259b7043aebcfdffa84af35bf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(subplot-0.12/default) >= 0.12.0
Requires:       crate(tracing-0.1/default) >= 0.1.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "subplot-build"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
