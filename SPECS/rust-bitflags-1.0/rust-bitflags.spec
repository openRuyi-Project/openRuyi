# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitflags
%global full_version 1.3.2
%global pkgname bitflags-1.0

Name:           rust-bitflags-1.0
Version:        1.3.2
Release:        %autorelease
Summary:        Rust crate "bitflags"
License:        MIT/Apache-2.0
URL:            https://github.com/bitflags/bitflags
#!RemoteAsset:  sha256:bef38d45163c2f1dde094a7dfd33ccf595c92905c8f8f4fdc18d06fb1037718a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(bitflags) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/example-generated)

%description
Source code for takopackized Rust crate "bitflags"

%package     -n %{name}+compiler-builtins
Summary:        Macro to generate structures which behave like bitflags - feature "compiler_builtins"
Requires:       crate(%{pkgname})
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/compiler-builtins)

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Macro to generate structures which behave like bitflags - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Macro to generate structures which behave like bitflags - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compiler-builtins)
Requires:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
