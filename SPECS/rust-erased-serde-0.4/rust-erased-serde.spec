# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name erased-serde
%global full_version 0.4.10
%global pkgname erased-serde-0.4

Name:           rust-erased-serde-0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Rust crate "erased-serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/erased-serde
#!RemoteAsset:  sha256:d2add8a07dd6a8d93ff627029c51de145e12686fbc36ecb298ac22e74cf02dec
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-core-1.0) >= 1.0.228
Requires:       crate(typeid-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable-debug)

%description
Source code for takopackized Rust crate "erased-serde"

%package     -n %{name}+alloc
Summary:        Type-erased Serialize and Serializer traits - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust erased-serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Type-erased Serialize and Serializer traits - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(serde-core-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust erased-serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
