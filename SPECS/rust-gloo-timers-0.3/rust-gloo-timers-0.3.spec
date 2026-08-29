# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gloo-timers
%global full_version 0.3.0
%global pkgname gloo-timers-0.3

Name:           rust-gloo-timers-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "gloo-timers"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustwasm/gloo
#!RemoteAsset:  sha256:bbb143cf96099802033e0d4f4963b19fd2e0b728bcf076cd9cf7f6634f092994
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3/default) >= 0.3.31
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gloo-timers"

%package     -n %{name}+futures
Summary:        Convenience crate for working with JavaScript timers - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-channel) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust gloo-timers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-channel
Summary:        Convenience crate for working with JavaScript timers - feature "futures-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-channel) = %{version}

%description -n %{name}+futures-channel
This metapackage enables feature "futures-channel" for the Rust gloo-timers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Convenience crate for working with JavaScript timers - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust gloo-timers crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
