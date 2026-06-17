# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gimli
%global full_version 0.32.3
%global pkgname gimli-0.32

Name:           rust-gimli-0.32
Version:        0.32.3
Release:        %autorelease
Summary:        Rust crate "gimli"
License:        MIT OR Apache-2.0
URL:            https://github.com/gimli-rs/gimli
#!RemoteAsset:  sha256:e629b9b98ef3dd8afe6ca2bd0f89306cec16d43d907889945bc5d6687f2f13c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/read) = %{version}
Provides:       crate(%{pkgname}/read-core) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description
Source code for takopackized Rust crate "gimli"

%package     -n %{name}+default
Summary:        Reading and writing the DWARF debugging format - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/read-all) = %{version}
Requires:       crate(%{pkgname}/write) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+endian-reader
Summary:        Reading and writing the DWARF debugging format - feature "endian-reader"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/read) = %{version}
Requires:       crate(stable-deref-trait-1) >= 1.1.0
Provides:       crate(%{pkgname}/endian-reader) = %{version}

%description -n %{name}+endian-reader
This metapackage enables feature "endian-reader" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fallible-iterator
Summary:        Reading and writing the DWARF debugging format - feature "fallible-iterator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fallible-iterator-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/fallible-iterator) = %{version}

%description -n %{name}+fallible-iterator
This metapackage enables feature "fallible-iterator" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+read-all
Summary:        Reading and writing the DWARF debugging format - feature "read-all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/endian-reader) = %{version}
Requires:       crate(%{pkgname}/fallible-iterator) = %{version}
Requires:       crate(%{pkgname}/read) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/read-all) = %{version}

%description -n %{name}+read-all
This metapackage enables feature "read-all" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Reading and writing the DWARF debugging format - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fallible-iterator-0.3/std) >= 0.3.0
Requires:       crate(stable-deref-trait-1/std) >= 1.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write
Summary:        Reading and writing the DWARF debugging format - feature "write"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/write) = %{version}

%description -n %{name}+write
This metapackage enables feature "write" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
