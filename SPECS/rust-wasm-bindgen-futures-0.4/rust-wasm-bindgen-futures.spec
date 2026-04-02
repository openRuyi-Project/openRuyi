# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-futures
%global full_version 0.4.67
%global pkgname wasm-bindgen-futures-0.4

Name:           rust-wasm-bindgen-futures-0.4
Version:        0.4.67
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-futures"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:03623de6905b7206edd0a75f69f747f134b7f0a2323392d664448bf2d3c5d87e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3/futures) >= 0.3.94
Requires:       crate(wasm-bindgen-0.2) >= 0.2.117
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "wasm-bindgen-futures"

%package     -n %{name}+futures-core-03-stream
Summary:        Bridging the gap between Rust Futures and JavaScript Promises - feature "futures-core-03-stream"
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3/futures) >= 0.3.94
Requires:       crate(js-sys-0.3/futures-core-03-stream) >= 0.3.94
Provides:       crate(%{pkgname}/futures-core-03-stream)

%description -n %{name}+futures-core-03-stream
This metapackage enables feature "futures-core-03-stream" for the Rust wasm-bindgen-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bridging the gap between Rust Futures and JavaScript Promises - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3/futures) >= 0.3.94
Requires:       crate(js-sys-0.3/std) >= 0.3.94
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.117
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasm-bindgen-futures crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
