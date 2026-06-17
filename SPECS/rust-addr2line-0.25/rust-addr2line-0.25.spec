# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gimli-0.32/read) >= 0.32.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cargo-all) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}

%description
Source code for takopackized Rust crate "addr2line"

%package     -n %{name}+all
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bin) = %{version}
Requires:       crate(%{pkgname}/wasm) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bin
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "bin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cpp-demangle) = %{version}
Requires:       crate(%{pkgname}/fallible-iterator) = %{version}
Requires:       crate(%{pkgname}/loader) = %{version}
Requires:       crate(%{pkgname}/rustc-demangle) = %{version}
Requires:       crate(%{pkgname}/smallvec) = %{version}
Requires:       crate(clap-4/default) >= 4.3.21
Requires:       crate(clap-4/wrap-help) >= 4.3.21
Provides:       crate(%{pkgname}/bin) = %{version}

%description -n %{name}+bin
This metapackage enables feature "bin" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cpp-demangle
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "cpp_demangle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cpp-demangle-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/cpp-demangle) = %{version}

%description -n %{name}+cpp-demangle
This metapackage enables feature "cpp_demangle" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cpp-demangle) = %{version}
Requires:       crate(%{pkgname}/fallible-iterator) = %{version}
Requires:       crate(%{pkgname}/loader) = %{version}
Requires:       crate(%{pkgname}/rustc-demangle) = %{version}
Requires:       crate(%{pkgname}/smallvec) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fallible-iterator
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "fallible-iterator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fallible-iterator-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/fallible-iterator) = %{version}

%description -n %{name}+fallible-iterator
This metapackage enables feature "fallible-iterator" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loader
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "loader"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(memmap2-0.9/default) >= 0.9.4
Requires:       crate(object-0.37/compression) >= 0.37.0
Requires:       crate(object-0.37/read) >= 0.37.0
Requires:       crate(typed-arena-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/loader) = %{version}

%description -n %{name}+loader
This metapackage enables feature "loader" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-demangle
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "rustc-demangle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-demangle-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/rustc-demangle) = %{version}

%description -n %{name}+rustc-demangle
This metapackage enables feature "rustc-demangle" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(gimli-0.32/read) >= 0.32.0
Requires:       crate(gimli-0.32/rustc-dep-of-std) >= 0.32.0
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gimli-0.32/read) >= 0.32.0
Requires:       crate(gimli-0.32/std) >= 0.32.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(object-0.37/compression) >= 0.37.0
Requires:       crate(object-0.37/read) >= 0.37.0
Requires:       crate(object-0.37/wasm) >= 0.37.0
Provides:       crate(%{pkgname}/wasm) = %{version}

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
