# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordermap
%global full_version 1.2.0
%global pkgname ordermap-1.0

Name:           rust-ordermap-1.0
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "ordermap"
License:        Apache-2.0 OR MIT
URL:            https://github.com/indexmap-rs/ordermap
#!RemoteAsset:  sha256:7f7476a5b122ff1fce7208e7ee9dccd0a516e835f5b8b19b8f3c98a34cf757c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2.0) >= 2.14.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "ordermap"

%package     -n %{name}+arbitrary
Summary:        Hash table with consistent order and fast iteration - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0) >= 1.0.0
Requires:       crate(indexmap-2.0/arbitrary) >= 2.14.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh
Summary:        Hash table with consistent order and fast iteration - feature "borsh"
Requires:       crate(%{pkgname})
Requires:       crate(borsh-1.0) >= 1.5.6
Requires:       crate(borsh-1.0/indexmap) >= 1.5.6
Provides:       crate(%{pkgname}/borsh)

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Hash table with consistent order and fast iteration - feature "quickcheck"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/quickcheck) >= 2.14.0
Requires:       crate(quickcheck-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Hash table with consistent order and fast iteration - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/rayon) >= 2.14.0
Requires:       crate(rayon-1.0/default) >= 1.9
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hash table with consistent order and fast iteration - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/serde) >= 2.14.0
Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-core-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Hash table with consistent order and fast iteration - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/std) >= 2.14.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+sval
Summary:        Hash table with consistent order and fast iteration - feature "sval"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/sval) >= 2.14.0
Requires:       crate(sval-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/sval)

%description -n %{name}+sval
This metapackage enables feature "sval" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
