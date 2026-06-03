# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name object
%global full_version 0.36.7
%global pkgname object-0.36

Name:           rust-object-0.36
Version:        0.36.7
Release:        %autorelease
Summary:        Rust crate "object"
License:        Apache-2.0 OR MIT
URL:            https://github.com/gimli-rs/object
#!RemoteAsset:  sha256:62948e14d923ea95ea2c7c86c71013138b66525b86bdc08d2dcc262bdb497b87
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0) >= 2.7.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/archive)
Provides:       crate(%{pkgname}/cargo-all)
Provides:       crate(%{pkgname}/coff)
Provides:       crate(%{pkgname}/elf)
Provides:       crate(%{pkgname}/macho)
Provides:       crate(%{pkgname}/pe)
Provides:       crate(%{pkgname}/read-core)
Provides:       crate(%{pkgname}/unaligned)
Provides:       crate(%{pkgname}/unstable)
Provides:       crate(%{pkgname}/xcoff)

%description
Source code for takopackized Rust crate "object"

%package     -n %{name}+build
Summary:        Unified interface for reading and writing object file formats - feature "build"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/build-core)
Requires:       crate(%{pkgname}/elf)
Requires:       crate(%{pkgname}/write-std)
Provides:       crate(%{pkgname}/build)

%description -n %{name}+build
This metapackage enables feature "build" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+build-core
Summary:        Unified interface for reading and writing object file formats - feature "build_core"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/read-core)
Requires:       crate(%{pkgname}/write-core)
Provides:       crate(%{pkgname}/build-core)

%description -n %{name}+build-core
This metapackage enables feature "build_core" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+read
Summary:        Unified interface for reading and writing object file formats - feature "read"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/archive)
Requires:       crate(%{pkgname}/coff)
Requires:       crate(%{pkgname}/elf)
Requires:       crate(%{pkgname}/macho)
Requires:       crate(%{pkgname}/pe)
Requires:       crate(%{pkgname}/read-core)
Requires:       crate(%{pkgname}/unaligned)
Requires:       crate(%{pkgname}/xcoff)
Provides:       crate(%{pkgname}/read)

%description -n %{name}+read
This metapackage enables feature "read" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Unified interface for reading and writing object file formats - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/std) >= 2.7.5
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write
Summary:        Unified interface for reading and writing object file formats - feature "write"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/coff)
Requires:       crate(%{pkgname}/elf)
Requires:       crate(%{pkgname}/macho)
Requires:       crate(%{pkgname}/pe)
Requires:       crate(%{pkgname}/write-std)
Requires:       crate(%{pkgname}/xcoff)
Provides:       crate(%{pkgname}/write)

%description -n %{name}+write
This metapackage enables feature "write" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write-core
Summary:        Unified interface for reading and writing object file formats - feature "write_core"
Requires:       crate(%{pkgname})
Requires:       crate(crc32fast-1.0) >= 1.2
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.0
Requires:       crate(indexmap-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/write-core)

%description -n %{name}+write-core
This metapackage enables feature "write_core" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write-std
Summary:        Unified interface for reading and writing object file formats - feature "write_std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/write-core)
Requires:       crate(crc32fast-1.0/std) >= 1.2
Requires:       crate(indexmap-2.0/std) >= 2.0.0
Provides:       crate(%{pkgname}/write-std)

%description -n %{name}+write-std
This metapackage enables feature "write_std" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
