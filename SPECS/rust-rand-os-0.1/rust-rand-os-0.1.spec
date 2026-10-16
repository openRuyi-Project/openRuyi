# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_os
%global full_version 0.1.3
%global pkgname rand-os-0.1

Name:           rust-rand-os-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "rand_os"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_os
#!RemoteAsset:  sha256:7b75f676a1e053fc562eafbb47838d67c84801e38fc1ba459e8f180deabd5071
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cloudabi-0.0.3/default) >= 0.0.3
Requires:       crate(fuchsia-cprng-0.1/default) >= 0.1.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(rand-core-0.4/default) >= 0.4.0
Requires:       crate(rand-core-0.4/std) >= 0.4.0
Requires:       crate(rdrand-0.4/default) >= 0.4.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/minwindef) >= 0.3.0
Requires:       crate(winapi-0.3/ntsecapi) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_os"

%package     -n %{name}+log
Summary:        OS backed Random Number Generator - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rand_os crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stdweb
Summary:        OS backed Random Number Generator - feature "stdweb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stdweb-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/stdweb) = %{version}

%description -n %{name}+stdweb
This metapackage enables feature "stdweb" for the Rust rand_os crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        OS backed Random Number Generator - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust rand_os crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
