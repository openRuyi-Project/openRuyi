# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name password-hash
%global full_version 0.6.1
%global pkgname password-hash-0.6

Name:           rust-password-hash-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "password-hash"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:aab41826031698d6ffcd9cff78ef56ef998e39dc7e5067cdfebe373842d4723b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Modular Crypt Format)
Source code for takopackized Rust crate "password-hash"

%package     -n %{name}+alloc
Summary:        Traits which describe the functionality of password hashing algorithms, with optional support for a `no_std`/`no_alloc`-friendly implementation of the PHC string format, as well as generic support for other formats (e.g - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phc-0.6/alloc) >= 0.6.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
Modular Crypt Format)
This metapackage enables feature "alloc" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Traits which describe the functionality of password hashing algorithms, with optional support for a `no_std`/`no_alloc`-friendly implementation of the PHC string format, as well as generic support for other formats (e.g - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4) >= 0.4.0
Requires:       crate(phc-0.6/getrandom) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
Modular Crypt Format)
This metapackage enables feature "getrandom" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phc
Summary:        Traits which describe the functionality of password hashing algorithms, with optional support for a `no_std`/`no_alloc`-friendly implementation of the PHC string format, as well as generic support for other formats (e.g - feature "phc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phc-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/phc) = %{version}

%description -n %{name}+phc
Modular Crypt Format)
This metapackage enables feature "phc" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits which describe the functionality of password hashing algorithms, with optional support for a `no_std`/`no_alloc`-friendly implementation of the PHC string format, as well as generic support for other formats (e.g - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phc-0.6/rand-core) >= 0.6.0
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
Modular Crypt Format)
This metapackage enables feature "rand_core" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
