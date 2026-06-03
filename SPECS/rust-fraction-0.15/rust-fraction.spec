# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
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

Requires:       crate(num-0.4) >= 0.4.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/with-decimal)
Provides:       crate(%{pkgname}/with-dynaint)
Provides:       crate(%{pkgname}/with-unicode)

%description
Source code for takopackized Rust crate "fraction"

%package     -n %{name}+byteorder
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "byteorder"
Requires:       crate(%{pkgname})
Requires:       crate(byteorder-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/byteorder)

%description -n %{name}+byteorder
This metapackage enables feature "byteorder" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/with-bigint)
Requires:       crate(%{pkgname}/with-decimal)
Requires:       crate(%{pkgname}/with-dynaint)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lazy-static
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "lazy_static"
Requires:       crate(%{pkgname})
Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Provides:       crate(%{pkgname}/lazy-static)

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "serde_derive"
Requires:       crate(%{pkgname})
Requires:       crate(serde-derive-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-derive)

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-bigint
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "with-bigint" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/lazy-static)
Requires:       crate(num-0.4/num-bigint) >= 0.4.3
Requires:       crate(num-0.4/std) >= 0.4.3
Provides:       crate(%{pkgname}/with-approx)
Provides:       crate(%{pkgname}/with-bigint)

%description -n %{name}+with-bigint
This metapackage enables feature "with-bigint" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-approx" feature.

%package     -n %{name}+with-serde-support
Summary:        Lossless fractions and decimals; drop-in float replacement - feature "with-serde-support"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/serde-derive)
Requires:       crate(num-0.4/serde) >= 0.4.3
Provides:       crate(%{pkgname}/with-serde-support)

%description -n %{name}+with-serde-support
This metapackage enables feature "with-serde-support" for the Rust fraction crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
