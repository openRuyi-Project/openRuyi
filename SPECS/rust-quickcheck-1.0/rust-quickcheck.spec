# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quickcheck
%global full_version 1.1.0
%global pkgname quickcheck-1.0

Name:           rust-quickcheck-1.0
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "quickcheck"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/quickcheck
#!RemoteAsset:  sha256:95c589f335db0f6aaa168a7cd27b1fc6920f5e1470c804f814d9cd6e62a0f70b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-0.10/sys-rng) >= 0.10.1
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "quickcheck"

%package     -n %{name}+default
Summary:        Automatic property based testing with shrinking - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/regex)
Requires:       crate(%{pkgname}/use-logging)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env-logger
Summary:        Automatic property based testing with shrinking - feature "env_logger"
Requires:       crate(%{pkgname})
Requires:       crate(env-logger-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/env-logger)

%description -n %{name}+env-logger
This metapackage enables feature "env_logger" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Automatic property based testing with shrinking - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Automatic property based testing with shrinking - feature "regex"
Requires:       crate(%{pkgname})
Requires:       crate(env-logger-0.11/regex) >= 0.11.0
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-logging
Summary:        Automatic property based testing with shrinking - feature "use_logging"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/env-logger)
Requires:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/use-logging)

%description -n %{name}+use-logging
This metapackage enables feature "use_logging" for the Rust quickcheck crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
