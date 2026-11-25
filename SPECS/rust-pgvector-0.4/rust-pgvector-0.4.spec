# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pgvector
%global full_version 0.4.1
%global pkgname pgvector-0.4

Name:           rust-pgvector-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "pgvector"
License:        MIT OR Apache-2.0
URL:            https://github.com/pgvector/pgvector-rust
#!RemoteAsset:  sha256:fc58e2d255979a31caa7cabfa7aac654af0354220719ab7a68520ae7a91e8c0b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pgvector"

%package     -n %{name}+diesel
Summary:        Pgvector support for Rust - feature "diesel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(diesel-2/postgres) >= 2.0.0
Provides:       crate(%{pkgname}/diesel) = %{version}

%description -n %{name}+diesel
This metapackage enables feature "diesel" for the Rust pgvector crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+halfvec
Summary:        Pgvector support for Rust - feature "halfvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(half-2) >= 2.0.0
Provides:       crate(%{pkgname}/halfvec) = %{version}

%description -n %{name}+halfvec
This metapackage enables feature "halfvec" for the Rust pgvector crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres
Summary:        Pgvector support for Rust - feature "postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(postgres-types-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/postgres) = %{version}

%description -n %{name}+postgres
This metapackage enables feature "postgres" for the Rust pgvector crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pgvector support for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pgvector crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx
Summary:        Pgvector support for Rust - feature "sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.8/postgres) >= 0.8.0
Provides:       crate(%{pkgname}/sqlx) = %{version}

%description -n %{name}+sqlx
This metapackage enables feature "sqlx" for the Rust pgvector crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
