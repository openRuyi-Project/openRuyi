# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pbkdf2
%global full_version 0.11.0
%global pkgname pbkdf2-0.11

Name:           rust-pbkdf2-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "pbkdf2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/pbkdf2
#!RemoteAsset:  sha256:83a0692ec44e4cf1ef28ca317f14f8f07da2d95ec3fa01f86e4467b725e60917
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.10/default) >= 0.10.3
Requires:       crate(digest-0.10/mac) >= 0.10.3

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pbkdf2"

%package     -n %{name}+hmac
Summary:        Generic implementation of PBKDF2 - feature "hmac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hmac-0.12) >= 0.12.0
Provides:       crate(%{pkgname}/hmac) = %{version}

%description -n %{name}+hmac
This metapackage enables feature "hmac" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Generic implementation of PBKDF2 - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Generic implementation of PBKDF2 - feature "password-hash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.4/rand-core) >= 0.4.0
Provides:       crate(%{pkgname}/password-hash) = %{version}

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Generic implementation of PBKDF2 - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Generic implementation of PBKDF2 - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha-1-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Generic implementation of PBKDF2 - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simple
Summary:        Generic implementation of PBKDF2 - feature "simple" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hmac) = %{version}
Requires:       crate(%{pkgname}/password-hash) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/simple) = %{version}

%description -n %{name}+simple
This metapackage enables feature "simple" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std
Summary:        Generic implementation of PBKDF2 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.4/rand-core) >= 0.4.0
Requires:       crate(password-hash-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
