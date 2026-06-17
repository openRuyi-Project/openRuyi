# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde
%global full_version 1.0.228
%global pkgname serde-1

Name:           rust-serde-1
Version:        1.0.228
Release:        %autorelease
Summary:        Rust crate "serde"
License:        MIT OR Apache-2.0
URL:            https://serde.rs
#!RemoteAsset:  sha256:9a8e94ea7f378bd32cbbd37198a4a91436180c5bb472411e48b5ec2e2124ae9e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-core-1/result) >= 1.0.228
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "serde"

%package     -n %{name}+alloc
Summary:        Generic serialization/deserialization framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.228
Requires:       crate(serde-core-1/result) >= 1.0.228
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rc
Summary:        Generic serialization/deserialization framework - feature "rc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/rc) >= 1.0.228
Requires:       crate(serde-core-1/result) >= 1.0.228
Provides:       crate(%{pkgname}/rc) = %{version}

%description -n %{name}+rc
This metapackage enables feature "rc" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Generic serialization/deserialization framework - feature "serde_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+std
Summary:        Generic serialization/deserialization framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/result) >= 1.0.228
Requires:       crate(serde-core-1/std) >= 1.0.228
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unstable
Summary:        Generic serialization/deserialization framework - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/result) >= 1.0.228
Requires:       crate(serde-core-1/unstable) >= 1.0.228
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
