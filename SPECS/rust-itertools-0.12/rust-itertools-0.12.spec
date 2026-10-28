# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name itertools
%global full_version 0.12.1
%global pkgname itertools-0.12

Name:           rust-itertools-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "itertools"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-itertools/itertools
#!RemoteAsset:  sha256:ba291022dbbd398a455acf126c1e341954079855bc60dfdda641363bd6922569
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/use-alloc) = %{version}

%description
Source code for takopackized Rust crate "itertools"

%package     -n %{name}+use-std
Summary:        Extra iterator adaptors, iterator methods, free functions, and macros - feature "use_std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/use-alloc) = %{version}
Requires:       crate(either-1/use-std) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description -n %{name}+use-std
This metapackage enables feature "use_std" for the Rust itertools crate,
by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
