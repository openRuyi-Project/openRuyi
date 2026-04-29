# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getrandom
%global full_version 0.2.17
%global pkgname getrandom-0.2

Name:           rust-getrandom-0.2
Version:        0.2.17
Release:        %autorelease
Summary:        Rust crate "getrandom"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-random/getrandom
#!RemoteAsset:  sha256:ff2abc00be7fca6ebc474524697ae276ad847ad0a6b3faa4bcb027e9a4614ad0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2) >= 0.2.184
Requires:       crate(wasi-0.11) >= 0.11.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/custom)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/linux-disable-fallback)
Provides:       crate(%{pkgname}/rdrand)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/test-in-browser)

%description
Source code for takopackized Rust crate "getrandom"

%package     -n %{name}+compiler-builtins
Summary:        Small cross-platform library for retrieving random data from system source - feature "compiler_builtins"
Requires:       crate(%{pkgname})
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/compiler-builtins)

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Small cross-platform library for retrieving random data from system source - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js
Summary:        Small cross-platform library for retrieving random data from system source - feature "js"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/js-sys)
Requires:       crate(%{pkgname}/wasm-bindgen)
Provides:       crate(%{pkgname}/js)

%description -n %{name}+js
This metapackage enables feature "js" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js-sys
Summary:        Small cross-platform library for retrieving random data from system source - feature "js-sys"
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/js-sys)

%description -n %{name}+js-sys
This metapackage enables feature "js-sys" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Small cross-platform library for retrieving random data from system source - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compiler-builtins)
Requires:       crate(%{pkgname}/core)
Requires:       crate(libc-0.2/rustc-dep-of-std) >= 0.2.184
Requires:       crate(wasi-0.11/rustc-dep-of-std) >= 0.11.1
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Small cross-platform library for retrieving random data from system source - feature "wasm-bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(wasm-bindgen-0.2) >= 0.2.62
Provides:       crate(%{pkgname}/wasm-bindgen)

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
