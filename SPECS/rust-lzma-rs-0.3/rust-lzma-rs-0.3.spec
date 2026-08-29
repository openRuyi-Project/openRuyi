# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lzma-rs
%global full_version 0.3.0
%global pkgname lzma-rs-0.3

Name:           rust-lzma-rs-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "lzma-rs"
License:        MIT
URL:            https://github.com/gendx/lzma-rs
#!RemoteAsset:  sha256:297e814c836ae64db86b36cf2a557ba54368d03f6afcd7d947c266692f71115e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.4.3
Requires:       crate(crc-3/default) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/raw-decoder) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}

%description
Source code for takopackized Rust crate "lzma-rs"

%package     -n %{name}+enable-logging
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust - feature "enable_logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/env-logger) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/enable-logging) = %{version}

%description -n %{name}+enable-logging
This metapackage enables feature "enable_logging" for the Rust lzma-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env-logger
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust - feature "env_logger"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(env-logger-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/env-logger) = %{version}

%description -n %{name}+env-logger
This metapackage enables feature "env_logger" for the Rust lzma-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.17
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust lzma-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
