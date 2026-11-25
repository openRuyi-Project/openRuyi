# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phc
%global full_version 0.6.1
%global pkgname phc-0.6

Name:           rust-phc-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "phc"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats
#!RemoteAsset:  sha256:44dc769b75f93afdddd8c7fa12d685292ddeff1e66f7f0f3a234cf1818afe892
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64ct-1/default) >= 1.7.0
Requires:       crate(ctutils-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "phc"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Password Hashing Competition (PHC) string format which is used for storing password hashes - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1/alloc) >= 1.7.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust phc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the Password Hashing Competition (PHC) string format which is used for storing password hashes - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust phc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of the Password Hashing Competition (PHC) string format which is used for storing password hashes - feature "rand_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust phc crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
