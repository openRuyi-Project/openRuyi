# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordered-multimap
%global full_version 0.7.3
%global pkgname ordered-multimap-0.7

Name:           rust-ordered-multimap-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "ordered-multimap"
License:        MIT
URL:            https://github.com/sgodwincs/ordered-multimap-rs
#!RemoteAsset:  sha256:49203cdcae0030493bad186b28da2fa25645fa276a51b6fec8010d281e02ef79
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dlv-list-0.5) >= 0.5.0
Requires:       crate(hashbrown-0.14) >= 0.14.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ordered-multimap"

%package     -n %{name}+serde
Summary:        Insertion ordered multimap - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ordered-multimap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Insertion ordered multimap - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dlv-list-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ordered-multimap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
