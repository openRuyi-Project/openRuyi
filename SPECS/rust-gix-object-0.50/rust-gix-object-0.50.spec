# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-object
%global full_version 0.50.2
%global pkgname gix-object-0.50

Name:           rust-gix-object-0.50
Version:        0.50.2
Release:        %autorelease
Summary:        Rust crate "gix-object"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:d69ce108ab67b65fbd4fb7e1331502429d78baeb2eee10008bdef55765397c07
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-actor-0.35/default) >= 0.35.4
Requires:       crate(gix-date-0.10/default) >= 0.10.5
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-path-0.10/default) >= 0.10.20
Requires:       crate(gix-utils-0.3/default) >= 0.3.0
Requires:       crate(gix-validate-0.10/default) >= 0.10.0
Requires:       crate(itoa-1/default) >= 1.0.1
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(smallvec-1/write) >= 1.15.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(winnow-0.7/default) >= 0.7.12
Requires:       crate(winnow-0.7/simd) >= 0.7.12
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-object"

%package     -n %{name}+document-features
Summary:        Immutable and mutable git objects with decoding and encoding support - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Immutable and mutable git objects with decoding and encoding support - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.12.0
Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-actor-0.35/serde) >= 0.35.4
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(serde-1/derive) >= 1.0.114
Requires:       crate(smallvec-1/serde) >= 1.15.1
Requires:       crate(smallvec-1/write) >= 1.15.1
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+verbose-object-parsing-errors
Summary:        Immutable and mutable git objects with decoding and encoding support - feature "verbose-object-parsing-errors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winnow-0.7/simd) >= 0.7.12
Requires:       crate(winnow-0.7/std) >= 0.7.12
Provides:       crate(%{pkgname}/verbose-object-parsing-errors) = %{version}

%description -n %{name}+verbose-object-parsing-errors
This metapackage enables feature "verbose-object-parsing-errors" for the Rust gix-object crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
