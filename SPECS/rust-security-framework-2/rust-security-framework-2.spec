# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name security-framework
%global full_version 2.11.1
%global pkgname security-framework-2

Name:           rust-security-framework-2
Version:        2.11.1
Release:        %autorelease
Summary:        Rust crate "security-framework"
License:        MIT OR Apache-2.0
URL:            https://lib.rs/crates/security_framework
#!RemoteAsset:  sha256:897b2245f0b511c87893af39b033e5ca9cce68824c4d7e7630b5a1d339658d02
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.6.0
Requires:       crate(core-foundation-0.9/default) >= 0.9.4
Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.6
Requires:       crate(libc-0.2/default) >= 0.2.139
Requires:       crate(security-framework-sys-2) >= 2.11.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alpn) = %{version}
Provides:       crate(%{pkgname}/job-bless) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/session-tickets) = %{version}

%description
Source code for takopackized Rust crate "security-framework"

%package     -n %{name}+osx-10-10
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/osx-10-9) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-10) >= 2.11.1
Provides:       crate(%{pkgname}/osx-10-10) = %{version}

%description -n %{name}+osx-10-10
This metapackage enables feature "OSX_10_10" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+osx-10-11
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_11"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/osx-10-10) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-11) >= 2.11.1
Provides:       crate(%{pkgname}/osx-10-11) = %{version}

%description -n %{name}+osx-10-11
This metapackage enables feature "OSX_10_11" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+osx-10-12
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_12" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/osx-10-11) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-12) >= 2.11.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/osx-10-12) = %{version}

%description -n %{name}+osx-10-12
This metapackage enables feature "OSX_10_12" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+osx-10-13
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_13"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alpn) = %{version}
Requires:       crate(%{pkgname}/osx-10-12) = %{version}
Requires:       crate(%{pkgname}/serial-number-bigint) = %{version}
Requires:       crate(%{pkgname}/session-tickets) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-13) >= 2.11.1
Provides:       crate(%{pkgname}/osx-10-13) = %{version}

%description -n %{name}+osx-10-13
This metapackage enables feature "OSX_10_13" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+osx-10-14
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/osx-10-13) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-14) >= 2.11.1
Provides:       crate(%{pkgname}/osx-10-14) = %{version}

%description -n %{name}+osx-10-14
This metapackage enables feature "OSX_10_14" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+osx-10-15
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_15"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/osx-10-14) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-15) >= 2.11.1
Provides:       crate(%{pkgname}/osx-10-15) = %{version}

%description -n %{name}+osx-10-15
This metapackage enables feature "OSX_10_15" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+osx-10-9
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-9) >= 2.11.1
Provides:       crate(%{pkgname}/osx-10-9) = %{version}

%description -n %{name}+osx-10-9
This metapackage enables feature "OSX_10_9" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Security.framework bindings for macOS and iOS - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.20
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serial-number-bigint
Summary:        Security.framework bindings for macOS and iOS - feature "serial-number-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/serial-number-bigint) = %{version}

%description -n %{name}+serial-number-bigint
This metapackage enables feature "serial-number-bigint" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
