# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indexmap
%global full_version 2.13.0
%global pkgname indexmap-2.0

Name:           rust-indexmap-2.0
Version:        2.13.0
Release:        %autorelease
Summary:        Rust crate "indexmap"
License:        Apache-2.0 OR MIT
URL:            https://github.com/indexmap-rs/indexmap
#!RemoteAsset:  sha256:7714e70437a7dc3ac8eb7e6f8df75fd8eb422675fc7678aff7364301092b1017
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(equivalent-1.0) >= 1.0.2
Requires:       crate(hashbrown-0.16) >= 0.16.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/test-debug)

%description
Source code for takopackized Rust crate "indexmap"

%package     -n %{name}+arbitrary
Summary:        Hash table with consistent order and fast iteration - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh
Summary:        Hash table with consistent order and fast iteration - feature "borsh"
Requires:       crate(%{pkgname})
Requires:       crate(borsh-1.0) >= 1.2
Provides:       crate(%{pkgname}/borsh)

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Hash table with consistent order and fast iteration - feature "quickcheck"
Requires:       crate(%{pkgname})
Requires:       crate(quickcheck-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Hash table with consistent order and fast iteration - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.9
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hash table with consistent order and fast iteration - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-core-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sval
Summary:        Hash table with consistent order and fast iteration - feature "sval"
Requires:       crate(%{pkgname})
Requires:       crate(sval-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/sval)

%description -n %{name}+sval
This metapackage enables feature "sval" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
