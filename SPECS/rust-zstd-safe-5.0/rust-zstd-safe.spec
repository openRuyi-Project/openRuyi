# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zstd-safe
%global full_version 5.0.2+zstd.1.5.2
%global pkgname zstd-safe-5.0

Name:           rust-zstd-safe-5.0
Version:        5.0.2
Release:        %autorelease
Summary:        Rust crate "zstd-safe"
License:        MIT/Apache-2.0
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:1d2a5585e04f9eea4b2a3d1eca508c4dee9592a89ef6f450c11719da0726f4db
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.21
Requires:       crate(zstd-sys-2.0) >= 2.0.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/arrays)
Provides:       crate(%{pkgname}/doc-cfg)

%description
Source code for takopackized Rust crate "zstd-safe"

%package     -n %{name}+bindgen
Summary:        Safe low-level bindings for the zstd compression library - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/bindgen) >= 2.0.1
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Safe low-level bindings for the zstd compression library - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/debug) >= 2.0.1
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Safe low-level bindings for the zstd compression library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arrays)
Requires:       crate(%{pkgname}/legacy)
Requires:       crate(%{pkgname}/zdict-builder)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental
Summary:        Safe low-level bindings for the zstd compression library - feature "experimental"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/experimental) >= 2.0.1
Provides:       crate(%{pkgname}/experimental)

%description -n %{name}+experimental
This metapackage enables feature "experimental" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy
Summary:        Safe low-level bindings for the zstd compression library - feature "legacy"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/legacy) >= 2.0.1
Provides:       crate(%{pkgname}/legacy)

%description -n %{name}+legacy
This metapackage enables feature "legacy" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-asm
Summary:        Safe low-level bindings for the zstd compression library - feature "no_asm"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/no-asm) >= 2.0.1
Provides:       crate(%{pkgname}/no-asm)

%description -n %{name}+no-asm
This metapackage enables feature "no_asm" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Safe low-level bindings for the zstd compression library - feature "pkg-config"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/pkg-config) >= 2.0.1
Provides:       crate(%{pkgname}/pkg-config)

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Safe low-level bindings for the zstd compression library - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/std) >= 2.0.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin
Summary:        Safe low-level bindings for the zstd compression library - feature "thin"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/thin) >= 2.0.1
Provides:       crate(%{pkgname}/thin)

%description -n %{name}+thin
This metapackage enables feature "thin" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zdict-builder
Summary:        Safe low-level bindings for the zstd compression library - feature "zdict_builder"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/zdict-builder) >= 2.0.1
Provides:       crate(%{pkgname}/zdict-builder)

%description -n %{name}+zdict-builder
This metapackage enables feature "zdict_builder" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstdmt
Summary:        Safe low-level bindings for the zstd compression library - feature "zstdmt"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-sys-2.0/zstdmt) >= 2.0.1
Provides:       crate(%{pkgname}/zstdmt)

%description -n %{name}+zstdmt
This metapackage enables feature "zstdmt" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
