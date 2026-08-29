# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-timer
%global full_version 3.0.4
%global pkgname futures-timer-3

Name:           rust-futures-timer-3
Version:        3.0.4
Release:        %autorelease
Summary:        Rust crate "futures-timer"
License:        MIT OR Apache-2.0
URL:            https://github.com/async-rs/futures-timer
#!RemoteAsset:  sha256:af43fadb8a98512d547e37b4e92e0ced13e205c061b87b4623eff01d918d6968
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "futures-timer"

%package     -n %{name}+gloo-timers
Summary:        Timeouts for futures - feature "gloo-timers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gloo-timers-0.4/default) >= 0.4.0
Requires:       crate(gloo-timers-0.4/futures) >= 0.4.0
Provides:       crate(%{pkgname}/gloo-timers) = %{version}

%description -n %{name}+gloo-timers
This metapackage enables feature "gloo-timers" for the Rust futures-timer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+send-wrapper
Summary:        Timeouts for futures - feature "send_wrapper"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(send-wrapper-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/send-wrapper) = %{version}

%description -n %{name}+send-wrapper
This metapackage enables feature "send_wrapper" for the Rust futures-timer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Timeouts for futures - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gloo-timers) = %{version}
Requires:       crate(%{pkgname}/send-wrapper) = %{version}
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust futures-timer crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
