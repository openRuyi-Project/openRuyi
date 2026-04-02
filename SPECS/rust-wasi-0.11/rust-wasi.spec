# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasi
%global full_version 0.11.1+wasi-snapshot-preview1
%global pkgname wasi-0.11

Name:           rust-wasi-0.11
Version:        0.11.1
Release:        %autorelease
Summary:        Rust crate "wasi"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasi
#!RemoteAsset:  sha256:ccf3ec651a847eb01de73ccad15eb7d99f80485de043efb2f370cd654f4ea44b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "wasi"

%package     -n %{name}+core
Summary:        Experimental WASI API bindings for Rust - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust wasi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Experimental WASI API bindings for Rust - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/core)
Requires:       crate(%{pkgname}/rustc-std-workspace-alloc)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust wasi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-std-workspace-alloc
Summary:        Experimental WASI API bindings for Rust - feature "rustc-std-workspace-alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustc-std-workspace-alloc)

%description -n %{name}+rustc-std-workspace-alloc
This metapackage enables feature "rustc-std-workspace-alloc" for the Rust wasi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
