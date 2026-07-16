# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rquickjs-sys
%global full_version 0.8.1
%global pkgname rquickjs-sys-0.8

Name:           rust-rquickjs-sys-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "rquickjs-sys"
License:        MIT
URL:            https://github.com/DelSkayn/rquickjs.git
#!RemoteAsset:  sha256:4bc352c6b663604c3c186c000cfcc6c271f4b50bc135a285dd6d4f2a42f9790a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dump-atoms) = %{version}
Provides:       crate(%{pkgname}/dump-bytecode) = %{version}
Provides:       crate(%{pkgname}/dump-free) = %{version}
Provides:       crate(%{pkgname}/dump-gc) = %{version}
Provides:       crate(%{pkgname}/dump-gc-free) = %{version}
Provides:       crate(%{pkgname}/dump-leaks) = %{version}
Provides:       crate(%{pkgname}/dump-mem) = %{version}
Provides:       crate(%{pkgname}/dump-module-resolve) = %{version}
Provides:       crate(%{pkgname}/dump-objects) = %{version}
Provides:       crate(%{pkgname}/dump-promise) = %{version}
Provides:       crate(%{pkgname}/dump-read-object) = %{version}
Provides:       crate(%{pkgname}/dump-shapes) = %{version}

%description
Source code for takopackized Rust crate "rquickjs-sys"

%package     -n %{name}+bindgen-rs
Summary:        QuickJS bindings for rquickjs - feature "bindgen-rs" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.69/default) >= 0.69.0
Provides:       crate(%{pkgname}/bindgen) = %{version}
Provides:       crate(%{pkgname}/bindgen-rs) = %{version}
Provides:       crate(%{pkgname}/update-bindings) = %{version}

%description -n %{name}+bindgen-rs
This metapackage enables feature "bindgen-rs" for the Rust rquickjs-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bindgen", and "update-bindings" features.

%package     -n %{name}+pretty-env-logger
Summary:        QuickJS bindings for rquickjs - feature "pretty_env_logger" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pretty-env-logger-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/logging) = %{version}
Provides:       crate(%{pkgname}/pretty-env-logger) = %{version}

%description -n %{name}+pretty-env-logger
This metapackage enables feature "pretty_env_logger" for the Rust rquickjs-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
