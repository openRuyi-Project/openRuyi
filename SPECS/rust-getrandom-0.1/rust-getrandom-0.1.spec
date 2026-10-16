# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getrandom
%global full_version 0.1.16
%global pkgname getrandom-0.1

Name:           rust-getrandom-0.1
Version:        0.1.16
Release:        %autorelease
Summary:        Rust crate "getrandom"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-random/getrandom
#!RemoteAsset:  sha256:8fc3cb4d91f53b50155bdcfd23f6a4c39ae1969c2ae85982b135750cccaf5fce
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2) >= 0.2.64
Requires:       crate(wasi-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dummy) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "getrandom"

%package     -n %{name}+bindgen
Summary:        Small cross-platform library for retrieving random data from system source - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.29
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiler-builtins
Summary:        Small cross-platform library for retrieving random data from system source - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js-sys
Summary:        Small cross-platform library for retrieving random data from system source - feature "js-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/js-sys) = %{version}

%description -n %{name}+js-sys
This metapackage enables feature "js-sys" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Small cross-platform library for retrieving random data from system source - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Small cross-platform library for retrieving random data from system source - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiler-builtins) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stdweb
Summary:        Small cross-platform library for retrieving random data from system source - feature "stdweb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stdweb-0.4/default) >= 0.4.18
Provides:       crate(%{pkgname}/stdweb) = %{version}

%description -n %{name}+stdweb
This metapackage enables feature "stdweb" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Small cross-platform library for retrieving random data from system source - feature "wasm-bindgen" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Requires:       crate(%{pkgname}/js-sys) = %{version}
Provides:       crate(%{pkgname}/test-in-browser) = %{version}
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "test-in-browser" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
