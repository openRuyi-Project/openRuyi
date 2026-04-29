# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name itertools
%global full_version 0.13.0
%global pkgname itertools-0.13

Name:           rust-itertools-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "itertools"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-itertools/itertools
#!RemoteAsset:  sha256:413ee7dfc52ee1a4949ceeb7dbc8a33f2d6c088194d9f922fb8318faf1f01186
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1.0) >= 1.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/use-alloc)

%description
Source code for takopackized Rust crate "itertools"

%package     -n %{name}+use-std
Summary:        Extra iterator adaptors, iterator methods, free functions, and macros - feature "use_std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/use-alloc)
Requires:       crate(either-1.0/use-std) >= 1.0.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/use-std)

%description -n %{name}+use-std
This metapackage enables feature "use_std" for the Rust itertools crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
