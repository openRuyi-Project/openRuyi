# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_spanned
%global full_version 1.0.4
%global pkgname serde-spanned-1.0

Name:           rust-serde-spanned-1.0
Version:        1.0.4
Release:        %autorelease
Summary:        Rust crate "serde_spanned"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:f8bbf91e5a4d6315eee45e704372590b30e260ee83af6639d64557f51b067776
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "serde_spanned"

%package     -n %{name}+alloc
Summary:        Serde-compatible spanned Value - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Serde-compatible spanned Value - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Serde-compatible spanned Value - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Serde-compatible spanned Value - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(serde-core-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
