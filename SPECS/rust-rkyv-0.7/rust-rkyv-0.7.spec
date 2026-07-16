# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rkyv
%global full_version 0.7.46
%global pkgname rkyv-0.7

Name:           rust-rkyv-0.7
Version:        0.7.46
Release:        %autorelease
Summary:        Rust crate "rkyv"
License:        MIT
URL:            https://github.com/rkyv/rkyv
#!RemoteAsset:  sha256:2297bf9c81a3f0dc96bc9521370b88f054168c29826a75e89c55ff196e7ed6a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ptr-meta-0.1) >= 0.1.3
Requires:       crate(rkyv-derive-0.7/default) >= 0.7.46
Requires:       crate(seahash-4/default) >= 4.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/copy-unsafe) = %{version}
Provides:       crate(%{pkgname}/size-16) = %{version}
Provides:       crate(%{pkgname}/size-32) = %{version}
Provides:       crate(%{pkgname}/size-64) = %{version}

%description
Source code for takopackized Rust crate "rkyv"

%package     -n %{name}+alloc
Summary:        Zero-copy deserialization framework for Rust - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hashbrown) = %{version}
Requires:       crate(bitvec-1/alloc) >= 1.0.0
Requires:       crate(tinyvec-1/alloc) >= 1.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arbitrary-enum-discriminant
Summary:        Zero-copy deserialization framework for Rust - feature "arbitrary_enum_discriminant"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-derive-0.7/arbitrary-enum-discriminant) >= 0.7.46
Provides:       crate(%{pkgname}/arbitrary-enum-discriminant) = %{version}

%description -n %{name}+arbitrary-enum-discriminant
This metapackage enables feature "arbitrary_enum_discriminant" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+archive-be
Summary:        Zero-copy deserialization framework for Rust - feature "archive_be"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rend) = %{version}
Requires:       crate(rkyv-derive-0.7/archive-be) >= 0.7.46
Provides:       crate(%{pkgname}/archive-be) = %{version}

%description -n %{name}+archive-be
This metapackage enables feature "archive_be" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+archive-le
Summary:        Zero-copy deserialization framework for Rust - feature "archive_le"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rend) = %{version}
Requires:       crate(rkyv-derive-0.7/archive-le) >= 0.7.46
Provides:       crate(%{pkgname}/archive-le) = %{version}

%description -n %{name}+archive-le
This metapackage enables feature "archive_le" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrayvec
Summary:        Zero-copy deserialization framework for Rust - feature "arrayvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/arrayvec) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitvec
Summary:        Zero-copy deserialization framework for Rust - feature "bitvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitvec-1) >= 1.0.0
Provides:       crate(%{pkgname}/bitvec) = %{version}

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytecheck
Summary:        Zero-copy deserialization framework for Rust - feature "bytecheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.6) >= 0.6.11
Provides:       crate(%{pkgname}/bytecheck) = %{version}

%description -n %{name}+bytecheck
This metapackage enables feature "bytecheck" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Zero-copy deserialization framework for Rust - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1) >= 1.4.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+copy
Summary:        Zero-copy deserialization framework for Rust - feature "copy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-derive-0.7/copy) >= 0.7.46
Provides:       crate(%{pkgname}/copy) = %{version}

%description -n %{name}+copy
This metapackage enables feature "copy" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Zero-copy deserialization framework for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/size-32) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Zero-copy deserialization framework for Rust - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Zero-copy deserialization framework for Rust - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-1) >= 1.7.0
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rend
Summary:        Zero-copy deserialization framework for Rust - feature "rend"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rend-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/rend) = %{version}

%description -n %{name}+rend
This metapackage enables feature "rend" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Zero-copy deserialization framework for Rust - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1) >= 1.7.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-str
Summary:        Zero-copy deserialization framework for Rust - feature "smol_str"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-str-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/smol-str) = %{version}

%description -n %{name}+smol-str
This metapackage enables feature "smol_str" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Zero-copy deserialization framework for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bytecheck-0.6/std) >= 0.6.11
Requires:       crate(bytes-1/std) >= 1.4.0
Requires:       crate(ptr-meta-0.1/std) >= 0.1.3
Requires:       crate(rend-0.4/std) >= 0.4.0
Requires:       crate(uuid-1/std) >= 1.3.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strict
Summary:        Zero-copy deserialization framework for Rust - feature "strict"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-derive-0.7/strict) >= 0.7.46
Provides:       crate(%{pkgname}/strict) = %{version}

%description -n %{name}+strict
This metapackage enables feature "strict" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tinyvec
Summary:        Zero-copy deserialization framework for Rust - feature "tinyvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tinyvec-1) >= 1.5.0
Provides:       crate(%{pkgname}/tinyvec) = %{version}

%description -n %{name}+tinyvec
This metapackage enables feature "tinyvec" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Zero-copy deserialization framework for Rust - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.6/uuid) >= 0.6.11
Requires:       crate(uuid-1) >= 1.3.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+validation
Summary:        Zero-copy deserialization framework for Rust - feature "validation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/bytecheck) = %{version}
Requires:       crate(rend-0.4/validation) >= 0.4.0
Provides:       crate(%{pkgname}/validation) = %{version}

%description -n %{name}+validation
This metapackage enables feature "validation" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
