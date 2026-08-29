# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minicbor
%global full_version 0.19.1
%global pkgname minicbor-0.19

Name:           rust-minicbor-0.19
Version:        0.19.1
Release:        %autorelease
Summary:        Rust crate "minicbor"
License:        BlueOak-1.0.0
URL:            https://gitlab.com/twittner/minicbor
#!RemoteAsset:  sha256:d7005aaf257a59ff4de471a9d5538ec868a21586534fff7f85dd97d4043a6139
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "minicbor"

%package     -n %{name}+alloc
Summary:        Small CBOR codec suitable for no_std environments - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(minicbor-derive-0.13/alloc) >= 0.13.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust minicbor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+half
Summary:        Small CBOR codec suitable for no_std environments - feature "half"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(half-1) >= 1.0.0
Provides:       crate(%{pkgname}/half) = %{version}

%description -n %{name}+half
This metapackage enables feature "half" for the Rust minicbor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+minicbor-derive
Summary:        Small CBOR codec suitable for no_std environments - feature "minicbor-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(minicbor-derive-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/minicbor-derive) = %{version}

%description -n %{name}+minicbor-derive
This metapackage enables feature "minicbor-derive" for the Rust minicbor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+std
Summary:        Small CBOR codec suitable for no_std environments - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(minicbor-derive-0.13/std) >= 0.13.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust minicbor crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
