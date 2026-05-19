# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pep440_rs
%global full_version 0.7.3
%global pkgname pep440-rs-0.7

Name:           rust-pep440-rs-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "pep440_rs"
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://github.com/konstin/pep440-rs
#!RemoteAsset:  sha256:31095ca1f396e3de32745f42b20deef7bc09077f918b085307e8eab6ddd8fb9c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1.0/default) >= 1.21.3
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Requires:       crate(unscanny-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "pep440_rs"

%package     -n %{name}+rkyv
Summary:        Python version numbers and specifiers, implementing PEP 440 - feature "rkyv"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.8/default) >= 0.8.9
Provides:       crate(%{pkgname}/rkyv)

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust pep440_rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Python version numbers and specifiers, implementing PEP 440 - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1/default) >= 0.1.40
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust pep440_rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+version-ranges
Summary:        Python version numbers and specifiers, implementing PEP 440 - feature "version-ranges"
Requires:       crate(%{pkgname})
Requires:       crate(version-ranges-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/version-ranges)

%description -n %{name}+version-ranges
This metapackage enables feature "version-ranges" for the Rust pep440_rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
