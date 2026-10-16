# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name win-crypto-ng
%global full_version 0.5.1
%global pkgname win-crypto-ng-0.5

Name:           rust-win-crypto-ng-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "win-crypto-ng"
License:        BSD-3-Clause
URL:            https://github.com/emgre/win-crypto-ng
#!RemoteAsset:  sha256:99abfb435a71e54ab2971d8d8c32f1a7e006cdbf527f71743b1d45b93517bb92
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(doc-comment-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/bcrypt) >= 0.3.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/ntstatus) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "win-crypto-ng"

%package     -n %{name}+cipher
Summary:        Safe bindings to Windows Cryptography API: Next Generation - feature "cipher" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/block-cipher) = %{version}
Provides:       crate(%{pkgname}/cipher) = %{version}

%description -n %{name}+cipher
This metapackage enables feature "cipher" for the Rust win-crypto-ng crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "block-cipher" feature.

%package     -n %{name}+rand-core
Summary:        Safe bindings to Windows Cryptography API: Next Generation - feature "rand_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust win-crypto-ng crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rand" feature.

%package     -n %{name}+zeroize
Summary:        Safe bindings to Windows Cryptography API: Next Generation - feature "zeroize" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust win-crypto-ng crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
