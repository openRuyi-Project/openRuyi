# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name generic-array
%global full_version 1.4.3
%global pkgname generic-array-1

Name:           rust-generic-array-1
Version:        1.4.3
Release:        %autorelease
Summary:        Rust crate "generic-array"
License:        MIT
URL:            https://github.com/fizyk20/generic-array.git
#!RemoteAsset:  sha256:c2e55f16dcf0e9c00efbe2e655ffe45fc98e7066b52bc92f8a79e64060a79351
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1/default) >= 1.0.0
Requires:       crate(typenum-1/const-generics) >= 1.20.1
Requires:       crate(typenum-1/default) >= 1.20.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/internals) = %{version}

%description
Source code for takopackized Rust crate "generic-array"

%package     -n %{name}+arbitrary
Summary:        Generic types implementing functionality of arrays - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+as-slice
Summary:        Generic types implementing functionality of arrays - feature "as_slice"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(as-slice-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/as-slice) = %{version}

%description -n %{name}+as-slice
This metapackage enables feature "as_slice" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitvec
Summary:        Generic types implementing functionality of arrays - feature "bitvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/const-default) = %{version}
Requires:       crate(bitvec-1) >= 1.0.0
Provides:       crate(%{pkgname}/bitvec) = %{version}

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytecheck-0-8
Summary:        Generic types implementing functionality of arrays - feature "bytecheck-0_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/bytecheck-0-8) = %{version}

%description -n %{name}+bytecheck-0-8
This metapackage enables feature "bytecheck-0_8" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Generic types implementing functionality of arrays - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compat-0-14
Summary:        Generic types implementing functionality of arrays - feature "compat-0_14"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compat-0-14) = %{version}

%description -n %{name}+compat-0-14
This metapackage enables feature "compat-0_14" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+const-default
Summary:        Generic types implementing functionality of arrays - feature "const-default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-default-1) >= 1.0.0
Provides:       crate(%{pkgname}/const-default) = %{version}

%description -n %{name}+const-default
This metapackage enables feature "const-default" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+faster-hex
Summary:        Generic types implementing functionality of arrays - feature "faster-hex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(faster-hex-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/faster-hex) = %{version}

%description -n %{name}+faster-hex
This metapackage enables feature "faster-hex" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hybrid-array-0-4
Summary:        Generic types implementing functionality of arrays - feature "hybrid-array-0_4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/hybrid-array-0-4) = %{version}

%description -n %{name}+hybrid-array-0-4
This metapackage enables feature "hybrid-array-0_4" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-0-8
Summary:        Generic types implementing functionality of arrays - feature "rkyv-0_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv-0-8) = %{version}

%description -n %{name}+rkyv-0-8
This metapackage enables feature "rkyv-0_8" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-0-8-full
Summary:        Generic types implementing functionality of arrays - feature "rkyv-0_8-full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytecheck-0-8) = %{version}
Requires:       crate(%{pkgname}/rkyv-0-8) = %{version}
Provides:       crate(%{pkgname}/rkyv-0-8-full) = %{version}

%description -n %{name}+rkyv-0-8-full
This metapackage enables feature "rkyv-0_8-full" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Generic types implementing functionality of arrays - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Generic types implementing functionality of arrays - feature "subtle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(subtle-2) >= 2.0.0
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Generic types implementing functionality of arrays - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
