# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.4.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/archive) = %{version}
Provides:       crate(%{pkgname}/cargo-all) = %{version}
Provides:       crate(%{pkgname}/coff) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/elf) = %{version}
Provides:       crate(%{pkgname}/macho) = %{version}
Provides:       crate(%{pkgname}/pe) = %{version}
Provides:       crate(%{pkgname}/read-core) = %{version}
Provides:       crate(%{pkgname}/unaligned) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/xcoff) = %{version}

%description
Source code for takopackized Rust crate "object"

%package     -n %{name}+all
Summary:        Unified interface for reading and writing object file formats - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/build) = %{version}
Requires:       crate(%{pkgname}/compression) = %{version}
Requires:       crate(%{pkgname}/read) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/wasm) = %{version}
Requires:       crate(%{pkgname}/write) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+build
Summary:        Unified interface for reading and writing object file formats - feature "build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/build-core) = %{version}
Requires:       crate(%{pkgname}/elf) = %{version}
Requires:       crate(%{pkgname}/write-std) = %{version}
Provides:       crate(%{pkgname}/build) = %{version}

%description -n %{name}+build
This metapackage enables feature "build" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+build-core
Summary:        Unified interface for reading and writing object file formats - feature "build_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/read-core) = %{version}
Requires:       crate(%{pkgname}/write-core) = %{version}
Provides:       crate(%{pkgname}/build-core) = %{version}

%description -n %{name}+build-core
This metapackage enables feature "build_core" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression
Summary:        Unified interface for reading and writing object file formats - feature "compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.0
Requires:       crate(ruzstd-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/compression) = %{version}

%description -n %{name}+compression
This metapackage enables feature "compression" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Unified interface for reading and writing object file formats - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compression) = %{version}
Requires:       crate(%{pkgname}/read) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+doc
Summary:        Unified interface for reading and writing object file formats - feature "doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/archive) = %{version}
Requires:       crate(%{pkgname}/build-core) = %{version}
Requires:       crate(%{pkgname}/coff) = %{version}
Requires:       crate(%{pkgname}/compression) = %{version}
Requires:       crate(%{pkgname}/elf) = %{version}
Requires:       crate(%{pkgname}/macho) = %{version}
Requires:       crate(%{pkgname}/pe) = %{version}
Requires:       crate(%{pkgname}/read-core) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/wasm) = %{version}
Requires:       crate(%{pkgname}/write-std) = %{version}
Requires:       crate(%{pkgname}/xcoff) = %{version}
Provides:       crate(%{pkgname}/doc) = %{version}

%description -n %{name}+doc
This metapackage enables feature "doc" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+read
Summary:        Unified interface for reading and writing object file formats - feature "read"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/archive) = %{version}
Requires:       crate(%{pkgname}/coff) = %{version}
Requires:       crate(%{pkgname}/elf) = %{version}
Requires:       crate(%{pkgname}/macho) = %{version}
Requires:       crate(%{pkgname}/pe) = %{version}
Requires:       crate(%{pkgname}/read-core) = %{version}
Requires:       crate(%{pkgname}/unaligned) = %{version}
Requires:       crate(%{pkgname}/xcoff) = %{version}
Provides:       crate(%{pkgname}/read) = %{version}

%description -n %{name}+read
This metapackage enables feature "read" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Unified interface for reading and writing object file formats - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(memchr-2/rustc-dep-of-std) >= 2.4.1
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Unified interface for reading and writing object file formats - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/std) >= 2.4.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-all
Summary:        Unified interface for reading and writing object file formats - feature "unstable-all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all) = %{version}
Requires:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/unstable-all) = %{version}

%description -n %{name}+unstable-all
This metapackage enables feature "unstable-all" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Unified interface for reading and writing object file formats - feature "wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasmparser-0.236) >= 0.236.0
Provides:       crate(%{pkgname}/wasm) = %{version}

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write
Summary:        Unified interface for reading and writing object file formats - feature "write"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/coff) = %{version}
Requires:       crate(%{pkgname}/elf) = %{version}
Requires:       crate(%{pkgname}/macho) = %{version}
Requires:       crate(%{pkgname}/pe) = %{version}
Requires:       crate(%{pkgname}/write-std) = %{version}
Requires:       crate(%{pkgname}/xcoff) = %{version}
Provides:       crate(%{pkgname}/write) = %{version}

%description -n %{name}+write
This metapackage enables feature "write" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write-core
Summary:        Unified interface for reading and writing object file formats - feature "write_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc32fast-1) >= 1.2.0
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.0
Requires:       crate(indexmap-2) >= 2.0.0
Provides:       crate(%{pkgname}/write-core) = %{version}

%description -n %{name}+write-core
This metapackage enables feature "write_core" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write-std
Summary:        Unified interface for reading and writing object file formats - feature "write_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/write-core) = %{version}
Requires:       crate(crc32fast-1/std) >= 1.2.0
Requires:       crate(indexmap-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/write-std) = %{version}

%description -n %{name}+write-std
This metapackage enables feature "write_std" for the Rust object crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
