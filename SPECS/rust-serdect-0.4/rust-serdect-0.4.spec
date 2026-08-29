# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serdect
%global full_version 0.4.3
%global pkgname serdect-0.4

Name:           rust-serdect-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "serdect"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/serdect
#!RemoteAsset:  sha256:66cf8fedced2fcf12406bcb34223dffb92eaf34908ede12fed414c82b7f00b3e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-1) >= 1.0.0
Requires:       crate(serde-1) >= 1.0.184
Provides:       crate(%{pkgname}) = %{version}

%description
cryptographic keys)
Source code for takopackized Rust crate "serdect"

%package     -n %{name}+alloc
Summary:        Constant-time serde serializer/deserializer helpers for data that potentially contains secrets (e.g - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base16ct-1/alloc) >= 1.0.0
Requires:       crate(serde-1/alloc) >= 1.0.184
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+alloc
cryptographic keys)
This metapackage enables feature "alloc" for the Rust serdect crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+derive
Summary:        Constant-time serde serializer/deserializer helpers for data that potentially contains secrets (e.g - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.184
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
cryptographic keys)
This metapackage enables feature "derive" for the Rust serdect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Constant-time serde serializer/deserializer helpers for data that potentially contains secrets (e.g - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
cryptographic keys)
This metapackage enables feature "zeroize" for the Rust serdect crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
