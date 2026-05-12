# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libc
%global full_version 0.2.183
%global pkgname libc-0.2

Name:           rust-libc-0.2
Version:        0.2.183
Release:        %autorelease
Summary:        Rust crate "libc"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/libc
#!RemoteAsset:  sha256:b5b646652bf6661599e1da8901b3b9522896f01e736bad5f723fe7a3a27f899d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/align)
Provides:       crate(%{pkgname}/const-extern-fn)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/extra-traits)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/use-std)

%description
Source code for takopackized Rust crate "libc"

%package     -n %{name}+rustc-dep-of-std
Summary:        Raw FFI bindings to platform libraries like libc - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/align)
Requires:       crate(%{pkgname}/rustc-std-workspace-core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust libc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-std-workspace-core
Summary:        Raw FFI bindings to platform libraries like libc - feature "rustc-std-workspace-core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname}/rustc-std-workspace-core)

%description -n %{name}+rustc-std-workspace-core
This metapackage enables feature "rustc-std-workspace-core" for the Rust libc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
