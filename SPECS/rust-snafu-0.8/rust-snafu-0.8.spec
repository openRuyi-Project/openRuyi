# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snafu
%global full_version 0.8.9
%global pkgname snafu-0.8

Name:           rust-snafu-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "snafu"
License:        MIT OR Apache-2.0
URL:            https://github.com/shepmaster/snafu
#!RemoteAsset:  sha256:6e84b3f4eacbf3a1ce05eac6763b4d629d60cbc94d632e4092c54ade71f1e1a2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(snafu-derive-0.8/default) >= 0.8.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/guide) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-core-error) = %{version}
Provides:       crate(%{pkgname}/unstable-try-trait) = %{version}

%description
Source code for takopackized Rust crate "snafu"

%package     -n %{name}+backtrace
Summary:        Ergonomic error handling library - feature "backtrace" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/backtrace) = %{version}
Provides:       crate(%{pkgname}/backtraces-impl-backtrace-crate) = %{version}

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "backtraces-impl-backtrace-crate" feature.

%package     -n %{name}+default
Summary:        Ergonomic error handling library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rust-1-65) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Ergonomic error handling library - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core-crate) = %{version}
Requires:       crate(%{pkgname}/pin-project) = %{version}
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core-crate
Summary:        Ergonomic error handling library - feature "futures-core-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures-core-crate) = %{version}

%description -n %{name}+futures-core-crate
This metapackage enables feature "futures-core-crate" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-crate
Summary:        Ergonomic error handling library - feature "futures-crate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3) >= 0.3.11
Provides:       crate(%{pkgname}/futures-crate) = %{version}
Provides:       crate(%{pkgname}/internal-dev-dependencies) = %{version}

%description -n %{name}+futures-crate
This metapackage enables feature "futures-crate" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "internal-dev-dependencies" feature.

%package     -n %{name}+pin-project
Summary:        Ergonomic error handling library - feature "pin-project"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-1) >= 1.0.2
Provides:       crate(%{pkgname}/pin-project) = %{version}

%description -n %{name}+pin-project
This metapackage enables feature "pin-project" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-1-61
Summary:        Ergonomic error handling library - feature "rust_1_61" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snafu-derive-0.8/rust-1-61) >= 0.8.9
Provides:       crate(%{pkgname}/rust-1-61) = %{version}
Provides:       crate(%{pkgname}/rust-1-65) = %{version}
Provides:       crate(%{pkgname}/rust-1-81) = %{version}

%description -n %{name}+rust-1-61
This metapackage enables feature "rust_1_61" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rust_1_65", and "rust_1_81" features.

%package     -n %{name}+unstable-provider-api
Summary:        Ergonomic error handling library - feature "unstable-provider-api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snafu-derive-0.8/unstable-provider-api) >= 0.8.9
Provides:       crate(%{pkgname}/unstable-provider-api) = %{version}

%description -n %{name}+unstable-provider-api
This metapackage enables feature "unstable-provider-api" for the Rust snafu crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
