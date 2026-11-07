# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name env_logger
%global full_version 0.6.2
%global pkgname env-logger-0.6

Name:           rust-env-logger-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "env_logger"
License:        MIT OR Apache-2.0
URL:            https://github.com/sebasmagri/env_logger/
#!RemoteAsset:  sha256:aafcde04e90a5226a6443b7aabdb016ba2f8307c847d524724bd9b346dd1a2d3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(log-0.4/std) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "env_logger"

%package     -n %{name}+atty
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "atty"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atty-0.2/default) >= 0.2.5
Provides:       crate(%{pkgname}/atty) = %{version}

%description -n %{name}+atty
This metapackage enables feature "atty" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/atty) = %{version}
Requires:       crate(%{pkgname}/humantime) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(%{pkgname}/termcolor) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+humantime
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "humantime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(humantime-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/humantime) = %{version}

%description -n %{name}+humantime
This metapackage enables feature "humantime" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.0.3
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+termcolor
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "termcolor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termcolor-1/default) >= 1.0.2
Provides:       crate(%{pkgname}/termcolor) = %{version}

%description -n %{name}+termcolor
This metapackage enables feature "termcolor" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
