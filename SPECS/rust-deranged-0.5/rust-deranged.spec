# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deranged
%global full_version 0.5.8
%global pkgname deranged-0.5

Name:           rust-deranged-0.5
Version:        0.5.8
Release:        %autorelease
Summary:        Rust crate "deranged"
License:        MIT OR Apache-2.0
URL:            https://github.com/jhpratt/deranged
#!RemoteAsset:  sha256:7cd812cc2bc1d69d4764bd80df88b4317eaef9e773c75226407d9bc0876b211c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "deranged"

%package     -n %{name}+macros
Summary:        Ranged integers - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(deranged-macros-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num
Summary:        Ranged integers - feature "num"
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2) >= 0.2.15
Provides:       crate(%{pkgname}/num)

%description -n %{name}+num
This metapackage enables feature "num" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+powerfmt
Summary:        Ranged integers - feature "powerfmt"
Requires:       crate(%{pkgname})
Requires:       crate(powerfmt-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/powerfmt)

%description -n %{name}+powerfmt
This metapackage enables feature "powerfmt" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Ranged integers - feature "quickcheck"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(quickcheck-1.0) >= 1.0.3
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Ranged integers - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand010)
Requires:       crate(%{pkgname}/rand08)
Requires:       crate(%{pkgname}/rand09)
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand010
Summary:        Ranged integers - feature "rand010"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand010)

%description -n %{name}+rand010
This metapackage enables feature "rand010" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand08
Summary:        Ranged integers - feature "rand08"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.4
Provides:       crate(%{pkgname}/rand08)

%description -n %{name}+rand08
This metapackage enables feature "rand08" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand09
Summary:        Ranged integers - feature "rand09"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rand09)

%description -n %{name}+rand09
This metapackage enables feature "rand09" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Ranged integers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust deranged crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
