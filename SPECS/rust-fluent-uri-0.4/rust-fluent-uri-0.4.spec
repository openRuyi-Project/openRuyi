# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fluent-uri
%global full_version 0.4.1
%global pkgname fluent-uri-0.4

Name:           rust-fluent-uri-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "fluent-uri"
License:        MIT
URL:            https://github.com/yescallop/fluent-uri-rs
#!RemoteAsset:  sha256:bc74ac4d8359ae70623506d512209619e5cf8f347124910440dbc221714b328e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(borrow-or-share-0.2) >= 0.2.4
Requires:       crate(ref-cast-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/impl-error) = %{version}
Provides:       crate(%{pkgname}/net) = %{version}

%description
Source code for takopackized Rust crate "fluent-uri"

%package     -n %{name}+alloc
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borrow-or-share-0.2/alloc) >= 0.2.4
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust fluent-uri crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust fluent-uri crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987 - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/impl-error) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust fluent-uri crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
