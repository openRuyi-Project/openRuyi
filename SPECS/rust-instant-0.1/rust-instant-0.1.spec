# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name instant
%global full_version 0.1.13
%global pkgname instant-0.1

Name:           rust-instant-0.1
Version:        0.1.13
Release:        %autorelease
Summary:        Rust crate "instant"
License:        BSD-3-Clause
URL:            https://github.com/sebcrozet/instant
#!RemoteAsset:  sha256:e0242819d153cba4b4b05a5a8f2a7e9bbf97b6055b2a002b395c96b5ff3c0222
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/inaccurate) = %{version}
Provides:       crate(%{pkgname}/now) = %{version}

%description
Source code for takopackized Rust crate "instant"

%package     -n %{name}+js-sys
Summary:        Unmaintained, consider using web-time instead - A partial replacement for std::time::Instant that works on WASM to - feature "js-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/js-sys) = %{version}

%description -n %{name}+js-sys
This metapackage enables feature "js-sys" for the Rust instant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stdweb
Summary:        Unmaintained, consider using web-time instead - A partial replacement for std::time::Instant that works on WASM to - feature "stdweb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stdweb-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/stdweb) = %{version}

%description -n %{name}+stdweb
This metapackage enables feature "stdweb" for the Rust instant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Unmaintained, consider using web-time instead - A partial replacement for std::time::Instant that works on WASM to - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/js-sys) = %{version}
Requires:       crate(%{pkgname}/wasm-bindgen-rs) = %{version}
Requires:       crate(%{pkgname}/web-sys) = %{version}
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust instant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen-rs
Summary:        Unmaintained, consider using web-time instead - A partial replacement for std::time::Instant that works on WASM to - feature "wasm-bindgen_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/wasm-bindgen-rs) = %{version}

%description -n %{name}+wasm-bindgen-rs
This metapackage enables feature "wasm-bindgen_rs" for the Rust instant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+web-sys
Summary:        Unmaintained, consider using web-time instead - A partial replacement for std::time::Instant that works on WASM to - feature "web-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(web-sys-0.3/default) >= 0.3.0
Requires:       crate(web-sys-0.3/performance) >= 0.3.0
Requires:       crate(web-sys-0.3/performancetiming) >= 0.3.0
Requires:       crate(web-sys-0.3/window) >= 0.3.0
Provides:       crate(%{pkgname}/web-sys) = %{version}

%description -n %{name}+web-sys
This metapackage enables feature "web-sys" for the Rust instant crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
