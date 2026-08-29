# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ecb
%global full_version 0.1.2
%global pkgname ecb-0.1

Name:           rust-ecb-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "ecb"
License:        MIT
URL:            https://github.com/magic-akari/ecb
#!RemoteAsset:  sha256:1a8bfa975b1aec2145850fcaa1c6fe269a16578c44705a532ae3edc92b8881c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ecb"

%package     -n %{name}+alloc
Summary:        Electronic Codebook (ECB) block cipher mode of operation - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/alloc) >= 0.4.4
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ecb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block-padding
Summary:        Electronic Codebook (ECB) block cipher mode of operation - feature "block-padding" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/block-padding) >= 0.4.4
Provides:       crate(%{pkgname}/block-padding) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust ecb crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std
Summary:        Electronic Codebook (ECB) block cipher mode of operation - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(cipher-0.4/std) >= 0.4.4
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ecb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
