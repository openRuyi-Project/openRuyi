# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libtest-mimic
%global full_version 0.7.3
%global pkgname libtest-mimic-0.7

Name:           rust-libtest-mimic-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "libtest-mimic"
License:        MIT/Apache-2.0
URL:            https://github.com/LukasKalbertodt/libtest-mimic
#!RemoteAsset:  sha256:cc0bda45ed5b3a2904262c1bb91e526127aa70e7ef3758aba2ef93cf896b9b58
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4.0/default) >= 4.6.1
Requires:       crate(clap-4.0/derive) >= 4.6.1
Requires:       crate(escape8259-0.5/default) >= 0.5.3
Requires:       crate(termcolor-1.0/default) >= 1.4.1
Requires:       crate(threadpool-1.0/default) >= 1.8.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "libtest-mimic"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
