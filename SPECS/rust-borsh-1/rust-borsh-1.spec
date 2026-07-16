# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name borsh
%global full_version 1.7.0
%global pkgname borsh-1

Name:           rust-borsh-1
Version:        1.7.0
Release:        %autorelease
Summary:        Rust crate "borsh"
License:        MIT OR Apache-2.0
URL:            https://borsh.io
#!RemoteAsset:  sha256:2f3f6da4992df95bbcd9af42a6c7dcb994498fc9048230405f3b36ff7cd3f145
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-aliases-0.2) >= 0.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/de-strict-order) = %{version}
Provides:       crate(%{pkgname}/rc) = %{version}

%description
Source code for takopackized Rust crate "borsh"

%package     -n %{name}+ascii
Summary:        Binary Object Representation Serializer for Hashing - feature "ascii"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ascii-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/ascii) = %{version}

%description -n %{name}+ascii
This metapackage enables feature "ascii" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh-derive
Summary:        Binary Object Representation Serializer for Hashing - feature "borsh-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borsh-derive-1/default) >= 1.7.0
Provides:       crate(%{pkgname}/borsh-derive) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+borsh-derive
This metapackage enables feature "borsh-derive" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+bson
Summary:        Binary Object Representation Serializer for Hashing - feature "bson"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bson-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/bson) = %{version}

%description -n %{name}+bson
This metapackage enables feature "bson" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Binary Object Representation Serializer for Hashing - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Binary Object Representation Serializer for Hashing - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Binary Object Representation Serializer for Hashing - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Binary Object Representation Serializer for Hashing - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unstable--schema
Summary:        Binary Object Representation Serializer for Hashing - feature "unstable__schema"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(borsh-derive-1/schema) >= 1.7.0
Provides:       crate(%{pkgname}/unstable--schema) = %{version}

%description -n %{name}+unstable--schema
This metapackage enables feature "unstable__schema" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Binary Object Representation Serializer for Hashing - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1) >= 1.0.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust borsh crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
