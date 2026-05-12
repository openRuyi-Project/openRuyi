# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde
%global full_version 1.0.228
%global pkgname serde-1.0

Name:           rust-serde-1.0
Version:        1.0.228
Release:        %autorelease
Summary:        Rust crate "serde"
License:        MIT OR Apache-2.0
URL:            https://serde.rs
#!RemoteAsset:  sha256:9a8e94ea7f378bd32cbbd37198a4a91436180c5bb472411e48b5ec2e2124ae9e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-core-1.0/result) >= 1.0.228
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "serde"

%package     -n %{name}+alloc
Summary:        Generic serialization/deserialization framework - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Requires:       crate(serde-core-1.0/result) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rc
Summary:        Generic serialization/deserialization framework - feature "rc"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/rc) >= 1.0.228
Requires:       crate(serde-core-1.0/result) >= 1.0.228
Provides:       crate(%{pkgname}/rc)

%description -n %{name}+rc
This metapackage enables feature "rc" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Generic serialization/deserialization framework - feature "serde_derive" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/serde-derive)

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+std
Summary:        Generic serialization/deserialization framework - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/result) >= 1.0.228
Requires:       crate(serde-core-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unstable
Summary:        Generic serialization/deserialization framework - feature "unstable"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/result) >= 1.0.228
Requires:       crate(serde-core-1.0/unstable) >= 1.0.228
Provides:       crate(%{pkgname}/unstable)

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
