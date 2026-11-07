# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quickcheck
%global full_version 0.3.2
%global pkgname quickcheck-0.3

Name:           rust-quickcheck-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "quickcheck"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/quickcheck
#!RemoteAsset:  sha256:0b333da40686cc05db13d933f8e7b450f403cfc5a4d005154d8d4a5ba9d14605
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "quickcheck"

%package     -n %{name}+env-logger
Summary:        Automatic property based testing with shrinking - feature "env_logger"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(env-logger-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/env-logger) = %{version}

%description -n %{name}+env-logger
This metapackage enables feature "env_logger" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Automatic property based testing with shrinking - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-logging
Summary:        Automatic property based testing with shrinking - feature "use_logging" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/env-logger) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-logging) = %{version}

%description -n %{name}+use-logging
This metapackage enables feature "use_logging" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
