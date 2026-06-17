# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mutants
%global full_version 0.0.3
%global pkgname mutants-0.0.3

Name:           rust-mutants-0.0.3
Version:        0.0.3
Release:        %autorelease
Summary:        Rust crate "mutants"
License:        MIT
URL:            https://github.com/sourcefrog/cargo-mutants
#!RemoteAsset:  sha256:bc0287524726960e07b119cebd01678f852f147742ae0d925e6a520dca956126
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mutants"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
