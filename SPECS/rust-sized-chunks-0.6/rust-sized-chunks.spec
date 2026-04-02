# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sized-chunks
%global full_version 0.6.5
%global pkgname sized-chunks-0.6

Name:           rust-sized-chunks-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "sized-chunks"
License:        MPL-2.0+
URL:            https://github.com/bodil/sized-chunks
#!RemoteAsset:  sha256:16d69225bde7a69b235da73377861095455d298f2b970996eec25ddbb42b3d1e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitmaps-2.0/default) >= 2.1.0
Requires:       crate(typenum-1.0/default) >= 1.19.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "sized-chunks"

%package     -n %{name}+arbitrary
Summary:        Efficient sized chunk datatypes - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust sized-chunks crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+array-ops
Summary:        Efficient sized chunk datatypes - feature "array-ops" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(array-ops-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/array-ops)
Provides:       crate(%{pkgname}/ringbuffer)

%description -n %{name}+array-ops
This metapackage enables feature "array-ops" for the Rust sized-chunks crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ringbuffer" feature.

%package     -n %{name}+refpool
Summary:        Efficient sized chunk datatypes - feature "refpool"
Requires:       crate(%{pkgname})
Requires:       crate(refpool-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/refpool)

%description -n %{name}+refpool
This metapackage enables feature "refpool" for the Rust sized-chunks crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
