# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-query-derive
%global full_version 1.0.0
%global pkgname sea-query-derive-1

Name:           rust-sea-query-derive-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "sea-query-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/SeaQL/sea-query
#!RemoteAsset:  sha256:a0b0f466921cdd3cf4b89d5c3ac2173dba89a873ab395b123a645de181ec7537
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/sea-orm) = %{version}

%description
Source code for takopackized Rust crate "sea-query-derive"

%package     -n %{name}+darling
Summary:        Derive macro for sea-query's Iden trait - feature "darling"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(darling-0.20) >= 0.20.0
Provides:       crate(%{pkgname}/darling) = %{version}

%description -n %{name}+darling
This metapackage enables feature "darling" for the Rust sea-query-derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heck
Summary:        Derive macro for sea-query's Iden trait - feature "heck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heck-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/heck) = %{version}

%description -n %{name}+heck
This metapackage enables feature "heck" for the Rust sea-query-derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sea-query
Summary:        Derive macro for sea-query's Iden trait - feature "sea-query" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/darling) = %{version}
Requires:       crate(%{pkgname}/heck) = %{version}
Requires:       crate(%{pkgname}/thiserror) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/sea-query) = %{version}

%description -n %{name}+sea-query
This metapackage enables feature "sea-query" for the Rust sea-query-derive crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+thiserror
Summary:        Derive macro for sea-query's Iden trait - feature "thiserror"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thiserror-2) >= 2.0.0
Provides:       crate(%{pkgname}/thiserror) = %{version}

%description -n %{name}+thiserror
This metapackage enables feature "thiserror" for the Rust sea-query-derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
