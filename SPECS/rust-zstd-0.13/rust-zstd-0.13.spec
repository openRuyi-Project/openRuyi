# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zstd
%global full_version 0.13.3
%global pkgname zstd-0.13

Name:           rust-zstd-0.13
Version:        0.13.3
Release:        %autorelease
Summary:        Rust crate "zstd"
License:        MIT
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:e91ee311a569c327171651566e07972200e76fcfe2242a4fa446149a3881c08a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/doc-cfg) = %{version}
Provides:       crate(%{pkgname}/wasm) = %{version}

%description
Source code for takopackized Rust crate "zstd"

%package     -n %{name}+arrays
Summary:        Binding for the zstd compression library - feature "arrays"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/arrays) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/arrays) = %{version}

%description -n %{name}+arrays
This metapackage enables feature "arrays" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bindgen
Summary:        Binding for the zstd compression library - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/bindgen) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Binding for the zstd compression library - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/debug) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Binding for the zstd compression library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arrays) = %{version}
Requires:       crate(%{pkgname}/legacy) = %{version}
Requires:       crate(%{pkgname}/zdict-builder) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental
Summary:        Binding for the zstd compression library - feature "experimental"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/experimental) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/experimental) = %{version}

%description -n %{name}+experimental
This metapackage enables feature "experimental" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fat-lto
Summary:        Binding for the zstd compression library - feature "fat-lto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/fat-lto) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/fat-lto) = %{version}

%description -n %{name}+fat-lto
This metapackage enables feature "fat-lto" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy
Summary:        Binding for the zstd compression library - feature "legacy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/legacy) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/legacy) = %{version}

%description -n %{name}+legacy
This metapackage enables feature "legacy" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-asm
Summary:        Binding for the zstd compression library - feature "no_asm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/no-asm) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/no-asm) = %{version}

%description -n %{name}+no-asm
This metapackage enables feature "no_asm" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Binding for the zstd compression library - feature "pkg-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/pkg-config) >= 7.1.0
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Provides:       crate(%{pkgname}/pkg-config) = %{version}

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin
Summary:        Binding for the zstd compression library - feature "thin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Requires:       crate(zstd-safe-7/thin) >= 7.1.0
Provides:       crate(%{pkgname}/thin) = %{version}

%description -n %{name}+thin
This metapackage enables feature "thin" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin-lto
Summary:        Binding for the zstd compression library - feature "thin-lto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Requires:       crate(zstd-safe-7/thin-lto) >= 7.1.0
Provides:       crate(%{pkgname}/thin-lto) = %{version}

%description -n %{name}+thin-lto
This metapackage enables feature "thin-lto" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zdict-builder
Summary:        Binding for the zstd compression library - feature "zdict_builder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Requires:       crate(zstd-safe-7/zdict-builder) >= 7.1.0
Provides:       crate(%{pkgname}/zdict-builder) = %{version}

%description -n %{name}+zdict-builder
This metapackage enables feature "zdict_builder" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstdmt
Summary:        Binding for the zstd compression library - feature "zstdmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7/std) >= 7.1.0
Requires:       crate(zstd-safe-7/zstdmt) >= 7.1.0
Provides:       crate(%{pkgname}/zstdmt) = %{version}

%description -n %{name}+zstdmt
This metapackage enables feature "zstdmt" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
