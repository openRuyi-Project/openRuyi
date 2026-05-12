# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smallvec
%global full_version 1.15.1
%global pkgname smallvec-1.0

Name:           rust-smallvec-1.0
Version:        1.15.1
Release:        %autorelease
Summary:        Rust crate "smallvec"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-smallvec
#!RemoteAsset:  sha256:67b1b7a3b5fe4f1376887184045fcf45c69e92af734b7aaddc05fb777b6fbd03
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-generics)
Provides:       crate(%{pkgname}/const-new)
Provides:       crate(%{pkgname}/debugger-visualizer)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/drain-filter)
Provides:       crate(%{pkgname}/drain-keep-rest)
Provides:       crate(%{pkgname}/may-dangle)
Provides:       crate(%{pkgname}/specialization)
Provides:       crate(%{pkgname}/union)
Provides:       crate(%{pkgname}/write)

%description
Source code for takopackized Rust crate "smallvec"

%package     -n %{name}+arbitrary
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bincode
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "bincode"
Requires:       crate(%{pkgname})
Requires:       crate(bincode-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/bincode)

%description -n %{name}+bincode
This metapackage enables feature "bincode" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+impl-bincode
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "impl_bincode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bincode)
Requires:       crate(%{pkgname}/unty)
Provides:       crate(%{pkgname}/impl-bincode)

%description -n %{name}+impl-bincode
This metapackage enables feature "impl_bincode" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+malloc-size-of
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "malloc_size_of"
Requires:       crate(%{pkgname})
Requires:       crate(malloc-size-of-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/malloc-size-of)

%description -n %{name}+malloc-size-of
This metapackage enables feature "malloc_size_of" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unty
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "unty"
Requires:       crate(%{pkgname})
Requires:       crate(unty-0.0.4) >= 0.0.4
Provides:       crate(%{pkgname}/unty)

%description -n %{name}+unty
This metapackage enables feature "unty" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
