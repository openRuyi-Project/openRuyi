# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio_with_wasm
%global full_version 0.8.8
%global pkgname tokio-with-wasm-0.8

Name:           rust-tokio-with-wasm-0.8
Version:        0.8.8
Release:        %autorelease
Summary:        Rust crate "tokio_with_wasm"
License:        MIT
URL:            https://github.com/cunarist/tokio-with-wasm
#!RemoteAsset:  sha256:34e40fbbbd95441133fe9483f522db15dbfd26dc636164ebd8f2dd28759a6aa6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3/default) >= 0.3.70
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-with-wasm-proc-0.8/default) >= 0.8.8
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.95
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.45
Requires:       crate(web-sys-0.3/blob) >= 0.3.70
Requires:       crate(web-sys-0.3/blobpropertybag) >= 0.3.70
Requires:       crate(web-sys-0.3/dedicatedworkerglobalscope) >= 0.3.70
Requires:       crate(web-sys-0.3/default) >= 0.3.70
Requires:       crate(web-sys-0.3/errorevent) >= 0.3.70
Requires:       crate(web-sys-0.3/messageevent) >= 0.3.70
Requires:       crate(web-sys-0.3/url) >= 0.3.70
Requires:       crate(web-sys-0.3/worker) >= 0.3.70
Requires:       crate(web-sys-0.3/workeroptions) >= 0.3.70
Requires:       crate(web-sys-0.3/workertype) >= 0.3.70

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rt) = %{version}
Provides:       crate(%{pkgname}/rt-multi-thread) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}

%patchlist
# Express the Tokio major-1 requirement as an equivalent caret range.
2000-Normalize-the-Tokio-major-version-requirement.patch

%description
Source code for takopackized Rust crate "tokio_with_wasm"

%package     -n %{name}+full
Summary:        Mimicking tokio functionalities on web browsers - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/rt) = %{version}
Requires:       crate(%{pkgname}/rt-multi-thread) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tokio_with_wasm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Mimicking tokio functionalities on web browsers - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/macros) >= 1.0.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust tokio_with_wasm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sync
Summary:        Mimicking tokio functionalities on web browsers - feature "sync"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/sync) >= 1.0.0
Provides:       crate(%{pkgname}/sync) = %{version}

%description -n %{name}+sync
This metapackage enables feature "sync" for the Rust tokio_with_wasm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
