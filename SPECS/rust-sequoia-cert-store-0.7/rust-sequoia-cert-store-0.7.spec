# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-cert-store
%global full_version 0.7.6
%global pkgname sequoia-cert-store-0.7

Name:           rust-sequoia-cert-store-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "sequoia-cert-store"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:966d3841a6ea69325719c742b8123c7757d18f0f2d4f728ec7b15e849df3ba35
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(crossbeam-0.8/default) >= 0.8.1
Requires:       crate(dirs-5/default) >= 5.0.0
Requires:       crate(gethostname-0.4/default) >= 0.4.0
Requires:       crate(num-cpus-1/default) >= 1.0.0
Requires:       crate(openpgp-cert-d-0.3) >= 0.3.4
Requires:       crate(rayon-1/default) >= 1.0.0
Requires:       crate(rusqlite-0.29/blob) >= 0.29.0
Requires:       crate(rusqlite-0.29/bundled) >= 0.29.0
Requires:       crate(rusqlite-0.29/collation) >= 0.29.0
Requires:       crate(rusqlite-0.29/default) >= 0.29.0
Requires:       crate(rusqlite-0.29/trace) >= 0.29.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(smallvec-1/default) >= 1.1.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(url-2/default) >= 2.5.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sequoia-cert-store"

%package     -n %{name}+keyserver
Summary:        Certificate database interface - feature "keyserver" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-net-0.30) >= 0.30.0
Requires:       crate(tokio-1/default) >= 1.13.0
Requires:       crate(tokio-1/rt) >= 1.13.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/keyserver) = %{version}

%description -n %{name}+keyserver
This metapackage enables feature "keyserver" for the Rust sequoia-cert-store crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
