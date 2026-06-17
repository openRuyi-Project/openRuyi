# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bincode
%global full_version 2.0.1
%global pkgname bincode-2

Name:           rust-bincode-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "bincode"
License:        MIT
URL:            https://github.com/bincode-org/bincode
#!RemoteAsset:  sha256:36eaf5d7b090263e8150820482d5d93cd964a81e4019913c972f4edcc6edb740
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unty-0.0.4/default) >= 0.0.4
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bincode"

%package     -n %{name}+alloc
Summary:        Binary serialization / deserialization strategy for transforming structs into bytes and vice versa! - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bincode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bincode-derive
Summary:        Binary serialization / deserialization strategy for transforming structs into bytes and vice versa! - feature "bincode_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bincode-derive-2/default) >= 2.0.1
Provides:       crate(%{pkgname}/bincode-derive) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+bincode-derive
This metapackage enables feature "bincode_derive" for the Rust bincode crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+default
Summary:        Binary serialization / deserialization strategy for transforming structs into bytes and vice versa! - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bincode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Binary serialization / deserialization strategy for transforming structs into bytes and vice versa! - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bincode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Binary serialization / deserialization strategy for transforming structs into bytes and vice versa! - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bincode crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
