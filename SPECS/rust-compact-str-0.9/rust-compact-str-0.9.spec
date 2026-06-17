# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name compact_str
%global full_version 0.9.0
%global pkgname compact-str-0.9

Name:           rust-compact-str-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "compact_str"
License:        MIT
URL:            https://github.com/ParkMyCar/compact_str
#!RemoteAsset:  sha256:3fdb1325a1cece981e8a296ab8f0f9b63ae357bd0784a9faaf548cc7b480707a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(castaway-0.2/alloc) >= 0.2.3
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(rustversion-1/default) >= 1.0.0
Requires:       crate(ryu-1/default) >= 1.0.0
Requires:       crate(static-assertions-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "compact_str"

%package     -n %{name}+arbitrary
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "borsh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borsh-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/borsh) = %{version}

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diesel
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "diesel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(diesel-2) >= 2.0.0
Provides:       crate(%{pkgname}/diesel) = %{version}

%description -n %{name}+diesel
This metapackage enables feature "diesel" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+markup
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "markup"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(markup-0.15) >= 0.15.0
Provides:       crate(%{pkgname}/markup) = %{version}

%description -n %{name}+markup
This metapackage enables feature "markup" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "proptest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/proptest) = %{version}

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-1) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.0.0
Requires:       crate(smallvec-1/union) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(sqlx-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/sqlx) = %{version}

%description -n %{name}+sqlx
This metapackage enables feature "sqlx" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-mysql
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "sqlx-mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx) = %{version}
Requires:       crate(sqlx-0.8/mysql) >= 0.8.0
Provides:       crate(%{pkgname}/sqlx-mysql) = %{version}

%description -n %{name}+sqlx-mysql
This metapackage enables feature "sqlx-mysql" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-postgres
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "sqlx-postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx) = %{version}
Requires:       crate(sqlx-0.8/postgres) >= 0.8.0
Provides:       crate(%{pkgname}/sqlx-postgres) = %{version}

%description -n %{name}+sqlx-postgres
This metapackage enables feature "sqlx-postgres" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-sqlite
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "sqlx-sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx) = %{version}
Requires:       crate(sqlx-0.8/sqlite) >= 0.8.0
Provides:       crate(%{pkgname}/sqlx-sqlite) = %{version}

%description -n %{name}+sqlx-sqlite
This metapackage enables feature "sqlx-sqlite" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Memory efficient string type that transparently stores strings on the stack, when possible - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust compact_str crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
