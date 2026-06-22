# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name whoami
%global full_version 2.1.2
%global pkgname whoami-2

Name:           rust-whoami-2
Version:        2.1.2
Release:        %autorelease
Summary:        Rust crate "whoami"
License:        Apache-2.0 OR BSL-1.0 OR MIT
URL:            https://github.com/ardaku/whoami/releases
#!RemoteAsset:  sha256:998767ef88740d1f5b0682a9c53c24431453923962269c2db68ee43788c5a40d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/force-stub) = %{version}

%description
Source code for takopackized Rust crate "whoami"

%package     -n %{name}+default
Summary:        Getting information about the current user and environment - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/wasi-wasite) = %{version}
Requires:       crate(%{pkgname}/wasm-web) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust whoami crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Getting information about the current user and environment - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.186
Requires:       crate(libc-0.2/std) >= 0.2.186
Requires:       crate(libredox-0.1/call) >= 0.1.16
Requires:       crate(objc2-system-configuration-0.3/scdynamicstore) >= 0.3.2
Requires:       crate(objc2-system-configuration-0.3/scdynamicstorecopyspecific) >= 0.3.2
Requires:       crate(web-sys-0.3/document) >= 0.3.85
Requires:       crate(web-sys-0.3/location) >= 0.3.85
Requires:       crate(web-sys-0.3/navigator) >= 0.3.85
Requires:       crate(web-sys-0.3/std) >= 0.3.85
Requires:       crate(web-sys-0.3/window) >= 0.3.85
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust whoami crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasi-wasite
Summary:        Getting information about the current user and environment - feature "wasi-wasite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasite-1) >= 1.0.2
Provides:       crate(%{pkgname}/wasi-wasite) = %{version}

%description -n %{name}+wasi-wasite
This metapackage enables feature "wasi-wasite" for the Rust whoami crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-web
Summary:        Getting information about the current user and environment - feature "wasm-web"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(web-sys-0.3/document) >= 0.3.85
Requires:       crate(web-sys-0.3/location) >= 0.3.85
Requires:       crate(web-sys-0.3/navigator) >= 0.3.85
Requires:       crate(web-sys-0.3/window) >= 0.3.85
Provides:       crate(%{pkgname}/wasm-web) = %{version}

%description -n %{name}+wasm-web
This metapackage enables feature "wasm-web" for the Rust whoami crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
