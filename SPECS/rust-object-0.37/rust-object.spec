# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name object
%global full_version 0.37.3
%global pkgname object-0.37

Name:           rust-object-0.37
Version:        0.37.3
Release:        %autorelease
Summary:        Rust crate "object"
License:        Apache-2.0 OR MIT
URL:            https://github.com/gimli-rs/object
#!RemoteAsset:  sha256:ff76201f031d8863c38aa7f905eca4f53abbfa15f609db4277d44cd8938f33fe
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0) >= 2.4.1
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

%package     -n %{name}+all
Summary:        Unified interface for reading and writing object file formats - feature "all"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/build)
Requires:       crate(%{pkgname}/compression)
Requires:       crate(%{pkgname}/read)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/wasm)
Requires:       crate(%{pkgname}/write)
Provides:       crate(%{pkgname}/all)

%description -n %{name}+all
This metapackage enables feature "all" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Unified interface for reading and writing object file formats - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

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

%package     -n %{name}+compression
Summary:        Unified interface for reading and writing object file formats - feature "compression"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(flate2-1.0/default) >= 1.0.0
Requires:       crate(ruzstd-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/compression)

%description -n %{name}+compression
This metapackage enables feature "compression" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Unified interface for reading and writing object file formats - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Unified interface for reading and writing object file formats - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compression)
Requires:       crate(%{pkgname}/read)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+doc
Summary:        Unified interface for reading and writing object file formats - feature "doc"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/archive)
Requires:       crate(%{pkgname}/build-core)
Requires:       crate(%{pkgname}/coff)
Requires:       crate(%{pkgname}/compression)
Requires:       crate(%{pkgname}/elf)
Requires:       crate(%{pkgname}/macho)
Requires:       crate(%{pkgname}/pe)
Requires:       crate(%{pkgname}/read-core)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/wasm)
Requires:       crate(%{pkgname}/write-std)
Requires:       crate(%{pkgname}/xcoff)
Provides:       crate(%{pkgname}/doc)

%description -n %{name}+doc
This metapackage enables feature "doc" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

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

%package     -n %{name}+rustc-dep-of-std
Summary:        Unified interface for reading and writing object file formats - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/core)
Requires:       crate(memchr-2.0/rustc-dep-of-std) >= 2.4.1
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Unified interface for reading and writing object file formats - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/std) >= 2.4.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-all
Summary:        Unified interface for reading and writing object file formats - feature "unstable-all"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/all)
Requires:       crate(%{pkgname}/unstable)
Provides:       crate(%{pkgname}/unstable-all)

%description -n %{name}+unstable-all
This metapackage enables feature "unstable-all" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Unified interface for reading and writing object file formats - feature "wasm"
Requires:       crate(%{pkgname})
Requires:       crate(wasmparser-0.236) >= 0.236.0
Provides:       crate(%{pkgname}/wasm)

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

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
