# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snafu
%global full_version 0.9.2
%global pkgname snafu-0.9

Name:           rust-snafu-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "snafu"
License:        MIT OR Apache-2.0
URL:            https://github.com/shepmaster/snafu
#!RemoteAsset:  sha256:e45cb604038abb7b926b679887b3226d8d0f23874b66623625a0454be425a4b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(snafu-derive-0.9/default) >= 0.9.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/backtrace) = %{version}
Provides:       crate(%{pkgname}/futures-core-crate) = %{version}
Provides:       crate(%{pkgname}/futures-crate) = %{version}
Provides:       crate(%{pkgname}/guide) = %{version}
Provides:       crate(%{pkgname}/pin-project) = %{version}
Provides:       crate(%{pkgname}/rust-1-81) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-try-trait) = %{version}

%description
Source code for takopackized Rust crate "snafu"

%package     -n %{name}+backtraces-impl-backtrace-crate
Summary:        Ergonomic error handling library - feature "backtraces-impl-backtrace-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/std) >= 0.3.0
Provides:       crate(%{pkgname}/backtraces-impl-backtrace-crate) = %{version}

%description -n %{name}+backtraces-impl-backtrace-crate
This metapackage enables feature "backtraces-impl-backtrace-crate" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Ergonomic error handling library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rust-1-81) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Ergonomic error handling library - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(pin-project-1) >= 1.0.2
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+internal-dev-dependencies
Summary:        Ergonomic error handling library - feature "internal-dev-dependencies"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/executor) >= 0.3.11
Provides:       crate(%{pkgname}/internal-dev-dependencies) = %{version}

%description -n %{name}+internal-dev-dependencies
This metapackage enables feature "internal-dev-dependencies" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-provider-api
Summary:        Ergonomic error handling library - feature "unstable-provider-api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snafu-derive-0.9/unstable-provider-api) >= 0.9.2
Provides:       crate(%{pkgname}/unstable-provider-api) = %{version}

%description -n %{name}+unstable-provider-api
This metapackage enables feature "unstable-provider-api" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
