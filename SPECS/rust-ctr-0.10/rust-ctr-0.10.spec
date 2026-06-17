# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctr
%global full_version 0.10.1
%global pkgname ctr-0.10

Name:           rust-ctr-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "ctr"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-modes
#!RemoteAsset:  sha256:baaca1c4b237092596f64d571e9db6ce4109c4ef9742e27590f1709594461f21
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.5/default) >= 0.5.2
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ctr"

%package     -n %{name}+alloc
Summary:        CTR block modes of operation - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5/alloc) >= 0.5.2
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ctr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block-padding
Summary:        CTR block modes of operation - feature "block-padding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5/block-padding) >= 0.5.2
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.2
Provides:       crate(%{pkgname}/block-padding) = %{version}

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust ctr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        CTR block modes of operation - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.2
Requires:       crate(cipher-0.5/zeroize) >= 0.5.2
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ctr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
