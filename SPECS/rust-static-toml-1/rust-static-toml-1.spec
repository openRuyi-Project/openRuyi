# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name static-toml
%global full_version 1.3.0
%global pkgname static-toml-1

Name:           rust-static-toml-1
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "static-toml"
License:        MIT
URL:            https://github.com/cptpiepmatz/static-toml
#!RemoteAsset:  sha256:b4df9e050de84b640ece7b8959a4a040600598c15f007bb39a7eeefe52f7a8cf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(convert-case-0.6/default) >= 0.6.0
Requires:       crate(proc-macro-error-1/default) >= 1.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(toml-0.8/default) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "static-toml"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
