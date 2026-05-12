# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasip2
%global full_version 1.0.2+wasi-0.2.9
%global pkgname wasip2-1.0

Name:           rust-wasip2-1.0
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "wasip2"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasi-rs
#!RemoteAsset:  sha256:9517f9239f02c069db75e65f174b3da828fe5f5b945c4dd26bd25d89c03ebcf5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(wit-bindgen-0.51) >= 0.51.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "wasip2"

%package     -n %{name}+alloc
Summary:        WASIp2 API bindings for Rust - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        WASIp2 API bindings for Rust - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(wit-bindgen-0.51/bitflags) >= 0.51.0
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        WASIp2 API bindings for Rust - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        WASIp2 API bindings for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        WASIp2 API bindings for Rust - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/core)
Requires:       crate(wit-bindgen-0.51/rustc-dep-of-std) >= 0.51.0
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
