# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ring
%global full_version 0.17.14
%global pkgname ring-0.17

Name:           rust-ring-0.17
Version:        0.17.14
Release:        %autorelease
Summary:        Rust crate "ring"
License:        Apache-2.0 AND ISC
URL:            https://github.com/briansmith/ring
#!RemoteAsset:  sha256:a4689e6c2294d81e88dc6261c768b63bc4fcdb852be6d1352498b114f61383b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.2.8
Requires:       crate(cfg-if-1) >= 1.0.0
Requires:       crate(getrandom-0.2/default) >= 0.2.10
Requires:       crate(libc-0.2) >= 0.2.148
Requires:       crate(untrusted-0.9/default) >= 0.9.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-threading) >= 0.52.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/dev-urandom-fallback) = %{version}
Provides:       crate(%{pkgname}/less-safe-getrandom-custom-or-rdrand) = %{version}
Provides:       crate(%{pkgname}/less-safe-getrandom-espidf) = %{version}
Provides:       crate(%{pkgname}/slow-tests) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/test-logging) = %{version}
Provides:       crate(%{pkgname}/unstable-testing-arm-no-hw) = %{version}
Provides:       crate(%{pkgname}/unstable-testing-arm-no-neon) = %{version}

%description
Source code for takopackized Rust crate "ring"

%package     -n %{name}+default
Summary:        Experiment - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/dev-urandom-fallback) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm32-unknown-unknown-js
Summary:        Experiment - feature "wasm32_unknown_unknown_js"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.2/js) >= 0.2.10
Provides:       crate(%{pkgname}/wasm32-unknown-unknown-js) = %{version}

%description -n %{name}+wasm32-unknown-unknown-js
This metapackage enables feature "wasm32_unknown_unknown_js" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
