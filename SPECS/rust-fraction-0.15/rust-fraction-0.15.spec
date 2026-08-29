# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fraction
%global full_version 0.15.3
%global pkgname fraction-0.15

Name:           rust-fraction-0.15
Version:        0.15.3
Release:        %autorelease
Summary:        Rust crate "fraction"
License:        MIT OR Apache-2.0
URL:            https://github.com/dnsl48/fraction.git
#!RemoteAsset:  sha256:0f158e3ff0a1b334408dc9fb811cd99b446986f4d8b741bb08f9df1604085ae7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-0.4) >= 0.4.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/with-decimal) = %{version}
Provides:       crate(%{pkgname}/with-dynaint) = %{version}
Provides:       crate(%{pkgname}/with-unicode) = %{version}

%description
Source code for takopackized Rust crate "fraction"

%package     -n %{name}+byteorder
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "byteorder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(byteorder-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/byteorder) = %{version}

%description -n %{name}+byteorder
This metapackage enables feature "byteorder" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/with-bigint) = %{version}
Requires:       crate(%{pkgname}/with-decimal) = %{version}
Requires:       crate(%{pkgname}/with-dynaint) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+juniper
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "juniper" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(juniper-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/juniper) = %{version}
Provides:       crate(%{pkgname}/with-juniper-support) = %{version}

%description -n %{name}+juniper
This metapackage enables feature "juniper" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-juniper-support" feature.

%package     -n %{name}+lazy-static
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "lazy_static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/lazy-static) = %{version}

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres-types
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "postgres-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(postgres-types-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/postgres-types) = %{version}

%description -n %{name}+postgres-types
This metapackage enables feature "postgres-types" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-bigint
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "with-bigint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lazy-static) = %{version}
Requires:       crate(num-0.4/num-bigint) >= 0.4.2
Requires:       crate(num-0.4/std) >= 0.4.2
Provides:       crate(%{pkgname}/with-approx) = %{version}
Provides:       crate(%{pkgname}/with-bigint) = %{version}

%description -n %{name}+with-bigint
This metapackage enables feature "with-bigint" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-approx" feature.

%package     -n %{name}+with-postgres-support
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "with-postgres-support"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/byteorder) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/postgres-types) = %{version}
Provides:       crate(%{pkgname}/with-postgres-support) = %{version}

%description -n %{name}+with-postgres-support
This metapackage enables feature "with-postgres-support" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-serde-support
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "with-serde-support"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Requires:       crate(num-0.4/serde) >= 0.4.2
Provides:       crate(%{pkgname}/with-serde-support) = %{version}

%description -n %{name}+with-serde-support
This metapackage enables feature "with-serde-support" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
