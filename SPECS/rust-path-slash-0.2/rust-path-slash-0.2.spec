# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name path-slash
%global full_version 0.2.1
%global pkgname path-slash-0.2

Name:           rust-path-slash-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "path-slash"
License:        MIT
URL:            https://github.com/rhysd/path-slash
#!RemoteAsset:  sha256:1e91099d4268b0e11973f036e885d652fb0b21fedcf69738c627f94db6a44f42
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "path-slash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
