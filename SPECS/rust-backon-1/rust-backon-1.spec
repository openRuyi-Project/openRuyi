# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name backon
%global full_version 1.6.0
%global pkgname backon-1

Name:           rust-backon-1
Version:        1.6.0
Release:        %autorelease
Summary:        Rust crate "backon"
License:        Apache-2.0
URL:            https://github.com/Xuanwo/backon
#!RemoteAsset:  sha256:cffb0e931875b666fc4fcb20fee52e9bbd1ef836fd9e9e04ec21555f9f85f7ef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

# Drop features that depend on unpackaged crates.
Patch2000:      2000-drop-unpackaged-features.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(fastrand-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std-blocking-sleep) = %{version}

%description
Source code for takopackized Rust crate "backon"

%package     -n %{name}+default
Summary:        Make retry like a built-in feature provided by Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gloo-timers-sleep) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/std-blocking-sleep) = %{version}
Requires:       crate(%{pkgname}/tokio-sleep) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust backon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gloo-timers
Summary:        Make retry like a built-in feature provided by Rust - feature "gloo-timers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gloo-timers-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/gloo-timers) = %{version}

%description -n %{name}+gloo-timers
This metapackage enables feature "gloo-timers" for the Rust backon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gloo-timers-sleep
Summary:        Make retry like a built-in feature provided by Rust - feature "gloo-timers-sleep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gloo-timers-0.3/futures) >= 0.3.0
Provides:       crate(%{pkgname}/gloo-timers-sleep) = %{version}

%description -n %{name}+gloo-timers-sleep
This metapackage enables feature "gloo-timers-sleep" for the Rust backon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Make retry like a built-in feature provided by Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fastrand-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust backon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Make retry like a built-in feature provided by Rust - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust backon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-sleep
Summary:        Make retry like a built-in feature provided by Rust - feature "tokio-sleep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/tokio-sleep) = %{version}

%description -n %{name}+tokio-sleep
This metapackage enables feature "tokio-sleep" for the Rust backon crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
