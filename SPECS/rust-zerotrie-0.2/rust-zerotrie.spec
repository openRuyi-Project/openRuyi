# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerotrie
%global full_version 0.2.4
%global pkgname zerotrie-0.2

Name:           rust-zerotrie-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "zerotrie"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:0f9152d31db0792fa83f70fb2f83148effb5c1f5b8c7686c3459e361d9bc20bf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(displaydoc-0.2) >= 0.2.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zerotrie"

%package     -n %{name}+alloc
Summary:        Data structure that efficiently maps strings to integers - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+databake
Summary:        Data structure that efficiently maps strings to integers - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(zerovec-0.11/databake) >= 0.11.6
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dense
Summary:        Data structure that efficiently maps strings to integers - feature "dense" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(zerovec-0.11) >= 0.11.6
Provides:       crate(%{pkgname}/dense)
Provides:       crate(%{pkgname}/zerovec)

%description -n %{name}+dense
This metapackage enables feature "dense" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zerovec" feature.

%package     -n %{name}+litemap
Summary:        Data structure that efficiently maps strings to integers - feature "litemap"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(litemap-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/litemap)

%description -n %{name}+litemap
This metapackage enables feature "litemap" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Data structure that efficiently maps strings to integers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(litemap-0.8/alloc) >= 0.8.0
Requires:       crate(litemap-0.8/serde) >= 0.8.0
Requires:       crate(serde-core-1.0) >= 1.0.220
Requires:       crate(zerovec-0.11/serde) >= 0.11.6
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yoke
Summary:        Data structure that efficiently maps strings to integers - feature "yoke"
Requires:       crate(%{pkgname})
Requires:       crate(yoke-0.8/derive) >= 0.8.2
Provides:       crate(%{pkgname}/yoke)

%description -n %{name}+yoke
This metapackage enables feature "yoke" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerofrom
Summary:        Data structure that efficiently maps strings to integers - feature "zerofrom"
Requires:       crate(%{pkgname})
Requires:       crate(zerofrom-0.1) >= 0.1.7
Provides:       crate(%{pkgname}/zerofrom)

%description -n %{name}+zerofrom
This metapackage enables feature "zerofrom" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
