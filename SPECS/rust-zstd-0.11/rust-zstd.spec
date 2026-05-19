# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zstd
%global full_version 0.11.2+zstd.1.5.2
%global pkgname zstd-0.11

Name:           rust-zstd-0.11
Version:        0.11.2
Release:        %autorelease
Summary:        Rust crate "zstd"
License:        MIT
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:20cc960326ece64f010d2d2107537f26dc589a6573a316bd5b1dba685fa5fde4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/doc-cfg)
Provides:       crate(%{pkgname}/wasm)

%description
Source code for takopackized Rust crate "zstd"

%package     -n %{name}+arrays
Summary:        Binding for the zstd compression library - feature "arrays"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/arrays) >= 5.0.1
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname}/arrays)

%description -n %{name}+arrays
This metapackage enables feature "arrays" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bindgen
Summary:        Binding for the zstd compression library - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/bindgen) >= 5.0.1
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Binding for the zstd compression library - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/debug) >= 5.0.1
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Binding for the zstd compression library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arrays)
Requires:       crate(%{pkgname}/legacy)
Requires:       crate(%{pkgname}/zdict-builder)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental
Summary:        Binding for the zstd compression library - feature "experimental"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/experimental) >= 5.0.1
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname}/experimental)

%description -n %{name}+experimental
This metapackage enables feature "experimental" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy
Summary:        Binding for the zstd compression library - feature "legacy"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/legacy) >= 5.0.1
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname}/legacy)

%description -n %{name}+legacy
This metapackage enables feature "legacy" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-asm
Summary:        Binding for the zstd compression library - feature "no_asm"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/no-asm) >= 5.0.1
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname}/no-asm)

%description -n %{name}+no-asm
This metapackage enables feature "no_asm" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Binding for the zstd compression library - feature "pkg-config"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/pkg-config) >= 5.0.1
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Provides:       crate(%{pkgname}/pkg-config)

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin
Summary:        Binding for the zstd compression library - feature "thin"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Requires:       crate(zstd-safe-5.0/thin) >= 5.0.1
Provides:       crate(%{pkgname}/thin)

%description -n %{name}+thin
This metapackage enables feature "thin" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zdict-builder
Summary:        Binding for the zstd compression library - feature "zdict_builder"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Requires:       crate(zstd-safe-5.0/zdict-builder) >= 5.0.1
Provides:       crate(%{pkgname}/zdict-builder)

%description -n %{name}+zdict-builder
This metapackage enables feature "zdict_builder" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstdmt
Summary:        Binding for the zstd compression library - feature "zstdmt"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-5.0/std) >= 5.0.1
Requires:       crate(zstd-safe-5.0/zstdmt) >= 5.0.1
Provides:       crate(%{pkgname}/zstdmt)

%description -n %{name}+zstdmt
This metapackage enables feature "zstdmt" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
