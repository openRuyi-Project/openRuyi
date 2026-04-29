# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name orion
%global full_version 0.17.13
%global pkgname orion-0.17

Name:           rust-orion-0.17
Version:        0.17.13
Release:        %autorelease
Summary:        Rust crate "orion"
License:        MIT
URL:            https://github.com/orion-rs/orion
#!RemoteAsset:  sha256:58fa7b8bd24f9f1b7fa56de934075adba4b6fb1bf0bf38db74f4236e05e14776
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fiat-crypto-0.3) >= 0.3.0
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/experimental)

%description
Source code for takopackized Rust crate "orion"

%package     -n %{name}+ct-codecs
Summary:        Usable, easy and safe pure-Rust crypto - feature "ct-codecs"
Requires:       crate(%{pkgname})
Requires:       crate(ct-codecs-1.0/default) >= 1.1.1
Provides:       crate(%{pkgname}/ct-codecs)

%description -n %{name}+ct-codecs
This metapackage enables feature "ct-codecs" for the Rust orion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Usable, easy and safe pure-Rust crypto - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/safe-api)
Requires:       crate(%{pkgname}/zeroize)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust orion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Usable, easy and safe pure-Rust crypto - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust orion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+safe-api
Summary:        Usable, easy and safe pure-Rust crypto - feature "safe_api"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ct-codecs)
Requires:       crate(%{pkgname}/getrandom)
Requires:       crate(zeroize-1.0/alloc) >= 1.1.0
Provides:       crate(%{pkgname}/safe-api)

%description -n %{name}+safe-api
This metapackage enables feature "safe_api" for the Rust orion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Usable, easy and safe pure-Rust crypto - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(serde-1.0/alloc) >= 1.0.124
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust orion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Usable, easy and safe pure-Rust crypto - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.1.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust orion crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
