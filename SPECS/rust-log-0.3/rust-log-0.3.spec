# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name log
%global full_version 0.3.9
%global pkgname log-0.3

Name:           rust-log-0.3
Version:        0.3.9
Release:        %autorelease
Summary:        Rust crate "log"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/log
#!RemoteAsset:  sha256:e19e8d5c34a3e0e2223db8e060f9e8264aeeb5c5fc64a4ee9965c062211c024b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "log"

%package     -n %{name}+max-level-debug
Summary:        Lightweight logging facade for Rust - feature "max_level_debug"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/max-level-debug) = %{version}

%description -n %{name}+max-level-debug
This metapackage enables feature "max_level_debug" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+max-level-error
Summary:        Lightweight logging facade for Rust - feature "max_level_error"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/max-level-error) = %{version}

%description -n %{name}+max-level-error
This metapackage enables feature "max_level_error" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+max-level-info
Summary:        Lightweight logging facade for Rust - feature "max_level_info"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/max-level-info) = %{version}

%description -n %{name}+max-level-info
This metapackage enables feature "max_level_info" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+max-level-off
Summary:        Lightweight logging facade for Rust - feature "max_level_off"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/max-level-off) = %{version}

%description -n %{name}+max-level-off
This metapackage enables feature "max_level_off" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+max-level-trace
Summary:        Lightweight logging facade for Rust - feature "max_level_trace"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/max-level-trace) = %{version}

%description -n %{name}+max-level-trace
This metapackage enables feature "max_level_trace" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+max-level-warn
Summary:        Lightweight logging facade for Rust - feature "max_level_warn"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/max-level-warn) = %{version}

%description -n %{name}+max-level-warn
This metapackage enables feature "max_level_warn" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+release-max-level-debug
Summary:        Lightweight logging facade for Rust - feature "release_max_level_debug"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/release-max-level-debug) = %{version}

%description -n %{name}+release-max-level-debug
This metapackage enables feature "release_max_level_debug" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+release-max-level-error
Summary:        Lightweight logging facade for Rust - feature "release_max_level_error"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/release-max-level-error) = %{version}

%description -n %{name}+release-max-level-error
This metapackage enables feature "release_max_level_error" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+release-max-level-info
Summary:        Lightweight logging facade for Rust - feature "release_max_level_info"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/release-max-level-info) = %{version}

%description -n %{name}+release-max-level-info
This metapackage enables feature "release_max_level_info" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+release-max-level-off
Summary:        Lightweight logging facade for Rust - feature "release_max_level_off"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/release-max-level-off) = %{version}

%description -n %{name}+release-max-level-off
This metapackage enables feature "release_max_level_off" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+release-max-level-trace
Summary:        Lightweight logging facade for Rust - feature "release_max_level_trace"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/release-max-level-trace) = %{version}

%description -n %{name}+release-max-level-trace
This metapackage enables feature "release_max_level_trace" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+release-max-level-warn
Summary:        Lightweight logging facade for Rust - feature "release_max_level_warn"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/release-max-level-warn) = %{version}

%description -n %{name}+release-max-level-warn
This metapackage enables feature "release_max_level_warn" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-std
Summary:        Lightweight logging facade for Rust - feature "use_std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description -n %{name}+use-std
This metapackage enables feature "use_std" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
