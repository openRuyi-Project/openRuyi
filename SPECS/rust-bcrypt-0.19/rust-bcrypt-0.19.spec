# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bcrypt
%global full_version 0.19.3
%global pkgname bcrypt-0.19

Name:           rust-bcrypt-0.19
Version:        0.19.3
Release:        %autorelease
Summary:        Rust crate "bcrypt"
License:        MIT
URL:            https://github.com/Keats/rust-bcrypt
#!RemoteAsset:  sha256:a0cd0bd35a28836d528d2b58ad499bc3c5641d59379421b1be9eeb0c2f2b912a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.23) >= 0.23.0
Requires:       crate(blowfish-0.10/bcrypt) >= 0.10.0
Requires:       crate(blowfish-0.10/default) >= 0.10.0
Requires:       crate(subtle-2) >= 2.4.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bcrypt"

%package     -n %{name}+alloc
Summary:        Easily hash and verify passwords using bcrypt - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(base64-0.23/alloc) >= 0.23.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bcrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Easily hash and verify passwords using bcrypt - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bcrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Easily hash and verify passwords using bcrypt - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust bcrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Easily hash and verify passwords using bcrypt - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.23/std) >= 0.23.0
Requires:       crate(getrandom-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bcrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Easily hash and verify passwords using bcrypt - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/default) >= 1.5.4
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust bcrypt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
