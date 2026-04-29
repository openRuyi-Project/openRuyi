# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
%global __debug_install_post %{nil}

%global crate_name hermit-abi
%global full_version 0.5.2
%global pkgname hermit-abi-0.5

Name:           rust-hermit-abi-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "hermit-abi"
License:        MIT OR Apache-2.0
URL:            https://github.com/hermit-os/hermit-rs
#!RemoteAsset:  sha256:fc0fef456e4baa96da950455cd02c081ca953b141298e41db3fc7e36b1da849c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "hermit-abi"

%package     -n %{name}+alloc
Summary:        Hermit system calls definitions - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust hermit-abi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Hermit system calls definitions - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust hermit-abi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Hermit system calls definitions - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust hermit-abi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
