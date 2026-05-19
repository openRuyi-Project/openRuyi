# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name newtype-uuid
%global full_version 1.3.2
%global pkgname newtype-uuid-1.0

Name:           rust-newtype-uuid-1.0
Version:        1.3.2
Release:        %autorelease
Summary:        Rust crate "newtype-uuid"
License:        MIT OR Apache-2.0
URL:            https://github.com/oxidecomputer/newtype-uuid
#!RemoteAsset:  sha256:5c012d14ef788ab066a347d19e3dda699916c92293b05b85ba2c76b8c82d2830
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(uuid-1.0) >= 1.23.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)

%description
Source code for takopackized Rust crate "newtype-uuid"

%package     -n %{name}+default
Summary:        Newtype wrapper around UUIDs - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(uuid-1.0/default) >= 1.23.1
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust newtype-uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest1
Summary:        Newtype wrapper around UUIDs - feature "proptest1"
Requires:       crate(%{pkgname})
Requires:       crate(proptest-1.0/std) >= 1.7.0
Provides:       crate(%{pkgname}/proptest1)

%description -n %{name}+proptest1
This metapackage enables feature "proptest1" for the Rust newtype-uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars08
Summary:        Newtype wrapper around UUIDs - feature "schemars08"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(schemars-0.8/default) >= 0.8.17
Requires:       crate(schemars-0.8/uuid1) >= 0.8.17
Requires:       crate(serde-json-1.0/default) >= 1.0.140
Provides:       crate(%{pkgname}/schemars08)

%description -n %{name}+schemars08
This metapackage enables feature "schemars08" for the Rust newtype-uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Newtype wrapper around UUIDs - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Requires:       crate(uuid-1.0/serde) >= 1.23.1
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust newtype-uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Newtype wrapper around UUIDs - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(uuid-1.0/std) >= 1.23.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust newtype-uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4
Summary:        Newtype wrapper around UUIDs - feature "v4"
Requires:       crate(%{pkgname})
Requires:       crate(uuid-1.0/v4) >= 1.23.1
Provides:       crate(%{pkgname}/v4)

%description -n %{name}+v4
This metapackage enables feature "v4" for the Rust newtype-uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v7
Summary:        Newtype wrapper around UUIDs - feature "v7"
Requires:       crate(%{pkgname})
Requires:       crate(uuid-1.0/v7) >= 1.23.1
Provides:       crate(%{pkgname}/v7)

%description -n %{name}+v7
This metapackage enables feature "v7" for the Rust newtype-uuid crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
