# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zstd-safe
%global full_version 7.2.4
%global pkgname zstd-safe-7

Name:           rust-zstd-safe-7
Version:        7.2.4
Release:        %autorelease
Summary:        Rust crate "zstd-safe"
License:        MIT OR Apache-2.0
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:8f49c4d5f0abb602a93fb8736af2a4f4dd9512e36f7f570d66e65ff867ed3b9d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zstd-sys-2) >= 2.0.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/arrays) = %{version}
Provides:       crate(%{pkgname}/doc-cfg) = %{version}

%description
Source code for takopackized Rust crate "zstd-safe"

%package     -n %{name}+bindgen
Summary:        Safe low-level bindings for the zstd compression library - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/bindgen) >= 2.0.15
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Safe low-level bindings for the zstd compression library - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/debug) >= 2.0.15
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Safe low-level bindings for the zstd compression library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arrays) = %{version}
Requires:       crate(%{pkgname}/legacy) = %{version}
Requires:       crate(%{pkgname}/zdict-builder) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental
Summary:        Safe low-level bindings for the zstd compression library - feature "experimental"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/experimental) >= 2.0.15
Provides:       crate(%{pkgname}/experimental) = %{version}

%description -n %{name}+experimental
This metapackage enables feature "experimental" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fat-lto
Summary:        Safe low-level bindings for the zstd compression library - feature "fat-lto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/fat-lto) >= 2.0.15
Provides:       crate(%{pkgname}/fat-lto) = %{version}

%description -n %{name}+fat-lto
This metapackage enables feature "fat-lto" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy
Summary:        Safe low-level bindings for the zstd compression library - feature "legacy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/legacy) >= 2.0.15
Provides:       crate(%{pkgname}/legacy) = %{version}

%description -n %{name}+legacy
This metapackage enables feature "legacy" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-asm
Summary:        Safe low-level bindings for the zstd compression library - feature "no_asm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/no-asm) >= 2.0.15
Provides:       crate(%{pkgname}/no-asm) = %{version}

%description -n %{name}+no-asm
This metapackage enables feature "no_asm" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Safe low-level bindings for the zstd compression library - feature "pkg-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/pkg-config) >= 2.0.15
Provides:       crate(%{pkgname}/pkg-config) = %{version}

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+seekable
Summary:        Safe low-level bindings for the zstd compression library - feature "seekable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/seekable) >= 2.0.15
Provides:       crate(%{pkgname}/seekable) = %{version}

%description -n %{name}+seekable
This metapackage enables feature "seekable" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Safe low-level bindings for the zstd compression library - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/std) >= 2.0.15
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin
Summary:        Safe low-level bindings for the zstd compression library - feature "thin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/thin) >= 2.0.15
Provides:       crate(%{pkgname}/thin) = %{version}

%description -n %{name}+thin
This metapackage enables feature "thin" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin-lto
Summary:        Safe low-level bindings for the zstd compression library - feature "thin-lto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/thin-lto) >= 2.0.15
Provides:       crate(%{pkgname}/thin-lto) = %{version}

%description -n %{name}+thin-lto
This metapackage enables feature "thin-lto" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zdict-builder
Summary:        Safe low-level bindings for the zstd compression library - feature "zdict_builder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/zdict-builder) >= 2.0.15
Provides:       crate(%{pkgname}/zdict-builder) = %{version}

%description -n %{name}+zdict-builder
This metapackage enables feature "zdict_builder" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstdmt
Summary:        Safe low-level bindings for the zstd compression library - feature "zstdmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-sys-2/zstdmt) >= 2.0.15
Provides:       crate(%{pkgname}/zstdmt) = %{version}

%description -n %{name}+zstdmt
This metapackage enables feature "zstdmt" for the Rust zstd-safe crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
