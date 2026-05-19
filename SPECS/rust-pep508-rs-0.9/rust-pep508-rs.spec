# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pep508_rs
%global full_version 0.9.2
%global pkgname pep508-rs-0.9

Name:           rust-pep508-rs-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "pep508_rs"
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://github.com/konstin/pep508_rs
#!RemoteAsset:  sha256:faee7227064121fcadcd2ff788ea26f0d8f2bd23a0574da11eca23bc935bcc05
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(boxcar-0.2/default) >= 0.2.14
Requires:       crate(indexmap-2.0/default) >= 2.14.0
Requires:       crate(itertools-0.13/default) >= 0.13.0
Requires:       crate(once-cell-1.0/default) >= 1.21.3
Requires:       crate(pep440-rs-0.7/default) >= 0.7.3
Requires:       crate(pep440-rs-0.7/version-ranges) >= 0.7.3
Requires:       crate(regex-1.0/default) >= 1.12.3
Requires:       crate(rustc-hash-2.0/default) >= 2.1.2
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-1.0/rc) >= 1.0.228
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-1.0/default) >= 1.0.69
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Requires:       crate(url-2.0/default) >= 2.5.8
Requires:       crate(url-2.0/serde) >= 2.5.8
Requires:       crate(urlencoding-2.0/default) >= 2.1.3
Requires:       crate(version-ranges-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/non-pep508-extensions)

%description
Source code for takopackized Rust crate "pep508_rs"

%package     -n %{name}+schemars
Summary:        Python dependency specifiers, better known as PEP 508 - feature "schemars"
Requires:       crate(%{pkgname})
Requires:       crate(schemars-0.8/default) >= 0.8.21
Provides:       crate(%{pkgname}/schemars)

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust pep508_rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Python dependency specifiers, better known as PEP 508 - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(pep440-rs-0.7/tracing) >= 0.7.3
Requires:       crate(pep440-rs-0.7/version-ranges) >= 0.7.3
Requires:       crate(tracing-0.1/default) >= 0.1.40
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust pep508_rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
