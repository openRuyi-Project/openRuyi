# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name av1-grain
%global full_version 0.2.5
%global pkgname av1-grain-0.2

Name:           rust-av1-grain-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "av1-grain"
License:        BSD-2-Clause
URL:            https://github.com/rust-av/av1-grain
#!RemoteAsset:  sha256:8cfddb07216410377231960af4fcab838eaa12e013417781b78bd95ee22077f8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(arrayvec-0.7/default) >= 0.7.6
Requires:       crate(log-0.4/default) >= 0.4.29
Provides:       crate(av1-grain) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/create)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "av1-grain"

%package     -n %{name}+default
Summary:        Helpers for generating and parsing AV1 film grain data - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/create)
Requires:       crate(%{pkgname}/diff)
Requires:       crate(%{pkgname}/estimate)
Requires:       crate(%{pkgname}/parse)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust av1-grain crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diff
Summary:        Helpers for generating and parsing AV1 film grain data - feature "diff"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/num-rational)
Requires:       crate(%{pkgname}/v-frame)
Provides:       crate(%{pkgname}/diff)

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust av1-grain crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nom
Summary:        Helpers for generating and parsing AV1 film grain data - feature "nom" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(nom-8.0/default) >= 8.0.0
Provides:       crate(%{pkgname}/nom)
Provides:       crate(%{pkgname}/parse)

%description -n %{name}+nom
This metapackage enables feature "nom" for the Rust av1-grain crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "parse" feature.

%package     -n %{name}+num-rational
Summary:        Helpers for generating and parsing AV1 film grain data - feature "num-rational"
Requires:       crate(%{pkgname})
Requires:       crate(num-rational-0.4/default) >= 0.4.2
Provides:       crate(%{pkgname}/num-rational)

%description -n %{name}+num-rational
This metapackage enables feature "num-rational" for the Rust av1-grain crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Helpers for generating and parsing AV1 film grain data - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.140
Requires:       crate(serde-1.0/derive) >= 1.0.140
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust av1-grain crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        Helpers for generating and parsing AV1 film grain data - feature "serialize"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(arrayvec-0.7/serde) >= 0.7.6
Provides:       crate(%{pkgname}/serialize)

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust av1-grain crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v-frame
Summary:        Helpers for generating and parsing AV1 film grain data - feature "v_frame" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(v-frame-0.3/default) >= 0.3.9
Provides:       crate(%{pkgname}/estimate)
Provides:       crate(%{pkgname}/v-frame)

%description -n %{name}+v-frame
This metapackage enables feature "v_frame" for the Rust av1-grain crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "estimate" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
