# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cc-traits
%global full_version 2.0.0
%global pkgname cc-traits-2

Name:           rust-cc-traits-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "cc-traits"
License:        MIT OR Apache-2.0
URL:            https://github.com/timothee-haudebourg/cc-traits
#!RemoteAsset:  sha256:060303ef31ef4a522737e1b1ab68c67916f2a787bb2f4f54f383279adba962b5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "cc-traits"

%package     -n %{name}+slab
Summary:        Common collection traits - feature "slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slab-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}/slab) = %{version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust cc-traits crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Common collection traits - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.6.0

Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust cc-traits crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
