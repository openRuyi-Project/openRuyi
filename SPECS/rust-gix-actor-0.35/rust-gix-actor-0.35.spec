# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-actor
%global full_version 0.35.6
%global pkgname gix-actor-0.35

Name:           rust-gix-actor-0.35
Version:        0.35.6
Release:        %autorelease
Summary:        Rust crate "gix-actor"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:987a51a7e66db6ef4dc030418eb2a42af6b913a79edd8670766122d8af3ba59e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-date-0.10/default) >= 0.10.7
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(itoa-1/default) >= 1.0.1
Requires:       crate(thiserror-2/default) >= 2.0.17
Requires:       crate(winnow-0.7/default) >= 0.7.12
Requires:       crate(winnow-0.7/simd) >= 0.7.12
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-actor"

%package     -n %{name}+document-features
Summary:        Way to identify git actors - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-actor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Way to identify git actors - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.12.0
Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-date-0.10/serde) >= 0.10.7
Requires:       crate(serde-1/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-actor crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
