# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name env_filter
%global full_version 0.1.3
%global pkgname env-filter-0.1

Name:           rust-env-filter-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "env_filter"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/env_logger
#!RemoteAsset:  sha256:186e05a59d4c50738528153b83b0b0194d3a29507dfec16eccd4b342903397d0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(log-0.4/std) >= 0.4.8

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "env_filter"

%package     -n %{name}+regex
Summary:        Filter log events using environment variables - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/perf) >= 1.0.3
Requires:       crate(regex-1/std) >= 1.0.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust env_filter crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
