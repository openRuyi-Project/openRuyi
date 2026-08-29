# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num_cpus
%global full_version 1.17.0
%global pkgname num-cpus-1

Name:           rust-num-cpus-1
Version:        1.17.0
Release:        %autorelease
Summary:        Rust crate "num_cpus"
License:        MIT OR Apache-2.0
URL:            https://github.com/seanmonstar/num_cpus
#!RemoteAsset:  sha256:91df4bbde75afed763b708b7eee1e8e7651e02d97f6d5dd763e89367e957b23b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hermit-abi-0.5/default) >= 0.5.0
Requires:       crate(libc-0.2/default) >= 0.2.26
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "num_cpus"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
