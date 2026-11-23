# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name execute-command-tokens
%global full_version 0.1.0
%global pkgname execute-command-tokens-0.1

Name:           rust-execute-command-tokens-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "execute-command-tokens"
License:        MIT
URL:            https://magiclen.org/execute
#!RemoteAsset:  sha256:de6a2462b6de04b8e6bd3b9a6eb8c0c980dc7f34136e4fb9e18e8ef2c7d69421
Source:         https://static.crates.io/crates/execute-command-tokens/0.1.0/download#/rust-execute-command-tokens-0.1-0.1.0.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "execute-command-tokens"

%package     -n %{name}+default
Summary:        Parse command strings - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust execute-command-tokens crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
