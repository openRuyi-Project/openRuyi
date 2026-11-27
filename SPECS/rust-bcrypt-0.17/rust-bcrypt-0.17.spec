# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bcrypt
%global full_version 0.17.1
%global pkgname bcrypt-0.17

Name:           rust-bcrypt-0.17
Version:        0.17.1
Release:        %autorelease
Summary:        Rust crate "bcrypt"
License:        MIT
URL:            https://github.com/Keats/rust-bcrypt
#!RemoteAsset:  sha256:abaf6da45c74385272ddf00e1ac074c7d8a6c1a1dda376902bd6a427522a8b2c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22) >= 0.22.0
Requires:       crate(blowfish-0.9/bcrypt) >= 0.9.0
Requires:       crate(blowfish-0.9/default) >= 0.9.0
Requires:       crate(subtle-2) >= 2.4.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bcrypt"

%package     -n %{name}+alloc
Summary:        Easily hash and verify passwords using bcrypt - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(base64-0.22/alloc) >= 0.22.0
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
Requires:       crate(getrandom-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust bcrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Easily hash and verify passwords using bcrypt - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/std) >= 0.22.0
Requires:       crate(getrandom-0.3/std) >= 0.3.0
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
