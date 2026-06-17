# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vmm-sys-util
%global full_version 0.15.0
%global pkgname vmm-sys-util-0.15

Name:           rust-vmm-sys-util-0.15
Version:        0.15.0
Release:        %autorelease
Summary:        Rust crate "vmm-sys-util"
License:        BSD-3-Clause
URL:            https://github.com/rust-vmm/vmm-sys-util
#!RemoteAsset:  sha256:506c62fdf617a5176827c2f9afbcf1be155b03a9b4bf9617a60dbc07e3a1642f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.127
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vmm-sys-util"

%package     -n %{name}+serde
Summary:        System utility set - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.27
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust vmm-sys-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        System utility set - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.27
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust vmm-sys-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-serde
Summary:        System utility set - feature "with-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+with-serde
This metapackage enables feature "with-serde" for the Rust vmm-sys-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
