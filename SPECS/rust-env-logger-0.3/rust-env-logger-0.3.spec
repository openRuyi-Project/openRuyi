# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name env_logger
%global full_version 0.3.5
%global pkgname env-logger-0.3

Name:           rust-env-logger-0.3
Version:        0.3.5
Release:        %autorelease
Summary:        Rust crate "env_logger"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/log
#!RemoteAsset:  sha256:15abd780e45b3ea4f76b4e9a26ff4843258dd8a3eed2775a0e7368c2e7936c2f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "env_logger"

%package     -n %{name}+regex
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
