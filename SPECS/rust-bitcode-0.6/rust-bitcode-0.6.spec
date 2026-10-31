# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitcode
%global full_version 0.6.9
%global pkgname bitcode-0.6

Name:           rust-bitcode-0.6
Version:        0.6.9
Release:        %autorelease
Summary:        Rust crate "bitcode"
License:        MIT OR Apache-2.0
URL:            https://github.com/SoftbearStudios/bitcode
#!RemoteAsset:  sha256:0a6ed1b54d8dc333e7be604d00fa9262f4635485ffea923647b6521a5fff045d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1/default) >= 1.14.0
Requires:       crate(bytemuck-1/min-const-generics) >= 1.14.0
Requires:       crate(bytemuck-1/must-cast) >= 1.14.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bitcode"

%package     -n %{name}+arrayvec
Summary:        Bitwise binary serializer - feature "arrayvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/arrayvec) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bitwise binary serializer - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Bitwise binary serializer - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitcode-derive-0.6/default) >= 0.6.9
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glam
Summary:        Bitwise binary serializer - feature "glam"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.21) >= 0.21.0
Provides:       crate(%{pkgname}/glam) = %{version}

%description -n %{name}+glam
This metapackage enables feature "glam" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Bitwise binary serializer - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1) >= 1.36.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Bitwise binary serializer - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bitwise binary serializer - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7/std) >= 0.7.0
Requires:       crate(glam-0.21/std) >= 0.21.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Bitwise binary serializer - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Bitwise binary serializer - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1) >= 1.10.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust bitcode crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
