# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0) >= 1.2.58
Requires:       crate(cfg-if-1.0) >= 1.0.4
Requires:       crate(getrandom-0.2/default) >= 0.2.17
Requires:       crate(libc-0.2) >= 0.2.184
Requires:       crate(untrusted-0.9/default) >= 0.9.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-threading) >= 0.52.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/dev-urandom-fallback)
Provides:       crate(%{pkgname}/less-safe-getrandom-custom-or-rdrand)
Provides:       crate(%{pkgname}/less-safe-getrandom-espidf)
Provides:       crate(%{pkgname}/slow-tests)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/test-logging)
Provides:       crate(%{pkgname}/unstable-testing-arm-no-hw)
Provides:       crate(%{pkgname}/unstable-testing-arm-no-neon)

%description
Source code for takopackized Rust crate "ring"

%package     -n %{name}+default
Summary:        Experiment - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/dev-urandom-fallback)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm32-unknown-unknown-js
Summary:        Experiment - feature "wasm32_unknown_unknown_js"
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.2/js) >= 0.2.17
Provides:       crate(%{pkgname}/wasm32-unknown-unknown-js)

%description -n %{name}+wasm32-unknown-unknown-js
This metapackage enables feature "wasm32_unknown_unknown_js" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
