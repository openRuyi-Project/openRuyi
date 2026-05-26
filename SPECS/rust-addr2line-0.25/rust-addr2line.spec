# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name addr2line
%global full_version 0.25.1
%global pkgname addr2line-0.25

Name:           rust-addr2line-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "addr2line"
License:        Apache-2.0 OR MIT
URL:            https://github.com/gimli-rs/addr2line
#!RemoteAsset:  sha256:1b5d307320b3181d6d7954e663bd7c774a838b8220fe0593c86d9fb09f498b4b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gimli-0.32/read) >= 0.32.3
Provides:       crate(addr2line) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cargo-all)

%description
Source code for takopackized Rust crate "addr2line"

%package     -n %{name}+all
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "all"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bin)
Requires:       crate(%{pkgname}/wasm)
Provides:       crate(%{pkgname}/all)

%description -n %{name}+all
This metapackage enables feature "all" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bin
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "bin"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cpp-demangle)
Requires:       crate(%{pkgname}/fallible-iterator)
Requires:       crate(%{pkgname}/loader)
Requires:       crate(%{pkgname}/rustc-demangle)
Requires:       crate(%{pkgname}/smallvec)
Requires:       crate(clap-4.0/default) >= 4.3.21
Requires:       crate(clap-4.0/wrap-help) >= 4.3.21
Provides:       crate(%{pkgname}/bin)

%description -n %{name}+bin
This metapackage enables feature "bin" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cpp-demangle
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "cpp_demangle"
Requires:       crate(%{pkgname})
Requires:       crate(cpp-demangle-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/cpp-demangle)

%description -n %{name}+cpp-demangle
This metapackage enables feature "cpp_demangle" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cpp-demangle)
Requires:       crate(%{pkgname}/fallible-iterator)
Requires:       crate(%{pkgname}/loader)
Requires:       crate(%{pkgname}/rustc-demangle)
Requires:       crate(%{pkgname}/smallvec)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fallible-iterator
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "fallible-iterator"
Requires:       crate(%{pkgname})
Requires:       crate(fallible-iterator-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/fallible-iterator)

%description -n %{name}+fallible-iterator
This metapackage enables feature "fallible-iterator" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loader
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "loader"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(memmap2-0.9/default) >= 0.9.4
Requires:       crate(object-0.37/compression) >= 0.37.0
Requires:       crate(object-0.37/read) >= 0.37.0
Requires:       crate(typed-arena-2.0/default) >= 2.0.0
Provides:       crate(%{pkgname}/loader)

%description -n %{name}+loader
This metapackage enables feature "loader" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-demangle
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "rustc-demangle"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-demangle-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/rustc-demangle)

%description -n %{name}+rustc-demangle
This metapackage enables feature "rustc-demangle" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/core)
Requires:       crate(gimli-0.32/read) >= 0.32.3
Requires:       crate(gimli-0.32/rustc-dep-of-std) >= 0.32.3
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "smallvec"
Requires:       crate(%{pkgname})
Requires:       crate(smallvec-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec)

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(gimli-0.32/read) >= 0.32.3
Requires:       crate(gimli-0.32/std) >= 0.32.3
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "wasm"
Requires:       crate(%{pkgname})
Requires:       crate(object-0.37/compression) >= 0.37.0
Requires:       crate(object-0.37/read) >= 0.37.0
Requires:       crate(object-0.37/wasm) >= 0.37.0
Provides:       crate(%{pkgname}/wasm)

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
