# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-futures
%global full_version 0.4.78
%global pkgname wasm-bindgen-futures-0.4

Name:           rust-wasm-bindgen-futures-0.4
Version:        0.4.78
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-futures"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:6ef4c5d3d2cdf5c54f4231181768f5510842e350db025faf1f7163b1030ed928
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3) >= 0.3.105
Requires:       crate(wasm-bindgen-0.2) >= 0.2.128

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "wasm-bindgen-futures"

%package     -n %{name}+futures-core-03-stream
Summary:        Bridging the gap between Rust Futures and JavaScript Promises - feature "futures-core-03-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/futures-core-03-stream) >= 0.3.105
Provides:       crate(%{pkgname}/futures-core-03-stream) = %{version}

%description -n %{name}+futures-core-03-stream
This metapackage enables feature "futures-core-03-stream" for the Rust wasm-bindgen-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bridging the gap between Rust Futures and JavaScript Promises - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/std) >= 0.3.105
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.128
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasm-bindgen-futures crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
