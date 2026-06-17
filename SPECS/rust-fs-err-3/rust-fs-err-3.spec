# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fs-err
%global full_version 3.3.0
%global pkgname fs-err-3

Name:           rust-fs-err-3
Version:        3.3.0
Release:        %autorelease
Summary:        Rust crate "fs-err"
License:        MIT OR Apache-2.0
URL:            https://github.com/andrewhickman/fs-err
#!RemoteAsset:  sha256:73fde052dbfc920003cfd2c8e2c6e6d4cc7c1091538c3a24226cec0665ab08c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/expose-original-error) = %{version}

%description
Source code for takopackized Rust crate "fs-err"

%package     -n %{name}+debug-tokio
Summary:        Drop-in replacement for std::fs with more helpful error messages - feature "debug_tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/path-facts) = %{version}
Requires:       crate(tokio-1/fs) >= 1.21.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.21.0
Provides:       crate(%{pkgname}/debug-tokio) = %{version}

%description -n %{name}+debug-tokio
This metapackage enables feature "debug_tokio" for the Rust fs-err crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+path-facts
Summary:        Drop-in replacement for std::fs with more helpful error messages - feature "path_facts" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(path-facts-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/path-facts) = %{version}

%description -n %{name}+path-facts
This metapackage enables feature "path_facts" for the Rust fs-err crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "debug" feature.

%package     -n %{name}+tokio
Summary:        Drop-in replacement for std::fs with more helpful error messages - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/fs) >= 1.21.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust fs-err crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
